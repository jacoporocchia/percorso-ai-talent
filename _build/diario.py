import openpyxl, datetime as dt
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
wb = openpyxl.Workbook()
ins = wb.active; ins.title = 'Istruzioni'
ws = wb.create_sheet('Diario')
H = PatternFill('solid', fgColor='1860A8'); Z = PatternFill('solid', fgColor='EEF4FA'); thin = Side(style='thin', color='BFBFBF')
rows = [('Diario del tempo · una settimana a scelta tra l’11 e il 29 gennaio 2027', True), ('', False),
 ('Quando: a metà giornata per la mattina e quando esci per il pomeriggio, all’ora che va bene a te. Mai a fine settimana: si registra il momento, non il ricordo.', False),
 ('Come: nel foglio Diario scrivi le date dei cinque giorni nella colonna Data; le mezz’ore dalle 8 alle 19 sono già scritte. Per ogni mezz’ora scrivi l’attività in poche parole e scegli le etichette dai menu.', False),
 ('Se una mezz’ora contiene più cose, scrivi quella che ha preso più tempo. Le righe fuori dal tuo orario lasciale vuote.', False),
 ('Tempo: 3-4 minuti ogni volta. Se ne servono di più, scrivi meno.', False), ('', False),
 ('Le etichette', True),
 ('Tipo: skilled (il lavoro per cui sei lì), strategico (pianificare, decidere priorità), coordinamento (allineamenti, messaggi, cercare informazioni, passare tra strumenti).', False),
 ('Goal: il goal del tuo goal.md a cui serve, in due parole, oppure “nessuno”.', False),
 ('Energia: + ti carica, = neutra, − ti scarica.', False),
 ('Pianificato: era in calendario o previsto? sì / no.', False), ('', False),
 ('Il file è tuo. Il venerdì lo dai al coach con /coach audit, nella tua cartella, e il coach aggiorna la sintesi. Non lo condividi con nessuno.', True)]
for i, (t, b) in enumerate(rows, 1):
    c = ins.cell(i, 1, t); c.font = Font(name='Calibri', size=14 if i == 1 else 11, bold=b, color='15428E' if b else '000000'); c.alignment = Alignment(wrap_text=True, vertical='top')
ins.column_dimensions['A'].width = 110
hdr = ['Giorno', 'Data', 'Dalle', 'Alle', 'Attività (poche parole)', 'Tipo', 'Goal', 'Energia', 'Pianificato']
for j, h in enumerate(hdr, 1):
    c = ws.cell(1, j, h); c.fill = H; c.font = Font(bold=True, color='FFFFFF'); c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
gg = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì']
r = 2
for d in range(5):
    day = None
    t = dt.datetime(2026, 1, 1, 8, 0)
    for k in range(22):
        vals = [gg[d], day, t.time(), (t + dt.timedelta(minutes=30)).time()]
        for j, v in enumerate(vals, 1):
            c = ws.cell(r, j, v)
        ws.cell(r, 2).number_format = 'DD/MM/YYYY'; ws.cell(r, 3).number_format = 'HH:MM'; ws.cell(r, 4).number_format = 'HH:MM'
        for j in range(1, 10):
            c = ws.cell(r, j); c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            if d % 2: c.fill = Z
        t += dt.timedelta(minutes=30); r += 1
last = r - 1
for col, opts in [('F', 'skilled,strategico,coordinamento'), ('H', '+,=,−'), ('I', 'sì,no')]:
    dv = DataValidation(type='list', formula1='"%s"' % opts, allow_blank=True); ws.add_data_validation(dv); dv.add('%s2:%s%d' % (col, col, last))
for col, w in zip('ABCDEFGHI', [11, 11, 7, 7, 42, 16, 22, 9, 11]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = 'E2'; ws.auto_filter.ref = 'A1:I%d' % last
ws.row_dimensions[1].height = 30
wb.save('/mnt/project-files/percorso-ai-talent/lezione-02/L02-diario-tempo.xlsx')
print('ok', last)
