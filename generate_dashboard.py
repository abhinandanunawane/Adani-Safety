import os, csv, json
from pathlib import Path

root = Path(r"c:/Users/abhinandan.unawane/Downloads/Demo Figma Prototype")
(root / "figma_import").mkdir(parents=True, exist_ok=True)
(root / "powerbi").mkdir(parents=True, exist_ok=True)
(root / "data").mkdir(parents=True, exist_ok=True)

pages = {
    "Page 1 - SOC Overview": [
        "Total Security Incidents",
        "Critical Incidents",
        "Mean Time to Detect (MTTD)",
        "Mean Time to Respond (MTTR)",
        "SLA Compliance Rate",
        "Open High-Risk Alerts",
        "False Positive Rate",
        "Incident Recurrence Rate",
        "SOC Analyst Utilization",
        "Escalation Rate",
    ],
    "Page 2 - Threat Detection": [
        "Threats Detected per Day",
        "Blocked Malware Attempts",
        "Ransomware Detection Count",
        "Phishing Detection Count",
        "EDR Coverage Rate",
        "XDR Alert Volume",
        "IOC Match Rate",
        "Suspicious Login Attempts",
        "Lateral Movement Alerts",
        "Anomalous Network Sessions",
    ],
    "Page 3 - Vulnerability & Patch": [
        "Critical Vulnerabilities Open",
        "High Vulnerabilities Open",
        "Vulnerability Remediation Rate",
        "Patch Compliance Rate",
        "Average Patch Age (Days)",
        "Internet-Facing Asset Risk Score",
        "Unpatched Endpoint Count",
        "CVSS Weighted Exposure",
        "Scan Coverage Rate",
        "Configuration Drift Incidents",
    ],
    "Page 4 - Identity & Access": [
        "MFA Adoption Rate",
        "Privileged Account Count",
        "Dormant Account Count",
        "Failed Login Rate",
        "Password Policy Compliance",
        "Access Review Completion Rate",
        "Unauthorized Access Attempts",
        "IAM Provisioning SLA",
        "PAM Session Violations",
        "Third-Party Access Risk Score",
    ],
    "Page 5 - Compliance & Resilience": [
        "Compliance Controls Pass Rate",
        "Audit Findings Open",
        "Data Loss Prevention (DLP) Incidents",
        "Backup Success Rate",
        "Recovery Time Objective (RTO) Achievement",
        "Disaster Recovery Drill Score",
        "Business Continuity Readiness",
        "Policy Acknowledgement Rate",
        "Security Awareness Training Completion",
        "Third-Party Compliance Score",
    ],
}

md = [
    "# Adani Group Security Dashboard - KPI Blueprint",
    "",
    "- Total KPIs: 50",
    "- Pages: 5",
    "- KPIs per page: 10",
    "- Recommended canvas: 1024 x 720 px",
    "",
    "## Page Navigation",
]
for i, title in enumerate(pages.keys(), start=1):
    md.append(f"- {i}. {title}")
for page, kpis in pages.items():
    md += ["", f"## {page}"]
    for idx, k in enumerate(kpis, start=1):
        md.append(f"{idx}. {k}")
(root / "powerbi" / "adani_security_kpi_catalog.md").write_text("\n".join(md), encoding="utf-8")

with (root / "powerbi" / "page_navigation.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["PageNo", "PageName", "TabLabel", "SortOrder"])
    for i, p in enumerate(pages.keys(), start=1):
        w.writerow([i, p, f"P{i}", i])

headers = ["Date","BusinessUnit","Site","Page","KPIName","KPIValue","KPIUnit","Target","ThresholdGreen","ThresholdAmber","ThresholdRed","Status","Trend","Owner"]
rows = []
for page, kpis in pages.items():
    for k in kpis:
        rows.append(["2026-03-01","Adani Group","Enterprise",page,k,0,"count",100,90,75,60,"Red","Flat","Security Operations"])
with (root / "data" / "adani_security_kpi_template.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)

theme = {
  "name": "Adani Security Theme",
  "dataColors": ["#0070AD", "#00A3E0", "#00B388", "#FFB81C", "#D92D20", "#3B3F46", "#A7B1C2", "#7A52C7"],
  "background": "#F5F7FA",
  "foreground": "#1F2937",
  "tableAccent": "#0070AD",
  "visualStyles": {
    "*": {
      "*": {
        "title": [{"show": True, "fontSize": 12, "fontFamily": "Segoe UI", "color": {"solid": {"color": "#1F2937"}}}],
        "background": [{"show": True, "color": {"solid": {"color": "#FFFFFF"}}, "transparency": 0}],
        "border": [{"show": True, "color": {"solid": {"color": "#D1D5DB"}}, "radius": 6}],
        "labels": [{"color": {"solid": {"color": "#1F2937"}}, "fontSize": 10}]
      }
    },
    "card": {
      "*": {
        "categoryLabels": [{"show": True, "color": {"solid": {"color": "#6B7280"}}, "fontSize": 9}],
        "calloutValue": [{"color": {"solid": {"color": "#111827"}}, "fontSize": 20}]
      }
    }
  }
}
(root / "powerbi" / "adani_security_theme.json").write_text(json.dumps(theme, indent=2), encoding="utf-8")

layout = {
    "canvas": {"width": 1024, "height": 720},
    "zones": {
        "header": {"x": 16, "y": 12, "w": 992, "h": 48},
        "nav": {"x": 16, "y": 68, "w": 992, "h": 32},
        "filters": {"x": 16, "y": 108, "w": 220, "h": 596},
        "kpi_grid": {"x": 248, "y": 108, "w": 760, "h": 236},
        "chart_a": {"x": 248, "y": 356, "w": 372, "h": 170},
        "chart_b": {"x": 636, "y": 356, "w": 372, "h": 170},
        "table": {"x": 248, "y": 536, "w": 760, "h": 168}
    }
}
(root / "powerbi" / "layout_spec.json").write_text(json.dumps(layout, indent=2), encoding="utf-8")

def make_svg(title, kpis, pindex):
    W, H = 1024, 720
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    lines.append('<rect x="0" y="0" width="1024" height="720" fill="#F5F7FA"/>')
    lines.append('<rect x="16" y="12" width="992" height="48" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
    lines.append(f'<text x="28" y="42" font-family="Segoe UI" font-size="18" font-weight="700" fill="#111827">Adani Group Security Dashboard - {title}</text>')
    lines.append('<rect x="16" y="68" width="992" height="32" rx="6" fill="#FFFFFF" stroke="#D1D5DB"/>')
    for i, name in enumerate(pages.keys(), start=1):
        x = 24 + (i-1)*194
        fill = "#0070AD" if i == pindex else "#E5E7EB"
        txt = "#FFFFFF" if i == pindex else "#374151"
        lines.append(f'<rect x="{x}" y="73" width="184" height="22" rx="4" fill="{fill}"/>')
        label = f'P{i}: {name.split(" - ")[1]}'
        lines.append(f'<text x="{x+8}" y="88" font-family="Segoe UI" font-size="10" fill="{txt}">{label}</text>')
    lines.append('<rect x="16" y="108" width="220" height="596" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
    lines.append('<text x="30" y="132" font-family="Segoe UI" font-size="13" font-weight="700" fill="#111827">Global Filters</text>')
    filters = ["Date", "Business Unit", "Site", "Severity", "Asset Type", "Source System"]
    y=150
    for flt in filters:
        lines.append(f'<text x="30" y="{y}" font-family="Segoe UI" font-size="10" fill="#4B5563">{flt}</text>')
        lines.append(f'<rect x="30" y="{y+6}" width="190" height="22" rx="4" fill="#F9FAFB" stroke="#D1D5DB"/>')
        y+=44
    x0,y0 = 248,108
    cw,ch,gx,gy = 146,108,8,8
    for idx,k in enumerate(kpis):
        r,c = divmod(idx,5)
        x = x0 + c*(cw+gx)
        y = y0 + r*(ch+gy)
        lines.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
        lines.append(f'<text x="{x+8}" y="{y+20}" font-family="Segoe UI" font-size="9" fill="#6B7280">KPI {idx+1}</text>')
        safe = k.replace('&','&amp;')
        lines.append(f'<text x="{x+8}" y="{y+38}" font-family="Segoe UI" font-size="10" font-weight="700" fill="#111827">{safe}</text>')
        lines.append(f'<text x="{x+8}" y="{y+72}" font-family="Segoe UI" font-size="22" font-weight="700" fill="#111827">0</text>')
        lines.append(f'<text x="{x+90}" y="{y+74}" font-family="Segoe UI" font-size="10" fill="#D92D20">vs target</text>')
    lines.append('<rect x="248" y="356" width="372" height="170" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
    lines.append('<text x="262" y="378" font-family="Segoe UI" font-size="12" font-weight="700" fill="#111827">Trend Chart</text>')
    lines.append('<rect x="636" y="356" width="372" height="170" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
    lines.append('<text x="650" y="378" font-family="Segoe UI" font-size="12" font-weight="700" fill="#111827">Distribution Chart</text>')
    lines.append('<polyline points="270,500 310,470 350,480 390,440 430,456 470,420 510,430 550,400 590,410" fill="none" stroke="#0070AD" stroke-width="3"/>')
    for bx in [680,730,780,830,880,930]:
        h = (bx//10)%70 + 40
        y = 510-h
        lines.append(f'<rect x="{bx}" y="{y}" width="24" height="{h}" fill="#00A3E0" opacity="0.85"/>')
    lines.append('<rect x="248" y="536" width="760" height="168" rx="8" fill="#FFFFFF" stroke="#D1D5DB"/>')
    lines.append('<text x="262" y="558" font-family="Segoe UI" font-size="12" font-weight="700" fill="#111827">Detailed KPI Table</text>')
    lines.append('<rect x="262" y="566" width="732" height="22" fill="#F3F4F6"/>')
    cols = ["KPI", "Current", "Target", "Status", "Owner", "Last Updated"]
    cx = [268,540,620,700,780,900]
    for c,xx in zip(cols,cx):
        lines.append(f'<text x="{xx}" y="581" font-family="Segoe UI" font-size="9" font-weight="700" fill="#374151">{c}</text>')
    yy = 600
    for r in range(4):
        lines.append(f'<line x1="262" y1="{yy}" x2="994" y2="{yy}" stroke="#E5E7EB"/>')
        yy += 24
    lines.append('</svg>')
    return "\n".join(lines)

for i,(title,kpis) in enumerate(pages.items(),start=1):
    svg = make_svg(title, kpis, i)
    (root / "figma_import" / f"adani_security_page_{i}.svg").write_text(svg, encoding="utf-8")

guide = """# Build Guide: Adani Group Security Dashboard (Power BI + Figma)

## Deliverables in this folder
- `figma_import/adani_security_page_1.svg` ... `adani_security_page_5.svg` (wireframes, 1024x720)
- `powerbi/adani_security_kpi_catalog.md` (all 50 KPIs, grouped by page)
- `powerbi/page_navigation.csv` (page tabs/navigation metadata)
- `powerbi/adani_security_theme.json` (Power BI theme)
- `powerbi/layout_spec.json` (visual placement coordinates)
- `data/adani_security_kpi_template.csv` (fact table template)

## Figma import steps
1. Open Figma file.
2. Drag and drop all 5 SVG files from `figma_import`.
3. Convert each imported SVG into a frame if needed.
4. Add your brand assets/icons, then publish as design system pages.

## Power BI build steps
1. In Power BI Desktop, set page size to **Custom**: Width `1024`, Height `720` for each page.
2. Import `data/adani_security_kpi_template.csv`.
3. Import theme from `powerbi/adani_security_theme.json`.
4. Create 5 report pages named exactly as in KPI catalog.
5. Add page navigation buttons using `powerbi/page_navigation.csv` values.
6. Add visuals per page:
   - 10 KPI Cards (top grid)
   - 2 Charts (line + bar/pie)
   - 1 Detail table
   - Left-side slicers/filters (Date, BU, Site, Severity, Asset Type, Source)

## Suggested core DAX measures
- `KPI Current = SUM('adani_security_kpi_template'[KPIValue])`
- `KPI Target = SUM('adani_security_kpi_template'[Target])`
- `KPI Variance = [KPI Current] - [KPI Target]`
- `KPI Variance % = DIVIDE([KPI Variance], [KPI Target])`

## Notes
- Replace template values with real SOC/SIEM/Vuln/IAM/Compliance feeds.
- Keep slicers synced across pages for consistent drill experience.
"""
(root / "README_Dashboard_Setup.md").write_text(guide, encoding="utf-8")

print("Created dashboard package successfully.")
