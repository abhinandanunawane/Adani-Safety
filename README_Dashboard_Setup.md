# Adani Group Safety — Dashboard setup

## Final layout (MIS + BSC, 6 pages)

All KPI mapping, page names, Power BI blueprint, and branding notes are documented here:

**→ [README_FINAL_LAYOUT.md](README_FINAL_LAYOUT.md)**

## Quick run — HTML prototype

1. Open **`prototype/index.html`** in your browser.
2. Use navigation **P1–P5** for MIS themes (75 KPIs across five pages).
3. Use **P6** for the **BSC Executive** view (hero metrics, quarterly bands by risk group, lollipop-style unit comparison — not a flat table).

Supporting data: **`prototype/mis-pages-data.js`** (generated from **`data/mis_kpi_by_page.csv`**).

## Power BI

Follow **`powerbi/BUILD_GUIDE_PowerBI.md`** and **`powerbi/visual_blueprint_6pages_1024x720.csv`**.

## Excel source

Place **`MIS and BSC Dashboard KPI List Final.xlsx`** in this folder — KPI lists were extracted from it for `data/mis_kpi_by_page.csv` and `data/bsc_kpi_list.csv`.

Align with your internal **Adani Safety Dashboards Confidential** PBIX when connecting real data.
