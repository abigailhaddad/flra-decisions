"""Build out/decision_text.parquet from the saved decision pages, plus out/text_report.json.

    python src/fetch_text.py          # first: every decision page -> raw/text_html
    python src/fetch_text.py --pdfs   # then: PDFs for rows whose page has no decision body
    python src/build_text.py

One row per row of authority_decisions.parquet and fsip_decisions.parquet, joined by html_url.
Columns: html_url, table, citation (Authority only), case_number, text_status, text_source,
text_chars, text.

text_status:
  ok          text taken from the HTML page's decision body
  ok_pdf      text is from the decision's PDF (pdftotext): the page has no decision body, or is in
              PAGE_INCOMPLETE or PAGE_WRONG_DECISION
  wrong_page  the page at html_url carries a different decision (PAGE_WRONG_DECISION) and the PDF
              gave no text with this row's case number; text is left empty rather than give the
              other decision's text
  partial     a page in PAGE_INCOMPLETE with no PDF: the text is what the page has, which is cut
              off or only a pointer to an attachment
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

# Pages whose decision body is there but incomplete as FLRA serves it, found 2026-11-16 by reading
# every ok text under 1,000 characters and every text ending in a lowercase letter, comma or
# semicolon (300 rows; most end in a signature block or a footnote). Checked in the raw HTML: the
# body field itself stops at these points. When the row has a pdf_url, its text comes from the PDF.
PAGE_INCOMPLETE = {
    "https://www.flra.gov/decisions/v07/07-005.html": "page body is only 'See attached text.'",
    "https://www.flra.gov/decisions/v63/63-125.html": "page body is only a link label for the PDF",
    "https://www.flra.gov/decisions/v36/36-032.html": "page body says 'FULL TEXT OF DECISION IS ATTACHED'",
    "https://www.flra.gov/decisions/v61/61-005.html": "page stops mid-sentence after the first paragraph",
    "https://www.flra.gov/decisions/v61/61-012.html": "page stops mid-sentence after the first paragraph",
    "https://www.flra.gov/decisions/v63/63-132.html": "page stops mid-sentence",
    "https://www.flra.gov/decisions/v63/63-141.html": "page stops mid-sentence",
}

# Pages that carry a different decision from the row, found 2026-11-16: the text has neither the
# row's case number nor its citation, and its caption names another case (in four of them the
# text is identical to the neighbouring page's). FLRA's error, not ours. Text comes from the row's
# PDF instead, and only if the PDF text contains the row's case number.
PAGE_WRONG_DECISION = {
    "https://www.flra.gov/decisions/v66/66-144.html": "page is 66 FLRA No. 120 (0-AR-4734)",
    "https://www.flra.gov/decisions/v64/64-132.html": "page is 64 FLRA No. 133 (0-AR-4294), same text as 64-133",
    "https://www.flra.gov/decisions/v64/64-130.html": "page is 64 FLRA No. 131 (0-AR-4382)",
    "https://www.flra.gov/decisions/v64/64-072.html": "page is 64 FLRA No. 73 (0-AR-4307), same text as 64-073",
    "https://www.flra.gov/decisions/v64/64-28.html": "page is 64 FLRA No. 26, same text as 64-026",
    "https://www.flra.gov/decisions/v63/63-190.html": "page is 63 FLRA No. 145 (0-AR-4056)",
    "https://www.flra.gov/decisions/v63/63-175.html": "page is 63 FLRA No. 174 (0-AR-4179), same text as 63-174",
    "https://www.flra.gov/decisions/v63/63-162.html": "page is 63 FLRA No. 163 (0-AR-4215)",
}


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


def cite_check(html_url, citation, txt):
    """Authority only: True if the text carries the row's citation, as '<vol> FLRA No. <n>' (n from
    the URL), '[ v<vol> p<page> ]', '<vol>:<page>(' or '<vol> FLRA <page>' (page from citation)."""
    c = re.match(r"(\d+) FLRA (\d+)$", citation or "")
    if not c:
        return False
    vol, pg = int(c.group(1)), int(c.group(2))
    m = re.search(r"/v?\d+/\d+-(\d+)", html_url)
    if m and re.search(rf"(?<!\d)0*{vol}\s*FLRA\s*N[oO0]\.?\s*0*{int(m.group(1))}(?!\d)", txt, re.I):
        return True
    return bool(re.search(rf"\[\s*v0*{vol}\s*p0*{pg}\s*\]|(?<!\d)0*{vol}:0*{pg}\(|(?<!\d)0*{vol}\s*FLRA\s*0*{pg}(?!\d)", txt))


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
            if r.html_url in PAGE_WRONG_DECISION:
                ptxt, why = None, "no pdf_url"
                if isinstance(r.pdf_url, str):
                    p = os.path.join(PDF_DIR, cache_name(r.pdf_url))
                    ptxt = pdf_text(p) if os.path.exists(p) else None
                    why = "pdf not fetched" if not os.path.exists(p) else ("pdf has no text" if not ptxt else None)
                    if ptxt and case_check(r.table, r.case_number, ptxt) == "none":
                        ptxt, why = None, "pdf text lacks the row's case number"
                if ptxt:
                    rec.update(text_status="ok_pdf", text_source="pdf", text=ptxt)
                else:
                    rec.update(text_status="wrong_page", text_source="none", text="")
                    rec["_why"] = PAGE_WRONG_DECISION[r.html_url] + "; " + why
            elif status == "ok" and r.html_url not in PAGE_INCOMPLETE:
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
                elif status == "ok":  # incomplete page, no PDF text: keep what the page has
                    rec.update(text_status="partial", text_source="html", text=txt)
                    rec["_why"] = PAGE_INCOMPLETE[r.html_url] + "; " + why
                else:
                    rec.update(text_status="empty", text_source="none", text="")
                    rec["_why"] = why
        else:
            missing.append(r.html_url)
            continue
        rec["text_chars"] = len(rec["text"])
        rec["case_in_text"] = case_check(r.table, r.case_number, rec["text"]) if rec["text"] else "no_text"
        rec["cite_in_text"] = bool(rec["text"]) and r.table == "authority" and cite_check(r.html_url, r.citation, rec["text"])
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
        "page_incomplete": [{"html_url": r["html_url"], "text_status": r["text_status"],
                             "note": PAGE_INCOMPLETE[r["html_url"]]} for r in rows
                            if r["html_url"] in PAGE_INCOMPLETE],
        "page_wrong_decision": [{"html_url": r["html_url"], "text_status": r["text_status"],
                                 "note": PAGE_WRONG_DECISION[r["html_url"]]} for r in rows
                                if r["html_url"] in PAGE_WRONG_DECISION],
        "ok_pdf": [r["html_url"] for r in rows if r["text_status"] == "ok_pdf"],
        "pages_with_more_than_one_body_field": multi_body,
        "pages_whose_body_links_a_pdf": len(pdf_linked),
        "possible_stubs_linking_a_pdf": [p for p in pdf_linked if p["possible_stub"]],
        "case_or_citation_in_text_by_table": {
            t: {"with_text": int((g.text_chars > 0).sum()),
                "case_number_all_parts": int((g.case_in_text == "all").sum()),
                "citation": int(g.cite_in_text.sum()),
                "either": int(((g.case_in_text == "all") | g.cite_in_text).sum())}
            for t, g in df.groupby("table")},
        "neither_case_nor_citation": df.loc[(df.text_chars > 0) & (df.case_in_text != "all") & ~df.cite_in_text,
                                            ["html_url", "table", "case_number", "text_status"]].to_dict("records"),
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
                                             "case_or_citation_in_text_by_table",
                                             "pages_whose_body_links_a_pdf")}, indent=1))
    print("possible stubs:", len(report["possible_stubs_linking_a_pdf"]),
          "| multi-body pages:", len(multi_body), "| case not in text:", len(report["case_not_in_text"]))


if __name__ == "__main__":
    main()
