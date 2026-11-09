"""Turn the saved listing pages into two parquet files and a reconciliation report.

    python src/build.py     # reads raw/authority and raw/fsip, writes out/

Reports, never hides: pages that don't hold the usual 10 decisions, rows that don't parse,
duplicate citations or case numbers, and how many decisions each page range contributed.
"""
import glob, json, os, sys
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import flra


def read(kind, parser):
    recs, problems, per_page = [], [], {}
    # raw/fsip_asc is a second pass of the same listing sorted the other way. The listing orders ties
    # unstably, so one pass can miss a row and repeat another; the union of both passes is complete.
    paths = sorted(glob.glob(f"raw/{kind}/*.html")) + sorted(glob.glob(f"raw/{kind}_asc/*.html"))
    for path in paths:
        n = int(os.path.basename(path)[:4])
        if "_asc/" in path:
            n += 1000
        d, p = parser(open(path, encoding="utf-8").read(), n)
        per_page[n] = len(d)
        recs += d
        problems += p
    return recs, problems, per_page


def main():
    os.makedirs("out", exist_ok=True)
    report = {}
    for kind, parser, keycol, name in (("authority", flra.parse_page, "citation", "authority_decisions"),
                                       ("fsip", flra.parse_fsip_page, "case_number", "fsip_decisions")):
        recs, problems, per_page = read(kind, parser)
        df = pd.DataFrame(recs)
        n_rows_read = len(df)
        df = df.drop_duplicates("html_url", keep="first").reset_index(drop=True)
        odd = {p: c for p, c in per_page.items() if c != 10 and p < 1000}
        dup_keys = df[df.duplicated([keycol], keep=False)][keycol].nunique() if len(df) else 0  # same citation, different page
        report[kind] = {"pages_read": len(per_page), "rows_read": n_rows_read, "decisions": len(df),
                        "pages_not_10": odd, "problems": problems[:50], "n_problems": len(problems),
                        "citations_appearing_more_than_once": int(dup_keys),
                        "date_min": str(df["issuance_date"].min()), "date_max": str(df["issuance_date"].max()),
                        "no_pdf": int(df["pdf_url"].isna().sum()), "no_html": int(df["html_url"].isna().sum())}
        df.to_parquet(f"out/{name}.parquet", index=False)
    json.dump(report, open("out/report.json", "w"), indent=1)
    print(json.dumps({k: {a: b for a, b in v.items() if a != "problems"} for k, v in report.items()}, indent=1))


if __name__ == "__main__":
    main()
