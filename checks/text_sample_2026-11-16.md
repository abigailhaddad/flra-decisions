# Decision text spot-check, 2026-11-16

Built from out/decision_text.parquet; live pages re-fetched 2026-11-16. 30 random rows (seed 20261115) plus edge cases, 60 rows in all.
Second reading: lxml text_content() of the whole live page (no container selection), or pypdf for PDF-sourced rows. A start/end is 'found' when our first/last 120 characters (whitespace collapsed) appear verbatim in that text. 'Whole text found' means our entire text, with all whitespace removed, is a substring of the live text with all whitespace removed (catches dropped or added passages in the middle).

Result: of 53 rows with text, opening found 43, closing found 44, whole text found 45, case number found 48. Rows with no text: 7.

### 59 FLRA 547 (authority, 2003-12-31 00:00:00) — random

- Page: https://www.flra.gov/decisions/v59/59-095.html
- Our status: `ok`, 16,046 characters; live fetch HTTP 200
- Opening, ours: `[ v59 p547 ] 59 FLRA No. 95 AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES NATIONAL COUNCIL OF FIELD LABOR LOCALS LOCAL 239`
- Live, 150 chars before it: `d Labor Locals, Local 2391 (Union) and United States, Department of Labor, Employee Benefit Security Administration, Seattle, Washington and (Agency) `
- Closing, ours: `t provisions of the parties' agreement and the cited law and regulations are set forth in the Appendix to this decision.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3680` in our text: all

### 07 FLRA 764 (authority, 1982-01-28 00:00:00) — random

- Page: https://www.flra.gov/decisions/v07/07-128.html
- Our status: `ok`, 2,264 characters; live fetch HTTP 200
- Opening, ours: `[ v07 p764 ] 07:0764(128)NG The decision of the Authority follows: 7 FLRA No. 128 AMERICAN FEDERATION OF GOVERNMENT EMPL`
- Live, 150 chars before it: `ty)&nbsp; American Federation of Government Employees, Local 1170, AFL-CIO (Union) and Public Health Service Hospital, Seattle, Washington (Activity) `
- Closing, ours: ` /1/ IN SO DECIDING TO DISMISS THIS CASE, THE AUTHORITY MAKES NO JUDGMENT ON THE NEGOTIABILITY OF THE PROPOSAL INVOLVED.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `O-NG-503` in our text: all

### 01 FLRA 252 (authority, 1979-05-01 00:00:00) — random

- Page: https://www.flra.gov/decisions/v01/01-033.html
- Our status: `ok`, 23,433 characters; live fetch HTTP 200
- Opening, ours: `[ v01 p252 ] 01:0252(33)RO The decision of the Authority follows: 1 FLRA NO. 33 DEPARTMENT OF STATE, PASSPORT OFFICE, CH`
- Live, 150 chars before it: `tment of State, Passport Office, Chicago Passport Agency (Activity) and American Federation of Government Employees, Local 3671, AFL-CIO (Petitioner) `
- Closing, ours: `ATION SERVICES OFFICES (DCASO'S), AKRON, OHIO, A/SLMR 687, 5 FLRC 631 (FLRC NO. 76A-97 (JULY 20, 1977), REPORT NO. 131).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `50-13100(RO)` in our text: all

### 57 FLRA 567 (authority, 2001-10-03 00:00:00) — random

- Page: https://www.flra.gov/decisions/v57/57-100.html
- Our status: `ok`, 2,856 characters; live fetch HTTP 200
- Opening, ours: `[ v57 p567 ] 57 FLRA No. 100 DEFENSE LOGISTICS AGENCY DEFENSE DISTRIBUTION DEPOT SAN JOAQUIN, CALIFORNIA (Activity) and `
- Live, 150 chars before it: `yees, AFL-CIO (Petitioner/Labor Organization) and Laborers' International Union of North America, Local 1276, AFL-CIO (Intervenor/Labor Organization) `
- Closing, ours: `ppropriately refused to consider the claims relating to this issue, pursuant to § 2429.5 of the Authority's Regulations.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `WA-RP-00062-Rec` in our text: all

### 56 FLRA 737 (authority, 2000-09-26 00:00:00) — random

- Page: https://www.flra.gov/decisions/v56/56-123.html
- Our status: `ok`, 32,911 characters; live fetch HTTP 200
- Opening, ours: `[ v56 p737 ] 56 FLRA No. 123 NATIONAL FEDERATION OF FEDERAL EMPLOYEES, FOREST SERVICE COUNCIL LOCAL 1771 (Union) and U.S`
- Live, 150 chars before it: `ral Employees, Forest Service Council, Local 1771 (Union) and U.S. Department of Agriculture, Forest Service, Shasta Trinity National Forest (Agency) `
- Closing, ours: `s to conclude that the findings made by the Arbitrator do not support his award of attorney fees or are contrary to law.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3262` in our text: all

### 14 FLRA 73 (authority, 1984-03-16 00:00:00) — random

- Page: https://www.flra.gov/decisions/v14/14-016.html
- Our status: `ok`, 5,918 characters; live fetch HTTP 200
- Opening, ours: `[ v14 p73 ] 14:0073(16)CU The decision of the Authority follows: 14 FLRA No. 16 DEPARTMENT OF THE ARMY U.S. ARMY CONCORD`
- Live, 150 chars before it: `and David Keuther -- 1984 FLRAdec RP 14:0073(16)CU - Army, Army Concord District Recruiting Command, Concord, NH and David Keuther -- 1984 FLRAdec RP `
- Closing, ours: `ed not more than 105 days and not less than 60 days before the expiration date of the collective bargaining agreement(.)`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `1-DR-20001` in our text: all

### 49 FLRA 1589 (authority, 1994-07-15 00:00:00) — random

- Page: https://www.flra.gov/decisions/v49/49-144.html
- Our status: `ok`, 14,600 characters; live fetch HTTP 200
- Opening, ours: `[ v49 p1589 ] 49:1589(144)AR The decision of the Authority follows: 49 FLRA No. 144 FEDERAL LABOR RELATIONS AUTHORITY WA`
- Live, 150 chars before it: ` FLRAdec AR - - v49 p1589 49:1589(144)AR - - AFGE Local 2608 and HHS, SSA, NY Region 2, San Juan Teleservice Center - - 1994 FLRAdec AR - - v49 p1589 `
- Closing, ours: `rior management approval, the working of credit hours is conditioned on the availability of appropriate work." Id. at 7.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-2589` in our text: all

### 35 FLRA 377 (authority, 1990-04-02 00:00:00) — random

- Page: https://www.flra.gov/decisions/v35/35-044.html
- Our status: `ok`, 13,808 characters; live fetch HTTP 200
- Opening, ours: `[ v35 p377 ] 35:0377(44)AR The decision of the Authority follows: 35 FLRA No. 44 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: `35:0377(44)AR - - SSA and AFGE Local 1923 - - 1990 FLRAdec AR - - v35 p377 35:0377(44)AR - - SSA and AFGE Local 1923 - - 1990 FLRAdec AR - - v35 p377 `
- Closing, ours: `, it is unnecessary to address the Agency's other exception contending that the award is contrary to 5 C.F.R. § 430.205.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-1633` in our text: all

### 33 FLRA 819 (authority, 1988-11-03 00:00:00) — random

- Page: https://www.flra.gov/decisions/v33/33-092.html
- Our status: `ok`, 1,803 characters; live fetch HTTP 200
- Opening, ours: `[ v33 p819 ] 33:0819(92)AR The decision of the Authority follows: 33 FLRA No. 92 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: `ec AR - - v33 p819 33:0819(92)AR - - Royal C. Johnson Veterans Memorial Hospital, Sioux Fall, SD and AFGE Local 1509 - - 1988 FLRAdec AR - - v33 p819 `
- Closing, ours: `_________ Clyde B. Blandford, Jr. Acting Executive Director FOOTNOTES: (If blank, the decision does not have footnotes.)`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-1596` in our text: all

### 05 FLRA 333 (authority, 1981-03-20 00:00:00) — random

- Page: https://www.flra.gov/decisions/v05/05-045.html
- Our status: `ok`, 14,478 characters; live fetch HTTP 200
- Opening, ours: `[ v05 p333 ] 05:0333(45)CA The decision of the Authority follows: 5 FLRA No. 45 OFFICE OF PROGRAM OPERATIONS, FIELD OPER`
- Live, 150 chars before it: `ancisco Region (Respondent) and Council of District Office Locals, American Federation of Government Employees, San Francisco Region (Charging Party) `
- Closing, ours: `EIN, I NEED NOT DECIDE WHETHER THE UNION WAIVED ITS RIGHT TO NEGOTIATE AND RETAINED ONLY THE LIMITED RIGHT TO "CONSULT."`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `9-CA-57` in our text: all

### 24 FLRA 154 (authority, 1986-11-21 00:00:00) — random

- Page: https://www.flra.gov/decisions/v24/24-022.html
- Our status: `ok`, 37,269 characters; live fetch HTTP 200
- Opening, ours: `[ v24 p154 ] 24:0154(22)CA The decision of the Authority follows: 24 FLRA No. 22 DEFENSE MAPPING AGENCY, WASHINGTON, D.C`
- Live, 150 chars before it: `0154(22)CA - Defense Mapping Agency, Washington, DC and Defense Mapping Agency Aerospace Center, St. Louis, MO and NFFE Local 1827 -- 1986 FLRAdec CA `
- Closing, ours: `on VII, whose address is: 535 - 16th Street, Suite 310, Denver, CO 80202, and whose telephone number is: (303) 837-5224.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `7-CA-50623` in our text: all

### 70 FLRA 496 (authority, 2018-04-20 00:00:00) — random

- Page: https://www.flra.gov/decisions/v70/70-100.html
- Our status: `ok`, 2,007 characters; live fetch HTTP 200
- Opening, ours: `70 FLRA No. 100 UNITED STATES DEPARTMENT OF VETERANS AFFAIRS MEDICAL CENTER (Agency) and NATIONAL ASSOCIATION OF GOVERNM`
- Live, 150 chars before it: ` (Union) United States Department of Veterans Affairs, Medical Center (Agency) and National Association of Government Employees, Local R5-136 (Union) `
- Closing, ours: `or; does not represent a plausible interpretation of the agreement; or evidences a manifest disregard of the agreement).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-5337` in our text: all

### 54 FLRA 1115 (authority, 1998-09-24 00:00:00) — random

- Page: https://www.flra.gov/decisions/v54/54-096.html
- Our status: `ok`, 1,252 characters; live fetch HTTP 200
- Opening, ours: `[ v54 p1115 ] 54:1115(96)AR The decision of the Authority follows: 54 FLRA No. 96 FEDERAL LABOR RELATIONS AUTHORITY WASH`
- Live, 150 chars before it: ` GA - - 1998 FLRAdec AR - - v54 p1115 54:1115(96)AR - - AFGE Local 987 and Air Force, Robins AFB, Warner Robins, GA - - 1998 FLRAdec AR - - v54 p1115 `
- Closing, ours: `f the grounds raised in the exceptions and set forth in section 7122(a). Accordingly, the Union's exceptions are denied.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3069` in our text: all

### 06 FLRA 292 (authority, 1981-07-20 00:00:00) — random

- Page: https://www.flra.gov/decisions/v06/06-054.html
- Our status: `ok`, 9,493 characters; live fetch HTTP 200
- Opening, ours: `[ v06 p292 ] 06:0292(54)AR The decision of the Authority follows: 6 FLRA No. 54 HEADQUARTERS, SAN ANTONIO AIR LOGISTICS `
- Live, 150 chars before it: ` Logistics Center, Kelly Air Force, Texas (Activity) and American Federation of Government Employees, Local 1617, AFL-CIO, San Antonio, Texas (Union) `
- Closing, ours: `CRETARY FOR LABOR-MANAGEMENT RELATIONS IN EFFECT AT THE TIME OF THE CONSOLIDATION OF THE AFLC-WIDE UNIT IN JANUARY 1978.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `O-AR-96` in our text: all

### 03 FLRA 555 (authority, 1980-06-30 00:00:00) — random

- Page: https://www.flra.gov/decisions/v03/03-090.html
- Our status: `ok`, 9,837 characters; live fetch HTTP 200
- Opening, ours: `[ v03 p555 ] 03:0555(90)AR The decision of the Authority follows: 3 FLRA No. 90 FEDERAL EMPLOYEES METAL TRADES COUNCIL U`
- Live, 150 chars before it: `ncil (Union) and Mare Island Naval Shipyard (Activity)&nbsp; Federal Employees Metal Trades Council (Union) and Mare Island Naval Shipyard (Activity) `
- Closing, ours: `TE OR THE RESULT WHICH WOULD BE REACHED BY THE AUTHORITY IF THE CASE HAD ARISEN UNDER THE STATUTE RATHER THAN THE ORDER.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `FLRC No. 78A-42` in our text: all

### 14 FLRA 65 (authority, 1984-03-16 00:00:00) — random

- Page: https://www.flra.gov/decisions/v14/14-015.html
- Our status: `ok`, 16,144 characters; live fetch HTTP 200
- Opening, ours: `[ v14 p65 ] 14:0065(15)NG The decision of the Authority follows: 14 FLRA No. 15 NATIONAL TREASURY EMPLOYEES UNION Union `
- Live, 150 chars before it: ` Home Decisions 14:0065(15)NG - NTEU and IRS, San Francisco, CA -- 1984 FLRAdec NG 14:0065(15)NG - NTEU and IRS, San Francisco, CA -- 1984 FLRAdec NG `
- Closing, ours: `h section 7106(a)(2)(A) or (b)(1) of the Statute. /7/ Union petition for review at 1; Agency statement of position at 1.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `O-NG-535` in our text: all

### 66 FLRA 441 (authority, 2012-01-25 00:00:00) — random

- Page: https://www.flra.gov/decisions/v66/66-84.html
- Our status: `ok`, 43,951 characters; live fetch HTTP 200
- Opening, ours: `66 FLRA No. 84 UNITED STATES DEPARTMENT OF TRANSPORTATION FEDERAL AVIATION ADMINISTRATION (Agency) and PROFESSIONAL AVIA`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: `clude the Agency from asserting that § 255(a) barred the recovery sought in the grievance and ordered by the Arbitrator.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-4713` in our text: all

### 19 FLRA 541 (authority, 1985-08-06 00:00:00) — random

- Page: https://www.flra.gov/decisions/v19/19-070.html
- Our status: `ok`, 1,442 characters; live fetch HTTP 200
- Opening, ours: `[ v19 p541 ] 19:0541(70)NG The decision of the Authority follows: 19 FLRA No. 70 NATIONAL TREASURY EMPLOYEES UNION Union`
- Live, 150 chars before it: `s 19:0541(70)NG - NTEU and Treasury, IRS National Office -- 1985 FLRAdec NG 19:0541(70)NG - NTEU and Treasury, IRS National Office -- 1985 FLRAdec NG `
- Closing, ours: `sed. For the Authority. Issued, Washington, D.C., August 6, 1985 Harold D. Kessler Managing Director for Case Processing`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `O-NG-1151` in our text: all

### 64 FLRA 1163 (authority, 2010-07-30 00:00:00) — random

- Page: https://www.flra.gov/decisions/v64/64-204.html
- Our status: `ok`, 18,927 characters; live fetch HTTP 200
- Opening, ours: `MEMORANDUM 64 FLRA No. 204 FEDERAL LABOR RELATIONS AUTHORITY WASHINGTON, D.C. _____ AMERICAN FEDERATION OF GOVERNMENT EM`
- Live, 150 chars before it: `an Federation of Government Employees, Local 2382 (Union) and United States Department of Veterans Affairs, Medical Center, Phoenix, Arizona (Agency) `
- Closing, ours: `ation, examination, or treatment, or to the period of disability while the patient was receiving professional treatment.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-4419` in our text: all

### 52 FLRA 400 (authority, 1996-10-08 00:00:00) — random

- Page: https://www.flra.gov/decisions/v52/52-038.html
- Our status: `ok`, 1,714 characters; live fetch HTTP 200
- Opening, ours: `[ v52 p400 ] 52:0400(38)AR The decision of the Authority follows: 52 FLRA No. 38 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: `1996 FLRAdec AR - - v52 p400 52:0400(38)AR - - NFFE, Local 858 and Agriculture, Farm Service Agency, Kansas City, MO - - 1996 FLRAdec AR - - v52 p400 `
- Closing, ours: `ration, Pittsburg, Kansas and American Federation of Government Employees, AFL-CIO, Local 1336, 27 FLRA 154, 155 (1987).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-2845` in our text: all

### 32 FLRA 633 (authority, 1988-07-13 00:00:00) — random

- Page: https://www.flra.gov/decisions/v32/32-092.html
- Our status: `ok`, 9,825 characters; live fetch HTTP 200
- Opening, ours: `[ v32 p633 ] 32:0633(92)AR The decision of the Authority follows: 32 FLRA No. 92 UNITED STATES OF AMERICA BEFORE THE FED`
- Live, 150 chars before it: `Philadelphia MTC - - 1988 FLRAdec AR - - v32 p633 32:0633(92)AR - - Philadelphia Naval Shipyard and Philadelphia MTC - - 1988 FLRAdec AR - - v32 p633 `
- Closing, ours: `airman Jean McKee, Member FEDERAL LABOR RELATIONS AUTHORITY FOOTNOTES: (If blank, the decision does not have footnotes.)`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-1525` in our text: all

### 42 FLRA 845 (authority, 1991-10-10 00:00:00) — random

- Page: https://www.flra.gov/decisions/v42/42-057.html
- Our status: `ok`, 26,145 characters; live fetch HTTP 200
- Opening, ours: `[ v42 p845 ] 42:0845(57)NG The decision of the Authority follows: 42 FLRA No. 57 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: ` - - Tidewater Virginia Federal Employee Metal Trades Council and Navy, Norfolk Naval Shipyard, Portsmouth, Virginia - - 1991 FLRAdec NG - - v42 p845 `
- Closing, ours: ` existing agreement. 2. In finding this proposal to be within the duty to bargain, we make no judgment as to its merits.`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): True
- Case number `0-NG-1821` in our text: all

### 33 FLRA 604 (authority, 1988-10-28 00:00:00) — random

- Page: https://www.flra.gov/decisions/v33/33-077.html
- Our status: `ok`, 29,167 characters; live fetch HTTP 200
- Opening, ours: `[ v33 p604 ] 33:0604(77)NG The decision of the Authority follows: 33 FLRA No. 77 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: `ec NG - - v33 p604 33:0604(77)NG - - NFFE Local 405 and Army Aviation Systems Command and Army Troop Support Command - - 1988 FLRAdec NG - - v33 p604 `
- Closing, ours: `e decision does not have footnotes.) */ In finding this proposal to be negotiable, we make no judgment as to its merits.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-NG-1546` in our text: all

### 28 FLRA 1134 (authority, 1987-09-23 00:00:00) — random

- Page: https://www.flra.gov/decisions/v28/28-147.html
- Our status: `ok`, 10,641 characters; live fetch HTTP 200
- Opening, ours: `[ v28 p1134 ] 28:1134(147)NG The decision of the Authority follows: 28 FLRA NO. 147 AMERICAN FEDERATION OF GOVERNMENT EM`
- Live, 150 chars before it: `ome Decisions 28:1134(147)NG - AFGE, LOCAL 1625 VS NAVY, FLEET COMBAT TRAINING CE 28:1134(147)NG - AFGE, LOCAL 1625 VS NAVY, FLEET COMBAT TRAINING CE `
- Closing, ours: `lity appeal contained four proposals. However, the parties have withdrawn sections 1111, 2402, and 3705 from the appeal.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-NG-1417` in our text: all

### 54 FLRA 700 (authority, 1998-07-31 00:00:00) — random

- Page: https://www.flra.gov/decisions/v54/54-073.html
- Our status: `ok`, 11,780 characters; live fetch HTTP 200
- Opening, ours: `[ v54 p700 ] 54:0700(73)AR The decision of the Authority follows: 54 FLRA No. 73 FEDERAL LABOR RELATIONS AUTHORITY WASHI`
- Live, 150 chars before it: `s International Union of North America, Local 1376 and HHS, Public Health Service, Navajo Area Indian Health Service - - 1998 FLRAdec AR - - v54 p700 `
- Closing, ours: `n's exception. V. Decision The Union's exception is denied. FOOTNOTES: (If blank, the decision does not have footnotes.)`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3006` in our text: all

### 2011 FSIP 115 (fsip, 2011-12-22 00:00:00) — random

- Page: https://www.flra.gov/fsip/2011fs_-23
- Our status: `ok`, 14,685 characters; live fetch HTTP 200
- Opening, ours: `In the Matter of DEPARTMENT OF THE AIR FORCE CHILD DEVELOPMENT CENTER TYNDALL AIR FORCE BASE, FLORIDA and AMERICAN FEDER`
- Live, 150 chars before it: `tion eFiling Available Here Breadcrumb Home DEPARTMENT OF THE AIR FORCE, CAMERICAN FEDERATION OF DEPARTMENT OF THE AIR FORCE, CAMERICAN FEDERATION OF `
- Closing, ours: `mber Edward F. Hartfield. [2]/ Management document entitled “Flex and Regular Hours Work (sic) s-CDC, 10/17/11-11/11/11.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `2011 FSIP 115` in our text: all

### 14 FLRA 712 (authority, 1984-05-24 00:00:00) — random

- Page: https://www.flra.gov/decisions/v14/14-096.html
- Our status: `ok`, 42,497 characters; live fetch HTTP 200
- Opening, ours: `[ v14 p712 ] 14:0712(96)CA The decision of the Authority follows: 14 FLRA No. 96 DEPARTMENT OF HEALTH AND HUMAN SERVICES`
- Live, 150 chars before it: `6)CA - HHS, SSA, San Francisco Region, San Francisco, CA and AFGE Council of Security District Office Locals, San Francisco Region -- 1984 FLRAdec CA `
- Closing, ours: `her than whether the meetings involved were "formal discussion(s)," was denied by the Authority. See 1 FLRA 137, No. 14.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `9-CA-578` in our text: all

### 56 FLRA 973 (authority, 2000-12-05 00:00:00) — random

- Page: https://www.flra.gov/decisions/v56/56-163.html
- Our status: `ok`, 24,204 characters; live fetch HTTP 200
- Opening, ours: `[ v56 p973 ] 56 FLRA No. 163 DEPARTMENT OF THE ARMY U.S. ARMY CORPS OF ENGINEERS LOS ANGELES DISTRICT LOS ANGELES, CALIF`
- Live, 150 chars before it: `s, Local 777 (Petitioner/Exclusive Representative) and International Federation of Professional and Technical Engineers, AFL-CIO (Labor Organization) `
- Closing, ours: ` where the RD quoted the ballot as stating that "[o]nce NFFE has affiliated with [IAM] we will no longer have a choice."`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `SF-RP-90103` in our text: all

### 56 FLRA 632 (authority, 2000-09-12 00:00:00) — random

- Page: https://www.flra.gov/decisions/v56/56-101.html
- Our status: `ok`, 19,974 characters; live fetch HTTP 200
- Opening, ours: `[ v56 p632 ] 56 FLRA No. 101 AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES, LOCAL 1501 (Union) and U.S. DEPARTMENT OF THE `
- Live, 150 chars before it: `cy) American Federation of Government Employees, Local 1501 (Union) and U.S. Department of the Air Force, Mcchord Air Force Base, Washington (Agency) `
- Closing, ours: `tinent part, for an appeal "within seven (7) calendar days after receipt of the first step decision." Second Award at 2.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3249` in our text: all

### 1998 FSIP 064 (fsip, 1998-05-12 00:00:00) — random

- Page: https://www.flra.gov/fsip/1998fs_-17
- Our status: `ok`, 45,231 characters; live fetch HTTP 200
- Opening, ours: `United States of America BEFORE THE FEDERAL SERVICE IMPASSES PANEL In the Matter of U.S. ARMY CORPS OF ENGINEERS SOUTH P`
- Live, 150 chars before it: `MY CORPS OF ENGINEERS SOUTH PACIFIC DIVISION SAN FRANCISCO, CALIFORNIA and LOCAL 49, INTERNATIONAL FEDERATION OF PROFESSIONAL AND TECHNICAL ENGINEERS `
- Closing, ours: `rning the SPD HQ FY98 drawdown and RIF. 1.The parties’ final offers are attached to this decision as Appendices A and B.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `1998 FSIP 064` in our text: all

### 01 FLRA 75 (authority, 1979-01-23 00:00:00) — oldest Authority

- Page: https://www.flra.gov/decisions/v01/01-001.html
- Our status: `ok`, 2,092 characters; live fetch HTTP 200
- Opening, ours: `[ v01 p75 ] 01:0075(1)RO The decision of the Authority follows: 1 FLRA No. 1 January 23, 1979 MR. STANLEY A. GORDON EXEC`
- Live, 150 chars before it: `, Assistant Secretary Case No. 22-08642 (RO), FLRC No. 78A-187 ACTION, Washington, D.C., Assistant Secretary Case No. 22-08642 (RO), FLRC No. 78A-187 `
- Closing, ours: `. Sincerely, Harold D. Kessler Deputy Executive Director Enclosure Cc: (W/c Enclosure) J. Mceleney Nteu P. Wright Action`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `22-08642(RO)` in our text: all

### 74 FLRA 660 (authority, 2026-10-30 00:00:00) — newest Authority

- Page: https://www.flra.gov/decisions/v74/74-89
- Our status: `ok`, 38,924 characters; live fetch HTTP 200
- Opening, ours: `74 FLRA No. 89 AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES LOCAL 421 (Union) and FEDERAL ENERGY REGULATORY COMMISSION (A`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: ` breach of agreement). [114] Award at 15-16; see id. at 13-14, 17. [115] NTEU III, 73 FLRA at 820; CFPB, 73 FLRA at 679.`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-6112` in our text: all

### 1988 FSIP 157 (fsip, 1988-09-16 00:00:00) — oldest FSIP

- Page: https://www.flra.gov/fsip/1988fs_-0
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 2024 FSIP 079 (fsip, 2025-01-15 00:00:00) — newest FSIP

- Page: https://www.flra.gov/fsip/2024fs_-6
- Our status: `ok`, 17,462 characters; live fetch HTTP 200
- Opening, ours: `ARBITRATOR’S OPINION AND DECISION The American Federation of Government Employees, Local 3954 (Union), filed a request f`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: ` its determination on the totality of the evidence presented.” S. REP. NO. 97-365, 97th Cong., 2d Sess. at 15-16 (1982).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `2024 FSIP 079` in our text: none

### 2010 FSIP 010 (fsip, 2011-01-10 00:00:00) — longest

- Page: https://www.flra.gov/fsip/2010fs_-11
- Our status: `ok`, 331,628 characters; live fetch HTTP 200
- Opening, ours: `ARBITRATOR’S OPINION AND DECISION The National Treasury Employees Union (Union or NTEU) filed a request for assistance w`
- Live, 150 chars before it: `AU OF CUSTOMS AND BORDER PROTECTION, WASHINGTON,&amp;nbsp;D.C. and NATIONAL&amp;nbsp;TREASURY&amp;nbsp;EMPLOYEES&amp;nbsp;UNION &amp;nbsp; &amp;nbsp; `
- Closing, ours: ` will be rare and that the Union will bear a heavy burden of justifying such requests if they are denied and arbitrated.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `2010 FSIP 010` in our text: none

### 56 FLRA 999 (authority, 2002-12-05 00:00:00) — shortest (with text)

- Page: https://www.flra.gov/decisions/v56/56-106.html
- Our status: `ok`, 16 characters; live fetch HTTP 200
- Opening, ours: `Decision Vacated`
- Live, 150 chars before it: `LRA on YouTube Course Materials Video Training Customer Feedback RSS Feeds Search Search description eFiling Available Here Breadcrumb Home Decisions `
- Closing, ours: `Decision Vacated`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `vacated` in our text: all

### 07 FLRA 13 (authority, 1981-10-15 00:00:00) — shortest (with text)

- Page: https://www.flra.gov/decisions/v07/07-005.html
- Our status: `partial`, 18 characters; live fetch HTTP 200
- Opening, ours: `See attached text.`
- Live, 150 chars before it: `eld Operations, Boston Region, Social Security Administration (Activity) and Local 1164, American Federation of Government Employees, AFL-CIO (Union) `
- Closing, ours: `See attached text.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-92` in our text: none

### 66 FLRA 81 (authority, 2011-08-31 00:00:00) — PDF-era Authority (has pdf_url), random

- Page: https://www.flra.gov/decisions/v66/66-19.html
- Our status: `ok`, 50,009 characters; live fetch HTTP 200
- Opening, ours: `66 FLRA No. 19 UNITED STATES DEPARTMENT OF JUSTICE FEDERAL BUREAU OF PRISONS METROPOLITAN DETENTION CENTER, GUAYNABO SAN`
- Live, 150 chars before it: `n Center, Guaynabo, San Juan, Puerto Rico (Agency) and American Federation of Government Employees, Council of Prison Locals C-33, Local 4052 (Union) `
- Closing, ours: `t of the award to the parties for resubmission to the Arbitrator, absent settlement, to formulate an alternative remedy.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-4228` in our text: all

### 69 FLRA 176 (authority, 2016-01-27 00:00:00) — PDF-era Authority (has pdf_url), random

- Page: https://www.flra.gov/decisions/v69/69-26.html
- Our status: `ok`, 28,904 characters; live fetch HTTP 200
- Opening, ours: `69 FLRA No. 26 UNITED STATES DEPARTMENT OF JUSTICE FEDERAL BUREAU OF PRISONS FEDERAL CORRECTIONAL INSTITUTION BASTROP, T`
- Live, 150 chars before it: `eral Bureau of Prisons, Federal Correctional Institution, Bastrop, Texas (Agency) and American Federation of Government Employees, Local 3828 (Union) `
- Closing, ours: `aking out “hot trash,” the latter of which the Arbitrator found non‑compensable (see id. at 62‑63)). [73] See id. at 71.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-4921` in our text: all

### 63 FLRA 356 (authority, 2009-05-22 00:00:00) — first year with PDFs (2009)

- Page: https://www.flra.gov/decisions/v63/63-118.html
- Our status: `ok`, 28,880 characters; live fetch HTTP 200
- Opening, ours: `356 Decisions of the Federal Labor Relations Authority 63 FLRA No. 118 63 FLRA No. 118 UNITED STATES DEPARTMENT OF TRANS`
- Live, 150 chars before it: ` Aviation Administration (Agency/Petitioner) and American Federation of State, County, and Municipal Employees Council 26, AFL-CIO (Union/Petitioner) `
- Closing, ours: `n has failed to demonstrate that review is warranted on any of the asserted grounds, we deny the application for review.`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `WA-RP-08-0080 WA-RP-08-0084` in our text: all

### 1994 FSIP 121 (fsip, 1995-01-11 00:00:00) — FSIP random

- Page: https://www.flra.gov/fsip/1994fs_-14
- Our status: `ok`, 44,169 characters; live fetch HTTP 200
- Opening, ours: `United States of America BEFORE THE FEDERAL SERVICE IMPASSES PANEL In the Matter of DEPARTMENT OF THE INTERIOR NATIONAL `
- Live, 150 chars before it: `AL PARK SERVICE GOLDEN GATE NATIONAL RECREATION AREA SAN FRANCISCO, CALIFORNIA and LOCAL 1276, LABORERS INTERNATIONAL UNION OF NORTH AMERICA, AFL-CIO `
- Closing, ours: `Government Employees, AFL-CIO, Local 331 and Veterans Administration Hospital, Perry Point, Maryland, 2 FLRA 428 (1980).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `1994 FSIP 121` in our text: all

### 2003 FSIP 010 (fsip, 2003-05-23 00:00:00) — FSIP random

- Page: https://www.flra.gov/fsip/2003fs_-12
- Our status: `ok`, 13,865 characters; live fetch HTTP 200
- Opening, ours: `United States of America BEFORE THE FEDERAL SERVICE IMPASSES PANEL In the Matter of DEPARTMENT OF JUSTICE FEDERAL BUREAU`
- Live, 150 chars before it: `TICE FEDERAL BUREAU OF PRISONS FEDERAL CORRECTIONAL INSTITUTION SHERIDAN, OREGON and LOCAL 3979, AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES, AFL-CIO `
- Closing, ours: `e its determination on the totality of the evidence presented. S. REP. NO. 97-365, 97th Cong., 2d Sess. at 15-16 (1982).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `2003 FSIP 010` in our text: all

### 66 FLRA 763 (authority, 2012-07-13 00:00:00) — text from PDF (ok_pdf)

- Page: https://www.flra.gov/decisions/v66/66-144.html
- PDF (text source): https://www.flra.gov/system/files/decisions/v66_144.pdf
- Our status: `ok_pdf`, 31,745 characters; live fetch HTTP 200
- Opening, ours: `66 FLRA No. 144 Decisions of the Federal Labor Relations Authority 763 Background and Arbitrator’s Award 66 FLRA No. 144`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: `ve any additional evidence to submit. .... Union’s Exceptions, Ex. C at 1-5; Agency Opp’n, Ex. 2 at 1-2. 66 FLRA No. 144`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-4781` in our text: all

### 2015 FSIP 079 (fsip, 2015-12-15 00:00:00) — text from PDF (ok_pdf)

- Page: https://www.flra.gov/fsip/2015fs_-2
- PDF (text source): https://www.flra.gov/system/files/fsip/O%26D%2015%20FSIP%2079%20pdf.pdf
- Our status: `ok_pdf`, 28,188 characters; live fetch HTTP 200
- Opening, ours: `United States of America BEFORE THE FEDERAL SERVICE IMPASSES PANEL In the Matter of DEPARTMENT OF HOMELAND SECURITY BURE`
- Live, 150 chars before it: ``
- Closing, ours: `sed work schedule. By direction of the Panel. H. Joseph Schimansky Executive Director December 15, 2015 Washington, D.C.`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `2015 FSIP 079` in our text: all

### 64 FLRA 227 (authority, 2009-10-29 00:00:00) — text from PDF (ok_pdf)

- Page: https://www.flra.gov/decisions/v64/64-28.html
- PDF (text source): https://www.flra.gov/system/files/decisions/64_028.pdf
- Our status: `ok_pdf`, 20,134 characters; live fetch HTTP 200
- Opening, ours: `64 FLRA No. 28 Decisions of the Federal Labor Relations Authority 64 FLRA No. 28 UNITED STATES ENVIRONMENTAL PROTECTION `
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: ` the management decision and its impact to the designated union representative. Award at 3 and Exceptions, Attachment 1.`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-4153` in our text: all

### 64 FLRA 709 (authority, 2010-04-28 00:00:00) — page carried a different decision (text now from PDF)

- Page: https://www.flra.gov/decisions/v64/64-130.html
- PDF (text source): https://www.flra.gov/system/files/decisions/64_130.pdf
- Our status: `ok_pdf`, 17,000 characters; live fetch HTTP 200
- Opening, ours: `64 FLRA No. 130 Decisions of the Federal Labor Relations Authority 64 FLRA No. 130 NATIONAL ASSOCIATION OF INDEPENDENT L`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: ` manifest disregard of the agreement, and we deny this exception. V. Decision The exceptions are denied. 64 FLRA No. 130`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-4442` in our text: all

### 63 FLRA 581 (authority, 2009-07-31 00:00:00) — page carried a different decision (text now from PDF)

- Page: https://www.flra.gov/decisions/v63/63-162.html
- PDF (text source): https://www.flra.gov/system/files/decisions/63_162.pdf
- Our status: `ok_pdf`, 13,498 characters; live fetch HTTP 200
- Opening, ours: `63 FLRA No. 162 Decisions of the Federal Labor Relations Authority 63 FLRA No. 162 AMERICAN FEDERATION OF GOVERNMENT EMP`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: `ed that the Arbitrator’s award is deficient, we deny the Union’s exception. V. Decision The Union’s exception is denied.`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-4204` in our text: all

### 2019 FSIP 049 (fsip, 2019-12-10 00:00:00) — case number not found in text

- Page: https://www.flra.gov/fsip/2019fs_-15
- Our status: `ok`, 33,099 characters; live fetch HTTP 200
- Opening, ours: `DECISION AND ORDER This case, filed by the American Federation of Government Employees, Local 3254 (Union) on June 5, 20`
- Live, 150 chars before it: `AIR FORCE, GRISSOM AIR FORCE BASE, 434TH AIR RESERVE WING GRISSOM AIR FORCE BASE, INDIANA And AMERICAN FEDERATION OF GOVERNMENT EMPLOYEES, LOCAL 3254 `
- Closing, ours: `e.g., AFGE, Local 3807 and U.S. Dep’t of the Energy, Western Area Power Admin., Golden, Colorado, 55 FLRA 1, 4-5 (1998).`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `2019 FSIP 049` in our text: none

### 1992 FSIP 054 (fsip, 1992-11-02 00:00:00) — case number not found in text

- Page: https://www.flra.gov/fsip/1992fs_-54
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 1991 FSIP 085 (fsip, 1991-12-30 00:00:00) — case number not found in text

- Page: https://www.flra.gov/fsip/1991fs_-55
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 1991 FSIP 091 (fsip, 1991-07-24 00:00:00) — case number not found in text

- Page: https://www.flra.gov/fsip/1991fs_-68
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 63 FLRA 280 (authority, 2009-04-30 00:00:00) — status empty

- Page: https://www.flra.gov/decisions/v63/63-095.html
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 33 FLRA 891 (authority, 1988-12-27 00:00:00) — status empty

- Page: https://www.flra.gov/decisions/v33/33-129.html
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 2018 FSIP 060 (fsip, 2018-11-14 00:00:00) — status empty

- Page: https://www.flra.gov/fsip/2018fs_-0
- Our status: `empty`, 0 characters; live fetch HTTP 200
- We have no text. Live page text (first 400 chars): `Skip to main content An official website of the United States government Here’s how you know Here’s how you know Official websites use .gov A .gov website belongs to an official government organization in the United States. Secure .gov websites use HTTPS A lock (LockA locked padlock) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure`

### 71 FLRA 1244 (authority, 2020-12-28 00:00:00) — status ok_pdf

- Page: https://www.flra.gov/decisions/v71/71-235.html
- PDF (text source): https://www.flra.gov/system/files/decisions/v71_235.pdf
- Our status: `ok_pdf`, 9,923 characters; live fetch HTTP 200
- Opening, ours: `1244 Decisions of the Federal Labor Relations Authority 71 FLRA No. 235 UNITED STATES DEPARTMENT OF HOMELAND SECURITY U.`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: `d be dismissed, without prejudice. 70 FLRA 806, 810-11 (2018) (Dissenting Opinion of Member DuBester). * 71 FLRA No. 235`
- Live, 150 chars after it: `NOT FOUND`
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-5638` in our text: all

### 71 FLRA 1161 (authority, 2020-12-08 00:00:00) — status ok_pdf

- Page: https://www.flra.gov/decisions/v71/71-221.html
- PDF (text source): https://www.flra.gov/system/files/decisions/v71_221.PDF
- Our status: `ok_pdf`, 19,664 characters; live fetch HTTP 200
- Opening, ours: `71 FLRA No. 221 Decisions of the Federal Labor Relations Authority 71 FLRA No. 221 II. UNITED STATES DEPARTMENT OF THE T`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: ` deferential standard of review” as applied by federal courts “in private[-]sector labor-management issues”).ment issues`
- Live, 150 chars after it: ``
- Whole text found in live text (all whitespace removed): False
- Case number `0-AR-5409` in our text: all

### 71 FLRA 918 (authority, 2020-08-13 00:00:00) — status ok_pdf

- Page: https://www.flra.gov/decisions/v71/71-177.html
- PDF (text source): https://www.flra.gov/system/files/decisions/v71_177.pdf
- Our status: `ok_pdf`, 21,898 characters; live fetch HTTP 200
- Opening, ours: `918 Decisions of the Federal Labor Relations Authority 71 FLRA No. 177 NATIONAL WEATHER SERVICE EMPLOYEES ORGANIZATION (`
- Live, 150 chars before it: `NOT FOUND`
- Closing, ours: `dency of parallel proceedings in federal district court.’” Mot. at 4 (quoting SSA II, 71 FLRA at 763). 18 Majority at 5.`
- Live, 150 chars after it: ``
- Whole text found in live text (all whitespace removed): False
- Case number `0-MC-0030` in our text: all

### 61 FLRA 68 (authority, 2005-06-30 00:00:00) — status partial

- Page: https://www.flra.gov/decisions/v61/61-012.html
- Our status: `partial`, 527 characters; live fetch HTTP 200
- Opening, ours: `[ v61 p68 ] 61 FLRA No. 12 UNITED STATES GENERAL SERVICES ADMINISTRATION NORTHEAST AND CARIBBEAN REGION NEW YORK, NEW YO`
- Live, 150 chars before it: `istration, Northeast and Caribbean Region, New York, New York (Agency) and American Federation of Government Employees, Council 236, Region 2 (Union) `
- Closing, ours: `ter is before the Authority on exceptions to an attorney fee award of Arbitrator Joan Ilivicky filed by the Agency under`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3900` in our text: all

### 61 FLRA 38 (authority, 2005-06-09 00:00:00) — status partial

- Page: https://www.flra.gov/decisions/v61/61-005.html
- Our status: `partial`, 506 characters; live fetch HTTP 200
- Opening, ours: `[ v61 p38 ] 61 FLRA No. 5 UNITED STATES DEPARTMENT OF THE NAVY NAVAL AIR DEPOT CHERRY POINT, NORTH CAROLINA (Agency) and`
- Live, 150 chars before it: `he Navy, Naval Air Depot, Cherry Point, North Carolina (Agency) and International Association of Machinists and Aerospace Workers, Local 1859 (Union) `
- Closing, ours: `ase This case is before the Authority on exceptions to an award of Arbitrator Charles H. Frost filed by the Agency under`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `0-AR-3912` in our text: all

### 36 FLRA 253 (authority, 1990-06-29 00:00:00) — status partial

- Page: https://www.flra.gov/decisions/v36/36-032.html
- Our status: `partial`, 178 characters; live fetch HTTP 200
- Opening, ours: `[ v36 p253 ] 36:0253(32)CO The decision of the Authority follows: ----- FULL TEXT OF DECISION IS ATTACHED ----- [] FOOTN`
- Live, 150 chars before it: `an Francisco, CA - - 1990 FLRAdec CO - - v36 p253 Other Files ALJ's Decision (80.67 KB) 36 FLRA No. 32 9-CO-90016- Authority Decision_0.pdf (41.8 KB) `
- Closing, ours: `y follows: ----- FULL TEXT OF DECISION IS ATTACHED ----- [] FOOTNOTES: (If blank, the decision does not have footnotes.)`
- Live, 150 chars after it: ` Return to top Home About Us Components & Offices Case Types Decisions Resources & Training Contact Us U.S. FEDERAL LABOR RELATIONS AUTHORITY 1400 K S`
- Whole text found in live text (all whitespace removed): True
- Case number `9-CO-90016` in our text: none


---

## Full-table checks (all 11,533 rows, not a sample)

Built 2026-11-16 from pages fetched 2026-11-15 13:45 UTC to 2026-11-16 20:32 UTC and PDFs fetched 2026-11-16 20:33-20:49 UTC. Source tables: out/authority_decisions.parquet (10,462 rows) and out/fsip_decisions.parquet (1,071 rows) as on the decision-text branch.

### Row reconciliation

decision_text.parquet has 11,533 rows: 10,462 authority + 1,071 fsip. Its html_url set equals each source table's html_url set exactly (asserted in build_text.py); html_url is unique in both. No page was missing at build time (the build stops otherwise).

### Coverage by text_status

| table | ok (HTML) | ok_pdf | partial | empty | rows |
|---|---|---|---|---|---|
| authority | 10,420 | 36 | 4 | 2 | 10,462 |
| fsip | 959 | 4 | 0 | 108 | 1,071 |

No page returned 404 or 410 (no http_error rows); no row is wrong_page after the PDF fallback.

### Rows without full text (114)

**empty (110: 108 FSIP, 2 Authority).** The page has no decision body (title only) and the PDF is an image scan with no text layer. Checked for all 110: `pdffonts` lists no fonts and `pdfimages -list` lists page images. OCR was not attempted.

- https://www.flra.gov/decisions/v63/63-095.html (CH-CA-05-0551)
- https://www.flra.gov/decisions/v33/33-129.html (1-RO-80003)
- https://www.flra.gov/fsip/2018fs_-0 (2018 FSIP 060)
- https://www.flra.gov/fsip/2016fs_-15 (2016 FSIP 120)
- https://www.flra.gov/fsip/2016fs_-14 (2016 FSIP 052)
- https://www.flra.gov/fsip/2016fs_-13 (2016 FSIP 113)
- https://www.flra.gov/fsip/2015fs_-6 (2015 FSIP 121)
- https://www.flra.gov/fsip/2016fs_-12 (2016 FSIP 084)
- https://www.flra.gov/fsip/2016fs_-11 (2016 FSIP 087)
- https://www.flra.gov/fsip/2016fs_-10 (2016 FSIP 056)
- https://www.flra.gov/fsip/2016fs_-9 (2016 FSIP 069)
- https://www.flra.gov/fsip/2016fs_-8 (2016 FSIP 048)
- https://www.flra.gov/fsip/2016fs_-7 (2016 FSIP 038)
- https://www.flra.gov/fsip/2016fs_-6 (2016 FSIP 051)
- https://www.flra.gov/fsip/2016fs_-5 (2016 FSIP 026)
- https://www.flra.gov/fsip/2016fs_-4 (2016 FSIP 013)
- https://www.flra.gov/fsip/2016fs_-2 (2016 FSIP 031)
- https://www.flra.gov/fsip/2016fs_-3 (2016 FSIP 023)
- https://www.flra.gov/fsip/2016fs_-1 (2016 FSIP 022)
- https://www.flra.gov/fsip/2015fs_-4 (2015 FSIP 135)
- https://www.flra.gov/fsip/2016fs_ (2016 FSIP 005)
- https://www.flra.gov/fsip/2016fs_-0 (2016 FSIP 017)
- https://www.flra.gov/fsip/2015fs_-3 (2015 FSIP 114)
- https://www.flra.gov/fsip/2015fs_-5 (2015 FSIP 125)
- https://www.flra.gov/fsip/2004fs_-33 (2004 FSIP 001)
- https://www.flra.gov/fsip/2002fs_-29 (2002 FSIP 153)
- https://www.flra.gov/fsip/2001fs_-42 (2001 FSIP 091)
- https://www.flra.gov/fsip/2001fs_-41 (2001 FSIP 089)
- https://www.flra.gov/fsip/2000fs_-32 (2000 FSIP 093)
- https://www.flra.gov/fsip/2000fs_-31 (2000 FSIP 086)
- https://www.flra.gov/fsip/1999fs_-36 (1999 FSIP 142)
- https://www.flra.gov/fsip/1999fs_-38 (1999 FSIP 111)
- https://www.flra.gov/fsip/1999fs_-39 (1999 FSIP 013)
- https://www.flra.gov/fsip/1992fs_-73 (1992 FSIP 232)
- https://www.flra.gov/fsip/1993fs_-48 (1993 FSIP 058)
- https://www.flra.gov/fsip/1992fs_-51 (1992 FSIP 167)
- https://www.flra.gov/fsip/1992fs_-52 (1992 FSIP 246)
- https://www.flra.gov/fsip/1992fs_-72 (1992 FSIP 072)
- https://www.flra.gov/fsip/1992fs_-53 (1992 FSIP 184)
- https://www.flra.gov/fsip/1992fs_-55 (1992 FSIP 109)
- https://www.flra.gov/fsip/1992fs_-54 (1992 FSIP 054)
- https://www.flra.gov/fsip/1992fs_-56 (1992 FSIP 165)
- https://www.flra.gov/fsip/1992fs_-58 (1992 FSIP 163)
- https://www.flra.gov/fsip/1992fs_-60 (1992 FSIP 112)
- https://www.flra.gov/fsip/1992fs_-59 (1992 FSIP 204)
- https://www.flra.gov/fsip/1992fs_-57 (1992 FSIP 095)
- https://www.flra.gov/fsip/1992fs_-63 (1992 FSIP 115)
- https://www.flra.gov/fsip/1992fs_-61 (1992 FSIP 036)
- https://www.flra.gov/fsip/1992fs_-62 (1992 FSIP 037)
- https://www.flra.gov/fsip/1992fs_-65 (1992 FSIP 007)
- https://www.flra.gov/fsip/1992fs_-66 (1992 FSIP 083)
- https://www.flra.gov/fsip/1991fs_-48 (1991 FSIP 246)
- https://www.flra.gov/fsip/1991fs_-47 (1991 FSIP 278)
- https://www.flra.gov/fsip/1992fs_-64 (1992 FSIP 076)
- https://www.flra.gov/fsip/1991fs_-58 (1991 FSIP 205)
- https://www.flra.gov/fsip/1991fs_-49 (1991 FSIP 212)
- https://www.flra.gov/fsip/1992fs_-70 (1992 FSIP 147)
- https://www.flra.gov/fsip/1992fs_-74 (1992 FSIP 150)
- https://www.flra.gov/fsip/1992fs_-75 (1992 FSIP 159)
- https://www.flra.gov/fsip/1991fs_-56 (1991 FSIP 095)
- https://www.flra.gov/fsip/1992fs_-68 (1992 FSIP 020)
- https://www.flra.gov/fsip/1991fs_-50 (1991 FSIP 081)
- https://www.flra.gov/fsip/1992fs_-67 (1992 FSIP 071)
- https://www.flra.gov/fsip/1992fs_-71 (1992 FSIP 056)
- https://www.flra.gov/fsip/1992fs_-69 (1992 FSIP 091)
- https://www.flra.gov/fsip/1991fs_-59 (1991 FSIP 092)
- https://www.flra.gov/fsip/1991fs_-57 (1991 FSIP 224)
- https://www.flra.gov/fsip/1991fs_-60 (1991 FSIP 282)
- https://www.flra.gov/fsip/1991fs_-54 (1991 FSIP 075)
- https://www.flra.gov/fsip/1991fs_-52 (1991 FSIP 248)
- https://www.flra.gov/fsip/1991fs_-55 (1991 FSIP 085)
- https://www.flra.gov/fsip/1991fs_-53 (1991 FSIP 107)
- https://www.flra.gov/fsip/1991fs_-66 (1991 FSIP 134)
- https://www.flra.gov/fsip/1990fs_-48 (1990 FSIP 248)
- https://www.flra.gov/fsip/1992fs_-76 (1992 FSIP 248)
- https://www.flra.gov/fsip/1988fs_ (1988 FSIP 248)
- https://www.flra.gov/fsip/1991fs_-63 (1991 FSIP 129)
- https://www.flra.gov/fsip/1991fs_-62 (1991 FSIP 191)
- https://www.flra.gov/fsip/1991fs_-64 (1991 FSIP 018)
- https://www.flra.gov/fsip/1990fs_-47 (1990 FSIP 162)
- https://www.flra.gov/fsip/1991fs_-51 (1991 FSIP 009)
- https://www.flra.gov/fsip/1990fs_-49 (1990 FSIP 168)
- https://www.flra.gov/fsip/1991fs_-68 (1991 FSIP 091)
- https://www.flra.gov/fsip/1990fs_-50 (1990 FSIP 258)
- https://www.flra.gov/fsip/1991fs_-67 (1991 FSIP 083)
- https://www.flra.gov/fsip/1991fs_-69 (1991 FSIP 087)
- https://www.flra.gov/fsip/1990fs_-51 (1990 FSIP 197)
- https://www.flra.gov/fsip/1991fs_-70 (1991 FSIP 078)
- https://www.flra.gov/fsip/1990fs_-54 (1990 FSIP 191)
- https://www.flra.gov/fsip/1990fs_-55 (1990 FSIP 249)
- https://www.flra.gov/fsip/1990fs_-52 (1990 FSIP 152)
- https://www.flra.gov/fsip/1990fs_-53 (1990 FSIP 165)
- https://www.flra.gov/fsip/1990fs_-57 (1990 FSIP 151)
- https://www.flra.gov/fsip/1990fs_-56 (1990 FSIP 236)
- https://www.flra.gov/fsip/1990fs_-58 (1990 FSIP 164)
- https://www.flra.gov/fsip/1990fs_-59 (1990 FSIP 154)
- https://www.flra.gov/fsip/1990fs_-60 (1990 FSIP 222)
- https://www.flra.gov/fsip/1991fs_-71 (1991 FSIP 076)
- https://www.flra.gov/fsip/1990fs_-61 (1990 FSIP 254)
- https://www.flra.gov/fsip/1990fs_-64 (1990 FSIP 217)
- https://www.flra.gov/fsip/1990fs_-63 (1990 FSIP 147)
- https://www.flra.gov/fsip/1990fs_-62 (1990 FSIP 231)
- https://www.flra.gov/fsip/1990fs_-65 (1990 FSIP 089)
- https://www.flra.gov/fsip/1990fs_-67 (1990 FSIP 113)
- https://www.flra.gov/fsip/1990fs_-66 (1990 FSIP 086)
- https://www.flra.gov/fsip/1990fs_-68 (1990 FSIP 004)
- https://www.flra.gov/fsip/1990fs_-69 (1990 FSIP 027)
- https://www.flra.gov/fsip/1989fs_ (1989 FSIP 198)
- https://www.flra.gov/fsip/1989fs_-0 (1989 FSIP 188)
- https://www.flra.gov/fsip/1988fs_-0 (1988 FSIP 157)

**partial (4, Authority).** FLRA's page is cut off or is only a pointer to an attachment, and no PDF text is available. text holds what the page has.

- https://www.flra.gov/decisions/v61/61-012.html (0-AR-3900): page stops mid-sentence after the first paragraph; pdf has no text
- https://www.flra.gov/decisions/v61/61-005.html (0-AR-3912): page stops mid-sentence after the first paragraph; no pdf_url
- https://www.flra.gov/decisions/v36/36-032.html (9-CO-90016): page body says 'FULL TEXT OF DECISION IS ATTACHED'; no pdf_url
- https://www.flra.gov/decisions/v07/07-005.html (0-AR-92): page body is only 'See attached text.'; pdf has no text

### Pages FLRA serves incorrectly (handled in build_text.py)

Found by reading every ok text under 1,000 characters, every text ending in a lowercase letter, comma or semicolon (300 rows; nearly all end in a signature block or a footnote), and every Authority text containing neither its case number nor its citation. Each was confirmed in the raw HTML.

Incomplete pages (PAGE_INCOMPLETE): text from the PDF where it has text, else `partial`.

- https://www.flra.gov/decisions/v63/63-141.html: page stops mid-sentence -> `ok_pdf`
- https://www.flra.gov/decisions/v63/63-132.html: page stops mid-sentence -> `ok_pdf`
- https://www.flra.gov/decisions/v63/63-125.html: page body is only a link label for the PDF -> `ok_pdf`
- https://www.flra.gov/decisions/v61/61-012.html: page stops mid-sentence after the first paragraph -> `partial`
- https://www.flra.gov/decisions/v61/61-005.html: page stops mid-sentence after the first paragraph -> `partial`
- https://www.flra.gov/decisions/v36/36-032.html: page body says 'FULL TEXT OF DECISION IS ATTACHED' -> `partial`
- https://www.flra.gov/decisions/v07/07-005.html: page body is only 'See attached text.' -> `partial`

Pages carrying a different decision (PAGE_WRONG_DECISION): text from the row's PDF, accepted only if the PDF text contains the row's case number (all 8 do).

- https://www.flra.gov/decisions/v66/66-144.html: page is 66 FLRA No. 120 (0-AR-4734) -> `ok_pdf`
- https://www.flra.gov/decisions/v64/64-132.html: page is 64 FLRA No. 133 (0-AR-4294), same text as 64-133 -> `ok_pdf`
- https://www.flra.gov/decisions/v64/64-130.html: page is 64 FLRA No. 131 (0-AR-4382) -> `ok_pdf`
- https://www.flra.gov/decisions/v64/64-072.html: page is 64 FLRA No. 73 (0-AR-4307), same text as 64-073 -> `ok_pdf`
- https://www.flra.gov/decisions/v64/64-28.html: page is 64 FLRA No. 26, same text as 64-026 -> `ok_pdf`
- https://www.flra.gov/decisions/v63/63-190.html: page is 63 FLRA No. 145 (0-AR-4056) -> `ok_pdf`
- https://www.flra.gov/decisions/v63/63-175.html: page is 63 FLRA No. 174 (0-AR-4179), same text as 63-174 -> `ok_pdf`
- https://www.flra.gov/decisions/v63/63-162.html: page is 63 FLRA No. 163 (0-AR-4215) -> `ok_pdf`

### Own case number or citation in the text

| table | rows with text | case number (every part) | citation | either |
|---|---|---|---|---|
| authority | 10,460 | 10,421 | 10,453 | 10,459 |
| fsip | 963 | 703 | 0 | 703 |

Citation = '<vol> FLRA No. <n>' with n from the URL, or the volume/page form ('[ v33 p819 ]', '33:0819(', '33 FLRA 819'). FSIP has no citation.

Every failure was classified:

- **Authority, 1 row with neither:** 07-005 (`partial`, the page is only 'See attached text.').
- **Authority, 38 rows where the case number check fails but the citation is found:** 4 rows have no case number in the listing; the other 34 are typos or format differences in the listing's case number (for example '0-AR3921', '0AR-3825', 'BN-PR--03-0030', 'CH-CA-09527'), lists of several case numbers where only some parts appear, and captions that drop the leading '0-' (e.g. 'AR-5948').
- **FSIP, 260 rows** (259 'none' + 1 with no case number):
  - 228: the case number is nowhere in the page's HTML, title included. The newer FSIP pages (mostly 2009-2024) start at 'DECISION AND ORDER' or 'ARBITRATOR'S OPINION AND DECISION'; the caption with the number is only in the PDF. As a weaker identity check, 198 of these 228 texts contain the listing's issuance date written out. The other 30 can't be confirmed from the text.
  - 13: multi-case captions where the row's number is in a list ('Case Nos. 05 FSIP 96, 97, 98, 99, and 100').
  - 11: the text only cites other FSIP cases; includes three rows (1992 FSIP 104/114/126) sharing one consolidated decision whose caption is split across lines and OCR-damaged.
  - 3: number only in the page title, which is not kept.
  - 2: listed as 'FSIDP' (2002, 2004); found by a looser pattern.
  - 2: classifier false hits (the number appears only in citations to other cases); these belong with the 228.
- **Shared text:** 98 FSIP rows share text in 41 groups. Every group is a consolidated decision whose caption lists all its rows' numbers, except 2010 FSIP 052, which is listed twice. Two Authority pairs share text: 70-152.html and 70-152.html-0 (the same decision listed twice), and 08-003 / 08-033 (the listing's row for 08-003 points at 8 FLRA No. 33 in its own detail field; the page matches that).

### Other source oddities kept as FLRA serves them

- 10-001 and 20-041: the page text ends in stray database-program output (dBase messages), after the decision text.
- 1991 FSIP 246/250: the Panel's order is complete; the factfinder's report attached after it stops at its 'APPEARANCES' heading.
- 56-106: the page body is only 'Decision Vacated'.

### PDF-sourced rows: second reading with pypdf (all 40)

Our text comes from pdftotext; this re-reads the same cached PDFs with pypdf and compares word multisets (lowercase alphanumeric tokens). Gaps come from pypdf running words together and from running headers.

| row | chars | pypdf words | our words found in pypdf | pypdf words found in ours |
|---|---|---|---|---|
| https://www.flra.gov/decisions/v71/71-235.html | 9,923 | 1,595 | 99.5% | 99.0% |
| https://www.flra.gov/decisions/v71/71-221.html | 19,664 | 3,219 | 99.4% | 98.8% |
| https://www.flra.gov/decisions/v71/71-177.html | 21,898 | 3,748 | 99.4% | 98.8% |
| https://www.flra.gov/decisions/v71/71-149.html | 28,868 | 5,111 | 97.6% | 93.0% |
| https://www.flra.gov/decisions/v71/71-131.html | 20,597 | 3,485 | 99.6% | 99.3% |
| https://www.flra.gov/decisions/v71/71-125.html | 81,864 | 13,505 | 99.5% | 99.2% |
| https://www.flra.gov/decisions/v71/71-85.html | 92,965 | 15,309 | 99.2% | 98.4% |
| https://www.flra.gov/decisions/v71/71-84.html | 11,205 | 1,905 | 99.6% | 99.3% |
| https://www.flra.gov/decisions/v71/71-72.html | 29,737 | 5,009 | 99.4% | 98.9% |
| https://www.flra.gov/decisions/v71/71-64.html | 9,272 | 1,519 | 99.0% | 98.0% |
| https://www.flra.gov/decisions/v71/71-35.html | 6,666 | 1,106 | 99.5% | 98.9% |
| https://www.flra.gov/decisions/v71/71-34.html | 13,320 | 2,166 | 99.7% | 99.4% |
| https://www.flra.gov/decisions/v71/71-28.html | 13,655 | 2,320 | 99.3% | 98.5% |
| https://www.flra.gov/decisions/v71/71-27.html | 9,924 | 1,631 | 99.0% | 98.0% |
| https://www.flra.gov/decisions/v71/71-26.html | 5,906 | 1,015 | 99.2% | 98.4% |
| https://www.flra.gov/decisions/v71/71-25.html | 10,527 | 1,777 | 99.5% | 99.1% |
| https://www.flra.gov/decisions/v66/66-144.html | 31,745 | 5,408 | 99.0% | 98.0% |
| https://www.flra.gov/decisions/v64/64-132.html | 9,412 | 1,650 | 96.8% | 93.8% |
| https://www.flra.gov/decisions/v64/64-130.html | 17,000 | 2,939 | 96.8% | 93.7% |
| https://www.flra.gov/decisions/v64/64-072.html | 10,955 | 1,948 | 96.7% | 93.3% |
| https://www.flra.gov/decisions/v64/64-28.html | 20,134 | 3,400 | 97.1% | 94.3% |
| https://www.flra.gov/decisions/v63/63-190.html | 14,226 | 2,383 | 96.5% | 93.3% |
| https://www.flra.gov/decisions/v63/63-175.html | 3,929 | 670 | 96.3% | 92.8% |
| https://www.flra.gov/decisions/v63/63-162.html | 13,498 | 2,267 | 96.7% | 93.6% |
| https://www.flra.gov/decisions/v63/63-144.html | 11,474 | 1,870 | 98.8% | 97.5% |
| https://www.flra.gov/decisions/v63/63-141.html | 12,247 | 2,136 | 96.7% | 93.5% |
| https://www.flra.gov/decisions/v63/63-133.html | 49,468 | 8,137 | 99.1% | 98.1% |
| https://www.flra.gov/decisions/v63/63-132.html | 2,567 | 437 | 96.0% | 92.2% |
| https://www.flra.gov/decisions/v63/63-130.html | 2,861 | 467 | 99.1% | 98.3% |
| https://www.flra.gov/decisions/v63/63-129.html | 38,884 | 6,557 | 99.1% | 98.3% |
| https://www.flra.gov/decisions/v63/63-125.html | 19,836 | 3,248 | 98.6% | 97.2% |
| https://www.flra.gov/decisions/v63/63-122.html | 14,555 | 2,500 | 99.1% | 98.2% |
| https://www.flra.gov/decisions/v63/63-120.html | 92,411 | 15,522 | 99.2% | 98.3% |
| https://www.flra.gov/decisions/v63/63-104.html | 2,269 | 398 | 92.8% | 90.7% |
| https://www.flra.gov/decisions/v63/63-101.html | 6,131 | 1,011 | 99.6% | 99.2% |
| https://www.flra.gov/decisions/v63/63-067.html | 1,569 | 264 | 98.9% | 97.7% |
| https://www.flra.gov/fsip/2017fs_-0 | 8,033 | 1,290 | 99.7% | 99.6% |
| https://www.flra.gov/fsip/2017fs_ | 7,467 | 1,240 | 99.9% | 99.8% |
| https://www.flra.gov/fsip/2015fs_-1 | 31,626 | 5,058 | 99.9% | 99.8% |
| https://www.flra.gov/fsip/2015fs_-2 | 28,188 | 4,865 | 100.0% | 99.9% |


### Reading the live sample above

All 45 HTML-sourced rows with text matched in full: the whole text, whitespace removed, is in the live page. Where an opening or closing shows NOT FOUND for an HTML row, it is because the page has no whitespace between inline elements, so whitespace-collapsed snippets differ. The 8 'whole text found: False' rows are all PDF-sourced, read by pdftotext versus pypdf; see the word-overlap table. All 45 means 41 `ok` and 4 `partial` rows. For the 7 no-text rows the 400-character preview is only site navigation, so it doesn't prove the page is title-only. That rests on the cached pages (fetched 2026-11-15/16): `text.extract` found no body text on any of the 110.

