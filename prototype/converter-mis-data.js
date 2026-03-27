/**
 * MIS data aligned to Excel workbook structure:
 * - Sheet "MIS dashboard" → master KPI list (Sr., KPI, Data source, Formulas)
 * - Sheet "MIS RAW data" / summary perspectives → summary rows
 * Place source file as: data/Converter_MIStoDB_Feb26.xlsx — Power BI should import the CSV exports in /data/.
 */
(function () {
  function h(s) {
    var x = 2166136261;
    for (var i = 0; i < s.length; i++) {
      x ^= s.charCodeAt(i);
      x = Math.imul(x, 16777619);
    }
    return x >>> 0;
  }
  var SRC = [
    'SAFEX I&M Module',
    'SAFEX Audit Module',
    'SAFEX Training Tracker Module',
    'SAFEX Hazard spotting Module',
    'SAFEX PTW Module',
    'SAFEX ATS Module',
    'SAFEX GOVERNANCE Module',
    'SAFEX SI/SRFA Module',
    'Sharepoint',
    'Kronos',
    'Manual / CMP Module'
  ];
  var FML = [
    'Direct value',
    'Direct Value',
    'Manual calculation',
    '(Closed/Total)*100',
    '(Total/raised)*100',
    'SAFEX formula'
  ];
  var BU = ['Power', 'Ports', 'AESL', 'Cements', 'Copper', 'Green PVC', 'Mining', 'Gas', 'Airports', 'MSPVL', 'Defense & Aerospace', 'ANIL-Wind', 'ANIL-BESS', 'Green Energy', 'Realty', 'RMRW', 'AEML', 'Data Center', 'Logistics', 'NMDPL', 'Smart Meters', 'Hydro PSP', 'Agri fresh', 'Dredging'];
  var SITE = ['Mumbai HQ', 'Mundra SEZ', 'Ahmedabad', 'Raipur', 'Hazira', 'Kandla'];
  var UPD = ['2026-03-25', '2026-03-24', '2026-03-23', '2026-03-22', '2026-03-21'];
  var master = [];
  var sr = 1;
  window.MIS_PAGE_DEF.forEach(function (p, pi) {
    p.kpis.forEach(function (k) {
      var base = 55 + (h(pi + '|' + k + '|v') % 40);
      var jitter = (h(pi + k + sr + 'j') % 7) - 3;
      var value = Math.min(100, Math.max(12, base + jitter));
      var delta = (h(pi + k + 'd') % 25) - 8;
      var status = value >= 90 ? 'Resolved' : value < 65 ? 'Open' : 'In Progress';
      master.push({
        sr: sr,
        kpi: k,
        dataSource: SRC[h(k + sr) % SRC.length],
        formulaNote: FML[h(k + pi) % FML.length],
        value: value,
        target: 100,
        delta: delta,
        trend: delta >= 0 ? 'up' : 'down',
        page: pi,
        lastUpdate: UPD[sr % UPD.length],
        owner: sr % 2 ? 'HSE Analytics' : 'BU Safety',
        bu: BU[h(k + sr) % BU.length],
        site: SITE[h(k) % SITE.length],
        severity: ['Critical', 'High', 'Medium', 'Low'][h(k + pi) % 4],
        status: status
      });
      sr++;
    });
  });
  window.CONVERTER_MIS = {
    source: 'Structure from MIS dashboard Excel (KPI master + data source + formula columns). Import data/Converter_MIS_master.csv and Converter_MIS_summary.csv into Power BI.',
    excelNote: 'If you add Converter_MIStoDB_Feb26.xlsx under /data/, refresh CSVs from Power Query.',
    summary: [
      { perspective: 'Financial', pillar: 'Incident & loss exposure', score: 81, kpiCount: 15 },
      { perspective: 'Customer', pillar: 'Stakeholder / assurance', score: 79, kpiCount: 15 },
      { perspective: 'Internal Business Process', pillar: 'Audit & hazards', score: 84, kpiCount: 15 },
      { perspective: 'Learning & Growth', pillar: 'Training & capability', score: 77, kpiCount: 15 },
      { perspective: 'Governance', pillar: 'PTW & standards', score: 83, kpiCount: 15 }
    ],
    master: master
  };
})();
