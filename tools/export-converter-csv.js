// Run: cscript //nologo tools\export-converter-csv.js (from project root)
// Requires: prototype\mis-pages-data.js and prototype\converter-mis-data.js (ES3-compatible output)

var fso = new ActiveXObject('Scripting.FileSystemObject');
var base = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName)) + '\\';
var proto = base + 'prototype\\';

function readUtf8(p) {
  var stream = new ActiveXObject('ADODB.Stream');
  stream.Type = 2;
  stream.Charset = 'utf-8';
  stream.Open();
  stream.LoadFromFile(p);
  var t = stream.ReadText();
  stream.Close();
  if (t.length && t.charCodeAt(0) === 65279) t = t.substring(1);
  return t;
}

function escCSV(s) {
  s = String(s == null ? '' : s);
  var needQ = false;
  for (var q = 0; q < s.length; q++) {
    var c = s.charAt(q);
    if (c === '"' || c === ',' || c === '\r' || c === '\n') { needQ = true; break; }
  }
  if (!needQ) return s;
  return '"' + s.replace(/"/g, '""') + '"';
}

if (!Math.imul) {
  Math.imul = function (a, b) {
    a = a | 0;
    b = b | 0;
    var ah = (a >>> 16) & 0xffff;
    var al = a & 0xffff;
    var bh = (b >>> 16) & 0xffff;
    var bl = b & 0xffff;
    return (al * bl + (((ah * bl + al * bh) << 16) >>> 0)) | 0;
  };
}
if (!Array.prototype.forEach) {
  Array.prototype.forEach = function (fn, thisArg) {
    var i, len = this.length;
    for (i = 0; i < len; i++) if (i in this) fn.call(thisArg, this[i], i, this);
  };
}

var window = {};
eval(readUtf8(proto + 'mis-pages-data.js'));
eval(readUtf8(proto + 'converter-mis-data.js'));

var dataDir = base + 'data\\';
if (!fso.FolderExists(dataDir)) fso.CreateFolder(dataDir);

var m = window.CONVERTER_MIS.master;
var h = ['SrNo','KPI_Name','Data_Source','Formula_Note','Current_Value','Target','Delta','PageIndex','Last_Update','BU','Site','Severity','Status'];
var lines = [];
lines.push(h.join(','));
for (var i = 0; i < m.length; i++) {
  var r = m[i];
  var cells = [r.sr, r.kpi, r.dataSource, r.formulaNote, r.value, r.target, r.delta, r.page, r.lastUpdate, r.bu, r.site, r.severity, r.status];
  var row = [];
  for (var k = 0; k < cells.length; k++) row.push(escCSV(cells[k]));
  lines.push(row.join(','));
}
var out1 = fso.CreateTextFile(dataDir + 'Converter_MIS_master.csv', true);
out1.Write(lines.join('\r\n'));
out1.Close();

var summ = window.CONVERTER_MIS.summary;
var h2 = ['Perspective','Pillar','Score','KPI_Count'];
var lines2 = [];
lines2.push(h2.join(','));
for (var j = 0; j < summ.length; j++) {
  var t = summ[j];
  var row2 = [escCSV(t.perspective), escCSV(t.pillar), escCSV(t.score), escCSV(t.kpiCount)];
  lines2.push(row2.join(','));
}
var out2 = fso.CreateTextFile(dataDir + 'Converter_MIS_summary.csv', true);
out2.Write(lines2.join('\r\n'));
out2.Close();

WScript.Echo('Wrote ' + m.length + ' master rows and ' + summ.length + ' summary rows to data\\');
