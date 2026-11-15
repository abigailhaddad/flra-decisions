"""Build out/decision_text.parquet from the saved decision pages, plus out/text_report.json.

    python src/fetch_text.py          # first: every decision page -> raw/text_html
    python src/fetch_text.py --pdfs   # then: PDFs for rows whose page has no decision body
    python src/build_text.py

One row per row of authority_decisions.parquet and fsip_decisions.parquet, joined by html_url.
Columns: html_url, table, citation (Authority only), case_number, text_status, text_source,
text_chars, text.

text_status:
  ok          text taken from the HTML page's decision body
  ok_pdf      the page has no decision body; text is from the decision's PDF (pdftotext)
  empty       no decision body on the page and no PDF text (no PDF, or the PDF has no text layer)
  http_error  the page returned 404/410 (see raw/text_html/*.err)
The build stops if any page hasn't been fetched yet, rather than writing a partial table.

The report counts every status, lists every non-ok row, lists pages whose body links to a PDF
(and flags the short ones as possible stubs), and checks whether each text contains its own
row's case number.
"""
import gzip, json, os, re, subprocess, sys
from urllib.parse import urlparse, quote

import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import text as textmod
from fetch_text import OUT, cache_name

PDF_DIR = os.path.join("raw", "text_pdf")
STUB_CHARS = 1500  # a body this short that links a PDF is listed as a possible stub


def pdf_text(path):
    r = subprocess.run(["pdftotext", "-enc", "UTF-8", path, "-"], capture_output=True)
    if r.returncode != 0:
        return None
    return textmod.normalise(r.stdout.decode("utf-8", "replace").replace("\f", "\n"))


# ---- case-number check -------------------------------------------------------------------------
DASHES = re.compile(r"[‐‑‒–—―−­]")


def squash(s):
    """Uppercase, unify dashes, drop whitespace, read letter O as zero (the site uses both)."""
    s = DASHES.sub("-", s or "").upper()
    s = re.sub(r"\s+", "", s)
    return s.replace("O", "0")


def case_parts(case_number):
    parts = re.split(r"\s*(?:,|;|&|\band\b)\s*", case_number or "")
    return [p.strip() for p in parts if len(p.strip()) >= 4]


def fsip_pattern(case_number):
    m = re.match(r"(\d{4}) FSIP (\d+)$", (case_number or "").strip())
    if not m:
        return None
    yy, n = m.group(1)[2:], int(m.group(2))
    return re.compile(rf"(?<!\d)(?:{m.group(1)}|{yy})[\s -]*FSIP[\s -]*0*{n}(?!\d)", re.I)


def case_check(table, case_number, txt):
    """'all' every part of the case number is in the text, 'some', 'none', or 'no_case_number'."""
    if not case_number:
        return "no_case_number"
    if table == "fsip":
        pat = fsip_pattern(case_number)
        if pat:
            return "all" if pat.search(DASHES.sub("-", txt)) else "none"
    parts = case_parts(case_number) or [case_number]
    sq = squash(txt)
    hits = sum(squash(p) in sq for p in parts)
    return "all" if hits == len(parts) else ("some" if hits else "none")


def main():
    a = pd.read_parquet("out/authority_decisions.parquet")
    f = pd.read_parquet("out/fsip_decisions.parquet")
    src = pd.concat([
        pd.DataFrame({"html_url": a.html_url, "table": "authority", "citation": a.citation,
                      "case_number": a.case_number, "pdf_url": a.pdf_url}),
        pd.DataFrame({"html_url": f.html_url, "table": "fsip", "citation": None,
                      "case_number": f.case_number, "pdf_url": f.pdf_url}),
    ], ignore_index=True)

    rows, missing = [], []
    multi_body, pdf_linked = [], []
    for r in src.itertuples(index=False):
        base = os.path.join(OUT, cache_name(r.html_url))
        rec = {"html_url": r.html_url, "table": r.table, "citation": r.citation,
               "case_number": r.case_number}
        if os.path.exists(base + ".err"):
            rec.update(text_status="http_error", text_source="none", text="")
            rec["_why"] = json.load(open(base + ".err"))
        elif os.path.exists(base + ".html.gz"):
            status, txt, nbody, pdfs = textmod.extract(gzip.decompress(open(base + ".html.gz", "rb").read()).decode("utf-8", "replace"))
            if nbody > 1:
                multi_body.append(r.html_url)
            if pdfs:
                pdf_linked.append({"html_url": r.html_url, "chars": len(txt), "pdf_links": pdfs,
                                   "possible_stub": len(txt) < STUB_CHARS})
            if status == "ok":
                rec.update(text_status="ok", text_source="html", text=txt)
            else:
                ptxt, why = None, "no pdf_url"
                if isinstance(r.pdf_url, str):
                    p = os.path.join(PDF_DIR, cache_name(r.pdf_url))
                    if os.path.exists(p):
                        ptxt = pdf_text(p)
                        why = "pdf has no text" if not ptxt else None
                    elif os.path.exists(p + ".err"):
                        why = "pdf fetch failed: " + open(p + ".err").read()
                    else:
                        why = "pdf not fetched"
                if ptxt:
                    rec.update(text_status="ok_pdf", text_source="pdf", text=ptxt)
                else:
                    rec.update(text_status="empty", text_source="none", text="")
                    rec["_why"] = why
        else:
            missing.append(r.html_url)
            continue
        rec["text_chars"] = len(rec["text"])
        rec["case_in_text"] = case_check(r.table, r.case_number, rec["text"]) if rec["text"] else "no_text"
        rows.append(rec)

    if missing:
        sys.exit(f"STOP: {len(missing)} pages not fetched yet (first: {missing[0]}). Run src/fetch_text.py.")

    df = pd.DataFrame(rows)
    # Reconcile: exactly one text row per row of each table, joined by html_url.
    assert df.html_url.is_unique, "duplicate html_url in text table"
    for name, t, key in (("authority", a, "authority"), ("fsip", f, "fsip")):
        got = set(df.loc[df.table == key, "html_url"])
        want = set(t.html_url)
        assert got == want, f"{name}: {len(want - got)} missing, {len(got - want)} extra"
        assert len(t) == len(want), f"{name}: html_url not unique in source table"

    report = {
        "rows": len(df), "authority_rows": int((df.table == "authority").sum()),
        "fsip_rows": int((df.table == "fsip").sum()),
        "source_rows": {"authority": len(a), "fsip": len(f)},
        "status_by_table": df.groupby(["table", "text_status"]).size().unstack(fill_value=0).to_dict("index"),
        "case_in_text_by_table": df.groupby(["table", "case_in_text"]).size().unstack(fill_value=0).to_dict("index"),
        "not_ok": [{k: r[k] for k in ("html_url", "table", "case_number", "text_status", "_why")}
                   for r in rows if r["text_status"] not in ("ok", "ok_pdf")],
        "ok_pdf": [r["html_url"] for r in rows if r["text_status"] == "ok_pdf"],
        "pages_with_more_than_one_body_field": multi_body,
        "pages_whose_body_links_a_pdf": len(pdf_linked),
        "possible_stubs_linking_a_pdf": [p for p in pdf_linked if p["possible_stub"]],
        "case_not_in_text": df.loc[df.case_in_text.isin(["none", "some"]),
                                   ["html_url", "table", "case_number", "case_in_text", "text_chars"]].to_dict("records"),
        "text_chars": df.groupby("table").text_chars.describe().round(0).to_dict("index"),
        "shortest_ok": df[df.text_status.str.startswith("ok")].nsmallest(15, "text_chars")[["html_url", "text_chars"]].to_dict("records"),
    }
    out = df[["html_url", "table", "citation", "case_number", "text_status", "text_source", "text_chars", "text"]]
    out.to_parquet("out/decision_text.parquet", index=False)
    json.dump(report, open("out/text_report.json", "w"), indent=1, default=str)
    print(json.dumps({k: report[k] for k in ("rows", "authority_rows", "fsip_rows", "source_rows",
                                             "status_by_table", "case_in_text_by_table",
                                             "pages_whose_body_links_a_pdf")}, indent=1))
    print("possible stubs:", len(report["possible_stubs_linking_a_pdf"]),
          "| multi-body pages:", len(multi_body), "| case not in text:", len(report["case_not_in_text"]))


if __name__ == "__main__":
    main()
