import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import flra

FX = os.path.join(os.path.dirname(__file__), "fixtures")


def load(n):
    return open(os.path.join(FX, n), encoding="utf-8").read()


def test_new_authority_page():
    d, p = flra.parse_page(load("auth_new.html"), 0)
    assert len(d) == 10 and p == []
    first = d[0]
    assert first["citation"] == "74 FLRA 660" and first["issuance_date"] == "2026-10-30"
    assert first["case_number"] == "0-AR-6112" and first["arbitrator"] == "Nicholas"
    assert first["pdf_url"].endswith("/system/files/decisions/v74_89.pdf")
    assert first["digest_url"] and first["pdf_size"] == "460.32 KB"
    assert "Federal Energy Regulatory Commission" in first["parties_or_detail"]


def test_old_authority_page_is_html_only():
    d, p = flra.parse_page(load("auth_old.html"), 500)
    assert len(d) == 10 and p == []
    assert all(r["pdf_url"] is None and r["html_url"] for r in d)
    assert d[0]["issuance_date"] == "1992-03-23"


def test_fsip_page():
    d, p = flra.parse_fsip_page(load("fsip_new.html"), 0)
    assert len(d) == 10 and p == []
    assert d[0]["case_number"] == "2024 FSIP 079" and d[0]["issuance_date"] == "2025-01-15"
    assert "AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES" in d[0]["parties"]


def test_unparseable_row_is_reported_not_dropped():
    page = '<tr class="group-one first"><td>nothing</td></tr><tr class="group-one last"><td>x</td></tr>'
    d, p = flra.parse_page(page, 3)
    assert d == [] and p and p[0]["why"] == "not a metadata row"


def test_bad_date_is_flagged():
    assert flra.iso_date("Sept. 5, 2001") == "2001-09-05"
    assert flra.iso_date("garbage") is None


def test_fsip_blank_case_number_row_is_kept():
    page = open(os.path.join(os.path.dirname(__file__), "..", "raw", "fsip", "0002.html"), encoding="utf-8").read() if os.path.exists(
        os.path.join(os.path.dirname(__file__), "..", "raw", "fsip", "0002.html")) else None
    if page is None:
        return  # raw pages are untracked; run after crawling
    d, p = flra.parse_fsip_page(page, 2)
    assert len(d) == 10 and p == []
    assert d[0]["case_number"] == "" and d[0]["case_number_from_pdf_name"] == "22 FSIP 025"


def test_refresh_merge_keeps_old_and_new_wins():
    import pandas as pd
    import refresh
    old = pd.DataFrame({"html_url": ["a", "b"], "v": [1, 1]})
    new = pd.DataFrame({"html_url": ["b", "c"], "v": [2, 2]})
    m = refresh.merge(old, new).set_index("html_url")
    assert sorted(m.index) == ["a", "b", "c"] and m.loc["b", "v"] == 2
