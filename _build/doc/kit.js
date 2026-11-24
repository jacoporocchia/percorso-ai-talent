// Generatore Word generico per i kit di lezione: node kit.js spec.json out.docx
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, HeadingLevel, AlignmentType, LevelFormat, BorderStyle, Footer, PageNumber, ExternalHyperlink } = require('docx');
const FONT = 'Calibri', W = 9638, ACCENT = '15428E';
const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8')), OUT = process.argv[3];
const URL_RE = /(https?:\/\/[^\s)]+)/g;
function runs(t) {
  const arr = Array.isArray(t) ? t : [t];
  const out = [];
  for (const x of arr) {
    const o = typeof x === 'string' ? { text: x } : x;
    const parts = String(o.text).split(URL_RE);
    for (const part of parts) {
      if (!part) continue;
      if (/^https?:\/\//.test(part)) out.push(new ExternalHyperlink({ link: part, children: [new TextRun({ ...o, text: part, style: 'Hyperlink', color: '0A9BD7', underline: {} })] }));
      else out.push(new TextRun({ ...o, text: part }));
    }
  }
  return out;
}
const bd = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
function table(widths, rows) {
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({ tableHeader: i === 0, cantSplit: true,
      children: r.map((c, j) => new TableCell({ width: { size: widths[j], type: WidthType.DXA }, borders: { top: bd, bottom: bd, left: bd, right: bd },
        shading: i === 0 ? { type: ShadingType.CLEAR, fill: '1860A8', color: 'auto' } : (i % 2 === 0 ? { type: ShadingType.CLEAR, fill: 'EEF4FA', color: 'auto' } : undefined),
        margins: { top: 70, bottom: 70, left: 110, right: 110 },
        children: String(c).split('\n').map(line => new Paragraph({ spacing: { after: 40, line: 260 }, children: [new TextRun({ text: line, size: 19, bold: i === 0 || j === 0, color: i === 0 ? 'FFFFFF' : undefined })] })) })) })) });
}
const C = [];
C.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun(spec.title)] }));
C.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: spec.subtitle, color: '595959' })] }));
for (const b of spec.blocks) {
  const [k, a, c] = b;
  if (k === 'h1') C.push(new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(a)] }));
  else if (k === 'h2') C.push(new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(a)] }));
  else if (k === 'p') C.push(new Paragraph({ spacing: { after: 120, line: 290 }, children: runs(a) }));
  else if (k === 'b') C.push(new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 70, line: 280 }, children: runs(a) }));
  else if (k === 'n') C.push(new Paragraph({ numbering: { reference: 'num', level: 0 }, spacing: { after: 70, line: 280 }, children: runs(a) }));
  else if (k === 'quote') C.push(new Paragraph({ spacing: { after: 120, line: 280 }, indent: { left: 400 }, border: { left: { style: BorderStyle.SINGLE, size: 12, color: '0A9BD7', space: 8 } }, children: [new TextRun({ text: a, italics: true, color: '1860A8' })] }));
  else if (k === 'table') { C.push(table(a, c)); C.push(new Paragraph({ spacing: { after: 100 }, children: [] })); }
}
const doc = new Document({ creator: 'Max', title: spec.title,
  styles: { default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 40, bold: true, color: ACCENT }, paragraph: { spacing: { before: 0, after: 100 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: ACCENT }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 24, bold: true, color: '404040' }, paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 1 } } ] },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] },
    { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 300 } } } }] } ] },
  sections: [{ properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: spec.footer + ' · ', size: 16, color: '808080' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '808080' })] })] }) },
    children: C }] });
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('ok', OUT.split('/').pop()); });
