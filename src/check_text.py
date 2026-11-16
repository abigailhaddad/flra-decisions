"""Spot-check decision_text.parquet against the live site and write checks/text_sample_<date>.md.

    python src/check_text.py 30      # 30 random rows plus edge cases

For each sampled row this re-fetches the live page (2 s apart) and reads its visible text a second
way: lxml's text_content() over the whole <body>, with no container selection, whitespace
collapsed. It then looks for our text's opening and closing ~120 characters in that page text and
prints what sits just before the opening and just after the closing, so a reader can see whether
decision text was cut at either end (before the opening there should only be the page title and
navigation; after the closing, only the site footer). For PDF-sourced rows the PDF is re-fetched
and read with pypdf instead of pdftotext.
Also: does the row's case number (or citation's "FLRA No.") appear in our text.
"""
import io, os, random, re, sys, time
from datetime import date

import lxml.html
import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(__file__))
from build_text import case_check, PAGE_WRONG_DECISION
from fetch_text import UA, PAUSE

SNIP = 120
WS = re.compile(r"\s+")


def flat(s):
    return WS.sub(" ", (s or "").replace(" ", " ")).strip()


def live_page_text(html_bytes):
    doc = lxml.html.fromstring(html_bytes)
    for bad in doc.xpath("//script|//style|//noscript"):
        bad.drop_tree()
    body = doc.find("body")
    return flat((body if body is not None else doc).text_content())


def live_pdf_text(pdf_bytes):
    from pypdf import PdfReader
    return flat(" ".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(pdf_bytes)).pages))


def pick(df, n, seed):
    rnd = df.sample(n, random_state=seed)
    a = pd.read_parquet("out/authority_decisions.parquet")[["html_url", "issuance_date", "pdf_url"]]
    f = pd.read_parquet("out/fsip_decisions.parquet")[["html_url", "issuance_date", "pdf_url"]]
    meta = pd.concat([a, f]).set_index("html_url")
    d = df.join(meta, on="html_url")
    d["issuance_date"] = pd.to_datetime(d.issuance_date, errors="coerce")
    ok = d[d.text_chars > 0]
    edge = {
        "oldest Authority": d[d.table == "authority"].nsmallest(1, "issuance_date"),
        "newest Authority": d[d.table == "authority"].nlargest(1, "issuance_date"),
        "oldest FSIP": d[d.table == "fsip"].nsmallest(1, "issuance_date"),
        "newest FSIP": d[d.table == "fsip"].nlargest(1, "issuance_date"),
        "longest": ok.nlargest(1, "text_chars"),
        "shortest (with text)": ok.nsmallest(2, "text_chars"),
        "PDF-era Authority (has pdf_url), random": d[(d.table == "authority") & d.pdf_url.notna()].sample(2, random_state=seed),
        "first year with PDFs (2009)": d[d.issuance_date.astype(str).str.startswith("2009")].sample(1, random_state=seed),
        "FSIP random": d[d.table == "fsip"].sample(2, random_state=seed),
        "text from PDF (ok_pdf)": d[d.text_status == "ok_pdf"].sample(min(3, (d.text_status == "ok_pdf").sum()), random_state=seed),
        "page carried a different decision (text now from PDF)": d[d.html_url.isin(list(PAGE_WRONG_DECISION))].sample(2, random_state=seed),
        "case number not found in text": d[d.html_url.isin(CASE_FAIL)].sample(min(4, len(CASE_FAIL)), random_state=seed),
    }
    for st in sorted(set(d.text_status) - {"ok"}):
        edge[f"status {st}"] = d[d.text_status == st].head(3)
    rows = [("random", r) for _, r in d.loc[rnd.index].iterrows()]
    for why, sub in edge.items():
        rows += [(why, r) for _, r in sub.iterrows()]
    return rows


CASE_FAIL = []


def main(n=30, seed=20261115):
    df = pd.read_parquet("out/decision_text.parquet")
    CASE_FAIL.extend(df[[case_check(t, c, x) in ("none", "some") for t, c, x in
                         zip(df.table, df.case_number, df.text)]].html_url.tolist())
    rows = pick(df, n, seed)
    s = requests.Session()
    s.headers["User-Agent"] = UA
    out, tally = [], {"start_found": 0, "end_found": 0, "case_found": 0, "checked": 0, "no_text": 0, "whole_found": 0}
    for why, r in rows:
        time.sleep(PAUSE)
        src_url = r.html_url if r.text_status != "ok_pdf" else r.pdf_url
        resp = s.get(src_url, timeout=60)
        if resp.status_code in (403, 429):
            sys.exit(f"STOP: {resp.status_code} on {src_url}. FLRA is refusing requests; not retrying.")
        key = r.citation if isinstance(r.citation, str) else r.case_number
        out.append(f"### {key} ({r.table}, {r.issuance_date}) — {why}\n")
        out.append(f"- Page: {r.html_url}" + (f"\n- PDF (text source): {r.pdf_url}" if r.text_status == "ok_pdf" else ""))
        out.append(f"- Our status: `{r.text_status}`, {r.text_chars:,} characters; live fetch HTTP {resp.status_code}")
        if resp.status_code != 200:
            out.append("- Could not re-fetch.\n")
            continue
        if r.text_chars == 0:
            tally["no_text"] += 1
            live = live_page_text(resp.content) if r.text_status != "ok_pdf" else ""
            out.append(f"- We have no text. Live page text (first 400 chars): `{live[:400]}`\n")
            continue
        tally["checked"] += 1
        live = live_pdf_text(resp.content) if r.text_status == "ok_pdf" else live_page_text(resp.content)
        ours = flat(r.text)
        head, tail = ours[:SNIP], ours[-SNIP:]
        i, j = live.find(head), live.rfind(tail)
        cc = case_check(r.table, r.case_number, r.text)
        nows = lambda x: re.sub(r"\s+", "", x)
        whole = nows(ours) in nows(live)
        tally["start_found"] += i >= 0
        tally["whole_found"] += whole
        tally["end_found"] += j >= 0
        tally["case_found"] += cc == "all"
        out.append(f"- Opening, ours: `{head}`")
        out.append(f"- Live, 150 chars before it: `{live[max(0, i - 150):i] if i >= 0 else 'NOT FOUND'}`")
        out.append(f"- Closing, ours: `{tail}`")
        out.append(f"- Live, 150 chars after it: `{live[j + len(tail):j + len(tail) + 150] if j >= 0 else 'NOT FOUND'}`")
        out.append(f"- Whole text found in live text (all whitespace removed): {whole}")
        out.append(f"- Case number `{r.case_number}` in our text: {cc}\n")
    today = date.today().isoformat()
    hdr = [f"# Decision text spot-check, {today}\n",
           f"Built from out/decision_text.parquet; live pages re-fetched {today}. {n} random rows "
           f"(seed {seed}) plus edge cases, {len(rows)} rows in all.",
           "Second reading: lxml text_content() of the whole live page (no container selection), "
           "or pypdf for PDF-sourced rows. A start/end is 'found' when our first/last "
           f"{SNIP} characters (whitespace collapsed) appear verbatim in that text. 'Whole text found' "
           "means our entire text, with all whitespace removed, is a substring of the live text with "
           "all whitespace removed (catches dropped or added passages in the middle).\n",
           f"Result: of {tally['checked']} rows with text, opening found {tally['start_found']}, "
           f"closing found {tally['end_found']}, whole text found {tally['whole_found']}, case number found {tally['case_found']}. "
           f"Rows with no text: {tally['no_text']}.\n"]
    os.makedirs("checks", exist_ok=True)
    path = f"checks/text_sample_{today}.md"
    open(path, "w", encoding="utf-8").write("\n".join(hdr + out) + "\n")
    print(path, tally)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30)
