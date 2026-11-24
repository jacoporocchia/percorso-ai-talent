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

if (mode === 'scaletta') {
  add(
    new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Lezione 1 · Il modello e il coach')] }),
    p([{ text: 'Scaletta del facilitatore · lunedì 7 dicembre 2026 · 2 ore · 5 colleghe', color: '595959' }]),
    h1('In una riga'),
    p('Le colleghe ricevono le regole del percorso, compresa la regola dati, vedono il modello sbagliare con sicurezza su un confronto Excel, imparano tre domande per non fidarsi alla cieca, capiscono dove vivono i file con cui lavoreranno e avviano il coach su di sé. Escono con un lavoro preciso per lunedì 14: finire l’intake e annotare tre usi reali di Claude.'),
    h1('Obiettivi della lezione'),
    table([2600, 7038], [
      ['Comportamento', 'Prima di usare un output di Claude, chiedere da dove viene il dato e cosa non è stato verificato. Prima di caricare un file grande, ridurlo a ciò che serve e chiedere il metodo invece del risultato.'],
      ['Output in aula', 'Istanza del coach aperta e intake avviato (almeno le parti 1-3: accordo, come lavorare, quadro).'],
      ['Output per il 14/12', 'goal.md con 2-3 goal di lavoro e un primo goal a 4-6 settimane; tre note su usi reali di Claude.'],
      ['Segnale che ha funzionato', 'Nella demo almeno una collega trova da sola un errore prima che tu lo mostri; tutte e cinque escono con l’istanza funzionante.'],
    ]),
    gap(),
    h1('Prima del 7 dicembre'),
    b([{ text: 'Passaggio con il DPO fatto. ', bold: true }, 'Tre risposte da avere in tasca: cosa fare degli usi su CV già in corso; quali dati minimi potranno usare gli agenti; conferma del divieto degli account personali. Se il passaggio non c’è stato, la regola dati della slide 4 è la sola copertura: dillo a te stesso prima di dirlo in aula.']),
    b([{ text: 'Patto con i responsabili firmato. ', bold: true }, 'Slot di 45 minuti a settimana nel calendario di ognuna, approvato per nome, e conferma scritta che alla demo le ore liberate si presentano per processo e non entrano in valutazioni.']),
    b([{ text: 'Setup fatto dall’IT. ', bold: true }, 'Cowork attivo, plugin coach installato sui 5 Mac e provato su un Mac che non sia il tuo, connettore Microsoft 365 autorizzato dall’amministratore.']),
    b('Inviti Outlook mandati per tutte le 12 lezioni e per la rimisura del 19 aprile. In aula: “fa fede l’invito”.'),
    b('Modulo su picchi e orario raccolto: sai già quali settimane sono critiche per ognuna.'),
    b('Regola dati stampata, una copia a testa (L01-regola-dati).'),
    b('Per ognuna, una cartella istanza coach-<nome> (copia di istanza-modello) con coach.json compilato: cliente e data di creazione.'),
    b('Pilota: intake completo con una collega, per misurare i tempi reali e vedere se la modalità coach (una domanda per messaggio) regge.'),
    b('Consenso alla registrazione firmato dalle cinque. Si registra la plenaria, non il lavoro individuale con il coach.'),
    b('Sul tuo Mac la cartella demo con i tre file Excel e la chiave della soluzione, che resta solo a te.'),
    b('Deck della lezione aperto, scheda della consegna stampata o pronta da condividere.'),
    h1('La scaletta'),
    table([1250, 2300, 6088], [
      ['Tempo', 'Blocco', 'Cosa fai'],
      ['0-15’', 'Apertura e patto', 'Perché siamo qui (slide 2). Le tre regole del percorso (slide 3): si registra la plenaria, l’istanza del coach è solo loro, ogni lezione lascia un lavoro da fare nello slot fisso di 45 minuti, con una versione minima da 15. Chiedi un sì esplicito a ognuna. Slide 4: la regola dati, e consegni la pagina stampata. Slide 5: cosa succede alla fine (demo per processo, tempo che resta loro, ruolo di docente volontario e in coppia).'],
      ['15-25’', 'Demo: il confronto perfetto', 'Condividi lo schermo. Carica in Claude i file di ottobre e di novembre e usa il prompt della demo (sotto). Leggi la risposta ad alta voce e lascia che sembri giusta. Poi chiedi: “Vi fidereste? Lo mandereste al responsabile?”.'],
      ['25-40’', 'La caccia all’errore', 'A coppie, 10 minuti, con la chiave in mano tua: “Trovate almeno un errore nella risposta”. Raccogli quello che trovano. Poi rivela i due livelli: le trappole nei dati (maiuscole, De Luca/Deluca, spazio finale, nome puntato, duplicato, data come testo) e il file giusto, che era un terzo, il DEF_v3 arrivato per mail.'],
      ['40-55’', 'Pillola: come ragiona un LLM', 'Slide 7 e 8. Tre idee: prevede testo plausibile e non consulta un archivio; vede solo quello che gli dai; quando non sa, inventa con lo stesso tono di quando sa. Poi le tre domande da fare sempre. Rifate insieme il confronto con le tre domande e guardate la differenza.'],
      ['55-65’', 'Token economy', 'Slide 9 e 10. Il token come moneta, la finestra di contesto come scrivania, ogni messaggio che rilegge tutta la chat. Poi il caso dei due Excel da 60 MB: perché non si caricano così e le quattro mosse alternative. Chiedi: “Quale file da 60 MB avete sul Mac in questo momento?”. Dettaglio sotto.'],
      ['65-75’', 'File e cartelle', 'Slide 11. Tre idee: un .md è un file di testo; locale, OneDrive e SharePoint sono tre posti diversi; il coach non si ricorda di loro, rilegge i suoi file. Ognuna apre la cartella del coach e un file .md. Chiedi chi ha il Desktop sincronizzato con OneDrive.'],
      ['75-80’', 'Il coach', 'Slide 12. Cos’è e cosa non è: un’AI che fa domande, non un coach certificato, non un valutatore. L’istanza è sulla loro macchina e la leggono solo loro. Due modalità: coach (domande) e consulente (proposte). Chi ha poco tempo può chiedere la modalità consulente: è legittimo.'],
      ['80-110’', 'Intake individuale', 'Slide 13. Ognuna apre la sua istanza e lancia /coach intake. Nel quadro del ruolo il coach chiede anche le settimane di picco: verifica che le scrivano. Indicazione chiave: “I goal che porti sono di lavoro, perché la prossima settimana li useremo per leggere il tuo tempo”. Tu giri: non leggi lo schermo se non te lo chiedono, sblocchi solo problemi tecnici o di comprensione.'],
      ['110-120’', 'Chiusura e consegna', 'Giro rapido: “Una cosa che ti ha sorpreso oggi”. Slide 14: la consegna per il 14/12, con la versione minima. Slide 15: i video per approfondire, facoltativi. Ognuna scrive in chat a che punto dell’intake è arrivata. Ricorda che la lezione 2 parte dal loro goal.md.'],
    ]),
    gap(),
    h1('La demo nel dettaglio'),
    h2('Il prompt da usare'),
    quote('Ti carico due file con le iscrizioni ai corsi di formazione, uno di ottobre e uno di novembre. Confrontali e dimmi: chi si è aggiunto, chi è stato cancellato, e di quante ore totali è cambiato il piano.'),
    p('Non aggiungere istruzioni di verifica: la demo funziona se il modello risponde come risponde di solito, in fretta e in ordine. Se la risposta esce già perfetta, non è un fallimento della demo. Chiedi: “Bene, ma è il file giusto?” e tira fuori il DEF_v3. Il messaggio regge in entrambi i casi.'),
    h2('Cosa c’è nei file (dalla chiave)'),
    table([3000, 6638], [
      ['Tipo', 'Dettaglio'],
      ['Cambi veri', '3 cancellati (Paolo Ricci, Fabio Moretti, Serena Martinelli), 5 nuovi (Sofia Conte, Lorenzo Ferraro, Martina Ferri, Emanuele Fabbri, Greta Bianco), 1 cambio corso (Ilaria Lombardo).'],
      ['Trappole', 'COSTA in maiuscolo, Deluca senza spazio, Rinaldi con spazio finale, “L.” al posto di Luca Romano, Davide Gallo duplicato (+8 ore finte), una data scritta come testo. Colonne in ordine diverso e intestazione “Ore formazione” al posto di “Ore”.'],
      ['Ore', 'Ottobre 324. Novembre così com’è 356, ma al netto del duplicato 348. Nel DEF_v3 anche Sara Esposito cancellata e Aurora Pellegrini aggiunta.'],
    ]),
    gap(),
    p([{ text: 'Il punto da far arrivare: ', bold: true }, 'il modello non ha sbagliato a fare i conti. Ha fatto bene i conti su dati sporchi e sul file sbagliato, e ha usato lo stesso tono sicuro per la parte giusta e per quella sbagliata. Le tre domande e una struttura dati ordinata (lezioni 5 e 6) servono a questo.']),
    h1('Le tre domande da fare sempre'),
    n('Da quale file e da quali righe viene questo risultato? Mostramele.'),
    n('Cosa non hai potuto verificare, o hai dovuto interpretare?'),
    n('Quali casi sono dubbi (nomi simili, duplicati, formati diversi)? Elencali prima di darmi il totale.'),
    h1('La token economy nel dettaglio'),
    p('Lo scopo non è insegnare la tecnica, ma un riflesso: prima di dare un file a Claude, chiedersi quanto è grande rispetto a quello che serve per rispondere.'),
    h2('Tre idee'),
    table([2900, 6738], [
      ['Idea', 'Come la dici'],
      ['Il token è la moneta', 'Claude non legge parole ma pezzi di parola. Un token è circa tre quarti di parola; italiano, numeri e tabelle ne consumano di più.'],
      ['La finestra di contesto è la scrivania', 'Circa 200.000 token: tutto quello che Claude può avere davanti in una conversazione. Sono un romanzo di 500 pagine, o circa 10.000 righe di una tabella da 10 colonne.'],
      ['Ogni messaggio rilegge tutto', 'A ogni turno la conversazione intera viene rimandata. Una chat lunga consuma di più il limite d’uso e peggiora le risposte, perché l’inizio si perde. Un compito, una chat.'],
    ]),
    gap(),
    h2('Il caso dei due Excel da 60 MB'),
    p('I numeri della slide 8 sono una stima fatta su un file di iscrizioni a 10 colonne: 4,3 MB di .xlsx contengono circa 100.000 righe, quindi 60 MB sono circa 1,4 milioni di righe, cioè circa 30 milioni di token, 150 volte la finestra. Due file, circa 300. Con un file diverso i numeri cambiano, l’ordine di grandezza no.'),
    p([{ text: 'Cosa succede se lo carichi così. ', bold: true }, 'Nella chat il file non passa, perché il limite di caricamento è 30 MB per file. Se lo strumento lo accetta, Claude non lo legge tutto: scrive codice che lo apre, ne guarda un campione e decide da solo quali colonne confrontare e su quale chiave. Sono proprio le scelte che nella demo hanno prodotto un risultato sbagliato con tono sicuro, solo che qui non le vedi. In più consumi il limite d’uso e carichi dati personali che per il confronto non servivano.']),
    p([{ text: 'Cosa fai invece. ', bold: true }, 'Riduci il file alle colonne e alle righe che servono, con una chiave univoca come la matricola. Chiedi a Claude il metodo, non il risultato: la formula CERCA.X o i passi di Power Query per confrontare i due file. Prova il metodo su 50 righe di cui conosci già la risposta, come i file della demo. Poi applicalo al file intero in Excel. Excel conta, Claude ragiona.']),
    h2('Il collegamento con il resto del percorso'),
    p('È la prima volta che compare il tema dei dati: le lezioni 5 e 6 su struttura e non duplicazione partono da qui. Se in aula esce un caso reale di file enorme, annotalo: è un buon candidato per la scheda automazione della lezione 4.'),
    h1('Se qualcosa va storto'),
    table([3300, 6338], [
      ['Situazione', 'Cosa fai'],
      ['Il coach non si avvia o non vede la memoria', 'Lancia /coach: legge da sé core e memoria anche se l’hook non è partito. Se la cartella non ha coach.json, il coach lo dice e chiede: rispondi di no e apri la cartella giusta.'],
      ['L’intake va lento, una domanda alla volta', 'È voluto. Se una collega si blocca, può scrivere “passa in modalità consulente e proponimi tu delle opzioni”.'],
      ['Una collega porta goal personali o delicati', 'Va bene: l’istanza è sua. Ricordale solo che per il time audit serve almeno un goal di lavoro.'],
      ['Una collega racconta un uso con dati personali (CV, valutazioni, account personale)', 'Niente colpa e niente discussione in plenaria. Ringrazia, ricorda la regola dati, e fissate dieci minuti a fine lezione. Dalle la risposta concordata con il DPO: cosa smettere, cosa fare al posto (checklist di screening scritta da lei, JD, scorecard vuote), cosa fare dei dati già caricati.'],
      ['Si sfora sui tempi', 'Taglia la caccia all’errore a 10 minuti, non l’intake né la regola dati. L’intake è la base della lezione 2.'],
      ['Chiedono quanto consuma il loro piano', 'Il limite d’uso dipende dal piano e si azzera a finestre di qualche ora. Non dare numeri: il punto è che chat lunghe e file grandi lo consumano più in fretta.'],
    ]),
    gap(),
    h1('Cosa entra nel basket'),
    p('La registrazione della plenaria (apertura, demo, pillola, chiusura), i tre file demo con la chiave, il deck e la scheda della consegna. Non entrano l’intake e niente delle istanze del coach.'),
  );
} else {
  add(
    new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun('Lezione 1 · Il lavoro per lunedì 14 dicembre')] }),
    p([{ text: 'Percorso AI per Talent · 45 minuti nel tuo slot settimanale · versione minima: 15 minuti', color: '595959' }]),
    p([{ text: 'Settimana piena? Fai la versione minima: ', bold: true }, 'solo il punto 1 fino ai goal (15’). Gli usi di Claude li annoti la settimana dopo.']),
    h1('1. Finisci l’intake con il coach (30’)'),
    p('Apri la tua cartella del coach in Cowork e scrivi /coach intake. Il coach riparte da dove eri arrivata. Arriva fino in fondo: i tuoi goal e il primo impegno della settimana.'),
    b('Porta 2 o 3 goal di lavoro per i prossimi 12 mesi, ognuno con un segnale per capire se lo hai raggiunto.'),
    b('Per il più importante, un goal a 4-6 settimane.'),
    b('Alla fine scrivi /coach memoria e controlla cosa ha scritto il coach. Se qualcosa non ti torna, correggilo: la memoria è tua.'),
    h1('2. Annota tre usi reali di Claude (15’ nella settimana)'),
    p('Ogni volta che usi Claude per lavoro, segna una riga. Ne bastano tre. Non scrivere nomi di persone: se l’uso conteneva dati personali, annota solo il tipo di compito e rileggi la regola dati.'),
    table([2000, 1900, 1900, 1938, 1900], [
      ['Cosa ho chiesto', 'Quanto era grande ciò che gli ho dato', 'Quanto tempo mi ha fatto risparmiare', 'Come ho verificato il risultato', 'Ho fatto una delle tre domande?'],
      [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
    ]),
    gap(),
    h1('Le tre domande da fare sempre'),
    n('Da quale file e da quali righe viene questo risultato? Mostramele.'),
    n('Cosa non hai potuto verificare, o hai dovuto interpretare?'),
    n('Quali casi sono dubbi? Elencali prima di darmi il totale.'),
    h1('Prima di dare un file a Claude'),
    p('Chiediti quante righe servono davvero per rispondere. Se il file è grande, riducilo alle colonne che servono e chiedi a Claude il metodo (una formula, i passi di Power Query) invece del risultato. Provalo su poche righe di cui sai già la risposta, poi applicalo in Excel. E un compito, una chat.'),
    h1('La regola dati del percorso'),
    b('Niente account personali (ChatGPT o Claude personali) per dati di lavoro.'),
    b('Niente CV né dati nominativi di candidati o colleghi in Claude.'),
    b('Quando serve riferirsi a una persona, la matricola, non il nome.'),
    b('Nel dubbio, chiedi a Claude il metodo (la formula, i passi di Power Query) e applicalo in Excel sui dati veri.'),
    h1('Dove sta cosa'),
    table([2900, 6738], [
      ['Domanda', 'Risposta'],
      ['Dove vive il mio coach?', 'Nella cartella coach-<tuonome> sul tuo Mac. In Cowork la apri con “Scegli cartella”. Se il Desktop o Documenti sono sincronizzati con OneDrive, la cartella è anche nel tuo OneDrive personale, non in quello del team.'],
      ['Cos’è un file .md e come lo apro?', 'Un file di testo semplice. Lo apri in Cowork, oppure con il tasto destro, Apri con, TextEdit. Se si apre un altro programma, chiudilo e usa TextEdit.'],
      ['Come capisco se una cartella è sincronizzata?', 'Nel Finder, a sinistra, guarda se sta sotto OneDrive. Un’icona a nuvola accanto al file vuol dire che è solo online: per usarlo in Cowork, tasto destro, Mantieni sempre su questo dispositivo.'],
      ['Il coach “ricorda” quello che ho detto?', 'No. Rilegge i suoi file (profilo, goal, impegni) a ogni sessione. Con /coach memoria vedi esattamente cosa rilegge, e puoi correggerlo.'],
    ]),
    gap(),
    h1('Se hai saltato la lezione'),
    p('Le decisioni prese: le tre regole del percorso, la regola dati, cosa succede alla demo finale. Il passo minimo per agganciarti (20 minuti): guarda la registrazione della demo e della pillola, leggi la regola dati qui sopra, apri la tua cartella del coach e lancia /coach intake fino al quadro del ruolo. La tua buddy ti racconta il resto in dieci minuti.'),
    h1('Per approfondire (facoltativo)'),
    p('Le basi in quattro pillole di Enkk, “AI in pillole”:'),
    b('Cos’è l’intelligenza artificiale? · https://www.youtube.com/watch?v=0eyKR8P1WR0'),
    b('Cosa sono i Large Language Models? · https://www.youtube.com/watch?v=fse5LxSRZAM'),
    b('Come si allena un modello come ChatGPT? · https://www.youtube.com/watch?v=NAJxUKCQwEE'),
    b('Come funzionano gli agenti AI? · https://www.youtube.com/watch?v=AYeCGb2ZaSU'),
    p('Per chi vuole vedere il motore, Andrej Karpathy in inglese con sottotitoli: Intro to Large Language Models (1 ora, https://www.youtube.com/watch?v=zjkBMFhNj_g) e Deep Dive into LLMs like ChatGPT (3,5 ore, https://www.youtube.com/watch?v=7xTGNNLPyMI).'),
    h1('Cosa porti alla lezione 2'),
    b('Il tuo goal.md compilato (lo apri tu dal tuo Mac, non lo condividi).'),
    b('Le tre righe sugli usi di Claude.'),
    p([{ text: 'La lezione 2 parte da qui: useremo i tuoi goal per capire dove va il tuo tempo.', italics: true, color: '1860A8' }]),
  );
}

const doc = new Document({
  creator: 'Max', title: mode === 'scaletta' ? 'Lezione 1 - Scaletta' : 'Lezione 1 - Consegna',
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
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ text: 'Percorso AI per Talent · Lezione 1 · ', size: 16, color: '808080' }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: '808080' })] })] }) },
    children: C,
  }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(OUT, buf); console.log('ok', mode); });
