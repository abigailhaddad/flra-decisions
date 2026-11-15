"""Fetch FLRA listing pages politely and keep the raw HTML (raw/ is untracked).

    python src/crawl.py authority 0 999   # pages first..last, resumable (skips pages already saved)
    python src/crawl.py authority_old 0 125  # decisions through 1982, past the listing's 10,000-row cap

One request every 2 seconds, honest User-Agent, stops on 403/429 or a non-200.
"""
import os, sys, time
import requests

UA = "abigailhaddad-research (github.com/abigailhaddad/flra-decisions)"
URLS = {"authority": "https://www.flra.gov/decisions/authority-decisions?page={}",
        "fsip": "https://www.flra.gov/decisions/fsip-decisions?page={}",
        # The unfiltered listing stops at page 999 (10,000 rows), so the oldest decisions are reached
        # through the issuance-date filter instead, oldest first. The range overlaps the main crawl on
        # purpose; build.py drops the repeats by decision page.
        "authority_old": ("https://www.flra.gov/decisions/authority-decisions?issuance_date_op=between"
                          "&issuance_date%5Bmin%5D=1900-01-01&issuance_date%5Bmax%5D=1982-12-31"
                          "&order=issuance_date&sort=asc&page={}")}


def main(kind, first, last, pause=2.0):
    out = os.path.join("raw", kind)
    os.makedirs(out, exist_ok=True)
    for p in range(first, last + 1):
        path = os.path.join(out, f"{p:04d}.html")
        if os.path.exists(path) and os.path.getsize(path) > 10000:
            continue
        time.sleep(pause)
        r = requests.get(URLS[kind].format(p), headers={"User-Agent": UA}, timeout=60)
        if r.status_code != 200:
            sys.exit(f"STOP: {r.status_code} on page {p}")
        open(path, "w", encoding="utf-8").write(r.text)
        if p % 50 == 0:
            print("page", p, flush=True)
    print("DONE", kind, first, last, flush=True)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
