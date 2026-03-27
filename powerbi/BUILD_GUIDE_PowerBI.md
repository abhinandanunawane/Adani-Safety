# Power BI Build Guide — Adani Group Safety (MIS 5 Pages + BSC Page 6)

This guide matches **`README_FINAL_LAYOUT.md`** and the Excel workbook **MIS and BSC Dashboard KPI List Final.xlsx**.

## 0) Files to import

| File | Role |
|------|------|
| `data/mis_kpi_by_page.csv` | **Master map**: each MIS KPI → page (1–5) + theme |
| `data/bsc_kpi_list.csv` | BSC KPI names (55) for scorecard filters |
| `data/bsc_scorecard_facts.csv` | Sample facts for Page 6 (replace with production) |
| `data/adani_security_facts.csv` | Optional legacy demo fact table — **replace** with your SAFEX / warehouse extracts |
| `powerbi/adani_security_theme.json` | Theme (logo gradient palette) |
| `powerbi/DAX_Measures_AdaniSecurity.txt` | Rename measures from “Security” to “Safety” if you prefer |
| `powerbi/visual_blueprint_6pages_1024x720.csv` | **Use this** for 6-page layout (supersedes `visual_blueprint_1024x720.csv`) |

**Note:** If **Adani Safety Dashboards Confidential** PBIX exists internally, use it as the **starting report** and add pages/KPIs from this pack instead of rebuilding from scratch.

## 1) Import and model

1. **Get Data → Text/CSV** — import `mis_kpi_by_page.csv`, `bsc_kpi_list.csv`, `bsc_scorecard_facts.csv`, and your operational fact table(s).
2. Create a **KPI dimension** from `mis_kpi_by_page` (unique `KPIName`) and relate to facts on `KPIName`.
3. Add a **Date** table (mark as date table) and relate to fact `Date`.

## 2) Theme

**View → Themes → Browse for themes** → `adani_security_theme.json`

## 3) Page size

Every page: **Custom** **1024 × 720**.

## 4) Create six pages (exact names)

1. `Page 1 - MIS Incident & Leading Indicators`
2. `Page 2 - MIS CMP Deltas & Vehicle`
3. `Page 3 - MIS Training & Man-Hours`
4. `Page 4 - MIS Audit Hazard & Observations`
5. `Page 5 - MIS PTW Standards & Governance`
6. `Page 6 - BSC Executive Scorecard`

## 5) Slicers (sync across pages where relevant)

- `Date`, `LastUpdate` (or `AsOfDate`)
- `Quarter` (for BSC and quarterly bands)
- `BusinessUnit`, `Site`
- Optional: `Severity`, `Status` for incident facts
- Page 6: `RiskGroup` (Group A / Group B), `BandLabel` if applicable

## 6) MIS pages (1–5)

- **15** **Card (new)** visuals per page (or fewer cards + **Matrix** for dense KPIs).
- Each card: **visual-level filter** `KPIName` = one KPI from `mis_kpi_by_page` for that `PageNo`.
- Charts: follow **`visual_blueprint_6pages_1024x720.csv`** (line, donut, column, funnel, map, gauge, heatmap as listed).
- **Tooltips** on all charts.

## 7) Page 6 — BSC (no flat “table only”)

**Section A — Hero**

- Three **Card** visuals: *Key elements* (count of parameters), *Performance index* (weighted), *Highest score achieved* (MAX).

**Section B — Bands by group (quarterly)**

- **100% stacked column** (or **Ribbon**)  
  - Axis: `Quarter`  
  - Legend: `BandLabel` (Red / Amber / Green)  
  - Small multiples or **RiskGroup** on separate charts: **Group A — High risk** vs **Group B — Moderate risk**.

**Section C — Unit comparison (creative)**

- Prefer **Scatter chart**: X = `RankInGroup`, Y = `WeightedScore`, Size = `PercentileInGroup`, Details = `UnitName`.  
- Or **horizontal bar** with **data labels** on `WeightedScore` and **tooltips** for Raw / Percentile / Weight / Overall rank.

## 8) Publish

Save PBIX → **Publish** to Power BI Service → share with your team.

## DAX naming

Rename `adani_security_facts` to `FactSafety` in production and update measures accordingly.
