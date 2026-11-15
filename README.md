# flra-decisions

A table of every decision on the Federal Labor Relations Authority's two public listings (Authority decisions and Federal Service Impasses Panel decisions), on Hugging Face: https://huggingface.co/datasets/abigailhaddad/flra-decisions. Not affiliated with the FLRA.

Metadata and links only (citation, dates, case number, parties, PDF and HTML links). A daily GitHub Action adds new decisions.

## Decision text

`decision_text.parquet` has the text of each decision, one row per row of the two tables, joined by `html_url`. It is built from the decision's HTML page on flra.gov: only the decision body (the page's body field), not the title, navigation or footer. The text is FLRA's, with whitespace tidied (old decisions are laid out with spaces in `<pre>` blocks; that layout is flattened). When a page has no decision body, the text comes from the decision's PDF via `pdftotext`, and `text_status` says `ok_pdf`. Rows with no text say why in `text_status`.

    python src/fetch_text.py          # every decision page -> raw/text_html, one every 2 seconds, resumable
    python src/fetch_text.py --pdfs   # PDFs for pages with no decision body -> raw/text_pdf
    python src/build_text.py          # -> out/decision_text.parquet and out/text_report.json
    python src/check_text.py 30       # live spot-check -> checks/text_sample_<date>.md

The daily job does not add text yet.

## Run it

    pip install -r requirements-dev.txt
    python -m pytest tests
    python src/crawl.py authority 0 999    # full listing, one request every 2 seconds, saves raw HTML to raw/
    python src/crawl.py authority_old 0 125   # decisions through 1982, reached by date filter (see below)
    python src/crawl.py fsip 0 109
    python src/build.py                    # raw/ -> out/*.parquet and out/report.json
    python src/check.py 25                 # gap check and a live sample
    python src/refresh.py --dry-run        # what the daily job does, without the upload

The FSIP listing orders same-date rows unstably, so one pass can miss a row and repeat another. `raw/fsip_asc` (the same listing sorted the other way) is read too and the two are unioned by decision page.

The unfiltered Authority listing stops at page 999, which is 10,000 decisions. FLRA's count on 2026-11-15 was 10,462. The older ones are fetched through the listing's issuance-date filter, oldest first, through 1982 (`raw/authority_old`). That range overlaps the main pass on purpose, because the end of the main pass also drops same-date decisions that move between pages. `build.py` merges the two passes by decision page. The 2026-11-15 build has 10,462 decisions, matching FLRA's own count both in total and year by year.
