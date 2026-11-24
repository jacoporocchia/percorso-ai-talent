// Lezione 1: scaletta del facilitatore (mode=scaletta) e scheda consegna (mode=scheda)
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  ShadingType, HeadingLevel, AlignmentType, LevelFormat, BorderStyle, Footer, PageNumber
} = require('docx');
const FONT = 'Calibri', W = 9638, ACCENT = '15428E';
const mode = process.argv[2], OUT = process.argv[3];

const run = t => typeof t === 'string' ? new TextRun({ text: t }) : new TextRun(t);
const p = (t, o = {}) => new Paragraph({ spacing: { after: 120, line: 290 }, ...o, children: (Array.isArray(t) ? t : [t]).map(run) });
const h1 = t => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)] });
const h2 = t => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const b = t => new Paragraph({ numbering: { reference: 'bul', level: 0 }, spacing: { after: 70, line: 280 }, children: (Array.isArray(t) ? t : [t]).map(run) });
const n = t => new Paragraph({ numbering: { reference: 'num', level: 0 }, spacing: { after: 70, line: 280 }, children: (Array.isArray(t) ? t : [t]).map(run) });
const quote = t => new Paragraph({ spacing: { after: 120, line: 280 }, indent: { left: 400 }, border: { left: { style: BorderStyle.SINGLE, size: 12, color: '0A9BD7', space: 8 } }, children: [new TextRun({ text: t, italics: true, color: '1860A8' })] });
const bd = { style: BorderStyle.SINGLE, size: 4, color: 'BFBFBF' };
function table(widths, rows) {
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, i) => new TableRow({
      tableHeader: i === 0, cantSplit: true,
      children: r.map((c, j) => new TableCell({
        width: { size: widths[j], type: WidthType.DXA }, borders: { top: bd, bottom: bd, left: bd, right: bd },
        shading: i === 0 ? { type: ShadingType.CLEAR, fill: '1860A8', color: 'auto' } : (i % 2 === 0 ? { type: ShadingType.CLEAR, fill: 'EEF4FA', color: 'auto' } : undefined),
        margins: { top: 70, bottom: 70, left: 110, right: 110 },
        children: String(c).split('\n').map(line => new Paragraph({ spacing: { after: 40, line: 260 }, children: [new TextRun({ text: line, size: 19, bold: i === 0 || j === 0, color: i === 0 ? 'FFFFFF' : undefined })] })),
      })),
    })),
  });
}
const gap = () => new Paragraph({ spacing: { after: 100 }, children: [] });
const C = [];
const add = (...x) => C.push(...x);

const PROMPT_CAL = 'Leggi dal mio calendario Outlook gli eventi della settimana dal 16 al 20 novembre. Trascrivi in una tabella: giorno, inizio, fine, tipo di riunione, se l’ho organizzata io. Non riportare nomi di persone. Non calcolare niente finché non ti confermo la tabella.';
const PROMPT_NUM = 'Ora che la tabella è confermata, sulle quattro settimane calcola: ore di riunione a settimana; quota di riunioni ricorrenti; quanti blocchi liberi da 90 minuti o più a settimana, tra le 9 e le 18; quota di riunioni organizzate da me. Per ogni numero dimmi da quali righe viene.';
if (mode === 'scaletta') {
  add(
    new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Lezione 2 · Dove va il mio tempo')] }),
    p([{ text: 'Scaletta del facilitatore · lunedì 14 dicembre 2026 · 2 ore · 5 colleghe', color: '595959' }]),
    h1('In una riga'),
    p('Le colleghe scrivono in busta quanto pensano di dedicare a tre tipi di lavoro, vedono il tuo scarto tra stima e calendario, imparano la griglia delle quattro etichette e costruiscono con il coach l’inventario delle loro attività ricorrenti. Escono con la raccolta dati avviata: calendario delle ultime quattro settimane da chiudere entro mercoledì, e una settimana di gennaio scelta per il diario.'),
    h1('Obiettivi della lezione'),
    table([2600, 7038], [
      ['Comportamento', 'Prima di decidere cosa automatizzare, chiedersi quanto tempo prende davvero un’attività e chi dovrebbe farla, invece di fidarsi della sensazione.'],
      ['Output in aula', 'Inventario di almeno 15 attività ricorrenti nella propria istanza, ognuna con frequenza, durata, goal e chi deve farlo. Primo prompt sul calendario già dato a Claude.'],
      ['Output per il 21/12', 'Calendario 16/11-11/12 letto con il connettore una settimana alla volta, trascritto, verificato e ridotto a quattro numeri. La settimana scelta per il diario, tra l’11 e il 29 gennaio.'],
      ['Segnale che ha funzionato', 'Tutte e cinque arrivano alle etichette goal e chi deve farlo per almeno 15 attività; almeno una trova un errore nella tabella che Claude ha estratto dal calendario.'],
    ]),
    gap(),
    h1('Prima del 14 dicembre'),
    b([{ text: 'Il tuo audit per la demo. ', bold: true }, 'Scrivi le tue tre percentuali prima di guardare il calendario. Poi fai il passo calendario sulle tue ultime quattro settimane con i due prompt qui sotto, verificando la tabella. Compila la slide 6 con i tuoi numeri e annota cosa ti ha sorpreso. Tieni a portata la tabella e, se c’è, l’errore che hai trovato: è il pezzo più forte della demo.']),
    b([{ text: 'Il connettore del calendario. ', bold: true }, 'Il connettore Microsoft 365 c’è ed è in sola lettura: Claude legge il calendario ma non può modificarlo. Verifica che sia attivo nel Cowork di tutte e cinque prima della lezione: è il primo prompt che daranno in aula.']),
    b('Prova /coach audit su un’istanza di prova: il coach deve partire da t01 (domanda dell’audit e tre percentuali) e passare all’inventario di t03.'),
    b('Cinque foglietti e cinque buste per la stima. Le buste restano a loro.'),
    b('Il file L02-diario-tempo.xlsx pronto da mandare a fine lezione: le date le scrive ognuna, l’orario si adatta al suo.'),
    b([{ text: 'La risposta sugli usi con dati personali. ', bold: true }, 'Nel giro iniziale qualcuna racconterà un uso con CV o dati di colleghi. Tieni pronta la risposta concordata con il DPO e la regola dati della lezione 1.']),
    b([{ text: 'Chi fa recruiting. ', bold: true }, 'Gli eventi di colloquio portano nomi di candidati: per loro il passo calendario si fa con lo screenshot della vista occupato/libero, non con il connettore.']),
    b('Promemoria del giro iniziale: chi non ha chiuso il goal.md lo chiude nei primi minuti dell’inventario.'),
    h1('La scaletta'),
    table([1250, 2300, 6088], [
      ['Tempo', 'Blocco', 'Cosa fai'],
      ['0-15’', 'Ripartenza', 'Slide 2 e 3. Giro di 2-3 minuti a testa: goal.md completato sì o no (il contenuto resta loro), e uno dei tre usi di Claude, con quanto era grande l’input e come hanno verificato. Ricorda la catena: senza goal non si legge il tempo. Se emerge un uso con dati personali: niente colpa, dieci minuti a fine lezione.'],
      ['15-20’', 'Stima in busta', 'Slide 4. Distribuisci foglietti e buste. Tre percentuali che sommano a 100, senza pensarci: skilled, strategico, coordinamento. La busta si chiude e si riapre alla lezione 3.'],
      ['20-35’', 'Pillola e demo', 'Slide 5: tre idee sulla memoria del tempo, e la frase chiave “senza una domanda l’audit è autosorveglianza”. Slide 6: la tua stima contro il tuo calendario, la tabella estratta da Claude e l’errore che hai trovato verificandola. Chiudi con quello che il calendario non mostra: messaggi, ricerche, passaggi tra strumenti. Per quello serve il diario.'],
      ['35-45’', 'La griglia', 'Slide 7 e 8. Le quattro etichette, con la regola che si può partire da goal e chi deve farlo. Classificate insieme tre attività della tua demo. Il test del neolaureato. Fai notare “io per ora”: è da lì che nascono le schede della lezione 4.'],
      ['45-100’', 'Inventario con il coach', 'Slide 9. Ognuna lancia /coach audit nella sua cartella. Il coach chiede cosa vogliono sapere alla fine e le tre percentuali: riportano quelle della busta. Poi “Ripercorri un mese tipico: cosa fai sempre?” e “Cos’altro?”, con frequenza, durata e ore al mese, e le etichette. Obiettivo: almeno 15 attività. Tu giri e sblocchi solo problemi tecnici o di comprensione.'],
      ['100-120’', 'Consegna avviata in aula', 'Slide 10 e 11. Spiega i due pezzi e la versione minima. Poi ognuna dà a Claude il primo prompt sulla prima settimana, così il gesto è già fatto una volta, e scrive in chat la settimana di gennaio scelta per il diario, guardando i suoi picchi. Manda il file del diario. Slide 12: i video per approfondire, facoltativi, da aprire prima per controllare i link. Chiusura con la slide 13: “Cosa ti aspetti di scoprire?”.'],
    ]),
    gap(),
    h1('La pillola nel dettaglio'),
    p([{ text: 'Sovrastimiamo. ', bold: true }, 'Gli studi che confrontano le ore dichiarate con i diari del tempo trovano che le stime superano i dati, e lo scarto cresce con le ore lavorate. Non serve citare numeri: serve che ognuna senta che la sua percentuale in busta è un’ipotesi.']),
    p([{ text: 'Il coordinamento è invisibile. ', bold: true }, 'Nel lavoro di conoscenza una quota ampia del tempo va in allineamenti, messaggi, ricerca di informazioni e passaggi tra strumenti. Sono pezzi brevi che la memoria non registra e che il calendario non mostra.']),
    p([{ text: 'Il confronto è con te. ', bold: true }, 'I benchmark dei report di settore non dicono niente della singola persona. Il confronto utile è la propria stima contro il proprio dato, e il prima contro il dopo: per questo ad aprile si rimisura.']),
    p([{ text: 'Il collegamento con la lezione 1: ', bold: true }, 'come Claude, anche la memoria risponde con sicurezza su cose che non ha davanti. Il rimedio è lo stesso: guardare la fonte.']),
    h1('Il calendario: i due prompt'),
    h2('Passo 1 · Trascrivere'),
    quote(PROMPT_CAL),
    p('Claude legge il calendario con il connettore Microsoft 365, in sola lettura. La verifica resta il punto: può saltare un evento, leggere male un ricorrente o un evento di tutto il giorno, contare due volte una riunione spostata. Si chiede una settimana alla volta: 150 eventi in una tabella sola non si verificano, e la verifica è il punto. Chiedere di non riportare nomi serve a due cose: minimizza i dati delle altre persone e alleggerisce l’input, come nella token economy della lezione 1.'),
    h2('Passo 2 · Calcolare'),
    quote(PROMPT_NUM),
    p('Poi chiedono al coach di salvare i quattro numeri in artefatti/time-audit. Il calendario mostra solo il tempo pianificato: è il dato robusto, ma non è tutto.'),
    h1('Il diario'),
    p('Cinque giorni in una settimana a scelta tra l’11 e il 29 gennaio, fuori dai picchi di ciascuna. Due momenti al giorno, a metà giornata e all’uscita, all’ora che va bene a lei: chi esce alle 17 compila alle 17. Il file ha le mezz’ore dalle 8 alle 19 e le etichette a menu; le righe fuori orario restano vuote. Il protocollo del coach dice che un log che richiede più di dieci minuti al giorno viene abbandonato: per questo due momenti da 3-4 minuti.'),
    p([{ text: 'Perché non a dicembre: ', bold: true }, 'nella v1 il diario cadeva nella settimana prima di Natale, atipica e piena di chiusure. Nella simulazione nessuna lo completava. La busta si apre lo stesso alla lezione 3, con il calendario, che è il dato pesante. Il diario arriva dopo e completa l’audit con ciò che il calendario non mostra: a fine settimana ognuna lo dà al coach con /coach audit, e il coach aggiorna la sintesi.']),
    h1('Se qualcosa va storto'),
    table([3300, 6338], [
      ['Situazione', 'Cosa fai'],
      ['Il coach salta la domanda dell’audit e parte dall’inventario', 'Fai scrivere: “Prima chiedimi cosa voglio sapere alla fine e le mie tre percentuali”. La domanda serve alla lezione 3 per leggere i dati.'],
      ['L’inventario si ferma a 6-8 attività', 'Suggerisci di ripercorrere un mese per frequenza: cosa fai ogni giorno, ogni settimana, ogni mese, una volta l’anno.'],
      ['Una collega non trova goal per molte attività', 'Va bene: “nessuno” è un’etichetta. È un dato, non un giudizio.'],
      ['Una collega racconta un uso con CV o dati di colleghi', 'Niente colpa e niente discussione in plenaria. Rimanda a dieci minuti a fine lezione e dai la risposta concordata con il DPO.'],
      ['Il connettore non risponde o non vede il calendario', 'Ripiego: uno screenshot della vista settimanale per ogni settimana, con gli orari leggibili, e lo stesso prompt cominciando con “Ti do lo screenshot della mia settimana”.'],
      ['Si sfora sui tempi', 'Taglia la griglia a 5 minuti, non l’inventario. L’avvio della consegna in aula non si salta: è la contromisura al lavoro non fatto.'],
    ]),
    gap(),
    h1('Privacy e articolo 4'),
    p('L’audit è di ciascuna e resta nella sua cartella. In aula non si mostrano schermi, se non per scelta. Alla lezione 3 si condivide solo ciò che ognuna sceglie di portare. Il calendario si analizza per sé, senza nomi di altre persone. Se il percorso venisse percepito come misura del tempo delle colleghe, perderemmo la sincerità dei dati e toccheremmo l’articolo 4 dello Statuto dei lavoratori.'),
    h1('Cosa entra nel basket'),
    p('La registrazione della plenaria (ripartenza, pillola, demo, griglia, consegna), il deck, la scheda della consegna, il file del diario e i due prompt del calendario. La tua demo entra solo se decidi di lasciarla. Non entrano l’inventario, le buste e niente delle istanze del coach.'),
  );
} else {
  add(
    new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Lezione 2 · Il lavoro per lunedì 21 dicembre')] }),
    p([{ text: 'Percorso AI per Talent · calendario 30 minuti entro mercoledì 16 · diario 40 minuti in una settimana di gennaio', color: '595959' }]),
    p([{ text: 'Settimana piena? Fai la versione minima: ', bold: true }, 'il calendario delle ultime due settimane invece di quattro (15’). Il resto lo recuperi nel tuo slot di gennaio.']),
    h1('1. Il calendario delle ultime quattro settimane (30’, entro mercoledì 16)'),
    p('Le settimane sono quattro, dal 16 novembre all’11 dicembre. Claude le legge dal tuo Outlook con il connettore Microsoft 365, che è in sola lettura: non può modificare niente.'),
    h2('Passo 1 · Claude trascrive, tu verifichi'),
    p('Nella tua cartella del coach scrivi:'),
    quote(PROMPT_CAL),
    p('Controlla la tabella con Outlook aperto accanto: mancano eventi? Gli orari sono giusti? Correggi, poi ripeti con la settimana dopo, fino all’11 dicembre. Se il connettore non funziona, o se i tuoi eventi portano nomi di candidati, fai uno screenshot per settimana della vista occupato/libero e scrivi “Ti do lo screenshot della mia settimana” al posto della prima frase.'),
    h2('Passo 2 · Quattro numeri'),
    quote(PROMPT_NUM),
    p('Poi chiedi al coach di salvare i numeri in artefatti/time-audit.'),
    h1('2. Il diario (3-4’ due volte al giorno, una settimana tra l’11 e il 29 gennaio)'),
    b('Scegli adesso la settimana, guardando le tue settimane di picco, e scrivila in chat.'),
    b('Apri L02-diario-tempo.xlsx: scrivi le date, le mezz’ore dalle 8 alle 19 sono già scritte. Quelle fuori dal tuo orario lasciale vuote.'),
    b('A metà giornata compili la mattina, quando esci il pomeriggio. Mai a fine settimana: si registra il momento, non il ricordo.'),
    b('Il venerdì dai il file al coach con /coach audit: aggiorna la sintesi del tuo audit (10’).'),
    b('Per ogni mezz’ora: l’attività in poche parole, poi tipo, goal, energia e se era pianificata, dai menu.'),
    b('Se ti servono più di 4 minuti, scrivi meno. Un diario breve completo vale più di uno dettagliato abbandonato.'),
    h1('Per approfondire (facoltativo)'),
    b('6 strategie di concentrazione da Deep Work (italiano): https://www.youtube.com/watch?v=BsFnWKcZTss'),
    b('Recensione di Deep Work (italiano): https://www.youtube.com/watch?v=CjNLMVBJLNY'),
    b('Come gestire il tempo in ufficio (italiano): https://www.youtube.com/watch?v=syO4kcv1kSY'),
    b('Cos’è l’intelligenza artificiale?, Enkk (italiano): https://www.youtube.com/watch?v=0eyKR8P1WR0'),
    h1('Cosa porti alla lezione 3'),
    b('I quattro numeri del calendario, salvati dal coach.'),
    b('La settimana scelta per il diario di gennaio.'),
    b('La busta con la tua stima, ancora chiusa.'),
    h1('Se hai saltato la lezione'),
    p('Le decisioni prese: la stima in busta, le quattro etichette (puoi partire da goal e chi deve farlo), l’inventario con il coach. Il passo minimo (20 minuti): scrivi su un foglio le tre percentuali e chiudilo in busta, lancia /coach audit e arriva a 10 attività, poi fai il calendario della sola ultima settimana. La tua buddy ti racconta il resto.'),
    p([{ text: 'Il file, i numeri e la busta sono tuoi: alla lezione 3 condividi solo quello che scegli.', italics: true, color: '1860A8' }]),
  );
}
const doc = new Document({
  creator: 'Max', title: mode === 'scaletta' ? 'Lezione 2 - Scaletta' : 'Lezione 2 - Consegna',
  styles: {
    default: { document: { run: { font: FONT, size: 22 } } },
    paragraphStyles: [
      { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: FONT, size: 40, bold: true, color: ACCENT }, paragraph: { spacing: { before: 0, after: 100 }, keepNext: true } },
      { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 28, bold: true, color: ACCENT }, paragraph: { spacing: { before: 280, after: 120 }, keepNext: true, outlineLevel: 0 } },
      { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: FONT, size: 24, bold: true, color: '404040' }, paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 1 } },
    ],
  },
  numbering: { config: [
    { reference: 'bul', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] },
    { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 300 } } } }] },
  ] },
  sections: [{
    properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: 'Percorso AI per Talent · Lezione 2 · ', size: 16, color: '808080' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '808080' })] })] }) },
    children: C,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('ok', mode); });
