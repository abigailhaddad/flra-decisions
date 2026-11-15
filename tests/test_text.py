import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import text
from build_text import case_check

FX = os.path.join(os.path.dirname(__file__), "fixtures")


def load(n):
    return open(os.path.join(FX, n), encoding="utf-8").read()


def test_1979_pre_formatted_decision():
    status, t, nbody, pdfs = text.extract(load("text_1979_v01_001.html"))
    assert status == "ok" and nbody == 1 and pdfs == []
    assert t.startswith("[ v01 p75 ]\n\n01:0075(1)RO\n\nThe decision of the Authority follows:\n\n1 FLRA No. 1\nJanuary 23, 1979")
    assert t.endswith("Cc: (W/c Enclosure)\n\nJ. Mceleney\n\nNteu\n\nP. Wright\n\nAction")
    assert "22-08642(RO)" in t
    # navigation, page title and footer are outside the body field
    assert "Skip to main content" not in t and "Privacy" not in t
    assert "Assistant Secretary Case No. 22-08642 (RO), FLRC No. 78A-187" not in t  # the page title
    assert "  " not in t and "\t" not in t


def test_2012_decision():
    status, t, nbody, pdfs = text.extract(load("text_2012_v66_78.html"))
    assert status == "ok" and nbody == 1
    assert t.startswith("66 FLRA No. 78\n\nAMERICAN FEDERATION\n\nOF GOVERNMENT EMPLOYEES")
    assert t.endswith("the text of which it attaches to its exceptions.")
    assert "Before the Authority: Carol Waller Pope, Chairman, and" in t
    assert "Skip to main content" not in t


def test_fsip_page_with_title_only_is_empty():
    status, t, nbody, pdfs = text.extract(load("text_fsip_1988_no_body.html"))
    assert (status, t, nbody) == ("empty", "", 0)


def test_normalise_keeps_words_and_one_blank_line():
    assert text.normalise("  a  b \t c \n\n\n\n d  ") == "a b c\n\nd"


def test_case_check():
    assert case_check("authority", "0-AR-5751", "x 0‑AR‑5751 y") == "all"  # non-breaking hyphens
    assert case_check("authority", "O-NG-339", "Case No. 0-NG-339") == "all"  # letter O vs zero
    assert case_check("authority", "DA-CA-1, DA-CA-2", "DA-CA-1 only") == "some"
    assert case_check("fsip", "2000 FSIP 063", "Case No. 00 FSIP 63") == "all"
    assert case_check("fsip", "2000 FSIP 063", "Case No. 00 FSIP 630") == "none"
    assert case_check("fsip", "", "anything") == "no_case_number"
