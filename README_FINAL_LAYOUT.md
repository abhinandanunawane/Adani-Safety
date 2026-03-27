# Adani Group Safety — Final Dashboard Layout (6 Pages)

## Source of truth

- **MIS KPIs (75 operational KPIs):** Parsed from `MIS and BSC Dashboard KPI List Final.xlsx` sheet 1 (MIS block). Excluded standalone section labels **CMP** and **Audit Assurance** from the KPI grid (they are headers, not measures).
- **BSC KPI list (55 KPIs):** `data/bsc_kpi_list.csv` from Excel sheet 2 (Balance Scorecard list).
- **BSC scorecard facts (sample):** `data/bsc_scorecard_facts.csv` — use for Page 6 visuals (bands, ranks, weightings).
- **Reference:** Align filters and layout with your internal **Adani Safety Dashboards Confidential** pack; that file was not present in this workspace — copy visuals/field names from your published PBIX when connecting.

## Six pages

| # | Page | Content |
|---|------|---------|
| 1 | **MIS Incident & Leading Indicators** | 15 KPIs — TRIR, PSI, PSTIR, PSNM, fire, leak, injury, property, rates, repeat, etc. |
| 2 | **MIS CMP Deltas & Vehicle** | 15 KPIs — deltas, CMP compliance, vehicle, investigation, leadership counts |
| 3 | **MIS Training & Man-Hours** | 15 KPIs — fatalities/near miss, man-hours, training, SI/SRFA, hazard spotting |
| 4 | **MIS Audit Hazard & Observations** | 15 KPIs — audits, hazard %, SI/SRFA closures, observation, investigations, FPSA |
| 5 | **MIS PTW Standards & Governance** | 15 KPIs — PTW, standards, actions, councils, taskforce, SAFEX, FRC/LFI, budget |
| 6 | **BSC Executive Scorecard** | **Not** a flat table: three zones — (A) hero KPIs, (B) quarterly **bands** by Group A / Group B, (C) **lollipop / rank** view for units × raw score × percentile × weight × weighted score × overall rank |

## Files

| File | Purpose |
|------|---------|
| `data/mis_kpi_by_page.csv` | Maps each MIS KPI to **PageNo** + **Theme** for Power BI filters and card filters |
| `data/bsc_kpi_list.csv` | Full BSC KPI list (55) for filters and scorecard |
| `data/bsc_scorecard_facts.csv` | Sample rows for BSC page (replace with production data) |
| `prototype/index.html` + `prototype/mis-pages-data.js` | Interactive **720px** prototype — 5 MIS layouts + 1 BSC creative layout |
| `powerbi/visual_blueprint_6pages_1024x720.csv` | Placement + visual types for Power BI Desktop |
| `powerbi/adani_security_theme.json` | Theme (rename to `adani_safety_theme.json` in repo if you prefer) |
| `powerbi/BUILD_GUIDE_PowerBI.md` | Build steps — update page names to **MIS + BSC** |

## Branding

- Logo: `prototype/assets/adani-logo.svg` (Wikimedia Commons Adani logo 2012 — replace with **official** media kit asset if required).
- Gradient palette: cyan → blue → purple → magenta (aligned with logo).

## Power BI notes (Page 6)

- **Section A:** Three **Card** or **Multi-row card** visuals for *Key elements*, *Performance index*, *Highest score achieved*.
- **Section B:** **100% stacked column** or **Ribbon** by **Quarter** and **RiskGroup** (Group A vs Group B) with **Band** (Red/Amber/Green) in legend.
- **Section C:** Prefer **Scatter chart** (Y = WeightedScore, X = RankInGroup, Size = Percentile) or **Horizontal bar / lollipop** (custom SVG not needed — use **Data bars** on a matrix or **Deneb** if licensed). Avoid a wide table; use **tooltip** drill to detail.

## Run prototype

Open `prototype/index.html` in a browser. Use **P** nav to switch pages; **P6** shows the BSC executive layout.
