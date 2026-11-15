"""Pull the decision text out of a saved FLRA decision page.

Every era of the site (1979 through 2026, Authority and FSIP) puts the decision in one Drupal
field inside the article: <article class="c-article"> ... <div class="c-field--name-body">.
Outside it are the page title (the parties, or for some 1990s pages a reference line), the site
navigation and the footer, none of which are kept.

The text is kept as FLRA wrote it. The only changes are whitespace: <br> and block elements become
line breaks, runs of spaces/tabs/non-breaking spaces become one space, lines are stripped, and runs
of blank lines become one blank line. Old decisions are in <pre> blocks laid out with spaces; that
layout is flattened by the same rule.

extract(html) returns (status, text, n_body_fields, pdf_links):
  "ok"     body field found with text
  "empty"  no body field, or a body field with no text (some FSIP pages are only a title; the
           decision is in the PDF linked from the listing)
"""
import re

from bs4 import BeautifulSoup, NavigableString

BLOCK = {"p", "div", "pre", "h1", "h2", "h3", "h4", "h5", "h6", "li", "ul", "ol", "tr", "td", "th",
         "table", "blockquote", "center", "hr", "dd", "dt", "dl", "section", "article"}
SPACES = re.compile(r"[ \t\r\f\v  -   　]+")


def normalise(s):
    lines = [SPACES.sub(" ", ln).strip() for ln in s.split("\n")]
    out, blank = [], False
    for ln in lines:
        if ln:
            out.append(ln)
            blank = False
        elif out and not blank:
            out.append("")
            blank = True
    return "\n".join(out).strip()


def _to_text(el):
    for t in el.find_all(["script", "style"]):
        t.decompose()
    for br in el.find_all("br"):
        br.replace_with(NavigableString("\n"))
    for b in el.find_all(BLOCK):
        b.insert_before(NavigableString("\n"))
        b.insert_after(NavigableString("\n"))
    return normalise(el.get_text(""))


def extract(page_html):
    soup = BeautifulSoup(page_html, "lxml")
    bodies = soup.select("article.c-article div.c-field--name-body")
    if not bodies:
        return "empty", "", 0, []
    pdfs = sorted({a["href"] for b in bodies for a in b.find_all("a", href=True)
                   if ".pdf" in a["href"].lower()})
    text = "\n\n".join(t for t in (_to_text(b) for b in bodies) if t)
    return ("ok" if text else "empty"), text, len(bodies), pdfs
