cover('Lezione 9 · Agente, fase 4: architettura', 'Lunedì 15 febbraio 2027')

agenda('Oggi il core si rivede insieme e ognuna scrive la sua skill dell’agente', [
    ('0-15’', 'Ripartenza', 'La regola su cui non eravate d’accordo'),
    ('15-25’', 'Pillola', 'Regole sempre, strumenti al bisogno'),
    ('25-55’', 'Plenaria', 'I due core, letti ad alta voce'),
    ('55-65’', 'Il modello', 'Com’è fatta una skill dell’agente'),
    ('65-95’', 'In gruppo', 'Una skill a testa'),
    ('95-108’', 'Prova', 'Ogni skill su un caso'),
    ('108-120’', 'Consegna', 'Rifinire e provare due volte')],
    'un core rivisto in plenaria e una skill dell’agente con il tuo nome, già provata una volta.',
    notes='Fase 4 del processo standard. Nella v1 architettura e scrittura stavano nella stessa lezione e le skill si scrivevano “una o due per gruppo”: nella simulazione finivano tutte in mano alla collega più veloce. Nella v2 ogni collega scrive la sua, in aula.')

cards3('La regola su cui non eravate d’accordo dice qualcosa sul processo', [
    ('Era una regola?', 'O era un caso particolare? I casi vanno nelle skill o negli esempi, non nel core.'),
    ('Era una scelta?', 'Due modi legittimi di lavorare. Decide la owner, e lo scrive nel diario.'),
    ('Era un buco?', 'Il processo reale non è chiaro neanche a voi. Va chiarito prima di scriverlo.')],
    R('Un agente non risolve un disaccordo: ', 'lo esegue in modo incoerente. Va risolto prima, tra persone.'),
    notes='Un minuto per gruppo. Il terzo caso, il buco nel processo, è il più prezioso: è il punto in cui l’agente sbaglierebbe. Se il buco riguarda il processo stabile (chi approva, quando si manda), lo chiarisce la titolare del processo, non il gruppo.')

compare('Le regole stanno sempre attive, gli strumenti si caricano al bisogno', (
    'Core: sempre attivo', BLU, ['Chi è, per chi lavora, cosa produce', 'Tono e formato di ogni risposta', 'Cosa chiedere se manca un dato, quando fermarsi', 'Cosa non fa mai']), (
    'Skill: al bisogno', CEL, ['Una procedura per una situazione', 'Template ed esempi riusciti', 'Criteri per un caso specifico', 'Si apre quando la richiesta somiglia alla riga “Usalo quando”']),
    [R('Perché le regole non vanno in una skill: ', 'un agente non si accorge di stare sbagliando,'), R('quindi non caricherebbe la regola ', 'proprio quando servirebbe.')],
    notes='È la decisione chiave dell’architettura del coach (fase 4, 9 novembre). Mostra il registro delle decisioni in PROCESSO.md. Le colleghe l’hanno già visto alla lezione 7 smontando il coach: qui lo applicano al loro agente.')

cards3('I due core in plenaria: ogni gruppo legge, l’altro fa tre domande', [
    ('Vale a ogni risposta?', 'Se una regola serve solo in una situazione, è una skill. Si sposta oggi.'),
    ('Comincia con un verbo?', '“Scrivi”, “chiedi”, “fermati”. Se comincia con “è importante che”, si riscrive alla lezione 10.'),
    ('Sta in una pagina?', 'Se no, qualcosa è riferimento e torna in fonti.')],
    R('Quindici minuti per gruppo: ', 'cinque di lettura, dieci di domande. La owner decide cosa cambiare e lo scrive nel diario.'),
    notes='Leggere ad alta voce il core è più efficace che leggerlo a schermo: le regole scritte male si sentono. Non correggere tu: fai le domande. Le regole che si spostano dal core diventano le skill di oggi.')

code_slide('Una skill dell’agente: la riga “Usalo quando”, poi sequenza, domande, output', 'skill/<nome-skill>/SKILL.md  (dal modello)',
           '---\nname: <nome-skill>\ndescription: Usalo quando <la\n  situazione, con le parole\n  di chi la chiede>.\n---\n## Sequenza\n1. …\n2. …\n## Se manca qualcosa, chiedi\n- …\n## Output\n<formato, esempio riuscito>\nAutrice: <nome> · <data>',
           'Una skill a testa', [
               ('Una procedura', 'dal mucchio “comportamento”, o una regola spostata dal core.'),
               ('La riga', 'descrive una situazione, non un contenuto.'),
               ('Un esempio', 'riuscito dentro la skill, dalle fonti.'),
               ('Il tuo nome', 'in fondo: chi l’ha scritta la corregge.')],
           R('Una skill, una situazione. ', 'Se la riga “Usalo quando” ha due “oppure”, sono due skill.'),
           notes='È la stessa struttura della skill personale della lezione 7, dentro l’agente invece che nella propria cartella. Stessa struttura dei file atomici del coach: riga “Usalo quando”, poi sequenza, domande, output.')

cards4('30 minuti di gruppo: come si dividono le skill', [
    ('Gruppo da tre', 'Tre skill, una a testa. La titolare del processo prende la procedura più delicata.'),
    ('Gruppo da due', 'Due skill. Il processo è stabile e piccolo: due bastano per la prima versione.'),
    ('Chi finisce prima', 'Legge la skill di un’altra e controlla la riga “Usalo quando”.'),
    ('Chi è indietro', 'Scrive solo riga e sequenza. Domande e output si completano a casa.')],
    R('Le skill non si scrivono a casa da sole: ', 'qui c’è chi vi risponde quando la procedura non è chiara.'),
    notes='Gira tra i gruppi e guarda solo una cosa: la riga “Usalo quando”. Se descrive un contenuto (“template per…”), falla riscrivere come situazione.')

prompt_slide('La prova: chiedi senza nominare la skill', 'In Cowork, nella cartella dell’agente',
             'Leggi core.md e comportati come descritto lì. Le skill sono nella cartella skill.\n\n<una richiesta come la farebbe una collega, senza nominare la skill>\n\nAlla fine dimmi quale skill hai usato.',
             'Se usa la skill sbagliata', 'Le due righe “Usalo quando” si somigliano troppo. Si riscrivono insieme, con l’altra autrice.',
             'Cosa guardare', [
                 ('È scattata?', 'Se no, si corregge la riga.'),
                 ('Ha seguito la sequenza?', 'Se no, la sequenza è ambigua.'),
                 ('Ha chiesto il dato mancante?', 'Se no, manca nella sezione “chiedi”.')],
             foot='Ogni collega prova la sua skill una volta in aula. Le altre due prove sono nella consegna.',
             notes='Nella seconda prova esplorativa (lezione 10) le skill lavoreranno insieme. Oggi basta che ognuna scatti quando deve.')

cards2('Per lunedì 22: la tua skill, rifinita e provata due volte', [
    (1, 'Rifinire', '15 minuti', 'Completa sequenza, domande e output. Aggiungi l’esempio riuscito, con i nomi inventati.'),
    (2, 'Provare su due casi', '15 minuti', 'Due richieste diverse, senza nominare la skill. Per ognuna una riga in PROCESSO.md: è scattata, cosa hai corretto.')],
    [R('Totale: 30 minuti nel tuo slot. ', 'Versione minima, 15 minuti: riga e sequenza complete, una prova.')],
    notes='La consegna è individuale ma la skill vive nella cartella del gruppo. La co-owner controlla lunedì mattina che ci siano tutte.')

VIDEOS = [
    ('Come usare le Skills per Claude', 'Se non l’hai visto alla lezione 7.', 'https://www.youtube.com/watch?v=gd5u63lx7Ug', 'italiano'),
    ('Come funzionano gli agenti AI?', 'Enkk sugli agenti: cosa c’è dentro, oltre il prompt.', 'https://www.youtube.com/watch?v=AYeCGb2ZaSU', 'italiano'),
    ('Building more effective AI agents', 'Anthropic: istruzioni chiare e strumenti ben descritti.', 'https://www.youtube.com/watch?v=uhJJgc-0iTQ', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: come un agente sceglie lo strumento giusto', VIDEOS)

closing('Quale regola è uscita dal core per diventare una skill?', 'Prossima lezione: lunedì 22 febbraio')

SCALETTA = {
    'title': 'Lezione 9 · Agente, fase 4: architettura',
    'subtitle': 'Scaletta del facilitatore · lunedì 15 febbraio 2027 · 2 ore · 5 colleghe in 2 gruppi',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'I gruppi portano il core completo, lo leggono ad alta voce in plenaria con tre domande e spostano nelle skill le regole che non valgono a ogni risposta. Poi, in trenta minuti di gruppo, ogni collega scrive la sua skill dell’agente dal modello e la prova su un caso. A casa la rifinisce e la prova due volte.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Separare ciò che vale sempre da ciò che serve in una situazione, e scrivere una skill che scatta quando deve.'],
            ['Output in aula', 'Core rivisto in plenaria, con le decisioni nel diario. Una skill per collega, con nome dell’autrice, provata una volta.'],
            ['Output per il 22/2', 'Ogni skill rifinita (sequenza, domande, output, esempio) e provata su due casi, con una riga a prova nel diario.'],
            ['Segnale che ha funzionato', 'Cinque skill, cinque autrici. Nessuna riga “Usalo quando” descrive un contenuto.']]],
        ['h1', 'Prima del 15 febbraio'],
        ['b', 'Leggi i due core: non correggerli, annota dove la plenaria potrebbe non vedere un problema.'],
        ['b', 'Controlla che in 04_modelli ci sia il modello SKILL.md con la riga dell’autrice.'],
        ['b', 'Tieni aperto PROCESSO.md del coach: il registro delle decisioni del 9 novembre spiega perché le regole stanno nel core.'],
        ['b', 'Verifica con le owner che le parti del core siano arrivate tutte. Se manca la parte di qualcuna, la si scrive nei primi 10 minuti della plenaria.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Ripartenza', 'Slide 3. La regola su cui non erano d’accordo: regola, scelta o buco?'],
            ['15-25’', 'Pillola', 'Slide 4. Core sempre attivo, skill al bisogno. Perché.'],
            ['25-55’', 'Plenaria sui core', 'Slide 5. Un gruppo legge, l’altro fa le tre domande, poi si scambia. La owner decide e scrive nel diario.'],
            ['55-65’', 'Il modello della skill', 'Slide 6. Il file SKILL.md dal modello. Una skill, una situazione.'],
            ['65-95’', 'Una skill a testa', 'Slide 7. Trenta minuti di gruppo. Tu guardi solo le righe “Usalo quando”.'],
            ['95-108’', 'Prova', 'Slide 8. Ognuna prova la sua skill una volta, senza nominarla.'],
            ['108-120’', 'Consegna', 'Slide 9, 10 e 11.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'L’architettura è una decisione su cosa l’agente legge sempre e cosa legge solo quando serve. Le regole di comportamento stanno sempre attive perché l’agente non si accorge di stare sbagliando. Le procedure stanno nelle skill perché caricarle sempre diluirebbe le regole. La riga “Usalo quando” è il punto in cui le due cose si incontrano: se descrive male la situazione, la skill giusta non si apre.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La plenaria diventa una critica', 'Riporta alle tre domande: si commenta il testo, non le persone. Decide la owner.'],
            ['Il core supera la pagina', 'Per ogni regola: vale a ogni risposta? Se no, è la skill di qualcuna.'],
            ['Una collega non sa quale procedura scegliere', 'Le dai la regola che la plenaria ha spostato dal core: è già una skill in potenza.'],
            ['Due skill si sovrappongono', 'Le due autrici riscrivono insieme le righe “Usalo quando” finché non descrivono situazioni diverse.'],
            ['Una skill non ha un esempio riuscito', 'Cercatelo nelle fonti. Se non c’è, il processo non ha ancora un “buon risultato” condiviso: annotatelo nel diario.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, i due core prima e dopo la plenaria, le skill degli agenti con le loro autrici.']]}

CONSEGNA = {
    'title': 'Lezione 9 · Il lavoro per lunedì 22 febbraio',
    'subtitle': 'Percorso AI per Talent · 30 minuti nel tuo slot · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'completa riga “Usalo quando” e sequenza, e prova la skill una volta (15’).']],
        ['h1', '1. Rifinire la tua skill (15’)'],
        ['p', 'Apri skill/<nome-skill>/SKILL.md nella cartella dell’agente. Controlla che ci siano tutte le parti:'],
        ['table', [2800, 6838], [
            ['Parte', 'Cosa controllare'],
            ['Usalo quando', 'Descrive una situazione con le parole di chi chiede. Una sola situazione, nessun “oppure”.'],
            ['Sequenza', 'Passi numerati, ognuno comincia con un verbo.'],
            ['Se manca qualcosa, chiedi', 'I dati senza cui la skill non può lavorare: date, nomi, ruolo, sede.'],
            ['Output', 'Il formato, e un esempio riuscito con i nomi inventati.'],
            ['Autrice', 'Il tuo nome e la data.']]],
        ['h1', '2. Provarla su due casi (15’)'],
        ['p', 'In una chat nuova, nella cartella dell’agente, fai due richieste diverse senza nominare la skill. Per ognuna una riga in PROCESSO.md:'],
        ['table', [2400, 2200, 2200, 2838], [
            ['Richiesta', 'È scattata?', 'Risultato giusto?', 'Cosa ho corretto'],
            [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]],
        ['h1', 'Cosa porti alla lezione 10'],
        ['b', 'La tua skill, rifinita.'],
        ['b', 'Le due righe di prova nel diario.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: il core è stato riletto in plenaria e le regole che non valgono sempre sono diventate skill. Ognuna ha scritto una skill dell’agente con il suo nome. Il passo minimo (25 minuti, prima della lezione 10): chiedi alla owner quale skill ti è stata assegnata, copia il modello SKILL.md da 04_modelli dentro skill/, scrivi riga “Usalo quando” e sequenza, e provala una volta.']]}
