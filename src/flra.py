"""Parse FLRA's Authority-decisions listing (https://www.flra.gov/decisions/authority-decisions).

Each decision is two table rows: a metadata row (citation, issuance number and date, case number,
arbitrator) and a links row (PDF, HTML, digest, then the parties). Newer decisions have a PDF; old
ones are HTML only and the links row also carries a reporter code. Nothing is dropped silently:
a row pair that doesn't match comes back in `problems`.
"""
import html as htmllib
import re
from datetime import datetime
from urllib.parse import unquote, urljoin

BASE = "https://www.flra.gov"
ROW = re.compile(r'<tr class="(group-[^"]*)"[^>]*>(.*?)</tr>', re.S)
CELL = re.compile(r'<td[^>]*views-field-([a-z-]+)"[^>]*>\s*<div class="label">[^<]*</div>(.*?)</td>', re.S)


def text(fragment):
    return re.sub(r"\s+", " ", htmllib.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def iso_date(s):
    s = s.replace("Sept.", "Sep.").strip()
    for fmt in ("%b. %d, %Y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return datetime.strptime(s, fmt).date().isoformat()
        except ValueError:
            pass
    return None


def parse_page(page_html, page_no=None):
    rows = ROW.findall(page_html)
    decisions, problems = [], []
    i = 0
    while i < len(rows):
        meta = dict(CELL.findall(rows[i][1]))
        if "ad-citation-number" not in meta or i + 1 >= len(rows):
            problems.append({"page": page_no, "row": i, "why": "not a metadata row", "text": text(rows[i][1])[:200]})
            i += 1
            continue
        links = rows[i + 1][1]
        i += 2
        hrefs = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', links, re.S)
        pdf = html = digest = None
        for href, label in hrefs:
            lab = text(label)
            if href.startswith("/themes"):
                continue
            if lab.startswith("PDF"):
                pdf = urljoin(BASE, href)
            elif lab == "HTML":
                html = urljoin(BASE, href)
            elif lab.startswith("Digest"):
                digest = urljoin(BASE, href)
        size = re.search(r"\(([\d.,]+ [KM]B)\)", links)
        bare = re.sub(r"<a[^>]*>.*?</a>", " ", links, flags=re.S)
        bare = re.sub(r'<span[^>]*c-file__size.*?</span>', " ", bare, flags=re.S)
        tail = text(bare).replace("|", " ")
        tail = re.sub(r"\s+", " ", tail).strip()
        rec = {
            "citation": text(meta["ad-citation-number"]),
            "issuance_number": text(meta.get("issuance-number", "")),
            "issuance_date_raw": text(meta.get("issuance-date", "")),
            "issuance_date": iso_date(text(meta.get("issuance-date", ""))),
            "case_number": text(meta.get("case-number", "")),
            "arbitrator": text(meta.get("arbitrator", "")),
            "parties_or_detail": tail,
            "pdf_url": pdf, "html_url": html, "digest_url": digest,
            "pdf_size": size.group(1) if size else None,
            "listing_page": page_no,
        }
        if not (pdf or html):
            problems.append({"page": page_no, "why": "no PDF or HTML link", "citation": rec["citation"]})
        if rec["issuance_date"] is None:
            problems.append({"page": page_no, "why": "unparsed date", "citation": rec["citation"], "raw": rec["issuance_date_raw"]})
        decisions.append(rec)
    return decisions, problems


def parse_fsip_page(page_html, page_no=None):
    """FSIP listing: metadata row (case number, date) then a links row whose last cell holds the
    parties in a nested table. Rows are split on the group marker because the nested table has
    <tr>s of its own."""
    chunks = re.split(r'<tr class="group-[^"]*"[^>]*>', page_html)[1:]
    decisions, problems = [], []
    i = 0
    while i < len(chunks):
        meta = chunks[i]
        m = re.search(r'Case Number</div>\s*([^<]+)<', meta)
        if not m and "views-field-complete-fsip-case-number" in meta and "Issuance Date" in meta:
            m = re.match(r"(?P<x>)", "")  # the site left the case-number cell empty for this decision
        if not m or i + 1 >= len(chunks):
            problems.append({"page": page_no, "why": "not a metadata row", "text": text(meta)[:200]})
            i += 1
            continue
        links = chunks[i + 1]
        i += 2
        t = re.search(r'<time datetime="(\d{4}-\d{2}-\d{2})', meta)
        hrefs = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', links, re.S)
        pdf = html = None
        for href, label in hrefs:
            lab = text(label)
            if href.startswith("/themes"):
                continue
            if lab.startswith("PDF") and not pdf:
                pdf = urljoin(BASE, href)
            elif lab == "HTML" and not html:
                html = urljoin(BASE, href)
        size = re.search(r"c-file__size\">\(([\d.,]+ [KM]B)\)", links)
        nested = re.search(r"<table>(.*?)</table>", links, re.S)
        parties = text(nested.group(1)) if nested else ""
        parties = re.sub(r"^In the Matter of\s*", "", parties)
        cn = m.group(1).strip() if m.re.groups and m.lastindex == 1 and m.group(1) is not None and "Case Number" in meta else ""
        fromfile = re.search(r"(\d{2}) FSIP (\d+)", unquote(pdf or ""))
        rec = {"case_number": cn,
               "case_number_from_pdf_name": f"{fromfile.group(1)} FSIP {int(fromfile.group(2)):03d}" if fromfile else None,
               "issuance_date": t.group(1) if t else None,
               "parties": parties, "pdf_url": pdf, "html_url": html,
               "pdf_size": size.group(1) if size else None, "listing_page": page_no}
        if not (pdf or html):
            problems.append({"page": page_no, "why": "no PDF or HTML link", "case": rec["case_number"]})
        if not t:
            problems.append({"page": page_no, "why": "no date", "case": rec["case_number"]})
        decisions.append(rec)
    return decisions, problems
