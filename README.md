<div align="center">

# 🎓 Summer 2027 and Fall 2026 Electrical Engineering Internships

**A self-updating engine that tracks Electrical Engineering internships so you don't have to.**

[![CI](https://img.shields.io/github/actions/workflow/status/austinwright-eng/Automated-List-of-Electrical-Engineering-Internships/ci.yml?branch=main&label=tests&style=flat-square&color=3fb950)](https://github.com/austinwright-eng/Automated-List-of-Electrical-Engineering-Internships/actions/workflows/ci.yml)&nbsp;[![Open roles](https://img.shields.io/badge/dynamic/json?label=open%20roles&query=open_total&url=https%3A%2F%2Faustinwright-eng.github.io%2FAutomated-List-of-Electrical-Engineering-Internships%2Fapi%2Fstats.json&color=2f81f7&style=flat-square)](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/)&nbsp;![Updates](https://img.shields.io/badge/updates-every%2030%20min-3fb950?style=flat-square)&nbsp;[![RSS](https://img.shields.io/badge/RSS-subscribe-e67e22?style=flat-square)](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/feed.xml)

### 438 open roles (302 listed below) · 26 new this week

4,811 employers tracked · data as of Nov 26, 2026 at 19:20 UTC

_316 have a cycle the employer stated · 122 are recent postings whose cycle isn't stated (listed separately, never mixed in)._

**[🖥️ Live dashboard](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/)** · **[📡 RSS](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/feed.xml)** · **[⚙️ JSON API](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/api/jobs.json)**

</div>

> [!TIP]
> **⭐ Star this repo** to save it and get updates when new roles are added.

Instead of refreshing a dozen career pages by hand, it reads company hiring feeds directly and keeps one live list — newest roles on top, refreshed automatically throughout the day.

**🔔 Follow new roles:** [RSS feed](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/feed.xml).

---

## What this is

This is an engine, not a hand-kept list. It polls company career feeds every 30 minutes, finds the internships, removes duplicates, and rebuilds this page on its own.

Every link comes straight from the source — so it's real and current, not a stale list someone forgot to update. Speed matters.

## What makes this different

| | |
|---|---|
| ⚡ **EE scope** | Electrical and related internships, with separate categories for circuits, digital, RF, power, embedded, and controls. Generic software and ambiguous systems/test titles are excluded. |
| 🛂 **Visa intel, computed** | 🇺🇸 / 🛂 flags detected automatically from every job description, plus ✓ for employers with a real H-1B track record (USCIS data, FY2022-23 — a history, not a promise). The big lists crowdsource this by hand; here it's code. Most postings say nothing either way, and those show as unknown rather than guessed. |
| 📆 **A real date on nearly every role** | Taken from the job portal itself wherever the portal states one, so newest-first actually means newest. The exact coverage figure is printed at the bottom of this page every run. |
| 🧰 **Skill tags + pay, extracted** | Every posting's text is scanned for the stack it wants (Python, C++, PyTorch, …) and the pay it states — searchable on the [dashboard](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/), and included in the CSV and API. |
| 🔔 **Alerts your way** | [RSS](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/feed.xml) — point any reader, or a Slack/Discord RSS integration, at it. Plus a [live dashboard](https://austinwright-eng.github.io/Automated-List-of-Electrical-Engineering-Internships/) with search, filters, and a saved-roles list that never leaves your browser. |
| ⚙️ **An engine, not a spreadsheet** | 5,101 job-board endpoints (4,811 distinct employers; some run more than one board) polled every 30 minutes across 12 ATS platforms. Full source and tests in this repo. |

## Scope

| | |
|---|---|
| **Roles** | Electrical/electronics, digital/semiconductors, RF, power, embedded/firmware, controls and instrumentation internships |
| **Region** | United States |
| **Cycles** | Summer 2027 and Fall 2026 |

## About

This EE fork builds on the upstream Internship Engine. See [EE development and upstream synchronization](EE_DEVELOPMENT.md).

Use it to spot roles early and apply before they fill up. Being first genuinely helps.

## Where this is going

I'm building this in the open and adding to it as it grows.

**Recently shipped:** email alerts · the Drop Radar · auto-detected sponsorship flags · the live dashboard

**Next up:** personalized alerts (pick your categories) · per-company hiring pages · a ghost-posting detector

If it helps you, a star means a lot and tells me to keep going.

## How to use

<details>
<summary><b>Reading the table — flags, dates, and the cycle split</b> (click to expand)</summary>

- Roles are grouped by cycle below - **newest posting on top, oldest at the bottom.**
- A cycle section holds only roles whose **employer stated that cycle** - in the title, or in the posting's own text. Postings that name no cycle anywhere are in *Recently posted — cycle not stated* further down, with **no cycle guessed for them**. Same quality bar, different amount of evidence.
- **Apply** is the third column, right after the role, so the link is on screen even when the table is wider than your window.
- The **Posted** column is the date the company published the role.
- **_(3 openings)_ after a role title** = the employer has that many separate live requisitions for the same job, in the same place, for the same cycle. They're all real and each takes its own application, so they're linked individually (**Apply**, then **#2**, **#3**) instead of repeating the row. Counts still count requisitions, and the CSV export is never grouped.
- **🆁 after a company name** = **this role is remote** — the posting's own location or title says so. It marks the role on that row, not the whole company.
- **Flags after a role title:** 🇺🇸 = requires U.S. citizenship or a security clearance · 🛂 = the posting says it won't sponsor a work visa · 🆕 = spotted in the last 48 hours. Sponsorship flags are detected automatically from each job description - treat them as a strong hint and confirm on the posting.
- **✓ after a company name** = a real H-1B track record: USCIS approved 10+ petitions for that employer in FY2022–2023 (matched automatically against the official [H-1B Employer Data Hub](https://www.uscis.gov/tools/reports-and-studies/h-1b-employer-data-hub)). No ✓ doesn't mean they won't sponsor - it means we can't prove they have.
- Track your applications with [`data/internships.csv`](data/internships.csv) (opens in Excel / Google Sheets).
- Missing a company? Adding one takes a single line, see [CONTRIBUTING.md](CONTRIBUTING.md).

</details>

---

## Summer 2027  (190 employer-stated)

| Company | Role | Apply | Location | Skills | Posted |
|---|---|---|---|---|---|
| Zebra Technologies ✓ | 2027 Summer Internship (US) - Electrical Engineer, Advanced Data Capture 🛂 🆕 | [Apply](https://zebra.wd501.myworkdayjobs.com/Zebra_careers/job/Holtsville-New-York/XMLNAME-2027-Summer-Internship--US----Electrical-Engineer--Advanced-Data-Capture_JR103913) | Holtsville, New York | Python, C++, MATLAB | Nov 25, 2026 |
| Stantec | Electrical Engineering Intern - Buildings (Summer 2027) 🆕 _(2 openings)_ | [Apply](https://hdhl.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1009012) [#2](https://hdhl.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1009013) | Lynnwood, WA, United States | No skills listed | Nov 25, 2026 |
| Stantec | Electrical Engineering Intern - Buildings (Summer 2027) 🆕 | [Apply](https://hdhl.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1009024) | Seattle, WA, United States | No skills listed | Nov 25, 2026 |
| Lightmatter | Firmware Intern – Summer 2027 🆕 | [Apply](https://boards.greenhouse.io/lightmatter/jobs/5492829008?gh_jid=5492829008) | Boston, MA | Python, C++, Linux, Git | Nov 25, 2026 |
| Lightmatter | Design Verificati​on, Intern Summer 2027 🆕 | [Apply](https://boards.greenhouse.io/lightmatter/jobs/5493962008?gh_jid=5493962008) | Boston, MA | Python, C++, Git, Verilog | Nov 24, 2026 |
| SharkNinja | Summer 2027: Firmware Engineering Intern, Advanced Development (May to August) | [Apply](https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4721682006) | Needham, MA, United States | No skills listed | Nov 23, 2026 |
| IMEG ✓ | Electrical Engineering Intern / Scottsdale, AZ 🛂 | [Apply](https://wd1.myworkdaysite.com/recruiting/imeg/Imeg_Careers/job/Phoenix-AZ/Electrical-Engineering-Intern---Scottsdale--AZ_R-17005) | Phoenix, AZ | No skills listed | Nov 23, 2026 |
| Neros Technologies | Firmware/Embedded Software Engineer Intern - Summer 2027 | [Apply](https://job-boards.greenhouse.io/nerostechnologies/jobs/5278981007) | Torrance, California, United States | Python, C++, Linux, Git | Nov 21, 2026 |
| Neros Technologies | Electrical Engineering Intern - Summer 2027 | [Apply](https://job-boards.greenhouse.io/nerostechnologies/jobs/5273149007) | Torrance, California, United States | Python, C++, MATLAB | Nov 21, 2026 |
| Lucid Motors | Power Electronics Control Engineer Intern, Summer 2027 | [Apply](https://lucidmotors.com/careers/search/5290949007?gh_jid=5290949007) | Newark, CA | MATLAB | Nov 20, 2026 |
| Lucid Motors | Intern, Vehicle Motion Controls Engineer, Summer 2027 | [Apply](https://lucidmotors.com/careers/search/5290899007?gh_jid=5290899007) | Newark, CA | Python, C++, MATLAB, Git | Nov 20, 2026 |
| Pacific Fusion | Summer 2027 Controls Electrical Engineer Internship | [Apply](https://job-boards.greenhouse.io/pacificfusion/jobs/4505719009) | San Leandro, CA | Python, MATLAB | Nov 20, 2026 |
| Mission Critical Group | 2027 Summer Internship - Electrical Engineering | [Apply](https://jobs.smartrecruiters.com/MissionCriticalGroup/3743990016997596) | Harleysville +2 more | No skills listed | Nov 20, 2026 |
| Lucid Motors | Intern, Embedded Software, Summer 2027 | [Apply](https://lucidmotors.com/careers/search/5290904007?gh_jid=5290904007) | Newark, CA | Python, C++, Git | Nov 19, 2026 |
| Ralliant | Electrical Design Engineer Intern (Summer 2027) | [Apply](https://ibwujb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/11169) | Beaverton, OR, United States | Python, C++, MATLAB | Nov 19, 2026 |
| Lightmatter | Silicon Validation & Test Automation, Intern Summer 2027 | [Apply](https://boards.greenhouse.io/lightmatter/jobs/5473832008?gh_jid=5473832008) | Mountain View, CA | Python, Java, Git | Nov 19, 2026 |
| IMEG ✓ | Electrical Engineering Intern / Idaho Falls, ID 🛂 | [Apply](https://wd1.myworkdaysite.com/recruiting/imeg/Imeg_Careers/job/Idaho-Falls-ID/Electrical-Engineering-Intern---Idaho-Falls--ID_R-17029) | Idaho Falls, ID | No skills listed | Nov 19, 2026 |
| Scout Space 🆁 | Embedded Firmware Engineering Intern (Summer 2027) 🇺🇸 | [Apply](https://job-boards.greenhouse.io/scoutspace/jobs/5489232008) | Reston, VA - Remote | Python, C++, Computer Vision, Linux | Nov 19, 2026 |
| Veolia | Instrument​ation & Equipment Engineering Intern | [Apply](https://jobs.smartrecruiters.com/VeoliaEnvironnementSA/744000162356599) | Cary, NC, United States (Hybrid) | No skills listed | Nov 18, 2026 |
| Mission Critical Group | 2027 Summer Internship - Electrical Engineering | [Apply](https://jobs.smartrecruiters.com/MissionCriticalGroup/3743990016934876) | Brookston, Indiana, United States | No skills listed | Nov 18, 2026 |
| RTX | Electrical Engineer Co-Op (Summer/Fall 2027) | [Apply](https://globalhr.wd5.myworkdayjobs.com/Private_Posting_No_TMP/job/US-IA-CEDAR-RAPIDS-131--5450-C-Ave-NE--BLDG-131/Electrical-Engineer-Co-Op--Summer-Fall-2027-_01873470-2) | US-IA-CEDAR RAPIDS-131 ~ 5450 C Ave NE… | No skills listed | Nov 17, 2026 |
| Ralliant | Hardware Verification Engineer Co-op (Summer 2027) | [Apply](https://ibwujb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/10491) | Solon, OH, United States | Python, C++, C#, Git | Nov 16, 2026 |
| Reliable Robotics | FPGA Engineering Intern (Summer 2027) | [Apply](https://jobs.ashbyhq.com/reliable-robotics/131987a0-ede9-4291-9cd2-1aaadabd2a54) | Mountain View, CA | Python, C++, Verilog | Nov 13, 2026 |
| Reliable Robotics | Avionics Intern (Summer 2027) | [Apply](https://jobs.ashbyhq.com/reliable-robotics/f4073938-ccdb-46fb-aa65-6715981d27ee) | Mountain View, CA | Python, MATLAB | Nov 13, 2026 |
| IMEG ✓ | Electrical Engineering Intern / Independen​ce, OH 🛂 _(2 openings)_ | [Apply](https://wd1.myworkdaysite.com/recruiting/imeg/Imeg_Careers/job/Cleveland-OH/Electrical-Engineering-Intern---Independence--OH_R-17000) [#2](https://wd1.myworkdaysite.com/recruiting/imeg/Imeg_Careers/job/Cleveland-OH/Electrical-Engineering-Intern---Independence--OH_R-17031) | Cleveland, OH | No skills listed | Nov 13, 2026 |
| Reliable Robotics | Hardware Test Engineering Intern (Summer 2027) | [Apply](https://jobs.ashbyhq.com/reliable-robotics/0af72d5a-87b7-49a1-b49e-424d28758c9e) | Mountain View, CA | Python, C++, MATLAB | Nov 13, 2026 |
| Global Infrastruc​ture | Intern Electrical Engineering Designer | [Apply](https://gi.wd1.myworkdayjobs.com/Global_Infrastructure/job/US--IL--Chicago---200-South-Wacker-Drive/Intern-Electrical-Engineering-Designer_6746) | US / IL / Chicago - 200 South Wacker Dr… | MATLAB | Nov 12, 2026 |
| CACI | Embedded Software Development Intern - Summer 2027 | [Apply](https://caci.wd1.myworkdayjobs.com/external/job/Denver-CO-US/Embedded-Software-Development-Intern---Summer-2027_333147) | Denver, CO, US | Python, C++, Rust, MATLAB | Nov 12, 2026 |
| ABB ✓ | Electrical Engineering Co-op- Summer 2027 🛂 | [Apply](https://abb.wd3.myworkdayjobs.com/external_career_page/job/USA-NC-Mebane/Electrical-Engineering-Co-op--Summer-2027_JR00051091) | USA, NC, Mebane | No skills listed | Nov 12, 2026 |
| WSP | Electrical Engineering (Substation) Intern - Summer 2027 | [Apply](https://emit.fa.ca3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/94171) | Freeport +5 more | No skills listed | Nov 12, 2026 |
| Entegris ✓ | Embedded Software Engineering Intern | [Apply](https://entegris.wd1.myworkdayjobs.com/entegriscareers/job/Bloomington-MN/Embedded-Software-Engineering-Intern_REQ-15870) | Bloomington, MN | Python, C++, Git | Nov 12, 2026 |
| Northrop Grumman | 2027 Electronics Engineering Intern - Elkridge MD 🇺🇸 | [Apply](https://ngc.wd1.myworkdayjobs.com/Northrop_Grumman_External_Site/job/United-States-Maryland-Elkridge/XMLNAME-2027-Electronics-Engineering-Intern---Elkridge-MD_R10260310) | United States-Maryland-Elkridge | Python, C++, MATLAB | Nov 12, 2026 |
| Formlabsin​ternships | Hardware Systems Integration Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/formlabsinternships/jobs/8381595) | Somerville, MA | Python | Nov 11, 2026 |
| Motorola | 2027 Summer Embedded SW Engineering Intern 🇺🇸 | [Apply](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Schaumburg-IL/XMLNAME-2027-Summer-Embedded-SW-Engineering-Intern_R67741-1) | Schaumburg, IL | Java, C++, C#, Linux | Nov 11, 2026 |
| Northrop Grumman | 2027 Electrical Engineering Intern - Sunnyvale CA 🇺🇸 | [Apply](https://ngc.wd1.myworkdayjobs.com/Northrop_Grumman_External_Site/job/United-States-California-Sunnyvale/XMLNAME-2027-Electrical-Engineering-Intern---Sunnyvale-CA_R10260307) | United States-California-Sunnyvale | MATLAB | Nov 11, 2026 |
| Emerson Electric | RF Engineering Co-op (Jul - Dec 2027) | [Apply](https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26013238) | Santa Rosa, CA, United States | Python, C++ | Nov 11, 2026 |
| RTX | Electrical (FCS Hardware) Engineering Intern (Summer 2027)(Onsi​te) | [Apply](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-193--1120-Collins-Rd-NE--BLDG193/Electrical--FCS-Hardware--Engineering-Intern--Summer-2027--Onsite-_01888815) | US-IA-CEDAR RAPIDS-193 ~ 1120 Collins R… | No skills listed | Nov 11, 2026 |
| Reworld | Summer 2027 Intern - Electrical and Instrument​ation | [Apply](https://reworld.wd5.myworkdayjobs.com/external/job/USA-PA-Chester/Summer-2027-Intern---Electrical-and-Instrumentation_JR14464) | USA, PA, Chester | No skills listed | Nov 11, 2026 |
| Global​Foundries | AI Processor Hardware/Software Integration Engineer Intern (Summer 2027) | [Apply](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Texas---Richardson/AI-Processor-Hardware-Software-Integration-Engineer-Intern--Summer-2027-_JR-2604028) | USA - Texas - Richardson | Python, C++, PyTorch, TensorFlow | Nov 11, 2026 |
| WSP | Electrical Engineering Intern - Summer 2027 | [Apply](https://emit.fa.ca3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/94977) | Hamilton, NJ, United States | No skills listed | Nov 10, 2026 |
| Western Digital | Summer 2027 Intern - Hardware Engineering | [Apply](https://jobs.smartrecruiters.com/WesternDigital/744000160975864) | San Jose, CA, United States (Hybrid) | Python, Java, C++, JavaScript | Nov 10, 2026 |
| Zekelman Industries | Electrical and Controls Engineer - Intern | [Apply](https://zekelman.wd12.myworkdayjobs.com/Careers/job/Rochelle-IL/Electrical-and-Controls-Engineer---Intern_JR002596) | Rochelle, IL | No skills listed | Nov 10, 2026 |
| CACI | Electrical Engineering Intern - Summer 2027 | [Apply](https://caci.wd1.myworkdayjobs.com/external/job/Sarasota-FL-US/Electrical-Engineering-Intern---Summer-2027_332614) | Sarasota, FL, US | No skills listed | Nov 10, 2026 |
| Momentive ✓ | 2027 Co-Op - Electronics & Aerospace | [Apply](https://momentive.wd1.myworkdayjobs.com/MC/job/US-NY-Waterford/XMLNAME-2027-Co-Op---Electronics---Aerospace_R10058) | US NY Waterford | No skills listed | Nov 10, 2026 |
| Global​Foundries | Silicon Photonics Process Integration Engineering Intern (Summer 2027) _(2 openings)_ | [Apply](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---New-York---Malta/Silicon-Photonics-Process-Integration-Engineering-Intern--Summer-2027-_JR-2605135) [#2](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---New-York---Malta/Silicon-Photonics-Process-Integration-Engineering-Intern--Summer-2027-_JR-2605134) | USA - New York - Malta | No skills listed | Nov 10, 2026 |
| Global​Foundries | Controls Engineering Intern (Summer 2027) | [Apply](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---Vermont---Essex-Junction/Controls-Engineering-Intern--Summer-2027-_JR-2604647) | USA - Vermont - Essex Junction | No skills listed | Nov 10, 2026 |
| The Aerospace Corporation | 2027 Power and Analog Circuit Engineering Grad Intern 🇺🇸 | [Apply](https://aero.wd5.myworkdayjobs.com/external/job/El-Segundo-CA/XMLNAME-2027-Power-and-Analog-Circuit-Engineering-Intern_R016430) | El Segundo, CA | No skills listed | Nov 09, 2026 |
| RTX | Digital Hardware Design Engineer Co-op (Summer/Fall 2027)(Onsi​te) 🇺🇸 | [Apply](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-130--5350-C-Ave-NE--BLDG-130/Digital-Hardware-Design-Engineer-Co-op--Summer-Fall-2027--Onsite-_01871519) | US-IA-CEDAR RAPIDS-130 ~ 5350 C Ave NE… | No skills listed | Nov 09, 2026 |
| Pivotal Software ✓ | Internship, Electrical Engineering (Summer 2027) 🇺🇸 | [Apply](https://jobs.lever.co/pivotal/442a0450-f911-4ac1-a112-03374217f7fb) | Palo Alto, CA | No skills listed | Nov 09, 2026 |
| Sierra Nevada Corporation | Firmware Engineer Intern (Summer 2027) 🇺🇸 | [Apply](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Sparks-NV/Firmware-Engineer-Intern--Summer-2027-_R0031233) | Sparks, NV | MATLAB | Nov 05, 2026 |
| Sierra Nevada Corporation | Electrical Engineering Intern (Summer 2027) 🇺🇸 | [Apply](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Hagerstown-MD/Electrical-Engineering-Intern--Summer-2027-_R0030743-1) | Hagerstown, MD | MATLAB | Nov 05, 2026 |
| Jabil ✓ | Low voltage switchgear Electrical Engineering Intern | [Apply](https://jabil.wd5.myworkdayjobs.com/Jabil_Careers/job/St-PetersburgTampa-FL/Low-voltage-switchgear-Electrical-Engineering-Intern_J2470772) | St. Petersburg/Tampa, FL | No skills listed | Nov 05, 2026 |
| Northrop Grumman | 2027 Guidance Navigation and Control Engineer Intern - Redondo Beach CA 🇺🇸 | [Apply](https://ngc.wd1.myworkdayjobs.com/Northrop_Grumman_External_Site/job/United-States-California-Redondo-Beach/XMLNAME-2027-Guidance-Navigation-and-Control-Engineer-Intern---Redondo-Beach-CA_R10259386) | United States-California-Redondo Beach | Python, C++, MATLAB | Nov 04, 2026 |
| Bracco | Electrical Engineering Intern (R&D Sustaining) | [Apply](https://bracco.wd103.myworkdayjobs.com/braccocareers/job/USA-Eden-Prairie-Minnesota-55344/Electrical-Engineering-Intern--R-D-Sustaining-_JR100315) | USA, Eden Prairie, Minnesota, 55344 | C++, MATLAB | Nov 04, 2026 |
| Clean Harbors | Electrical Engineer Intern - Summer 2027 | [Apply](https://epyc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/168340) | Fallon, NV, United States | No skills listed | Nov 04, 2026 |
| CACI | Electrical Engineering Co-op/Intern - Summer 2027 | [Apply](https://caci.wd1.myworkdayjobs.com/external/job/Rochester-NY-US/Electrical-Engineering-Co-op-Intern---Spring-2027_334155) | Rochester, NY, US | Python | Nov 04, 2026 |
| Draper | Sensor Electrical Engineering Intern (Summer 2027) 🇺🇸 | [Apply](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Sensor-Electrical-Engineering-Intern--Summer-2027-_JR003095) | Cambridge, MA | MATLAB | Nov 04, 2026 |
| LG Electronics | Vanderbilt University x LG Electronics Summer Internship Program | [Apply](https://job-boards.greenhouse.io/lgelectronics/jobs/5473012008) | Englewood Cliffs, NJ | No skills listed | Nov 04, 2026 |
| Lawrence Livermore National Laboratory (LLNL) | Power Systems Graduate Intern - Cyber and Critical Infrastruc​ture Summer Institute - Summer 2027 🇺🇸 | [Apply](https://jobs.smartrecruiters.com/LLNL/3743990016610436) | Livermore, CA, United States | Python, C++, MATLAB | Nov 04, 2026 |
| Lawrence Livermore National Laboratory (LLNL) | Power Systems Undergradu​ate Intern - Cyber and Critical Infrastruc​ture Summer Institute - Summer 2027 🇺🇸 | [Apply](https://jobs.smartrecruiters.com/LLNL/3743990016610446) | Livermore, CA, United States | Python, C++, MATLAB | Nov 04, 2026 |
| Zurn Elkay Water Solutions | Electrical & Electronics Engineering Intern (Summer 2027) | [Apply](https://elkay.wd1.myworkdayjobs.com/Elkay_External/job/Downers-Grove-IL/Electrical---Electronics-Engineering-Intern--Summer-2027-_REQ-020097) | Downers Grove, IL | No skills listed | Nov 03, 2026 |
| Westlake | Process Control Engineer Intern (Summer 2027) 🛂 | [Apply](https://westlake.wd1.myworkdayjobs.com/westlake/job/US---Calvert-City-KY/Process-Control-Engineer-Intern--Summer-2027-_R33711-1) | US - Calvert City, KY | No skills listed | Nov 03, 2026 |
| Marvell | Hardware Signal Integrity Intern, MS - Summer 2027 | [Apply](https://marvell.wd1.myworkdayjobs.com/marvellcareers2/job/Santa-Clara-CA/Hardware-Signal-Integrity-Intern--MS---Summer-2027_2603877) | Santa Clara, CA | No skills listed | Nov 03, 2026 |
| Zoox ✓ | Hardware Engineer Intern, Vehicle Development [Summer 2027] | [Apply](https://jobs.lever.co/zoox/0accbf9e-9b09-4733-b495-fb6dce13ba62) | Foster City, CA | Python, MATLAB | Nov 02, 2026 |
| Zoox ✓ | Hardware Engineer Intern, Vehicle Systems [Summer 2027] | [Apply](https://jobs.lever.co/zoox/0c32245b-f51d-40d2-8e57-a0be1b744c5b) | Foster City, CA | Python | Nov 02, 2026 |
| Zoox ✓ | Hardware Engineer Intern, Manufactur​ing Operations [Summer 2027] | [Apply](https://jobs.lever.co/zoox/53f5297a-fe30-4e1e-ab1c-96db5b23eded) | Foster City, CA | Python, SQL, Databricks | Nov 02, 2026 |
| Applied Materials ✓ | 2027 Summer Electrical Engineer Intern- Master's (Santa Clara, CA) | [Apply](https://amat.wd1.myworkdayjobs.com/External/job/Santa-ClaraCA/XMLNAME-2027-Summer-Electrical-Engineer-Intern--Master-s--Santa-Clara--CA-_R2629967) | Santa Clara,CA | No skills listed | Nov 02, 2026 |
| WSP | Electrical Engineering Intern - Summer 2027 | [Apply](https://emit.fa.ca3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/98684) | San Diego, CA, United States | No skills listed | Nov 02, 2026 |
| NVIDIA ✓ | VLSI CAD Timing Intern, Applied AI - Summer 2027 | [Apply](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/VLSI-CAD-Timing-Intern--Applied-AI---Summer-2027_JR2026799) | US, CA, Santa Clara | Python | Oct 30, 2026 |
| Stratolaunch | Manufactur​ing (Electrical) Engineering Intern Summer 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/stratolaunch/jobs/5467832008) | Mojave, California, United States | No skills listed | Oct 30, 2026 |
| Johnson & Johnson | Electrical Engineering Intern - Robotics R&D 🛂 | [Apply](https://jj.wd5.myworkdayjobs.com/JJ/job/Santa-Clara-California-United-States-of-America/Electrical-Engineering-Intern---Robotics-R-D_R-099626-1) | Santa Clara +2 more | Python, MATLAB | Oct 29, 2026 |
| The Aerospace Corporation | 2027 Power Systems Engineering Graduate Intern 🇺🇸 | [Apply](https://aero.wd5.myworkdayjobs.com/external/job/El-Segundo-CA/XMLNAME-2027-Power-Systems-Engineering-Graduate-Intern_R016527) | El Segundo, CA | No skills listed | Oct 28, 2026 |
| The Aerospace Corporation | 2027 Power Systems Engineering Undergradu​ate Intern 🇺🇸 | [Apply](https://aero.wd5.myworkdayjobs.com/external/job/El-Segundo-CA/XMLNAME-2027-Power-Systems-Engineering-Undergraduate-Intern_R016530) | El Segundo, CA | No skills listed | Oct 28, 2026 |
| Centene 🆁 | Digital Design Operations Intern (Master's - Summer 2027) | [Apply](https://centene.wd5.myworkdayjobs.com/Centene_External/job/Remote-MO/Digital-Design-Operations-Intern--Master-s---Summer-2027-_1667736) | Remote-MO | No skills listed | Oct 28, 2026 |
| Draper | Analog ASIC Design Intern (Summer 2027) 🇺🇸 | [Apply](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Analog-ASIC-Design-Intern--Summer-2027-_JR003085) | Cambridge, MA | Python, MATLAB, Verilog | Oct 28, 2026 |
| Emerson Electric | Electrical Engineering Co-op (Summer 2027) | [Apply](https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26011003) | Elyria +5 more | Python, C++ | Oct 28, 2026 |
| Global Infrastruc​ture | Intern, Electrical Engineering Designer | [Apply](https://gi.wd1.myworkdayjobs.com/Global_Infrastructure/job/US--KS--Overland-Park---10561-Barkley-Street/Electrical-Engineering-Intern-Co-Op_6631) | US / KS / Overland Park - 10561 Barkley… | No skills listed | Oct 27, 2026 |
| Global Infrastruc​ture | Electrical Engineering Intern/Co-Op | [Apply](https://gi.wd1.myworkdayjobs.com/Global_Infrastructure/job/US--MO--Kansas-City---1600-Genessee-Street/Electrical-Engineering-Intern-Co-Op_6631) | US / MO / Kansas City - 1600 Genessee S… | No skills listed | Oct 27, 2026 |
| Commonwealth Fusion Systems | Intern - Microwave Engineer - Summer 2027 | [Apply](https://jobs.lever.co/cfsenergy/79cd53ba-b864-4bcb-8421-60cf58f7df54) | Devens, MA | MATLAB | Oct 26, 2026 |
| Applied Materials ✓ | 2027 Summer Electrical Engineering Intern - BS or MS (Gloucester, MA) | [Apply](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineering-Intern---BS-or-MS--Gloucester--MA-_R2630812) | Gloucester​,MA | No skills listed | Oct 26, 2026 |
| HP IQ | Engineering Intern, Wireless Automation and Test (Summer 2027) | [Apply](https://job-boards.greenhouse.io/hpiq/jobs/6114741004) | San Francisco, CA | Python, Bash | Oct 26, 2026 |
| HP IQ | Electrical Engineering Intern, Hardware (Summer 2027) | [Apply](https://job-boards.greenhouse.io/hpiq/jobs/6116396004) | San Francisco, CA | Python | Oct 26, 2026 |
| Upscale AI | Advanced SerDes & Analog/Mixed-Signal IC Design Intern – Summer 2027 | [Apply](https://jobs.lever.co/upscale-ai/2bad3e47-6c00-4ec2-94b5-feb4009619c9) | US - Santa Clara, CA | Python, MATLAB | Oct 23, 2026 |
| Clean Harbors | Electrical Engineer Intern - Summer 2027 | [Apply](https://epyc.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/167556) | El Dorado, AR, United States | No skills listed | Oct 22, 2026 |
| Marvell | Silicon Validation Intern, BS - Summer 2027 | [Apply](https://marvell.wd1.myworkdayjobs.com/marvellcareers2/job/Santa-Clara-CA/Silicon-Validation-Intern--BS---Summer-2027_2603850) | Santa Clara, CA | Python | Oct 21, 2026 |
| Smith+Nephew ✓ | Intern Electrical Engineering | [Apply](https://smithnephew.wd5.myworkdayjobs.com/External/job/Andover-MA/Intern-Electrical-Engineering_R92957) | Andover, MA | No skills listed | Oct 21, 2026 |
| Smith+Nephew ✓ | Co-Op Embedded Software Engineering | [Apply](https://smithnephew.wd5.myworkdayjobs.com/External/job/Andover-MA/Intern-Embedded-Software-Engineering_R92952) | Andover, MA | C++, Computer Vision | Oct 21, 2026 |
| Skydio ✓ | Electrical Engineer Intern | [Apply](https://jobs.ashbyhq.com/skydio/57336f0f-a8ed-4ede-b6da-d399e5335fe4) | San Mateo, California, United States | No skills listed | Oct 20, 2026 |
| Skydio ✓ | Wireless Hardware Engineer Intern - Summer 2027 | [Apply](https://jobs.ashbyhq.com/skydio/1ac972b1-8094-4765-8869-63e1c4d50dea) | San Mateo, California, United States | Python | Oct 20, 2026 |
| Skydio ✓ | Hardware Test and Reliability Intern - Summer 2027 | [Apply](https://jobs.ashbyhq.com/skydio/36d75e36-eeb2-4399-8887-37c4a5ff5800) | San Mateo, California, United States | Python | Oct 20, 2026 |
| Stantec | Electrical Engineering Intern - Buildings (Summer 2027) | [Apply](https://hdhl.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1008372) | Austin, TX, United States | No skills listed | Oct 20, 2026 |
| Hitachi Energy | Controls Engineering Internship | [Apply](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Ogden-Utah-United-States/Controls-Engineering-Internship_R0148732) | Ogden, Utah, United States | No skills listed | Oct 20, 2026 |
| Moog | Intern, Electrical Engineering _(2 openings)_ | [Apply](https://moog.wd5.myworkdayjobs.com/moog_external_career_site/job/Torrance-CA/Intern--Electrical-Engineering_R-26-19827) [#2](https://moog.wd5.myworkdayjobs.com/moog_external_career_site/job/Torrance-CA/Intern--Electrical-Engineering_R-26-19824) | Torrance, CA | C++, MATLAB, Verilog | Oct 20, 2026 |
| Rockwell Automation ✓ | Intern, Hardware Development Engineer (May - Aug 2027) 🛂 | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mayfield-Heights-Ohio-United-States/Intern--Hardware-Development-Engineer--May---Aug-2027-_R26-6892-2) | Mayfield Heights, Ohio, United States | Python, C++ | Oct 20, 2026 |
| Anduril | 2027 Guidance, Navigation, & Control Engineer Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5268736007?gh_jid=5268736007) | Costa Mesa, California, United States | MATLAB, Computer Vision | Oct 19, 2026 |
| Nissan | Mechanical & Electrical Engineer Intern - Summer 2027 - Canton, MS 🛂 | [Apply](https://alliance.wd3.myworkdayjobs.com/nissanjobs/job/Canton-Mississippi---United-States-of-America/Mechanical---Electrical-Engineer-Intern---Summer-2027---Canton--MS_R00214259) | Canton +1 more | No skills listed | Oct 19, 2026 |
| Charter Manufactur​ing | Controls Engineer Intern (Summer 2027) | [Apply](https://chartermfg.wd5.myworkdayjobs.com/Charter_Careers/job/Charter-Aarrowcast---Shawano-WI/Controls-Engineer-Intern--Summer-2027-_R08167) | Charter Aarrowcast - Shawano, WI | SQL | Oct 19, 2026 |
| Charter Manufactur​ing | Electrical Maintenance Engineer Intern (Summer 2027) | [Apply](https://chartermfg.wd5.myworkdayjobs.com/Charter_Careers/job/Charter-Aarrowcast---Shawano-WI/Electrical-Maintenance-Engineer-Intern--Summer-2027-_R08189) | Charter Aarrowcast - Shawano, WI | No skills listed | Oct 19, 2026 |
| Sierra Nevada Corporation | Electrical Engineering Intern - Summer 2027 (For SNC Summer 2026 Interns Only) | [Apply](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Lone-Tree-CO/Electrical-Engineering-Intern---Summer-2027--For-SNC-Summer-2026-Interns-Only-_R0031088) | Lone Tree, CO | MATLAB | Oct 16, 2026 |
| Inversion Space | Avionics Mechanical Engineer - Summer Internship 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/inversionspace/jobs/4744390005) | Playa Vista, California, United States | No skills listed | Oct 15, 2026 |
| Commonwealth Fusion Systems | Intern - Controls Engineer - Summer 2027 | [Apply](https://jobs.lever.co/cfsenergy/e3408817-347e-45bc-8627-305b75b6b978) | Milpitas, CA | No skills listed | Oct 15, 2026 |
| Inversion Space | Avionics Embedded Software Engineer - Summer Internship 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/inversionspace/jobs/4744391005) | Playa Vista, California, United States | Python, C++, Linux, Git | Oct 15, 2026 |
| Charter Manufactur​ing | Electrical Controls Engineer Intern (Summer 2027) | [Apply](https://chartermfg.wd5.myworkdayjobs.com/Charter_Careers/job/Charter-Wire---81st-Street---Milwaukee-WI/Electrical-Controls-Engineer-Intern_R08114) | Charter Wire - 81st Street - Milwaukee +1 more | Python, Java, SQL | Oct 14, 2026 |
| Motorola | Electrical Engineer / PCB Designer Intern - Summer 2027 🇺🇸 | [Apply](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Plantation-FL/Electrical-Engineer---PCB-Designer-Intern---Summer-2027_R69679) | Plantation, FL | No skills listed | Oct 14, 2026 |
| Rockwell Automation ✓ | Co-op, Electrical Engineer (June - Dec 2027) 🛂 | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Chelmsford-Massachusetts-United-States/Co-op--Electrical-Engineer--June---Dec-2027-_R26-7706) | Chelmsford, Massachuse​tts, United States | Python, MATLAB | Oct 14, 2026 |
| Rockwell Automation ✓ | Co-op, Hardware Development Engineer (June - Dec 2027) 🛂 | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mayfield-Heights-Ohio-United-States/Co-op--Hardware-Development-Engineer--June---Dec-2027-_R26-6891) | Mayfield Heights, Ohio, United States | Python, C++ | Oct 14, 2026 |
| Amazon ✓ | ASIC Engineer Intern, Summer 2027 | [Apply](https://www.amazon.jobs/en/jobs/10576619/asic-engineer-intern-summer-2027) | Sunnyvale, California, USA | C++, Verilog | Oct 13, 2026 |
| Amazon ✓ | Hardware Development Engineer Intern,  Summer 2027 | [Apply](https://www.amazon.jobs/en/jobs/10578090/hardware-development-engineer-intern-summer-2027) | Sunnyvale, California, USA | No skills listed | Oct 13, 2026 |
| Inversion Space | RF Engineer - Summer Internship 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/inversionspace/jobs/4743497005) | Playa Vista, California, United States | Python, MATLAB | Oct 13, 2026 |
| Howmet Aerospace | Intern & Co-op – Electrical/Controls Engineer - Whitehall, MI (2027) 🛂 | [Apply](https://fa-exty-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/119924) | Whitehall, MI, United States | No skills listed | Oct 13, 2026 |
| STV ✓ | Electrical Engineering Intern - Summer 2027 🛂 | [Apply](https://stvinc.wd5.myworkdayjobs.com/stv/job/Oklahoma-City-Oklahoma/Electrical-Engineering-Intern---Summer-2027_JR6227) | Oklahoma City, Oklahoma | No skills listed | Oct 13, 2026 |
| Anduril | 2027 Firmware Engineer Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5265158007?gh_jid=5265158007) | Costa Mesa, California, United States | Computer Vision | Oct 13, 2026 |
| DoorDash ✓ | Electrical Engineer, Intern - Labs (Summer 2027) | [Apply](https://job-boards.greenhouse.io/doordashusa/jobs/8274095) | Oakland, CA | Python, C++ | Oct 12, 2026 |
| NVIDIA ✓ | PCIe Design Verification Intern - Summer 2027 | [Apply](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/US-TX-Austin/PCIe-Design-Verification-Intern---Summer-2027_JR2026708) | US, TX, Austin | Python, Verilog | Oct 12, 2026 |
| Applied Materials ✓ | 2027 Summer Electrical Engineer  Intern (Controls/PCB) - BS or MS (Gloucester, MA) | [Apply](https://amat.wd1.myworkdayjobs.com/External/job/GloucesterMA/XMLNAME-2027-Summer-Electrical-Engineer--Intern--Controls-PCB----BS-or-MS--Gloucester--MA-_R2630658) | Gloucester​,MA | No skills listed | Oct 09, 2026 |
| Draper | Integrated Circuits Intern (Summer 2027) 🇺🇸 | [Apply](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Integrated-Circuits-Intern_JR002973) | Cambridge, MA | Python, MATLAB, Verilog | Oct 09, 2026 |
| STV ✓ | Electrical Engineering Intern - Summer 2027 🛂 | [Apply](https://stvinc.wd5.myworkdayjobs.com/stv/job/Boston-Massachusetts/Electrical-Engineering-Intern---Summer-2027_JR6127) | Boston, Massachuse​tts | No skills listed | Oct 09, 2026 |
| Rugged Robotics | Electrical Engineering Intern/Co-op (Spring or Summer '27) | [Apply](https://job-boards.greenhouse.io/ruggedrobotics/jobs/4724214005) | Houston, TX | No skills listed | Oct 08, 2026 |
| Amazon ✓ | Software Development Engineer (Embedded Systems) Intern, Amazon Leo - Summer 2027 (USA) 🇺🇸 | [Apply](https://www.amazon.jobs/en/jobs/10571374/software-development-engineer-embedded-systems-intern-amazon-leo-summer-2027-usa) | Redmond, Washington, USA | Python, Java, C++, C# | Oct 07, 2026 |
| Carpenter Technology | Maintenance Intern - Electrical | [Apply](https://cartech.wd5.myworkdayjobs.com/CTCExternal/job/Reading-PA/Maintenance-Intern---Electrical_26884) | Reading, PA | No skills listed | Oct 06, 2026 |
| The Toro Company | Electronics Technician Intern - The Toro Company 🛂 | [Apply](https://ttc.wd1.myworkdayjobs.com/Toro_External_Careers/job/Bloomington-MN/Electronics-Technician-Intern---The-Toro-Company_JR17552) | Bloomington, MN | No skills listed | Oct 06, 2026 |
| Arc | Electrical Integration Engineering Intern | [Apply](https://job-boards.greenhouse.io/arcboatcompany/jobs/5442838008) | Torrance, CA | MATLAB | Oct 05, 2026 |
| Arc | Vehicle Controls Engineering Intern | [Apply](https://job-boards.greenhouse.io/arcboatcompany/jobs/5442902008) | Torrance, CA | MATLAB | Oct 05, 2026 |
| Arc | Electrical Engineering Intern - Powertrain | [Apply](https://job-boards.greenhouse.io/arcboatcompany/jobs/5443971008) | Torrance, CA | Python | Oct 05, 2026 |
| Hitachi Energy | Controls Engineering Internship/Co-op | [Apply](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Auburn-Hills-Michigan-United-States/Controls-Engineering-Internship-Co-op_R0143858) | Auburn Hills, Michigan, United States | No skills listed | Oct 05, 2026 |
| Hitachi Energy | Controls Engineering Internship/Co-op _(2 openings)_ | [Apply](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Holland-Michigan-United-States/Controls-Engineering-Internship-Co-op_R0144971) [#2](https://hitachi.wd1.myworkdayjobs.com/hitachi/job/Holland-Michigan-United-States/Controls-Engineering-Internship-Co-op_R0144972) | Holland, Michigan, United States | No skills listed | Oct 05, 2026 |
| Marvell | Hardware Engineer Intern, BS - Summer 2027 | [Apply](https://marvell.wd1.myworkdayjobs.com/marvellcareers2/job/Santa-Clara-CA/Hardware-Engineer-Intern--BS---Summer-2027_2604975) | Santa Clara, CA | Linux | Oct 05, 2026 |
| Muon Space | Electrical Engineering Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/muonspace/jobs/5255112007) | San Jose, CA | Python, C++ | Oct 01, 2026 |
| Varda Space | Avionics Engineering Internship - Summer 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/vardaspace/jobs/8010158003) | El Segundo, California, United States | Python | Oct 01, 2026 |
| Xcimer Energy | Summer 2027 Internship - Electrical Engineering 🇺🇸 | [Apply](https://jobs.lever.co/xcimer/87bceb04-faeb-4365-9fed-d8f5cd3fb8ac) | Denver, CO | No skills listed | Sep 30, 2026 |
| ABB ✓ | Electrical Design Engineer Intern- Summer 2027 🛂 | [Apply](https://abb.wd3.myworkdayjobs.com/external_career_page/job/Fort-Smith-Arkansas-United-States-of-America/Electrical-Design-Engineer-Intern--Summer-2027_JR00045726) | Fort Smith +2 more | No skills listed | Sep 30, 2026 |
| Muon Space | GNC Hardware Engineering Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/muonspace/jobs/5252677007) | Mountain View, CA | No skills listed | Sep 29, 2026 |
| nVent | Electrical/Controls Engineering Co-Op (June - December 2027) | [Apply](https://nvent.wd5.myworkdayjobs.com/nVent/job/Anoka-MN-US/Electrical-Controls-Engineering-Co-Op_R23626) | Anoka, MN, US | No skills listed | Sep 29, 2026 |
| Hermeus | Flight Software Engineering Intern (Simulation/Hardware-In-The-Loop) - Spring & Summer 2027 🇺🇸 | [Apply](https://jobs.lever.co/hermeus/78008094-ca81-4a0c-9a18-93b30f932acd) | Los Angeles, CA | Python, C++, MATLAB, Linux | Sep 29, 2026 |
| General Dynamics Mission Systems | Electrical Engineering Intern (Summer 2027) 🇺🇸 | [Apply](https://careers-gdms.icims.com/jobs/75138/electrical-engineering-intern-%28summer-2027%29/job?in_iframe=1) | West Valley City, UT, US | No skills listed | Sep 28, 2026 |
| HNTB ✓ | WED - Intern Electrical Power System (Summer 2027) (For Current & Recent HNTB Interns Only) 🛂 | [Apply](https://hntb.wd5.myworkdayjobs.com/hntb_careers/job/Los-Angeles-CA-Figueroa-Street/WED---Intern-Electrical-Power-System--Summer-2027---For-Current---Recent-HNTB-Interns-Only-_R-31767-1) | Los Angeles, CA (Figueroa Street) | No skills listed | Sep 28, 2026 |
| AtkinsRéalis | Instrument​ation & Controls Engineering Intern - Summer 2027 | [Apply](https://slihrms.wd3.myworkdayjobs.com/careers/job/USWABothell/Instrumentation---Controls-Engineering-Intern---Summer-2027_R-162442-1) | US.WA.Both​ell | No skills listed | Sep 28, 2026 |
| Philips | Intern – Embedded Systems Test Automation Engineer – Bothell, WA – Summer 2027 | [Apply](https://philips.wd3.myworkdayjobs.com/jobs-and-careers/job/Bothell-Washington-United-States/Intern---Embedded-Systems-Test-Automation-Engineer---Bothell--WA---Summer-2027_592074) | Bothell, Washington, United States | Python, C++ | Sep 28, 2026 |
| Helion Energy | Electrical Engineering Summer 2027 Intern | [Apply](https://jobs.ashbyhq.com/helion/045d97eb-5efd-4e35-90f5-65eebe3363f4) | Everett, WA | No skills listed | Sep 25, 2026 |
| Mach Industries | Summer 2027 Engineering Internship, Electrical 🛂 | [Apply](https://job-boards.greenhouse.io/machindustries/jobs/4420623009) | Huntington Beach +5 more | No skills listed | Sep 25, 2026 |
| Zurn Elkay Water Solutions | Embedded Hardware Intern (Summer 2027) | [Apply](https://elkay.wd1.myworkdayjobs.com/Elkay_External/job/Milwaukee-WI/Embedded-Hardware-Intern--Summer-2027-_REQ-020151) | Milwaukee, WI | No skills listed | Sep 25, 2026 |
| Stanley Black & Decker ✓ | Electrical Engineering Intern Summer 2027 🛂 | [Apply](https://sbdinc.wd1.myworkdayjobs.com/Stanley_Black_Decker_Career_Site/job/Towson-MD-United-States/Electrical-Engineering-Intern-Summer-2027_REQ-1000052018) | Towson, MD, United States | No skills listed | Sep 24, 2026 |
| General Dynamics Mission Systems | Electrical Intern Engineer 🇺🇸 | [Apply](https://careers-gdms.icims.com/jobs/75111/electrical-intern-engineer/job?in_iframe=1) | Canonsburg, PA, US | No skills listed | Sep 22, 2026 |
| Xcimer Energy | Summer 2027 Internship - Controls Systems Engineering 🇺🇸 | [Apply](https://jobs.lever.co/xcimer/4b031cd4-5f45-4d53-9332-dd23bc349480) | Denver, CO | No skills listed | Sep 22, 2026 |
| Formlabsin​ternships | Embedded Software Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/formlabsinternships/jobs/8222268) | Somerville, MA | Python, C++, Linux | Sep 21, 2026 |
| Rocket Lab | Electrical Engineering Intern Summer 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/rocketlab/jobs/7998598003) | Pasadena, CA | No skills listed | Sep 17, 2026 |
| Rehiko | Electrical Engineering Intern 2027 | [Apply](https://rehlko.wd12.myworkdayjobs.com/Reh/job/SheboyganWI/Electrical-Engineering-Intern-2027_R04824) | Sheboygan,WI | No skills listed | Sep 16, 2026 |
| AspenTech | Power System Engineering Intern - Digital Grid Management - Summer 2027 | [Apply](https://aspentech.wd5.myworkdayjobs.com/aspentech/job/Medina-Minnesota/Power-System-Engineering-Intern---Digital-Grid-Management---Summer-2027_R9458) | Medina, Minnesota | Python, Linux | Sep 15, 2026 |
| nVent | Electrical Engineering Co-Op (June - Dec 2027) | [Apply](https://nvent.wd5.myworkdayjobs.com/nVent/job/Solon-OH-US/Electrical-Engineering-Co-Op_R23593) | Solon, OH, US | MATLAB | Sep 15, 2026 |
| Bedrock Robotics | 2027 Internship Hardware Engineer, Machine Integration & Test | [Apply](https://jobs.ashbyhq.com/bedrock-robotics/c9c08251-6a42-4f9c-be4d-2621995cc8f9) | San Francisco, CA | No skills listed | Sep 14, 2026 |
| Michael Baker Internatio​nal ✓ | Electrical Engineering Intern, Summer 2027 | [Apply](https://ebxs.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2/job/309857) | San Diego, CA, United States | No skills listed | Sep 14, 2026 |
| Formlabsin​ternships | Electrical Engineering Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/formlabsinternships/jobs/8381504) | Somerville, MA | Python | Sep 13, 2026 |
| Xcimer Energy | Summer 2027 Internship - Pulsed Power Engineering 🇺🇸 | [Apply](https://jobs.lever.co/xcimer/39fd5473-58a8-446c-86fb-258c1dd0f67d) | Denver, CO | No skills listed | Sep 11, 2026 |
| Emerson Electric | Hardware Design Engineer Intern | [Apply](https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/26010801) | Round Rock, TX, United States | Python, C++, MATLAB, Verilog | Sep 11, 2026 |
| Motorola | DSP (Digital Signal Processing) Software Engineering Intern - Summer 2027 | [Apply](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Plantation-FL/DSP--Digital-Signal-Processing--Software-Engineering-Intern---Summer-2027_R68734) | Plantation, FL | Python, C++, MATLAB, Linux | Sep 11, 2026 |
| Bedrock Robotics | 2027 Internship Sensor Hardware Test Engineer | [Apply](https://jobs.ashbyhq.com/bedrock-robotics/1f413f83-b897-4938-a19e-ab91bd326c51) | San Francisco, CA | Python, Git | Sep 10, 2026 |
| Bedrock Robotics | 2027 Internship Hardware Engineer | [Apply](https://jobs.ashbyhq.com/bedrock-robotics/949feb1b-c60f-43c5-94de-7dd9cd70ba4a) | San Francisco, CA | Python, C++, Rust, Git | Sep 10, 2026 |
| Rocket Lab | Electrical Engineering Intern Summer 2027 🇺🇸 | [Apply](https://job-boards.greenhouse.io/rocketlab/jobs/7990683003) | Long Beach, CA | Python, C++, Verilog | Sep 10, 2026 |
| Avav | Summer 2027 Embedded Software Engineering Intern | [Apply](https://avav.wd1.myworkdayjobs.com/avav/job/Simi-Valley-CA/Summer-2027-Embedded-Software-Engineering-Intern_8549) | Simi Valley, CA | Python, C++, Linux | Sep 10, 2026 |
| The Toro Company | Hardware and Software Engineering Intern - Ditch Witch 🛂 | [Apply](https://ttc.wd1.myworkdayjobs.com/Toro_External_Careers/job/Perry-OK/Hardware-and-Software-Engineering-Intern---Ditch-Witch_JR17183) | Perry, OK | Python, Java, C++, C# | Sep 10, 2026 |
| General Dynamics Mission Systems | Payload Control System - Software/Systems Engineering Intern (Summer 2027) 🇺🇸 | [Apply](https://careers-gdms.icims.com/jobs/74848/payload-control-system---software-systems-engineering-intern-%28summer-2027%29/job?in_iframe=1) | Manassas, VA, US | Python, Java, C++, TypeScript | Sep 09, 2026 |
| Saronic | Electrical Engineer Intern (Summer 2027) 🇺🇸 | [Apply](https://jobs.ashbyhq.com/saronic/c7779462-3c4c-44d9-8314-1be93a0e478a) | Austin, TX | Python, C++, Linux | Sep 09, 2026 |
| Hermeus | Avionics Electrical Engineering Intern - Summer 2027 🇺🇸 | [Apply](https://jobs.lever.co/hermeus/b7babdb5-64ee-49ad-a193-918d6a31c462) | Atlanta, GA | C++ | Sep 09, 2026 |
| Allen Control Systems | Electrical Engineering Intern, 2027 | [Apply](https://jobs.ashbyhq.com/allen-control-systems/cc1618f1-e4b8-4dcb-88fd-9771da972220) | Austin, TX | Computer Vision | Sep 08, 2026 |
| RF-SMART | Hardware Support Internship - Summer 2027 🛂 | [Apply](https://job-boards.greenhouse.io/rfsmart/jobs/5407220008) | Jacksonvil​le, Florida, United States | No skills listed | Sep 08, 2026 |
| Sensata | Electrical Engineer Intern (Dynapower) - Summer 2027 | [Apply](https://sensata.wd1.myworkdayjobs.com/Sensata-Careers/job/Dynapower-South-Burlington-VT/Electrical-Engineer-Intern--Dynapower----Summer-2027_IRC98423) | Dynapower South Burlington, VT | No skills listed | Sep 08, 2026 |
| Stryker ✓ | Summer 2027 Internship - Electrical Engineering - Florida | [Apply](https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Weston-Florida/Electrical-Engineering-Intern---Weston--FL_R572740) | Weston, Florida | No skills listed | Sep 08, 2026 |
| AMCA | Electrical Engineering Internship (Summer 2027) | [Apply](https://job-boards.greenhouse.io/amca/jobs/4396690009) | El Segundo, CA | No skills listed | Sep 04, 2026 |
| HNTB ✓ | Intern Electrical and Mechanical/Fire Protection Engineering (Summer 2027) 🛂 | [Apply](https://hntb.wd5.myworkdayjobs.com/hntb_careers/job/Bellevue-WA-Seattle/Intern-Electrical-and-Mechanical-Fire-Protection-Engineering--Summer-2027-_R-31482-1) | Bellevue, WA (Seattle) | No skills listed | Sep 04, 2026 |
| Vermeer | Electrical Engineer Internship Summer 2027 | [Apply](https://vermeer.wd5.myworkdayjobs.com/externalcareersite/job/Pella-Iowa-USA---Corporate-Office/Electrical-Engineer-Internship-Summer-2027_REQ-22166) | Pella, Iowa, USA - Corporate Office | MATLAB | Sep 04, 2026 |
| Stanley Black & Decker ✓ | Embedded Engineering Summer Intern 2027 | [Apply](https://sbdinc.wd1.myworkdayjobs.com/Stanley_Black_Decker_Career_Site/job/Towson-MD-United-States/Embedded-Engineering-Summer-Intern-2027_REQ-1000052019) | Towson, MD, United States | No skills listed | Sep 01, 2026 |
| Vermeer | Embedded Software Engineer Internship Summer 2027 | [Apply](https://vermeer.wd5.myworkdayjobs.com/externalcareersite/job/Pella-Iowa-USA---Corporate-Office/Embedded-Software-Engineer-Internship-Summer-2027_REQ-22165) | Pella, Iowa, USA - Corporate Office | C++, MATLAB, Git | Sep 01, 2026 |
| Hudson River Trading ✓ | Hardware Engineer Internship - Summer 2027 | [Apply](https://www.hudsonrivertrading.com/careers/job/?gh_jid=7899574) | New York, NY, United States | Python, C++, Linux, Verilog | Aug 31, 2026 |
| Stryker ✓ | Summer 2027 Internship - Electrical Engineering - Michigan | [Apply](https://stryker.wd1.myworkdayjobs.com/StrykerCareers/job/Portage-Michigan/Summer-2027-Internship---Electrical-Engineering---Michigan_R572609) | Portage, Michigan | No skills listed | Aug 31, 2026 |
| Honeywell | Electrical Engineering - Summer 2027 Intern (US Person Required) 🇺🇸 | [Apply](https://ibqbjb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/155537) | United States | No skills listed | Aug 25, 2026 |
| Honeywell | Electrical Engineering - Summer 2027 Intern | [Apply](https://ibqbjb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/155540) | United States | No skills listed | Aug 25, 2026 |
| Honeywell | Embedded Engineer - Summer 2027 Intern (US Person Required) 🇺🇸 | [Apply](https://ibqbjb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/155561) | United States | Python, C++, MATLAB | Aug 25, 2026 |
| Verkada ✓ | Embedded Software Engineering Intern 2027 | [Apply](https://job-boards.greenhouse.io/verkada/jobs/5211595007) | San Mateo, CA United States | C++, Linux | Aug 25, 2026 |
| General Matter | Summer 2027 Internship - Electrical Engineering (Buildings) | [Apply](https://job-boards.greenhouse.io/generalmatter/jobs/5376639008) | Los Angeles, CA | Python, C# | Aug 20, 2026 |
| Freeform | Electrical Engineering Intern (Summer 2027) | [Apply](https://job-boards.greenhouse.io/freeformfuturecorp/jobs/7895657003) | Los Angeles, CA (On-site) | No skills listed | Aug 19, 2026 |
| Montenson | Electrical Engineering Intern – Summer 2027 🛂 | [Apply](https://fa-esgu-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/23239) | United States | No skills listed | Aug 10, 2026 |
| Nexus Engineering Group | Electrical/Substation Engineering Internship or Co-Op (Summer 2027) | [Apply](https://jobs.lever.co/nexuse-group/9c859eeb-b251-4865-bc1a-a5737ef42620) | Maumee, OH | No skills listed | Aug 05, 2026 |
| HPR (Hyannis Port Research) | FPGA Engineering Intern - Summer 2027 | [Apply](https://job-boards.greenhouse.io/hyannisportresearch/jobs/7822801003) | Needham, MA | Python, Linux, Verilog | Jul 31, 2026 |
| Kairos Power | Electrical Engineering Internship - Summer 2027 | [Apply](https://job-boards.greenhouse.io/kairospower/jobs/6123657004) | Alameda +4 more | No skills listed | Jul 23, 2026 |
| Virtu Financial | 2027 Internship- Hardware Engineer (FPGA) | [Apply](https://job-boards.greenhouse.io/virtu/jobs/8657286002) | Austin, TX | Python, Java, C++, JavaScript | Jul 21, 2026 |
| Anduril | 2027 Electrical Engineer Intern | [Apply](https://boards.greenhouse.io/andurilindustries/jobs/5148101007?gh_jid=5148101007) | Atlanta +26 more | Python, C++, Rust, Computer Vision | Jun 11, 2026 |
| Forterra | 2027 Intern - Electrical Engineer | [Apply](https://ats.rippling.com/forterra/jobs/bb7de11c-a4ea-4a91-ab98-8b4a36a37311) | Clarksburg, MD | No skills listed | — |
| Omnis | Electrical Engineering Intern (Spring and Summer 2027) | [Apply](https://ats.rippling.com/omnis-corporation/jobs/3834b774-a185-4106-a04a-969bd42af220) | Los Angeles, CA | No skills listed | — |
| Omnis | Wireless Systems Intern, MAC and PHY (Spring and Summer 2027) | [Apply](https://ats.rippling.com/omnis-corporation/jobs/c534b2ba-a409-4c26-bb92-704e48fccb63) | Venice, Los Angeles, CA | No skills listed | — |
| Torus | Power Electrical Engineer Intern (Summer 2027) | [Apply](https://ats.rippling.com/torus/jobs/ee8aa54d-a03b-4ca5-a0c5-d301f7cd67d8) | Salt Lake City, UT | No skills listed | — |

## Fall 2026  (10 employer-stated)

| Company | Role | Apply | Location | Skills | Posted |
|---|---|---|---|---|---|
| WSP | Power System Optimization Intern - Fall 2026/Spring 2027 | [Apply](https://emit.fa.ca3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/98600) | Houston, TX, United States | Python | Nov 09, 2026 |
| WSP | Data Center Electrical Engineering Intern - Fall 2026 - Spring 2027 | [Apply](https://emit.fa.ca3.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/97816) | New York, NY, United States | No skills listed | Oct 19, 2026 |
| Moog | Intern, Embedded Design Engineering | [Apply](https://moog.wd5.myworkdayjobs.com/moog_external_career_site/job/Blacksburg-VA/Intern--Embedded-Design-Engineering_R-26-20053) | Blacksburg, VA | No skills listed | Sep 11, 2026 |
| Cadence Design Systems ✓ | Product Engineering Internship, Electronics Hardware Design (Fall 2026) | [Apply](https://cadence.wd1.myworkdayjobs.com/University_Talent/job/Burlington-MA/Product-Engineering-Internship--Electronics-Hardware-Design--Fall-2026-_R54158-1) | Burlington, MA | No skills listed | Aug 25, 2026 |
| Mill | Electrical Engineering Intern, Fall/Winter 2026 🛂 | [Apply](https://job-boards.greenhouse.io/mill/jobs/4724014005) | San Bruno, California | Python | Aug 13, 2026 |
| RoboForce | Robotics Electrical Engineering Intern (Fall/Winter 2026) | [Apply](https://job-boards.greenhouse.io/roboforce/jobs/5181214008) | Milpitas, CA | Python, C++, Linux, Git | Apr 14, 2026 |
| Motorola | R&D Intern - Wireless Systems Engineer - 2026 🇺🇸 | [Apply](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Los-Angeles-CA/R-D-Intern---Wireless-Systems-Engineer---2026_R62376) | Los Angeles, CA | MATLAB | Mar 30, 2026 |
| Motorola | Intern - Embedded Software, System, and Test Engineer - 2026 🇺🇸 | [Apply](https://motorolasolutions.wd5.myworkdayjobs.com/Careers/job/Irvine-CA/Intern---Embedded-Software--System--and-Test-Engineer---2026_R62372) | Irvine, CA | No skills listed | Mar 30, 2026 |
| Amazon ✓ | Robotics - Hardware Development Engineer Intern/Co-op - 2026 (Robotics, Mechanical, Electrical, Hardware Test, Reliability, Failure Analysis, Operations, and more) | [Apply](https://www.amazon.jobs/en/jobs/3145033/robotics-hardware-development-engineer-intern-co-op-2026-robotics-mechanical-electrical-hardware-test-reliability-failure-analysis-operations-and-more) | Westboro, Massachuse​tts, USA | No skills listed | Dec 17, 2025 |
| Nightwing Intelligence Solutions | RF Engineering Intern - 2026 | [Apply](https://nwis.wd12.myworkdayjobs.com/NW/job/Sterling-VA/RF-Engineering-Intern---2026_JR101095) | Sterling, VA | No skills listed | Dec 12, 2025 |

## Recently posted — cycle not stated  (91 roles)

These postings never name a cycle — not in the title, not in the posting text — so neither do we. They're recent internships (posted within the last few weeks), often exactly the early drops worth applying to first; we just can't tell you which cycle they're for, and we'd rather say so than guess. The moment a posting's own text states a cycle, the role moves up into that section automatically.

| Company | Role | Apply | Location | Skills | Posted |
|---|---|---|---|---|---|
| Neuralink | Electrical Test Engineer Intern 🆕 | [Apply](https://boards.greenhouse.io/neuralink/jobs/8197808003?gh_jid=8197808003) | South San Francisco +2 more | Python, C++, Rust | Nov 24, 2026 |
| Ralliant | Hardware Engineering Co-Op 🆕 | [Apply](https://ibwujb.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/10451) | Solon, OH, United States | No skills listed | Nov 24, 2026 |
| Samsung | Intern, RF Analog Circuit Design Engineer 🆕 | [Apply](https://job-boards.greenhouse.io/samsungsemiconductor/jobs/8213439003) | San Jose, California, United States | Python, Verilog | Nov 24, 2026 |
| Rockwell Automation ✓ | Intern, Mechatronics & Electromag​netics | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Mequon-Wisconsin-United-States/Intern--Mechatronics---Electromagnetics_R26-8372-1) | Mequon, Wisconsin, United States | No skills listed | Nov 23, 2026 |
| Legrand | Electrical Engineering Intern | [Apply](https://iadugs.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/1948) | Canonsburg, PA, United States | No skills listed | Nov 23, 2026 |
| Samsung | Intern, Serdes Analog Design Engineer | [Apply](https://job-boards.greenhouse.io/samsungsemiconductor/jobs/8197312003) | San Jose, California, United States | Python, MATLAB, Verilog | Nov 19, 2026 |
| Graco | Electrical Engineering Intern 🛂 | [Apply](https://graco.wd501.myworkdayjobs.com/Graco_Careers/job/Flagstaff-Arizona-USA/Mechanical-Engineering-Intern_R0023552) | Flagstaff, Arizona, USA | Python | Nov 19, 2026 |
| First Quality | Controls Engineer Intern | [Apply](https://firstquality.wd5.myworkdayjobs.com/firstquality/job/US-PA-Lock-Haven/Controls-Engineer-Intern_R12278) | US PA Lock Haven | No skills listed | Nov 18, 2026 |
| Samsung | Intern, SSD Firmware Engineer | [Apply](https://job-boards.greenhouse.io/samsungsemiconductor/jobs/8208662003) | San Jose, California, United States | Python, C++, JavaScript | Nov 18, 2026 |
| Texas Instruments ✓ | Analog IC Design (AI/ML) Engineering Intern | [Apply](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/25020319) | Dallas, TX, United States | Python, PyTorch, TensorFlow, scikit-learn | Nov 17, 2026 |
| Lunar Energy ✓ | Power Electronics Test Intern | [Apply](https://job-boards.greenhouse.io/lunarenergy/jobs/6220078004) | Mountain View, CA | Python, C++ | Nov 16, 2026 |
| Texas Instruments ✓ | Kilby Labs RF Analog Design Intern - RF Modeling | [Apply](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/25016351) | Dallas, TX, United States | No skills listed | Nov 16, 2026 |
| IMEG ✓ | Electrical Engineering Intern / Indianapol​is, IN 🛂 | [Apply](https://wd1.myworkdaysite.com/recruiting/imeg/Imeg_Careers/job/Indianapolis-IN/Electrical-Engineering-Intern---Indianapolis--IN_R-16961) | Indianapol​is, IN | No skills listed | Nov 16, 2026 |
| Bloom Energy ✓ | Electrical Engineering Intern 🛂 | [Apply](https://bloomenergy.wd1.myworkdayjobs.com/bloomenergycareers/job/Fremont-California/Electrical-Engineering-Intern_JR-25271) | Fremont, California | MATLAB | Nov 13, 2026 |
| Bloom Energy ✓ | Electrical Engineering Intern (Masters) 🛂 | [Apply](https://bloomenergy.wd1.myworkdayjobs.com/bloomenergycareers/job/San-Jose-California/Electrical-Engineering-Intern--Masters-_JR-25385) | San Jose, California | No skills listed | Nov 13, 2026 |
| Texas Instruments ✓ | Analog Design Eng Intern (GaN Device) _(2 openings)_ | [Apply](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/25016345) [#2](https://edbz.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/25020327) | Santa Clara, CA, United States | Verilog | Nov 13, 2026 |
| KLA ✓ | Electrical Engineering Intern | [Apply](https://kla.wd1.myworkdayjobs.com/AnnArbor/job/Ann-Arbor-MI/Electrical-Engineering-Intern_2642897-1) | Ann Arbor, MI | No skills listed | Nov 11, 2026 |
| Badger Meter | Electronics/Electrical Engineering Internship | [Apply](https://badgermeter.wd5.myworkdayjobs.com/US_CareerSite/job/US---WI---Racine-Facility/Electronics-Electrical-Engineering-Internship_4633) | US - WI - Racine Facility | No skills listed | Nov 11, 2026 |
| Bose ✓ | Digital Signal Processing ML Software Development Co-op | [Apply](https://boseallaboutme.wd503.myworkdayjobs.com/Bose_Careers/job/US-MA---Framingham/Digital-Signal-Processing-ML-Software-Development-Co-op_R29372) | US, MA - Framingham | Python, MATLAB | Nov 11, 2026 |
| Entrust | Electrical Engineer Co-op | [Apply](https://entrust.wd1.myworkdayjobs.com/entrustcareers/job/United-States---Shakopee-MN-GHQ/Electrical-Engineer-Co-op_R004413) | United States - Shakopee, MN (GHQ) | No skills listed | Nov 11, 2026 |
| KLA ✓ | Electrical Engineering Internship | [Apply](https://kla.wd1.myworkdayjobs.com/UR/job/Milpitas-CA/Electrical-Engineering-Internship_2643472) | Milpitas, CA | No skills listed | Nov 11, 2026 |
| REGENT | Radar Signal Processing Intern (Summer) | [Apply](https://jobs.ashbyhq.com/REGENT/2b98602b-2060-45c7-a916-ae7ca9656fd3) | North Kingstown, Rhode Island, USA | Python, MATLAB | Nov 11, 2026 |
| Analog Devices ✓ | Mechatronics Engineering Intern | [Apply](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-OR-Beaverton/Mechatronics-Engineering-Intern_R268831) | US, OR, Beaverton | Python, C++, MATLAB | Nov 10, 2026 |
| REGENT | Embedded Software Engineering Intern (Summer) | [Apply](https://jobs.ashbyhq.com/REGENT/9f25824f-486e-4d3a-b444-116b474619d7) | North Kingstown, Rhode Island, USA | Python, C++, Git | Nov 10, 2026 |
| Hewlett Packard Enterprise ✓ | Wireless Hardware Engineering Intern | [Apply](https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/San-Jose-California-United-States-of-America/Wireless-Hardware-Engineering-Intern_1218701) | San Jose +2 more | Python, MATLAB, HTML/CSS | Nov 09, 2026 |
| RTX | Digital Hardware Design Engineer Co-op (Winter/Spring)(On​site) 🇺🇸 | [Apply](https://globalhr.wd5.myworkdayjobs.com/rec_rtx_ext_gateway/job/US-IA-CEDAR-RAPIDS-130--5350-C-Ave-NE--BLDG-130/Digital-Hardware-Design-Engineer-Co-op--Spring-Summer-_01871518-1) | US-IA-CEDAR RAPIDS-130 ~ 5350 C Ave NE… | No skills listed | Nov 09, 2026 |
| Marathon Petroleum ✓ | Electrical Engineer I - Midstream Natural Gas & NGL Services (Intern to Full-Time Conversion) | [Apply](https://mpc.wd1.myworkdayjobs.com/MPCCareers/job/Canonsburg-Pennsylvania/Electrical-Engineer-I---Midstream-Natural-Gas---NGL-Services--Intern-to-Full-Time-Conversion-_00024745) | Canonsburg, Pennsylvania | No skills listed | Nov 09, 2026 |
| KLA ✓ | Electrical Engineering Intern | [Apply](https://kla.wd1.myworkdayjobs.com/Search/job/Milpitas-CA/Electrical-Engineering-Intern_2641972-1) | Milpitas, CA | Python | Nov 09, 2026 |
| Viavi Solutions ✓ | Digital Hardware Engineering Intern | [Apply](https://viavisolutions.wd1.myworkdayjobs.com/careers/job/Lenexa-KS-USA/Digital-Hardware-Engineering-Intern_260005289-1) | Lenexa, KS, USA | No skills listed | Nov 09, 2026 |
| Agiliti | DOD SkillBridge Instrument​ation Surgical Equipment Repair Technician Internship | [Apply](https://agiliti.wd5.myworkdayjobs.com/careers/job/Novi-MI---Lab/DOD-SkillBridge-Instrumentation-Surgical-Equipment-Repair-Technician-Internship_JR33659) | Novi MI - Lab | No skills listed | Nov 09, 2026 |
| Hewlett Packard Enterprise ✓ | Electrical Hardware Engineer Intern | [Apply](https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Sunnyvale-California-United-States-of-America/Electrical-Hardware-Engineer-Intern_1214992) | Sunnyvale +2 more | Python, HTML/CSS, Linux | Nov 08, 2026 |
| Fresenius Medical Care | Embedded Software Co-Op | [Apply](https://freseniusmedicalcare.wd3.myworkdayjobs.com/fme/job/Lawrence-MA-USA/Embedded-Software-Co-Op_R0273960) | Lawrence, MA, USA | No skills listed | Nov 05, 2026 |
| Legrand | Firmware Engineering Intern | [Apply](https://iadugs.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/1809) | Reno, NV, United States | Python, C++, TypeScript, Linux | Nov 05, 2026 |
| Rockwell Automation ✓ | Intern, Electrical Engineering 🛂 | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External_Rockwell_Automation/job/Chelmsford-Massachusetts-United-States/Intern--Electrical-Engineering_R26-8341-1) | Chelmsford, Massachuse​tts, United States | No skills listed | Nov 04, 2026 |
| Badger Meter | Firmware Test Engineer Intern | [Apply](https://badgermeter.wd5.myworkdayjobs.com/US_CareerSite/job/US---WI---Milwaukee-HQ/Firmware-Test-Engineer-Intern_4675) | US - WI - Milwaukee HQ | Python, Git | Nov 04, 2026 |
| Logiqal | Quantum Hardware Intern | [Apply](https://jobs.ashbyhq.com/logiqal/2734f991-1e21-4c77-bb41-211ffa88449d) | Princeton, NJ | Python, C++ | Nov 04, 2026 |
| Hewlett Packard Enterprise ✓ | Hardware Engineering Intern | [Apply](https://hpe.wd5.myworkdayjobs.com/Jobsathpe/job/Westford-Massachusetts-United-States-of-America/Hardware-Engineering-Intern_1214170) | Westford +2 more | Python, HTML/CSS, Linux, Verilog | Nov 03, 2026 |
| Bose ✓ | Electrical Engineering Co-op — FPGA and Audio Research Platforms | [Apply](https://boseallaboutme.wd503.myworkdayjobs.com/Bose_Careers/job/US-MA---Framingham/Electrical-Engineering-Co-op---FPGA-and-Audio-Research-Platforms_R29366) | US, MA - Framingham | MATLAB, Verilog | Nov 03, 2026 |
| ASML | CoOp - Electrical Engineer (Internship) | [Apply](https://asml.wd3.myworkdayjobs.com/asmlext1/job/Wilton-CT-USA/CoOp---Electrical-Engineer--Internship-_J-00356208) | Wilton, CT, USA | Python, MATLAB | Nov 02, 2026 |
| ASML | Coop - Mechatronics Engineer (Internship) | [Apply](https://asml.wd3.myworkdayjobs.com/asmlext1/job/Wilton-CT-USA/Coop---Mechatronics-Engineer--Internship-_J-00356203) | Wilton, CT, USA | MATLAB, Git | Nov 02, 2026 |
| ASML | Internship - Electrical Engineer _(2 openings)_ | [Apply](https://asml.wd3.myworkdayjobs.com/asmlext1/job/Wilton-CT-USA/Internship---Electrical-Engineer_J-00356457) [#2](https://asml.wd3.myworkdayjobs.com/asmlext1/job/Wilton-CT-USA/Internship---Electrical-Engineer_J-00355801) | Wilton, CT, USA | Python, MATLAB | Nov 02, 2026 |
| KION Group | Controls Engineering Intern/Co-Op | [Apply](https://kiongroup.wd3.myworkdayjobs.com/kiongroup/job/Grand-Rapids-MI-United-States/Controls-Engineering-Intern-Co-Op_JR-0094002-1) | Grand Rapids, MI, United States | No skills listed | Nov 02, 2026 |
| Valmont | Embedded Systems Engineering Intern | [Apply](https://valmont.wd1.myworkdayjobs.com/ValmontCareers/job/Valley-NE/Embedded-Systems-Engineering-Intern_R29223) | Valley NE | C++, Linux, Git | Nov 02, 2026 |
| Micron Technology ✓ | Intern - YE-Electrical Failure Analysis Engineer | [Apply](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---ID1/Intern---YE-Electrical-Failure-Analysis-Engineer_JR114538) | Boise, ID - ID1 | Python, SQL, LLMs, Tableau | Nov 02, 2026 |
| Johnson Controls ✓ | HVAC Control Systems Engineering Intern | [Apply](https://jci.wd5.myworkdayjobs.com/JCI/job/Glendale-Wisconsin-United-States-of-America/HVAC-Control-Systems-Engineering-Intern_WD30282523) | Glendale-Wisconsin-United States of Ame… | No skills listed | Nov 02, 2026 |
| Sierra Nevada Corporation | Firmware Engineering Intern 🇺🇸 | [Apply](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Folsom-CA/Firmware-Engineering-Intern_R0031219) | Folsom, CA | MATLAB | Oct 30, 2026 |
| Nokia | Silicon Photonics Packaging Engineer Co-op | [Apply](https://fa-evmr-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/40848) | United States | No skills listed | Oct 30, 2026 |
| Berkshire Hathaway Energy | Intern (Electrical Engineering) _(2 openings)_ | [Apply](https://fa-essf-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/10005978) [#2](https://fa-essf-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/10005994) | Lusby, MD, United States | No skills listed | Oct 30, 2026 |
| Global​Foundries | Digital Design Backend Engineering Intern, 3D and AI Flows | [Apply](https://globalfoundries.wd1.myworkdayjobs.com/External/job/USA---California---Santa-Clara/Digital-Design-Backend-Engineering-Intern--3D-and-AI-Flows_JR-2604355) | USA - California - Santa Clara | Python, SQL, Pandas | Oct 29, 2026 |
| Johnson Controls ✓ | HVAC Controls Systems Intern | [Apply](https://jci.wd5.myworkdayjobs.com/JCI/job/Glendale-Wisconsin-United-States-of-America/HVAC-Controls-Systems-Intern_WD30282521-1) | Glendale-Wisconsin-United States of Ame… | No skills listed | Oct 29, 2026 |
| Diversified Automation | Hardware Engineering Co-Op | [Apply](https://jobs.lever.co/diversified-automation/7a1f1890-bc5d-4e5e-a510-7fe7f85660d3) | Louisville, KY | No skills listed | Oct 29, 2026 |
| Diversified Automation | Controls Engineering Co-Op | [Apply](https://jobs.lever.co/diversified-automation/9506c50b-2859-4a78-a6b2-229b1366611d) | Louisville, KY | No skills listed | Oct 29, 2026 |
| AECOM | Electrical Engineering Intern | [Apply](https://jobs.smartrecruiters.com/AECOM2/744000158577089) | Roanoke, VA, United States (Hybrid) | No skills listed | Oct 29, 2026 |
| Base Power | Power Systems Engineering Intern | [Apply](https://jobs.ashbyhq.com/base-power/8397f115-7806-4911-a12b-6231852c3443) | Austin, TX | Python, Pandas | Oct 29, 2026 |
| FormFactor ✓ | Electrical Design Automation Intern – AI & EDA Automation | [Apply](https://formfactor.wd1.myworkdayjobs.com/FFI-Careers/job/Livermore-CA/Electrical-Design-Automation-Intern---AI---EDA-Automation_JR101304) | Livermore, CA | Python, Pandas, LLMs, Azure | Oct 28, 2026 |
| Micron Technology ✓ | Intern - Embedded Software Engineer | [Apply](https://micron.wd1.myworkdayjobs.com/External/job/Boise-ID---SIG-Building/Embedded-Software-Engineering-Intern_JR115959) | Boise, ID - SIG Building | Python, C++, Bash, Linux | Oct 28, 2026 |
| Austal USA | Electrical Engineering Intern | [Apply](https://austalusa.wd1.myworkdayjobs.com/austal/job/Mobile-AL/Electrical-Engineering-Intern_R0012154) | Mobile, AL | No skills listed | Oct 28, 2026 |
| Flextronics Internatio​nal | Intern - Electrical Engineer | [Apply](https://flextronics.wd1.myworkdayjobs.com/Careers/job/USA-IA-Des-Moines/Intern---Electrical-Engineer_WD232918-1) | USA, IA, Des Moines | No skills listed | Oct 28, 2026 |
| Avav | Electrical Engineering Intern - Space Technologies 🇺🇸 | [Apply](https://avav.wd1.myworkdayjobs.com/avav/job/Albuquerque-NM/Electrical-Engineering-Intern---Space-Technologies_9256) | Albuquerque, NM | No skills listed | Oct 27, 2026 |
| Marvell | Design Verification- Intern | [Apply](https://marvell.wd1.myworkdayjobs.com/MarvellCareers/job/IL---Petah-Tikva/Design-Verification--Intern_2604486) | IL - Petah Tikva | Python, C++, Verilog | Oct 27, 2026 |
| Mayo Clinic ✓ | Graduate Engineering Intern - Electronics | [Apply](https://fa-euwp-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/394029) | Rochester, MN, United States | No skills listed | Oct 27, 2026 |
| Avav | Electrical Engineering Intern | [Apply](https://avav.wd1.myworkdayjobs.com/avav/job/Sunrise-FL/Electrical-Engineering-Intern_9185) | Sunrise, FL | Python, C++, C#, Git | Oct 26, 2026 |
| Global Infrastruc​ture | Intern, Electrical Designer | [Apply](https://gi.wd1.myworkdayjobs.com/Global_Infrastructure/job/CA--ON--Toronto---380-Wellington-Street-West/Intern--Electrical-Designer_6599) | CA / ON / Toronto - 380 Wellington Stre… | No skills listed | Oct 26, 2026 |
| Parallel Systems | Software Engineering Intern (Embedded, Backend, Fullstack) | [Apply](https://boards.greenhouse.io/parallel/jobs/5275690007?gh_jid=5275690007) | Los Angeles, CA | Python, C++, Rust, TypeScript | Oct 26, 2026 |
| Cisco | Hardware Engineer II (Co-op) - United States | [Apply](https://cisco.wd5.myworkdayjobs.com/cisco_careers/job/San-Jose-California-US/Hardware-Engineer-II--Co-op----United-States_2025375) | San Jose, California, US | Python | Oct 26, 2026 |
| Lila Sciences | Co-op, Mechatronics Engineer | [Apply](https://job-boards.greenhouse.io/lilasciences/jobs/4465068009) | Cambridge, MA USA | No skills listed | Oct 26, 2026 |
| General Dynamics Mission Systems | Software Test Engineering Intern - Space and Embedded Crypto 🇺🇸 _(2 openings)_ | [Apply](https://careers-gdms.icims.com/jobs/75163/software-test-engineering-intern---space-and-embedded-crypto/job?in_iframe=1) [#2](https://careers-gdms.icims.com/jobs/75633/software-test-engineering-intern---space-and-embedded-crypto/job?in_iframe=1) | Scottsdale, AZ, US | Python | Oct 26, 2026 |
| Analog Devices ✓ | Embedded Systems Co-Op | [Apply](https://analogdevices.wd1.myworkdayjobs.com/External/job/US-MA-Boston/Embedded-Systems-Co-Op_R267689) | US, MA, Boston | Python, Rust, Bash, Linux | Oct 26, 2026 |
| Leidos ✓ | Electrical Design Engineering Intern 🇺🇸 | [Apply](https://leidos.wd5.myworkdayjobs.com/External/job/Huntsville-AL/Electrical-Design-Engineering-Intern_R-00195400) | Huntsville, AL | No skills listed | Oct 26, 2026 |
| First Quality | Controls Engineering Intern _(2 openings)_ | [Apply](https://firstquality.wd5.myworkdayjobs.com/firstquality/job/US-PA-McElhattan/Controls-Engineering-Intern_R12306) [#2](https://firstquality.wd5.myworkdayjobs.com/firstquality/job/US-PA-McElhattan/Controls-Engineering-Intern_R12307) | US PA McElhattan | No skills listed | Oct 26, 2026 |
| KION Group | Controls Engineer - Co-Op | [Apply](https://kiongroup.wd3.myworkdayjobs.com/kiongroup/job/Grand-Rapids-MI-United-States/Controls-Engineer---Co-Op_JR-0089161-1) | Grand Rapids, MI, United States | No skills listed | Oct 26, 2026 |
| American Electric Power ✓ | Electrical Designer Intern - New Albany, OH | [Apply](https://aep.wd1.myworkdayjobs.com/AEPCareerSite/job/New-Albany-OH/Electrical-Designer-Intern---New-Albany--OH_R19380-1) | New Albany, OH | No skills listed | Oct 22, 2026 |
| American Electric Power ✓ | Electrical Designer Intern - Roanoke, VA | [Apply](https://aep.wd1.myworkdayjobs.com/AEPCareerSite/job/Roanoke-VA/Electrical-Designer-Intern---Roanoke--VA_R19379) | Roanoke, VA | No skills listed | Oct 22, 2026 |
| American Electric Power ✓ | Electrical Designer Intern - Tulsa, OK | [Apply](https://aep.wd1.myworkdayjobs.com/AEPCareerSite/job/Tulsa-OK/Electrical-Designer-Intern---Tulsa--OK_R19378) | Tulsa, OK | No skills listed | Oct 22, 2026 |
| BorgWarner | Advanced Inverter Electrical Engineering Intern 🛂 | [Apply](https://borgwarner.wd5.myworkdayjobs.com/BorgWarner_Careers/job/Kokomo-Technical-Center---Indiana---USA/Advanced-Inverter-Electrical-Engineering-Intern_R2026-4197) | Kokomo Technical Center - Indiana - USA | No skills listed | Oct 21, 2026 |
| Daikin Applied | Power Electronics Intern | [Apply](https://daikinapplied.wd1.myworkdayjobs.com/Daikin-Careers/job/Staunton-VA-24402/Power-Electronics-Intern_R004448) | Staunton, VA 24402 | No skills listed | Oct 21, 2026 |
| Microchip Technology ✓ | Intern - Engineering (ASIC Verificati​on) | [Apply](https://microchiphr.wd5.myworkdayjobs.com/external/job/CA---San-Jose---3870-N-First-St/Intern---Engineering--ASIC-Verification-_R3851-26) | CA - San Jose - 3870 N. First St | Python, Bash, Verilog | Oct 21, 2026 |
| Matic | Electrical Design Engineer Intern | [Apply](https://jobs.ashbyhq.com/MaticRobots/2f93fe19-0d71-4972-98da-8baf9d4ab05e) | Menlo Park, CA | No skills listed | Oct 20, 2026 |
| Avav | Electrical Engineering Intern | [Apply](https://avav.wd1.myworkdayjobs.com/avav/job/San-Diego-CA/Electrical-Engineering-Intern_9143) | San Diego, CA | Python, C++, C#, MATLAB | Oct 20, 2026 |
| Heidelberg Materials | Electrical Engineer Intern | [Apply](https://heidelbergmaterials.wd3.myworkdayjobs.com/global_hm_career_site/job/Lexington-SC/Electrical-Engineer-Intern_JR10019490) | Lexington, SC | No skills listed | Oct 20, 2026 |
| Mii | Electrical Engineering Intern | [Apply](https://mii.wd5.myworkdayjobs.com/universityrecruiting/job/Earth-City-Missouri-USA/Electrical-Engineering-Intern_R06665-5) | Earth City, Missouri, USA | No skills listed | Oct 20, 2026 |
| Rockwell Automation ✓ | Intern - Embedded Controls Engineering 🛂 | [Apply](https://rockwellautomation.wd1.myworkdayjobs.com/External-Rockwell-Automation-Early-Careers/job/Orlando-Florida-United-States/Intern---Embedded-Controls-Engineering_R26-5043-1) | Orlando, Florida, United States | No skills listed | Oct 20, 2026 |
| Applied Materials ✓ | Electrical Engineer Intern | [Apply](https://amat.wd1.myworkdayjobs.com/External/job/TempeAZ/Electrical-Engineer-Intern_R2631303) | Tempe,AZ | No skills listed | Oct 19, 2026 |
| Micron Technology ✓ | Intern - ASIC Digital Design | [Apply](https://micron.wd1.myworkdayjobs.com/External/job/Minneapolis-MN/Intern---ASIC-Digital-Design_JR112163) | Minneapolis, MN | Python, LLMs, Linux | Oct 19, 2026 |
| Moog | Intern, Electrical Engineering | [Apply](https://moog.wd5.myworkdayjobs.com/moog_external_career_site/job/Buffalo-NY/Intern--Electrical-Engineering_R-26-20268) | Buffalo, NY | No skills listed | Oct 19, 2026 |
| Sierra Nevada Corporation | RF Engineer Intern 🇺🇸 | [Apply](https://snc.wd1.myworkdayjobs.com/snc_external_career_site/job/Lone-Tree-CO/RF-Engineer-Intern_R0031110) | Lone Tree, CO | MATLAB | Oct 19, 2026 |
| Bosch ✓ | AI Research Intern: Wireless Foundation Models | [Apply](https://jobs.smartrecruiters.com/BoschGroup/744000156323136) | Pittsburgh, PA, United States | Python, PyTorch | Oct 19, 2026 |
| Draper | Integrated Circuits Intern 🇺🇸 _(2 openings)_ | [Apply](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Integrated-Circuits-Intern_JR003036) [#2](https://draper.wd5.myworkdayjobs.com/Draper_Careers/job/Cambridge-MA/Integrated-Circuits-Intern_JR002783) | Cambridge, MA | Python, MATLAB, Verilog | Oct 15, 2026 |
| Astera Labs ✓ | AMS Digital Design Engineer Intern | [Apply](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4739915005) | San Jose, CA | Python, Verilog | Oct 13, 2026 |
| Astera Labs ✓ | AMS Design Verification Engineer Intern | [Apply](https://job-boards.greenhouse.io/asteraearlycareer2027/jobs/4743360005) | San Jose, CA | Python, C++, Verilog | Oct 13, 2026 |
| Fortive | Electrical Engineering Intern | [Apply](https://ejta.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/10876) | Irvine, CA, United States | No skills listed | Oct 13, 2026 |

<details>
<summary><strong>Recently closed</strong> — 30 roles that left the list in the last 14 days</summary>

_Why each one left is in the last column, because the two reasons carry different evidence. **Gone from feed** = two consecutive complete reads of the employer's board no longer returned it (strong, but not the employer telling us directly). **Out of scope** = still posted, but it no longer passes our filters — our call, not theirs. **Not recorded** = closed before we started tracking the reason._

| Company | Role | Cycle | Closed | Why |
|---|---|---|---|---|
| Rendezvous Robotics | Avionics Engineering Intern (Summer 2027) | Summer 2027 | 2026-11-24 | gone from feed |
| Renesas Electronics | PMIC Analog Intern | Summer 2027 | 2026-11-24 | gone from feed |
| Lucid Motors | Intern, Embedded Software – BSP/Platform (ADAS/Autonomous Driving), Summer 2027 | Summer 2027 | 2026-11-24 | gone from feed |
| General Dynamics Mission Systems | Electrical Engineering Intern (Summer 2027) | Summer 2027 | 2026-11-23 | gone from feed |
| RESPEC | Student Engineering Intern (Mechanical or Electrical) | Summer 2027 | 2026-11-23 | gone from feed |
| Marvell | Electrical Validation Intern, BS - Summer 2027 | Summer 2027 | 2026-11-23 | gone from feed |
| Parallel Systems | Hardware Engineering Intern (Mechanical & Electrical) | Summer 2027 | 2026-11-23 | gone from feed |
| General Matter | Summer 2027 Internship - Electrical I&C Engineering | Summer 2027 | 2026-11-23 | gone from feed |
| Renesas Electronics | Firmware Engineering Intern | Summer 2027 | 2026-11-23 | gone from feed |
| SharkNinja | Summer 2027: Control Systems & Algorithms Intern (May to August) | Summer 2027 | 2026-11-23 | gone from feed |
| KLA | Mechatronics Summer Intern | Summer 2027 | 2026-11-21 | gone from feed |
| Renesas Electronics | Digital Design Engineer Intern | Summer 2027 | 2026-11-20 | gone from feed |
| Lightmatter | Laser Firmware Intern - Summer 2027 | Summer 2027 | 2026-11-20 | gone from feed |
| Lightmatter | Hardware Test Engineering, Intern (Summer 2027) | Summer 2027 | 2026-11-19 | gone from feed |
| Northwood Space | Electrical Engineering Intern (2027 Summer Internship) | Summer 2027 | 2026-11-19 | gone from feed |
| General Matter | Summer 2027 Internship - Embedded Software Engineering | Summer 2027 | 2026-11-17 | gone from feed |
| Lightmatter | Silicon, Hardware, & Photonics Engineering Intern – Summer 2027 | Summer 2027 | 2026-11-17 | gone from feed |
| Pacific Fusion | Summer 2027 Internship - Electrical Engineering | Summer 2027 | 2026-11-17 | gone from feed |
| General Dynamics Mission Systems | Electrical Intern Engineer | Summer 2027 | 2026-11-17 | gone from feed |
| American Electric Power | Electrical Engineering Intern- Summer 2027 | Summer 2027 | 2026-11-16 | gone from feed |
| General Dynamics Mission Systems | Electrical Engineer Co-Op (May - December 2027) | Summer 2027 | 2026-11-13 | gone from feed |
| Shield AI | Summer 2027 - Electrical Engineering Intern | Summer 2027 | 2026-11-13 | gone from feed |
| Shield AI | June 2027 Co-0p - Electrical Engineering Intern | Summer 2027 | 2026-11-13 | gone from feed |
| Shield AI | 2027 June Co-op - Hardware Test - #6426 | Summer 2027 | 2026-11-13 | gone from feed |
| The Toro Company | Electrical Engineering Intern - The Toro Company | Summer 2027 | 2026-11-12 | gone from feed |
| The Toro Company | Embedded Software Engineering Intern - The Toro Company | Summer 2027 | 2026-11-12 | gone from feed |
| The Toro Company | Embedded Software Engineering Intern - The Toro Company | Summer 2027 | 2026-11-12 | gone from feed |
| Wavetronix | Electrical/Computer Engineering Internship Summer 2027 | Summer 2027 | 2026-11-12 | gone from feed |
| K2 Space | Electrical Engineering Intern – Summer 2027 | Summer 2027 | 2026-11-12 | gone from feed |
| K2 Space | Avionics Systems/Test Engineering Intern – Summer 2027 | Summer 2027 | 2026-11-12 | gone from feed |

</details>

---

## Hiring timeline

Internships posted per week, from each role's real published date - redrawn automatically on every run. When this line takes off, recruiting season is open:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/trends-dark.svg">
  <img alt="Internships posted per week, drawn from real published dates" src="docs/trends-light.svg">
</picture>

## How it stays current

A small Python engine reads public company hiring feeds directly, keeps the roles that match the scope above, de-duplicates across sources, records each role's published date once (so it never shifts), and regenerates this page through GitHub Actions. It polls every company concurrently (async) with retry/backoff and per-host rate limits. The full source is in this repo.

_Engine (last run): 3,007 of 5,108 registered boards returned successfully across 14 ATS platforms (62% of boards attempted, 58% of the full registry) · completed in 1179.1s · 90 board(s) returned a capped result set, so their roles were not eligible to be closed this run · employer or source-derived date on 99% of open roles · Workday coverage degraded, with some previously listed roles unverified._

## How this list is built

[METHODOLOGY.md](METHODOLOGY.md) documents exactly what every label claims — what separates a stated cycle from an inferred one, what the ✓ H-1B badge does and doesn't mean, how a role gets closed, and which limitations are known. Anything on this page that doesn't match the code is a bug worth reporting.

## Contributing

Adding a company takes one line, see [CONTRIBUTING.md](CONTRIBUTING.md), or just [open a request](../../issues/new?template=add-company.yml) with the board URL. **Spotted something wrong?** [Report the exact field](../../issues/new?template=wrong-data.yml) — wrong country, wrong cycle, closed role, bad sponsorship flag. Those reports usually fix a rule, which fixes every other role too.

Also here: [PRIVACY.md](PRIVACY.md) (what the email list stores — an address and nothing else) · [SECURITY.md](SECURITY.md) · [ARCHITECTURE.md](ARCHITECTURE.md) · [MIT licensed](LICENSE).

Built by one student with AI assistance, in the open. The part that matters isn't who typed it — it's that the rules, the tests, and every run's output are all public and checkable.

## Note on dates

The **Posted** column shows when a role was published, with the newest at the top. I pull the posting date straight from each job portal, but a lot of them don't expose one publicly, so those rows show a dash (—) for now instead of a guessed date. The ones that do publish a date are dated. Know the real date for a dashed role? Open a PR and I'll merge it.

Roles can close at any time, so always confirm on the company's own site before applying.
