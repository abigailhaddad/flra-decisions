"""Fetch every decision's HTML page (both tables) and keep it raw in raw/text_html/ (untracked).

    python src/fetch_text.py            # resumable: skips pages already saved
    python src/fetch_text.py --limit 20 # stop after 20 new requests (for a trial run)

Reads the html_url column of out/authority_decisions.parquet and out/fsip_decisions.parquet.
One request every 2 seconds (robots.txt on 2026-11-15 sets no Crawl-delay). Each page is written to
a temp file and then renamed, so a half-written page is never taken as done.

What gets saved, per URL (file name = URL path with "/" turned into "__"):
  <name>.html.gz  the page as served, gzipped (status 200); ~100 KB a page uncompressed
  <name>.err      a JSON note for a permanent miss (404 or 410), so reruns don't ask again
Stops, without saving, on 403 or 429 (FLRA refusing us) and after 5 errors in a row of any other
kind (5xx, timeouts, connection errors). Those pages are retried on the next run.
Progress goes to stdout and raw/text_fetch.log.
"""
import gzip, json, os, sys, time
from datetime import datetime, timezone
from urllib.parse import urlparse, quote

import pandas as pd
import requests

# A generic User-Agent for this bulk fetch of decision pages.
UA = "Mozilla/5.0 (compatible; research-crawler/1.0)"
OUT = os.path.join("raw", "text_html")
LOG = os.path.join("raw", "text_fetch.log")
PAUSE = 2.0
MAX_ERRORS_IN_A_ROW = 5


def cache_name(url):
    path = urlparse(url).path.strip("/")
    return quote(path.replace("/", "__"), safe="._-")


def urls():
    a = pd.read_parquet("out/authority_decisions.parquet")["html_url"].tolist()
    f = pd.read_parquet("out/fsip_decisions.parquet")["html_url"].tolist()
    return a + f


def log(msg):
    line = f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def write_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def done(base):
    return os.path.exists(base + ".html.gz") or os.path.exists(base + ".err")


def main(limit=None):
    os.makedirs(OUT, exist_ok=True)
    todo = [u for u in urls() if not done(os.path.join(OUT, cache_name(u)))]
    total = len(urls())
    log(f"START total={total} already_done={total - len(todo)} to_fetch={len(todo)}")
    errors_in_a_row, fetched = 0, 0
    session = requests.Session()
    session.headers["User-Agent"] = UA
    for u in todo:
        if limit is not None and fetched >= limit:
            break
        base = os.path.join(OUT, cache_name(u))
        time.sleep(PAUSE)
        fetched += 1
        try:
            r = session.get(u, timeout=60)
        except requests.RequestException as e:
            errors_in_a_row += 1
            log(f"ERROR {type(e).__name__} {u} ({errors_in_a_row} in a row)")
            if errors_in_a_row >= MAX_ERRORS_IN_A_ROW:
                log("STOP: too many errors in a row")
                sys.exit(2)
            continue
        if r.status_code in (403, 429):
            log(f"STOP: {r.status_code} on {u}. FLRA is refusing requests; not retrying.")
            sys.exit(3)
        if r.status_code == 200:
            write_atomic(base + ".html.gz", gzip.compress(r.content))
            errors_in_a_row = 0
        elif r.status_code in (404, 410):
            write_atomic(base + ".err", json.dumps({"url": u, "status": r.status_code,
                                                    "final_url": r.url}).encode())
            errors_in_a_row = 0
            log(f"MISS {r.status_code} {u}")
        else:
            errors_in_a_row += 1
            log(f"ERROR {r.status_code} {u} ({errors_in_a_row} in a row)")
            if errors_in_a_row >= MAX_ERRORS_IN_A_ROW:
                log("STOP: too many errors in a row")
                sys.exit(2)
            continue
        if fetched % 100 == 0:
            log(f"progress fetched_this_run={fetched} remaining={len(todo) - fetched}")
    left = sum(not done(os.path.join(OUT, cache_name(u))) for u in urls())
    log(f"END fetched_this_run={fetched} remaining={left}")
    if left == 0:
        log("DONE")


if __name__ == "__main__":
    lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    main(lim)
