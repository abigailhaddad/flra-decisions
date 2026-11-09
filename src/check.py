"""Second checks on the built tables, independent of the parser's own counts.

1. Gaps: within each FLRA volume the issuance numbers should run 1..N. Gaps are listed, not fixed.
2. Live sample: re-fetch the decision's own page and compare citation and date to the table.
   python src/check.py [n_sample]
"""
import json, random, re, sys, time
import pandas as pd
import requests

UA = "abigailhaddad-research (github.com/abigailhaddad/flra-decisions)"


def gaps(df):
    out = {}
    d = df.assign(vol=df["citation"].str.extract(r"^(\d+) FLRA")[0],
                  num=pd.to_numeric(df["issuance_number"], errors="coerce"))
    for vol, g in d.groupby("vol"):
        nums = sorted(set(g["num"].dropna().astype(int)))
        if not nums:
            continue
        missing = sorted(set(range(1, nums[-1] + 1)) - set(nums))
        dupes = int(g.duplicated(["num"], keep=False).sum())
        if missing or dupes:
            out[vol] = {"max": nums[-1], "missing": missing[:30], "n_missing": len(missing), "rows_sharing_a_number": dupes}
    return out


def live_sample(df, n, seed=20261108):
    rows = df[df["html_url"].notna()].sample(n=n, random_state=seed)
    results = []
    for r in rows.itertuples():
        time.sleep(2)
        t = requests.get(r.html_url, headers={"User-Agent": UA}, timeout=60)
        txt = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t.text))
        cite = r.citation.lstrip("0")
        results.append({"citation": r.citation, "date": r.issuance_date, "status": t.status_code,
                        "citation_on_page": r.citation in txt or cite in txt,
                        "case_on_page": bool(r.case_number) and r.case_number.split(",")[0].strip() in txt,
                        "url": r.html_url})
    return results


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    a = pd.read_parquet("out/authority_decisions.parquet")
    g = gaps(a)
    s = live_sample(a, n)
    json.dump({"gaps": g, "sample": s}, open("out/check.json", "w"), indent=1)
    print("volumes with gaps or shared numbers:", len(g), "of", a["citation"].str.extract(r"^(\d+) FLRA")[0].nunique())
    print("sample:", len(s), "citation on page:", sum(x["citation_on_page"] for x in s), "case on page:", sum(x["case_on_page"] for x in s),
          "non-200:", sum(x["status"] != 200 for x in s))
