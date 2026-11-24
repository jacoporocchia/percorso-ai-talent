cover('Lezione 11 · Agente, fase 6: contratto e prove', 'Lunedì 1° marzo 2027')

agenda('Oggi l’agente passa la sua batteria di prova e diventa un plugin installabile', [
    ('0-15’', 'Ripartenza', 'I casi di prova, scambiati'),
    ('15-30’', 'Pillola', 'Un agente si misura, non si ammira'),
    ('30-50’', 'Contratto', 'Una pagina, cinque voci'),
    ('50-100’', 'Prove', 'Eseguire, correggere, rieseguire'),
    ('100-120’', 'Plugin', 'Confezione e consegna')],
    'un agente con contratto, batteria di prova eseguita e plugin installato, pronto per una settimana di uso vero.',
    notes='Fase 6 del processo standard. È la lezione in cui l’agente smette di essere un esercizio.')

cards3('I casi di prova si leggono prima di eseguirli: la risposta attesa è chiara?', [
    ('Lo scambio', 'Ogni gruppo legge i casi dell’altro. Manca un caso ovvio? Uno è ambiguo?'),
    ('I casi di stop', 'Sono davvero situazioni in cui l’agente deve fermarsi? Sono realistici?'),
    ('La risposta attesa', 'È scritta abbastanza bene da dire, dopo, se l’agente ha fatto ok o no?')],
    R('Un caso senza risposta attesa chiara ', 'non misura niente: diventa un’opinione su una risposta.'),
    notes='Cinque minuti di lettura per gruppo. Ogni gruppo può aggiungere un caso suggerito dall’altro.')

cards3('Un agente si misura, non si ammira: tre esiti per ogni caso', [
    ('ok', 'Fa quello che la risposta attesa diceva. Si può usare così.'),
    ('fix', 'Va nella direzione giusta ma serve una correzione: un dato, un tono, un passo mancante.'),
    ('fail', 'Sbaglia, inventa, o non si ferma quando doveva.')],
    R('Obiettivo del percorso: ', 'almeno l’80% dei casi ok. I casi di stop devono essere tutti ok.'),
    notes='Gli stessi tre esiti del registro evals del coach (data, task, outcome, note, by). La continuità è voluta: dopo il percorso, il registro continua.')

cards4('Il mini-contratto sta in una pagina, e ha cinque voci', [
    ('Cosa fa', 'Il compito, per chi, in una frase.'),
    ('Input e output', 'Cosa riceve, cosa restituisce, in che formato.'),
    ('Cosa non fa mai', 'Ripreso dal core, identico. Si cambia solo con una nuova versione.'),
    ('Chi lo mantiene', 'La owner: corregge, aggiorna, decide le nuove versioni.')],
    R('Il contratto è per chi lo usa, ', 'non per chi lo costruisce: deve capirlo una collega che non c’era.'),
    notes='Cinque voci, quattro riquadri: input e output stanno insieme. Il contratto va in contratto.md, nella cartella dell’agente.')

steps('La batteria si esegue, si corregge e si riesegue', [
    ('Esegui tutti i casi', 'Senza fermarti a correggere.'),
    ('Segna l’esito', 'ok, fix o fail, con una nota.'),
    ('Correggi', 'Prima una regola esistente, poi una nuova.'),
    ('Riesegui tutto', 'Una correzione può rompere altro.'),
    ('Registra', 'Una riga per caso nel registro.')],
    [R('La regola del coach: ', 'correggere una regola esistente prima di aggiungerne una nuova.'), R('Un core che cresce a ogni errore ', 'torna a essere un prompt lungo.')],
    notes='Riesegui tutto dopo ogni correzione importante: è il punto che si salta. Una regola nuova sul tono può cambiare la risposta a un caso di stop.')

code_slide('Il plugin è lo stesso pacchetto del coach: si installa, si usa, si aggiorna per versioni', 'plugin <nome-agente>/  v1.0.0',
           'core.md\nskill/\n   <skill-1>/SKILL.md\n   <skill-2>/SKILL.md\nCONTRACT.md\nCHANGELOG.md     ← cosa cambia a ogni versione\n\nfuori dal plugin, in 05_agenti:\n   casi-prova.md\n   registro-usi.csv\n   PROCESSO.md',
           'Cosa si fa oggi', [
               ('Claude confeziona', 'la cartella come plugin, in Cowork.'),
               ('Si installa', 'sui Mac del gruppo, e si prova un caso.'),
               ('Versione 1.0.0', 'nel CHANGELOG, con la data.'),
               ('Il registro', 'resta fuori dal plugin: è di chi lo usa.')],
           R('Ogni modifica al core ', 'è una nuova versione, con una riga nel CHANGELOG. Così si sa sempre quale agente ha prodotto cosa.'),
           notes='Prima della lezione verifica il flusso di creazione e installazione di un plugin in Cowork sulla versione installata. Il coach è un esempio funzionante.')

cards3('Prima dell’uso reale: tre controlli che non si saltano', [
    ('Dati', 'L’agente lavora su dati che si possono dare a Claude? Niente dati personali non anonimizzati.'),
    ('Decisioni', 'Prepara e propone. Su persone non decide e non valuta niente.'),
    ('Azioni', 'Non invia, non pubblica, non modifica senza l’ok di chi lo usa.')],
    R('Se un controllo non passa, ', 'l’agente non va in uso. Si corregge il core o si restringe il compito.'),
    notes='Sono i punti di a04 del coach, ridotti al minimo. Se un agente non li passa, meglio una settimana di ritardo che un uso fuori perimetro.')

cards2('Per lunedì 8: usare l’agente su casi reali e registrare ogni uso', [
    (1, 'Usarlo davvero', 'Tutta la settimana', 'Ogni volta che il processo si presenta, si passa dall’agente. Chi è nel gruppo, e chi vuole provarlo.'),
    (2, 'Registrare ogni uso', '1 minuto per uso', 'Una riga in registro-usi.csv: data, compito, esito (ok, fix, fail), nota, chi.')],
    [R('Un fail non è un fallimento: ', 'è il dato che serve alla lezione 12 per correggerlo.'), R('Tempo: ', 'circa 45 minuti in tutto, oltre al lavoro che avresti fatto comunque.')],
    notes='Se il processo non si presenta in settimana, usate i casi di prova come casi reali e annotatelo.')

VIDEOS = [
    ('Tips for building AI agents', 'Anthropic: come capire se un agente funziona.', 'https://www.youtube.com/watch?v=LP5OCa20Zpg', 'inglese, sottotitoli'),
    ('AI Act nel recruiting', 'Perché le decisioni su persone restano umane.', 'https://www.youtube.com/watch?v=Il-aSdEfqow', 'italiano'),
    ('Pericoli e limiti dell’intelligenza artificiale', 'Enkk: i limiti da tenere a mente quando un agente va in uso.', 'https://www.youtube.com/watch?v=Yg4dgh6FU3Y', 'italiano'),
    ('MCP: cos’è e come usarlo', 'Per chi vuole collegare l’agente ad altri strumenti, più avanti.', 'https://www.youtube.com/watch?v=JHDAqk3_lWY', 'italiano')]
EXTRA = None
links('Per approfondire: misurare un agente e usarlo con giudizio', VIDEOS)

closing('Quale caso di prova vi ha sorpreso?', 'Prossima lezione: lunedì 8 marzo')

SCALETTA = {
    'title': 'Lezione 11 · Agente, fase 6: contratto e prove',
    'subtitle': 'Scaletta del facilitatore · lunedì 1° marzo 2027 · 2 ore · 5 colleghe in 2 gruppi',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'I gruppi scambiano e rifiniscono i casi di prova, scrivono il mini-contratto, eseguono la batteria con esiti ok, fix e fail, correggono e rieseguono, poi confezionano l’agente come plugin e lo installano. A casa lo usano su casi reali per tutta la settimana e registrano ogni uso.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Un agente si giudica dall’esito su casi scritti prima, non dall’impressione di una risposta riuscita.'],
            ['Output in aula', 'contratto.md, batteria eseguita con esiti registrati, plugin v1.0.0 installato sui Mac del gruppo.'],
            ['Output per l’8/3', 'registro-usi.csv con ogni uso della settimana: data, compito, esito, nota, chi.'],
            ['Segnale che ha funzionato', 'Almeno l’80% dei casi ok dopo la seconda esecuzione, e tutti i casi di stop ok.']]],
        ['h1', 'Prima del 1° marzo'],
        ['b', 'Verifica in Cowork il flusso per confezionare una cartella come plugin e installarlo su un altro Mac. Il coach è il tuo esempio funzionante: il percorso di installazione deve essere ripetibile dalle colleghe.'],
        ['b', 'Leggi i due casi-prova.md: segnati i casi di stop deboli.'],
        ['b', 'Prepara registro-usi.csv vuoto con l’intestazione data,compito,esito,nota,chi nelle due cartelle agente.'],
        ['b', 'Avvisa il responsabile per la demo della lezione 12: 30 minuti, l’8 marzo.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Ripartenza', 'Slide 3. Scambio dei casi di prova tra gruppi.'],
            ['15-30’', 'Pillola', 'Slide 4. ok, fix, fail. Obiettivo 80%, stop tutti ok.'],
            ['30-50’', 'Contratto', 'Slide 5. contratto.md in una pagina, cinque voci.'],
            ['50-100’', 'Prove', 'Slide 6. Esecuzione completa, esiti, correzioni (prima una regola esistente), riesecuzione completa.'],
            ['100-112’', 'Plugin e controlli', 'Slide 7 e 8. Confezione, installazione, CHANGELOG. I tre controlli prima dell’uso reale.'],
            ['112-120’', 'Consegna', 'Slide 9, 10 e 11.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Una risposta brillante convince più di dieci casi registrati, ed è il motivo per cui si registrano i casi. L’ammirazione è il rischio specifico di questa lezione: il gruppo ha costruito qualcosa e vuole vederlo funzionare. La batteria scritta prima protegge dal vedere solo quello che si vuole vedere.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Molti fail alla prima esecuzione', 'Normale. Si guarda se il problema è il core (regola mancante o ambigua), una skill (riga che non scatta) o il caso (risposta attesa irrealistica).'],
            ['Un caso di stop fallisce', 'Si corregge prima di tutto il resto, nel “cosa non fa mai” del core. L’agente non va in uso finché non passa.'],
            ['Il plugin non si installa', 'L’agente si usa per la settimana direttamente dalla cartella in Cowork. L’installazione si sistema prima della lezione 12.'],
            ['Il gruppo vuole aggiungere funzioni', 'Si annotano nel diario per la v1.1. La v1.0.0 resta piccola.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, i due contratti, le due batterie con gli esiti, i CHANGELOG. Insieme ai diari, sono la traccia completa del processo standard applicato due volte.']]}

CONSEGNA = {
    'title': 'Lezione 11 · Il lavoro per lunedì 8 marzo',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 45 minuti nella settimana',
    'blocks': [
        ['h1', '1. Usa l’agente su casi reali'],
        ['p', 'Per tutta la settimana, ogni volta che il processo si presenta, passa dall’agente. Se il processo non si presenta, usa uno dei casi di prova come se fosse reale e annotalo.'],
        ['h1', '2. Registra ogni uso (1 minuto)'],
        ['p', 'Una riga in registro-usi.csv, nella cartella dell’agente:'],
        ['table', [1500, 2900, 1300, 2638, 1300], [
            ['data', 'compito', 'esito', 'nota', 'chi'],
            ['2027-03-01', 'conferma docente corso X', 'ok', ' ', 'iniziali'],
            [' ', ' ', 'fix', 'cosa hai dovuto correggere', ' '],
            [' ', ' ', 'fail', 'cosa ha sbagliato', ' ']]],
        ['h2', 'I tre controlli, sempre'],
        ['b', 'Dati: niente dati personali non anonimizzati.'],
        ['b', 'Decisioni: l’agente prepara e propone, non decide su persone.'],
        ['b', 'Azioni: non invia e non modifica niente senza il tuo ok.'],
        ['h1', 'Cosa porti alla lezione 12'],
        ['b', 'Il registro degli usi della settimana.'],
        ['b', 'Il fail più istruttivo, da raccontare in due minuti.']]}
