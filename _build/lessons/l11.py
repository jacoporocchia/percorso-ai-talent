cover('Lezione 11 · Agente, fase 6: contratto e prove', 'Lunedì 1° marzo 2027')

agenda('Oggi l’agente passa la sua batteria di prova e diventa un plugin installato', [
    ('0-10’', 'Ripartenza', 'I casi di prova, scambiati'),
    ('10-20’', 'Pillola', 'Un agente si misura, non si ammira'),
    ('20-35’', 'Contratto', 'Una pagina, cinque voci'),
    ('35-80’', 'In gruppo', 'Eseguire, correggere, rieseguire'),
    ('80-100’', 'Plugin', 'Dal modello, installato con l’IT'),
    ('100-112’', 'Dopo', 'I controlli e il lavoro dopo il percorso'),
    ('112-120’', 'Consegna', 'Una settimana di uso vero')],
    'un agente con contratto, batteria eseguita e plugin installato, e un impegno dopo il percorso dichiarato in minuti.',
    notes='Fase 6 del processo standard. È la lezione in cui l’agente smette di essere un esercizio. Se il passaggio con il DPO non è avvenuto, oggi l’agente non va in uso reale: si fa la lezione, si installa, e l’uso parte dopo il via libera.')

cards3('I casi di prova si leggono prima di eseguirli: la risposta attesa è chiara?', [
    ('Lo scambio', 'Ogni gruppo legge i casi dell’altro. Manca un caso ovvio? Uno è ambiguo?'),
    ('I casi di stop', 'Sono davvero situazioni in cui l’agente deve fermarsi? Sono realistici?'),
    ('La risposta attesa', 'È scritta abbastanza bene da dire, dopo, se l’agente ha fatto ok o no?')],
    R('Un caso senza risposta attesa chiara ', 'non misura niente: diventa un’opinione su una risposta.'),
    notes='Cinque minuti di lettura per gruppo. Ogni gruppo può aggiungere un caso suggerito dall’altro. Se a qualcuna mancano risposte attese, le scrive adesso, prima di eseguire.')

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
    ('Chi lo mantiene', 'Owner e co-owner: correggono, aggiornano, decidono le nuove versioni. Se una manca, l’altra basta.')],
    R('Il contratto è per chi lo usa, ', 'non per chi lo costruisce: deve capirlo una collega che non c’era.'),
    notes='Cinque voci, quattro riquadri: input e output stanno insieme. Si parte da contratto.md del modello. La co-owner esiste perché la simulazione ha mostrato che la owner scelta per competenza è spesso la più carica: con due nomi, l’agente non si ferma per una settimana di picco.')

steps('30 minuti di gruppo: la batteria si esegue, si corregge e si riesegue', [
    ('Esegui tutti i casi', 'Senza fermarti a correggere.'),
    ('Segna l’esito', 'ok, fix o fail, con una nota.'),
    ('Correggi', 'Chi ha scritto la parte la corregge. Prima una regola esistente.'),
    ('Riesegui tutto', 'Una correzione può rompere altro.'),
    ('Registra', 'Una riga per caso nel registro Excel.')],
    [R('La regola del coach: ', 'correggere una regola esistente prima di aggiungerne una nuova.'), R('Un core che cresce a ogni errore ', 'torna a essere un prompt lungo.')],
    notes='La owner esegue, la co-owner registra, le altre leggono gli esiti e propongono la correzione sulla loro parte. Riesegui tutto dopo ogni correzione importante: è il punto che si salta. Una regola nuova sul tono può cambiare la risposta a un caso di stop.')

code_slide('Il plugin nasce dal modello, come il coach: si installa, si usa, si aggiorna per versioni', '04_modelli/plugin/  →  plugin <nome-agente>/  v1.0.0',
           'core.md\nskill/\n   <skill-1>/SKILL.md\n   <skill-2>/SKILL.md\n   …\nCONTRACT.md\nCHANGELOG.md     ← cosa cambia a ogni versione\n\nfuori dal plugin, in 05_agenti:\n   casi-prova.md\n   registro-usi.xlsx\n   PROCESSO.md',
           'Cosa si fa oggi', [
               ('Si copia', 'la struttura del plugin dal modello, e ci si mettono core, skill e contratto.'),
               ('L’IT installa', 'il plugin sui Mac del gruppo. Si prova un caso.'),
               ('Versione 1.0.0', 'nel CHANGELOG, con la data e i nomi.'),
               ('Il registro', 'resta fuori dal plugin: è di chi lo usa.')],
           R('Ogni modifica al core ', 'è una nuova versione, con una riga nel CHANGELOG. Così si sa sempre quale agente ha prodotto cosa.'),
           notes='Nella v1 il facilitatore confezionava e installava in aula. Nella v2 la struttura è già pronta in 04_modelli e l’installazione è concordata con l’IT, presente o in remoto per questi 20 minuti. Il facilitatore non diventa l’assistenza tecnica di due agenti.')

cards3('Prima dell’uso reale: tre controlli, più uno', [
    ('Dati', 'L’agente lavora solo su dati che la regola dati della lezione 1 consente. Niente dati personali non necessari.'),
    ('Decisioni', 'Prepara e propone. Su persone non decide e non valuta niente.'),
    ('Azioni', 'Non invia, non pubblica, non modifica senza l’ok di chi lo usa.')],
    R('E il quarto: il DPO ha visto il perimetro dei dati. ', 'Se un controllo non passa, l’agente non va in uso: si corregge o si restringe il compito.'),
    notes='Sono i punti di a04 del coach, ridotti al minimo. Il quarto è il gate del DPO: se il passaggio è avvenuto prima della lezione 1, basta verificare che il perimetro dell’agente stia dentro quanto concordato. Meglio una settimana di ritardo che un uso fuori perimetro.')

rows('Il lavoro dopo il percorso, in minuti: si dichiara oggi, non si scopre alla fine', [
    ('Owner e co-owner', 'Circa un’ora per la v1.1, alla lezione 12 o subito dopo. Poi 15 minuti al mese per leggere il registro e decidere le correzioni.'),
    ('Chi usa l’agente', 'Un minuto per uso, una riga nel registro.'),
    ('Tutte', 'Rimisura: calendario 15/3-9/4 (20 minuti), diario 12-16/4 (cinque giorni, 5 minuti al giorno), incontro lunedì 19/4 (un’ora).'),
    ('Chi vuole fare da docente', 'In coppia, su base volontaria. Se ne parla alla lezione 12, non si decide oggi.')],
    side=('Perché adesso', ['Nella simulazione la sorpresa più amara era alla fine: “quindi il lavoro continua?”.', 'Detto oggi, ognuna può dire di no a una parte, e il gruppo si organizza.']),
    notes='Leggi la tabella e chiedi a ognuna, a voce, se regge. Se una owner dice che non ce la fa, la co-owner diventa owner: si scrive nel contratto oggi.')

cards2('Per lunedì 8: usare l’agente su casi reali e registrare ogni uso', [
    (1, 'Usarlo davvero', '30 minuti', 'Ogni volta che il processo si presenta, si passa dall’agente. Al posto del lavoro che avresti fatto comunque, non in aggiunta.'),
    (2, 'Registrare ogni uso', '1 minuto per uso', 'Una riga in registro-usi.xlsx: data, compito, esito (ok, fix, fail), nota, chi.')],
    [R('Un fail non è un fallimento: ', 'è il dato che serve alla lezione 12 per correggerlo.'), R('Versione minima, 15 minuti: ', 'un uso reale, registrato.')],
    notes='Se il processo non si presenta in settimana, usate i casi di prova come casi reali e annotatelo. Se il DPO non ha ancora dato il via, la settimana si fa sui casi di prova.')

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
        ['p', 'I gruppi scambiano i casi di prova, scrivono il mini-contratto con owner e co-owner, eseguono la batteria in trenta minuti di gruppo, correggono e rieseguono. Poi copiano la struttura del plugin dal modello e lo installano con l’IT. Si chiude con i controlli prima dell’uso reale e con il lavoro dopo il percorso, dichiarato in minuti. A casa l’agente si usa su casi reali e ogni uso si registra in Excel.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Un agente si giudica dall’esito su casi scritti prima, non dall’impressione di una risposta riuscita.'],
            ['Output in aula', 'contratto.md con owner e co-owner, batteria eseguita con esiti registrati, plugin v1.0.0 installato sui Mac del gruppo, impegno dopo il percorso accettato a voce da ognuna.'],
            ['Output per l’8/3', 'registro-usi.xlsx con ogni uso della settimana: data, compito, esito, nota, chi.'],
            ['Segnale che ha funzionato', 'Almeno l’80% dei casi ok dopo la seconda esecuzione, e tutti i casi di stop ok.']]],
        ['h1', 'Prima del 1° marzo'],
        ['b', 'DPO: verifica che il passaggio sia avvenuto e che il perimetro dei dati dei due agenti stia dentro quanto concordato. Se non è avvenuto, l’uso reale aspetta.'],
        ['b', 'IT: concorda 20 minuti (80-100’) per installare i due plugin sui Mac del gruppo, in presenza o in remoto. Fai una prova a secco con il coach la settimana prima.'],
        ['b', 'Controlla che in 04_modelli ci siano la struttura del plugin, contratto.md e registro-usi.xlsx con le colonne data, compito, esito, nota, chi e un menu a tendina per l’esito.'],
        ['b', 'Leggi i due casi-prova.md: segnati i casi di stop deboli.'],
        ['b', 'Avvisa il responsabile per la demo della lezione 12: 30 minuti, l’8 marzo. Concorda la regola: ore liberate per processo, con il consenso della owner, mai per persona.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-10’', 'Ripartenza', 'Slide 3. Scambio dei casi di prova tra gruppi.'],
            ['10-20’', 'Pillola', 'Slide 4. ok, fix, fail. Obiettivo 80%, stop tutti ok.'],
            ['20-35’', 'Contratto', 'Slide 5. contratto.md dal modello, cinque voci, owner e co-owner.'],
            ['35-80’', 'Prove', 'Slide 6. Trenta minuti di gruppo per esecuzione, esiti e correzioni; quindici per la riesecuzione completa.'],
            ['80-100’', 'Plugin', 'Slide 7. Struttura dal modello, installazione con l’IT, CHANGELOG.'],
            ['100-112’', 'Controlli e dopo', 'Slide 8 e 9. I tre controlli più il DPO. Il lavoro dopo il percorso, in minuti: ognuna dice se regge.'],
            ['112-120’', 'Consegna', 'Slide 10, 11 e 12.']]],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Una risposta brillante convince più di dieci casi registrati, ed è il motivo per cui si registrano i casi. L’ammirazione è il rischio specifico di questa lezione: il gruppo ha costruito qualcosa e vuole vederlo funzionare. La batteria scritta prima protegge dal vedere solo quello che si vuole vedere. Il secondo punto è meno tecnico: chi mantiene l’agente lo dice oggi, con i minuti davanti, e può dire di no.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Molti fail alla prima esecuzione', 'Normale. Si guarda se il problema è il core (regola mancante o ambigua), una skill (riga che non scatta) o il caso (risposta attesa irrealistica).'],
            ['Un caso di stop fallisce', 'Si corregge prima di tutto il resto, nel “cosa non fa mai” del core. L’agente non va in uso finché non passa.'],
            ['Il plugin non si installa', 'L’agente si usa per la settimana direttamente dalla cartella in Cowork. L’IT sistema l’installazione prima della lezione 12; tu non fai assistenza tecnica.'],
            ['Una owner dice che non regge il dopo', 'La co-owner diventa owner, e si cerca una nuova co-owner nel gruppo. Si scrive nel contratto oggi.'],
            ['Il gruppo vuole aggiungere funzioni', 'Si annotano nel diario per la v1.1. La v1.0.0 resta piccola.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, i due contratti, le due batterie con gli esiti, i CHANGELOG. Insieme ai diari, sono la traccia completa del processo standard applicato due volte.']]}

CONSEGNA = {
    'title': 'Lezione 11 · Il lavoro per lunedì 8 marzo',
    'subtitle': 'Percorso AI per Talent · 30 minuti nel tuo slot, più 1 minuto per uso · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'un uso reale dell’agente, registrato (15’).']],
        ['h1', '1. Usa l’agente su casi reali (30’)'],
        ['p', 'Per tutta la settimana, ogni volta che il processo si presenta, passa dall’agente al posto del lavoro che avresti fatto a mano. Se il processo non si presenta, usa uno dei casi di prova come se fosse reale e annotalo. Se il gruppo non ha ancora il via libera sui dati, usa solo i casi di prova.'],
        ['h1', '2. Registra ogni uso (1 minuto)'],
        ['p', 'Una riga in registro-usi.xlsx, nella cartella dell’agente. L’esito si sceglie dal menu.'],
        ['table', [1500, 2900, 1300, 2638, 1300], [
            ['data', 'compito', 'esito', 'nota', 'chi'],
            ['02/03/2027', 'conferma docente corso X', 'ok', ' ', 'iniziali'],
            ['03/03/2027', 'convocazione colloquio, ruolo Y', 'fix', 'cosa hai dovuto correggere', ' '],
            [' ', ' ', 'fail', 'cosa ha sbagliato', ' ']]],
        ['h2', 'I controlli, sempre'],
        ['b', 'Dati: solo quelli che la regola dati consente, niente dati personali non necessari.'],
        ['b', 'Decisioni: l’agente prepara e propone, non decide su persone.'],
        ['b', 'Azioni: non invia e non modifica niente senza il tuo ok.'],
        ['h1', 'Cosa porti alla lezione 12'],
        ['b', 'Il registro degli usi della settimana.'],
        ['b', 'Il fail più istruttivo, da raccontare in due minuti.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: il contratto dell’agente con owner e co-owner, la batteria eseguita e corretta, il plugin installato, il lavoro dopo il percorso (un minuto per uso; per owner e co-owner circa un’ora per la v1.1 e 15 minuti al mese). Il passo minimo (20 minuti, prima della lezione 12): leggi contratto.md, chiedi all’IT o alla co-owner di installarti il plugin, usalo una volta e registra l’uso. Se non sei d’accordo con l’impegno dopo il percorso, dillo alla owner prima di lunedì.']]}
