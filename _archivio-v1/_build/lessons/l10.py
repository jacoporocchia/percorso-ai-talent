cover('Lezione 10 · Agente, fasi 4-5: architettura e scrittura', 'Lunedì 22 febbraio 2027')

agenda('Oggi il core si rivede tra gruppi e l’agente riceve le sue prime skill', [
    ('0-15’', 'Ripartenza', 'La regola su cui non eravate d’accordo'),
    ('15-30’', 'Pillola', 'Regole sempre, strumenti al bisogno'),
    ('30-60’', 'Revisione', 'Ogni gruppo legge il core dell’altro'),
    ('60-105’', 'Scrittura', 'Una o due skill per agente'),
    ('105-120’', 'Consegna', 'I casi di prova')],
    'un core rivisto da occhi esterni e le prime skill dell’agente, scritte come istruzioni.',
    notes='Fasi 4 e 5 del processo standard. La revisione incrociata è la versione ridotta del “controllo dei rimandi” fatto sul coach.')

cards3('La regola su cui non eravate d’accordo dice qualcosa sul processo', [
    ('Era una regola?', 'O era un caso particolare? I casi vanno nelle skill o negli esempi, non nel core.'),
    ('Era una scelta?', 'Due modi legittimi di lavorare. Decide la owner, e lo scrive nel diario.'),
    ('Era un buco?', 'Il processo reale non è chiaro neanche a voi. Va chiarito prima di scriverlo.')],
    R('Un agente non risolve un disaccordo: ', 'lo esegue in modo incoerente. Va risolto prima, tra persone.'),
    notes='Un minuto per gruppo. Il terzo caso, il buco nel processo, è il più prezioso: è il punto in cui l’agente sbaglierebbe.')

compare('Le regole stanno sempre attive, gli strumenti si caricano al bisogno', (
    'Core: sempre attivo', BLU, ['Chi è, per chi lavora, cosa produce', 'Tono e formato di ogni risposta', 'Cosa chiedere se manca un dato, quando fermarsi', 'Cosa non fa mai']), (
    'Skill: al bisogno', CEL, ['Una procedura per una situazione', 'Template ed esempi riusciti', 'Criteri per un caso specifico', 'Si apre quando la richiesta somiglia alla riga “Usalo quando”']),
    [R('Perché le regole non vanno in una skill: ', 'un agente non si accorge di stare sbagliando,'), R('quindi non caricherebbe la regola ', 'proprio quando servirebbe.')],
    notes='È la decisione chiave dell’architettura del coach (fase 4, 9 novembre). Mostra il registro delle decisioni in PROCESSO.md.')

cards4('Revisione incrociata: ogni gruppo legge il core dell’altro con quattro domande', [
    ('Istruzione o spiegazione?', '“Scrivi”, “chiedi”, “fermati” sono istruzioni. “È importante che…” è una spiegazione.'),
    ('Si applica a un caso?', 'Prendete un caso reale: la regola dice cosa fare, sì o no?'),
    ('Si contraddice?', 'Due regole che in un caso dicono cose diverse.'),
    ('Manca un “mai”?', 'C’è un errore grave che il core non vieta?')],
    R('Si scrivono i commenti, non le correzioni: ', 'il gruppo autore decide cosa cambiare. 15 minuti per leggere, 15 per discutere.'),
    notes='Scambiate i file in 05_agenti: i commenti in un file revisione.md nella cartella dell’altro gruppo.')

compare('Istruzioni, non spiegazioni: la stessa regola, scritta due volte', (
    'Spiegazione', FUX, ['“È importante che le comunicazioni ai docenti siano complete e professionali, perché rappresentano l’azienda.”']), (
    'Istruzione', BLU, ['“Prima di scrivere al docente, verifica di avere corso, date, aula e materiali. Se manca uno, chiedilo. Tono cordiale, massimo dieci righe.”']),
    [R('Il test: ', 'se la regola non dice cosa fare in un caso concreto, il modello la interpreta. E ognuno la interpreta a modo suo.')],
    notes='Esempio inventato: adattalo a uno dei due processi scelti.', size=20)

code_slide('Una skill dell’agente: la riga “Usalo quando”, poi sequenza, domande, output', 'skill/<nome-skill>/SKILL.md',
           '---\nname: <nome-skill>\ndescription: Usalo quando <la\n  situazione, con le parole di\n  chi la chiede>.\n---\n## Sequenza\n1. …\n2. …\n## Se manca qualcosa, chiedi\n- …\n## Output\n<formato, esempio riuscito>',
           'Per ogni gruppo, oggi', [
               ('Una o due skill,', 'dalle procedure nel mucchio “comportamento”.'),
               ('La riga', 'descrive situazioni, non contenuti.'),
               ('Un esempio', 'riuscito dentro la skill, dalle fonti.'),
               ('Il controllo', 'dei rimandi: ogni file citato esiste.')],
           R('Una skill, una situazione. ', 'Se la riga “Usalo quando” ha due “oppure”, sono due skill.'),
           notes='Stessa struttura dei file atomici del coach: riga “Usalo quando” identica all’indice, poi sequenza, domande, output.')

cards2('Per lunedì 1° marzo: da 6 a 8 casi di prova, di cui due in cui l’agente deve fermarsi', [
    (1, 'Casi normali', '4-6 casi', 'Un input realistico, preso da un caso vero (senza dati personali), e la risposta che vi aspettate.'),
    (2, 'Casi di stop', '2 casi', 'Un input in cui l’agente deve rifiutare o fermarsi: manca un dato, tocca una persona, gli chiedono di inviare.')],
    [R('Scrivete la risposta attesa prima di provare: ', 'altrimenti la prova diventa un’ammirazione.'), R('Tempo totale: ', 'circa 45 minuti, divisi nel gruppo.')],
    notes='La batteria si esegue alla lezione 11. Obiettivo del percorso: almeno 80% di casi ok.')

VIDEOS = [
    ('La masterclass su Claude: 5 livelli', 'Dalle richieste semplici alle istruzioni strutturate.', 'https://www.youtube.com/watch?v=iAgSjh0_H4I', 'italiano'),
    ('Scrivere prompt migliori in 12 minuti', 'Le regole di scrittura che valgono anche per core e skill.', 'https://www.youtube.com/watch?v=bviJO4SPzh4', 'italiano'),
    ('Come usare le Skills per Claude', 'Se non l’hai visto alla lezione 8.', 'https://www.youtube.com/watch?v=gd5u63lx7Ug', 'italiano'),
    ('Building more effective AI agents', 'Anthropic: istruzioni chiare e strumenti ben descritti.', 'https://www.youtube.com/watch?v=uhJJgc-0iTQ', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: scrivere istruzioni che un modello segue', VIDEOS)

closing('Quale regola del vostro core avete riscritto oggi?', 'Prossima lezione: lunedì 1° marzo')

SCALETTA = {
    'title': 'Lezione 10 · Agente, fasi 4-5: architettura e scrittura',
    'subtitle': 'Scaletta del facilitatore · lunedì 22 febbraio 2027 · 2 ore · 5 colleghe in 2 gruppi',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'I gruppi portano la bozza del core, la rivedono incrociata con quattro domande, imparano a scrivere istruzioni invece di spiegazioni e scrivono una o due skill con la riga “Usalo quando”. A casa preparano la batteria di prova, con due casi di stop.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Scrivere regole che dicono cosa fare in un caso concreto, e tenerle separate dagli strumenti.'],
            ['Output in aula', 'Core rivisto (revisione.md dall’altro gruppo, correzioni decise dal gruppo autore). Una o due skill per agente.'],
            ['Output per l’1/3', 'casi-prova.md con 6-8 casi, di cui 2 di rifiuto o stop, con la risposta attesa scritta prima.'],
            ['Segnale che ha funzionato', 'Nessuna regola del core comincia con “è importante che”. Ogni skill ha una sola situazione.']]],
        ['h1', 'Prima del 22 febbraio'],
        ['b', 'Leggi le due bozze di core: non correggerle, annota solo dove la revisione incrociata potrebbe non vedere un problema.'],
        ['b', 'Prepara l’esempio della slide 6 su uno dei due processi reali.'],
        ['b', 'Tieni aperto PROCESSO.md del coach: il registro delle decisioni del 9 novembre spiega perché le regole stanno nel core.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Ripartenza', 'Slide 3. La regola su cui non erano d’accordo: regola, scelta o buco?'],
            ['15-30’', 'Pillola', 'Slide 4. Core sempre attivo, skill al bisogno. Perché.'],
            ['30-60’', 'Revisione incrociata', 'Slide 5. Scambio dei core, 15 minuti di lettura con le quattro domande, 15 di discussione. Commenti in revisione.md.'],
            ['60-70’', 'Istruzioni', 'Slide 6. La stessa regola scritta due volte. Ogni gruppo riscrive due regole del suo core.'],
            ['70-105’', 'Scrittura delle skill', 'Slide 7. Una o due skill per agente. Controllo dei rimandi alla fine.'],
            ['105-120’', 'Consegna', 'Slide 8, 9 e 10.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Il modello non “capisce l’intenzione” di una regola: la esegue. Una spiegazione lascia a lui la scelta di cosa fare, e la scelta cambia da una risposta all’altra. Un’istruzione toglie la scelta dove non deve esserci. Per questo il coach ha file di istruzioni, e la ricerca da cui vengono è rimasta fuori.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La revisione incrociata diventa una critica', 'Riporta alle quattro domande: si commenta il testo, non le persone. Decide il gruppo autore.'],
            ['Il core supera la pagina', 'Chiedi per ogni regola: vale a ogni risposta? Se no, va in una skill.'],
            ['Un gruppo vuole scrivere cinque skill', 'Una o due bastano per la prima versione. Le altre si aggiungono quando l’uso le chiede.'],
            ['Una skill non ha un esempio riuscito', 'Cercatelo nelle fonti. Se non c’è, il processo non ha ancora un “buon risultato” condiviso: annotatelo nel diario.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, i due core prima e dopo la revisione (ottimo materiale didattico), le revisioni incrociate, le skill degli agenti.']]}

CONSEGNA = {
    'title': 'Lezione 10 · Il lavoro per lunedì 1° marzo',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 45 minuti, divisi nel gruppo',
    'blocks': [
        ['h1', 'La batteria di prova: da 6 a 8 casi'],
        ['p', 'Scriveteli in casi-prova.md, nella cartella dell’agente. Per ogni caso:'],
        ['table', [800, 3700, 3500, 1638], [
            ['#', 'Input realistico', 'Risposta attesa', 'Tipo'],
            ['1', 'Preso da un caso vero, senza dati personali', 'Cosa deve fare e cosa deve contenere la risposta', 'normale'],
            ['…', ' ', ' ', ' '],
            ['7', 'Manca un dato essenziale', 'Si ferma e lo chiede, senza inventarlo', 'stop'],
            ['8', 'Gli si chiede di inviare o di decidere su una persona', 'Rifiuta e spiega cosa può fare invece', 'stop']]],
        ['h2', 'Regole'],
        ['b', 'Da 4 a 6 casi normali, presi da situazioni vere.'],
        ['b', 'Almeno 2 casi di stop: rifiutare o fermarsi.'],
        ['b', 'Scrivete la risposta attesa prima di provare l’agente.'],
        ['b', 'Niente dati personali di candidati o dipendenti: nomi inventati.'],
        ['h1', 'Cosa porti alla lezione 11'],
        ['b', 'casi-prova.md del tuo gruppo.'],
        ['b', 'Il core e le skill, con le correzioni della revisione.']]}
