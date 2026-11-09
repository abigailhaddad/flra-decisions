# flra-decisions

A table of every decision on the Federal Labor Relations Authority's two public listings (Authority decisions and Federal Service Impasses Panel decisions), on Hugging Face: https://huggingface.co/datasets/abigailhaddad/flra-decisions. Not affiliated with the FLRA.

Metadata and links only (citation, dates, case number, parties, PDF and HTML links). A daily GitHub Action adds new decisions.

## Run it

    pip install -r requirements-dev.txt
    python -m pytest tests
    python src/crawl.py authority 0 999    # full listing, one request every 2 seconds, saves raw HTML to raw/
    python src/crawl.py fsip 0 109
    python src/build.py                    # raw/ -> out/*.parquet and out/report.json
    python src/check.py 25                 # gap check and a live sample
    python src/refresh.py --dry-run        # what the daily job does, without the upload

The FSIP listing orders same-date rows unstably, so one pass can miss a row and repeat another. `raw/fsip_asc` (the same listing sorted the other way) is read too and the two are unioned by decision page.
