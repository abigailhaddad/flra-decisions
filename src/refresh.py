"""Daily refresh: read the first pages of FLRA's two listings, merge into the Hugging Face tables, upload.

    python src/refresh.py            # needs HF_TOKEN
    python src/refresh.py --dry-run

New decisions appear at the top of each listing (sorted newest first), so the first PAGES pages are enough.
Rows are keyed by html_url; new wins, rows no longer listed are kept. The run stops without uploading if a
fetch fails, a page parses to nothing, or the merge would shrink a table.
"""
import os, sys, time
import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(__file__))
import flra

UA = "abigailhaddad-research (github.com/abigailhaddad/flra-decisions)"
REPO = "abigailhaddad/flra-decisions"
PAGES = 5
KINDS = {"authority_decisions": ("https://www.flra.gov/decisions/authority-decisions?page={}", flra.parse_page),
         "fsip_decisions": ("https://www.flra.gov/decisions/fsip-decisions?page={}", flra.parse_fsip_page)}


def merge(old, new):
    """New wins by html_url; rows only in old are kept."""
    kept = old[~old["html_url"].isin(set(new["html_url"]))]
    return pd.concat([new, kept], ignore_index=True)


def fetch_new(url, parser, pause=2.0):
    rows = []
    for p in range(PAGES):
        time.sleep(pause)
        r = requests.get(url.format(p), headers={"User-Agent": UA}, timeout=60)
        if r.status_code != 200:
            sys.exit(f"STOP: {r.status_code} on page {p}; nothing uploaded")
        d, problems = parser(r.text, p)
        if not d or problems:
            sys.exit(f"page {p} parsed to {len(d)} rows with {len(problems)} problems; nothing uploaded")
        rows += d
    return pd.DataFrame(rows).drop_duplicates("html_url")


def main():
    dry = "--dry-run" in sys.argv
    out, summary = {}, {}
    for name, (url, parser) in KINDS.items():
        old = pd.read_parquet(f"https://huggingface.co/datasets/{REPO}/resolve/main/{name}.parquet")
        new = fetch_new(url, parser)
        merged = merge(old, new)
        if len(merged) < len(old):
            sys.exit(f"{name}: would shrink the table; nothing uploaded")
        assert merged["html_url"].is_unique
        out[name] = merged
        summary[name] = {"rows": len(merged), "added": len(merged) - len(old)}
    print(summary)
    if dry or all(v["added"] == 0 for v in summary.values()):
        print("dry run" if dry else "nothing new")
        return
    from huggingface_hub import CommitOperationAdd, HfApi
    os.makedirs("out", exist_ok=True)
    ops = []
    for name, df in out.items():
        df.to_parquet(f"out/{name}.parquet", index=False)
        ops.append(CommitOperationAdd(path_in_repo=f"{name}.parquet", path_or_fileobj=f"out/{name}.parquet"))
    HfApi().create_commit(repo_id=REPO, repo_type="dataset", operations=ops,
                          commit_message="Refresh: " + ", ".join(f"+{v['added']} {k}" for k, v in summary.items()))


if __name__ == "__main__":
    main()
