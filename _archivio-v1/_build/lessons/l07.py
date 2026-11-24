cover('Lezione 7 · Claude sui dati ordinati', 'Lunedì 1° febbraio 2027')

agenda('Oggi rifacciamo il confronto della lezione 1, sulla cartella ordinata', [
    ('0-15’', 'Il test', 'Gli stessi cinque file, sulla struttura nuova'),
    ('15-30’', 'Pillola', 'Claude vede solo ciò che gli dai'),
    ('30-55’', 'Demo', 'Lo stesso confronto, due mesi dopo'),
    ('55-105’', 'Laboratorio', 'Chiedere bene, verificare, cosa non caricare'),
    ('105-120’', 'Consegna', 'Un compito reale con nota sugli errori')],
    'un prompt in quattro pezzi, un metodo di verifica, e la regola su cosa non dare a Claude.',
    notes='Chiude il blocco B. Il messaggio: la struttura non serve all’ordine, serve a dare a Claude, e alle persone, il dato giusto.')

rows('Il test dei cinque file, rifatto: stesse richieste, struttura nuova', [
    ('Stesse richieste', 'Le cinque della lezione 5, lette nello stesso ordine.'),
    ('Un minuto', 'Cronometro. Si cerca nella struttura condivisa.'),
    ('Il confronto', 'Quante trovate in tempo, prima e adesso.'),
    ('Cosa non ha funzionato', 'Se un file non si trova, la regola che manca va nel 00_LEGGIMI.')],
    side=('Il KPI del blocco B', ['Test di reperibilità: un file si trova in meno di un minuto.', 'Risultato aggregato, come alla lezione 5. Il punto è il sistema.']),
    notes='Se qualche richiesta riguarda temi non ancora migrati, dillo: il test misura la parte migrata. Annota cosa cambia nel 00_LEGGIMI.')

cards3('Claude vede solo ciò che gli dai, e la scrivania è piccola: la struttura decide cosa gli dai', [
    ('Vede solo il contesto', 'Se il file giusto non è nella cartella che gli dai, per lui non esiste. Come il DEF_v3 della lezione 1.'),
    ('La scrivania ha un limite', 'Circa 200.000 token. Una cartella disordinata la riempie di copie e versioni inutili.'),
    ('Il LEGGIMI è contesto', 'Tre righe che dicono cosa c’è e da dove arriva: Claude le legge come le leggi tu.')],
    R('Una cartella ordinata è il prompt migliore: ', 'meno da spiegare, meno da indovinare, meno da sbagliare.'),
    notes='Richiama la token economy della lezione 1: due Excel da 60 MB. Oggi il rimedio non è solo ridurre, è avere una fonte sola.')

compare('Lo stesso confronto, due mesi dopo: cambia la cartella, non Claude', (
    'Lezione 1', FUX, ['Tre file con nomi ambigui, il giusto arrivato per mail', 'Colonne in ordine diverso, intestazioni diverse', 'Nomi scritti in tre modi, un duplicato, una data come testo', 'Nessuna chiave: si confronta per nome']), (
    'Oggi', BLU, ['Un file per mese in 01_fonti/formazione', 'Stesse colonne, stesso ordine, nomi AAAA-MM-GG', 'Matricola come chiave, nomi puliti, nessun duplicato', 'Un LEGGIMI che dice da dove arrivano i dati']),
    [R('Il prompt è quasi lo stesso. ', 'La differenza la fa la cartella: Claude trova 4 cancellati, 6 nuovi, 1 cambio corso.'), R('Ma si verifica comunque: ', 'il tono era sicuro anche quando sbagliava.')],
    notes='Usa la cartella demo/Talent-demo della lezione 7. La chiave è nel file CHIAVE_lezione7. Dopo la risposta, fate insieme le tre domande della lezione 1: questa volta reggono.')

cards4('Un buon prompt ha quattro pezzi', [
    ('Contesto', 'Dove sono i dati e cosa sono: “nella cartella 01_fonti/formazione, export mensili”.'),
    ('Compito', 'Cosa deve fare, con un verbo: confronta, elenca, riassumi.'),
    ('Formato', 'Come vuoi il risultato: una tabella con queste colonne, tre righe, un file.'),
    ('Verifica', 'Come lo controllerai: “per ogni numero, dimmi da quali righe viene”.')],
    R('Il quarto pezzo è quello che manca quasi sempre. ', 'Chiederlo nel prompt cambia la risposta, non solo il controllo.'),
    notes='Fai scrivere a ognuna un prompt in quattro pezzi per un compito della settimana. Leggetene due ad alta voce.')

steps('Verificare è un metodo, non un sospetto', [
    ('Le tre domande', 'Da dove viene? Cosa non hai verificato? Quali casi sono dubbi?'),
    ('Un campione', 'Cinque righe controllate a mano.'),
    ('Un ricalcolo', 'Un totale rifatto in Excel.'),
    ('I casi limite', 'Il primo, l’ultimo, il più strano.')],
    [R('Quanto verificare dipende dal costo dell’errore: ', 'una bozza di mail meno, un numero che va al responsabile di più.'), R('È la matrice della lezione 4, ', 'applicata a ogni singola risposta.')],
    notes='Il ricalcolo in Excel è la verifica più robusta per i numeri: Excel conta, Claude ragiona, come nella lezione 1.')

cards4('Cosa non si dà a Claude, nemmeno sulla struttura ordinata', [
    ('Dati di persone', 'Candidati e dipendenti non anonimizzati: restano nei sistemi di record.'),
    ('Dati particolari', 'Salute, provvedimenti disciplinari, sindacato: mai.'),
    ('Documenti riservati', 'Di altri team o della direzione, se non sono tuoi da usare.'),
    ('Credenziali', 'Password, codici di accesso, chiavi: mai, in nessun prompt.')],
    R('La policy aziendale vince su questa slide. ', 'Se c’è un dubbio, il dato non si carica e si chiede.'),
    notes='Se l’azienda ha una policy sull’uso dell’AI generativa, citala qui e aggiungi le regole specifiche. Le quattro categorie sono il minimo.')

cards2('Per lunedì 8: un compito reale, partendo dalla struttura, con nota sugli errori', [
    (1, 'Un compito reale', '20 minuti', 'Uno che dovevi fare comunque. Parti da un file della struttura condivisa, con un prompt in quattro pezzi.'),
    (2, 'La nota sugli errori', '10 minuti', 'Dove ha sbagliato Claude, come te ne sei accorta, cosa hai cambiato nel prompt o nei dati.')],
    [R('Se non ha sbagliato niente: ', 'scrivi come hai verificato. Anche questo è un risultato.'), R('Tempo totale: ', 'circa 30 minuti.')],
    notes='Le note sugli errori sono l’apertura della lezione 8: le classificheremo insieme.')

VIDEOS = [
    ('Pericoli e limiti dell’intelligenza artificiale', 'Enkk sui limiti dei modelli, senza allarmismi.', 'https://www.youtube.com/watch?v=Yg4dgh6FU3Y', 'italiano'),
    ('Le allucinazioni dell’AI', 'Perché un modello inventa, e come accorgersene.', 'https://www.youtube.com/watch?v=mrP6P_1bSRg', 'italiano'),
    ('Le allucinazioni non sono ciò che pensi', 'Un punto di vista diverso sullo stesso fenomeno.', 'https://www.youtube.com/watch?v=Q3-TSh32WqI', 'italiano'),
    ('Deep Dive into LLMs like ChatGPT', 'Karpathy: la parte su token e contesto, per chi vuole il motore.', 'https://www.youtube.com/watch?v=7xTGNNLPyMI', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: perché i modelli sbagliano, e come accorgersene', VIDEOS)

closing('Cosa hai smesso di dare a Claude da quando c’è la struttura?', 'Prossima lezione: lunedì 8 febbraio')

SCALETTA = {
    'title': 'Lezione 7 · Claude sui dati ordinati',
    'subtitle': 'Scaletta del facilitatore · lunedì 1° febbraio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Le colleghe rifanno il test dei cinque file sulla struttura nuova e vedono lo stesso confronto della lezione 1 funzionare su una cartella ordinata. Poi imparano il prompt in quattro pezzi, un metodo di verifica proporzionato al costo dell’errore e cosa non si dà mai a Claude. Chiude il blocco B.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Dare a Claude la fonte giusta e dire nel prompt come si verificherà la risposta.'],
            ['Output in aula', 'Risultato del test dei cinque file, secondo giro. Un prompt in quattro pezzi per un compito reale.'],
            ['Output per l’8/2', 'Un compito reale fatto partendo dalla struttura, con una nota su dove Claude ha sbagliato e come se ne sono accorte.'],
            ['Segnale che ha funzionato', 'Il test dei cinque file migliora rispetto alla lezione 5 sulla parte migrata.']]],
        ['h1', 'Prima del 1° febbraio'],
        ['b', 'Le cinque richieste della lezione 5, identiche.'],
        ['b', 'La cartella demo/Talent-demo di questa lezione copiata in un posto da cui la apri in Cowork. La chiave è in demo/CHIAVE_lezione7_solo_facilitatore.txt.'],
        ['b', 'Prova il prompt della demo: deve trovare 4 cancellati, 6 nuovi, 1 cambio corso, ore da 324 a 356.'],
        ['b', 'Se l’azienda ha una policy sull’uso dell’AI generativa, aggiungine i punti specifici alla slide 8.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Il test, secondo giro', 'Slide 3. Stesse cinque richieste, un minuto ciascuna. Confronto aggregato con la lezione 5.'],
            ['15-30’', 'Pillola', 'Slide 4. Contesto, scrivania, LEGGIMI come contesto.'],
            ['30-55’', 'Demo', 'Slide 5. Il prompt della demo sulla cartella ordinata. Poi le tre domande della lezione 1: questa volta reggono. Mostra la differenza con la lezione 1.'],
            ['55-80’', 'Chiedere bene', 'Slide 6. Ognuna scrive un prompt in quattro pezzi per un compito della settimana e lo prova sulla struttura. Due letti ad alta voce.'],
            ['80-95’', 'Verificare', 'Slide 7. Sul risultato appena ottenuto: le tre domande, un campione, un ricalcolo, i casi limite.'],
            ['95-105’', 'Cosa non caricare', 'Slide 8. Quattro categorie e la policy aziendale.'],
            ['105-120’', 'Consegna', 'Slide 9, 10 e 11.']]],
        ['h1', 'Il prompt della demo'],
        ['quote', 'Nella cartella 01_fonti/formazione ci sono gli export mensili delle iscrizioni ai corsi, uno per mese, con la matricola come chiave (vedi il LEGGIMI). Confronta ottobre e novembre: dimmi chi si è aggiunto, chi è stato cancellato, chi ha cambiato corso e di quante ore è cambiato il piano. Rispondi con una tabella per ciascun gruppo. Per ogni numero dimmi da quali righe viene.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['La demo sbaglia anche sulla cartella ordinata', 'È un’ottima demo: le tre domande e il ricalcolo in Excel lo trovano. Il messaggio regge: si verifica sempre.'],
            ['Il test dei cinque file non migliora', 'Guardate perché: tema non migrato, nome poco chiaro, LEGGIMI mancante. Ogni causa diventa una regola nel 00_LEGGIMI.'],
            ['Una collega carica dati personali per il laboratorio', 'Fermala con calma: si usa un estratto anonimo o un altro compito.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda, la cartella demo strutturata con la chiave, il prompt della demo, la slide su cosa non caricare (con la policy aziendale), la registrazione di pillola e demo. È il modulo più riusabile del percorso per altri team.']]}

CONSEGNA = {
    'title': 'Lezione 7 · Il lavoro per lunedì 8 febbraio',
    'subtitle': 'Percorso AI per Talent · tempo stimato: circa 30 minuti',
    'blocks': [
        ['h1', '1. Un compito reale (20’)'],
        ['p', 'Scegli un compito che dovevi fare comunque questa settimana. Parti da un file della struttura condivisa e scrivi un prompt in quattro pezzi:'],
        ['n', 'Contesto: dove sono i dati e cosa sono.'],
        ['n', 'Compito: cosa deve fare, con un verbo.'],
        ['n', 'Formato: come vuoi il risultato.'],
        ['n', 'Verifica: “per ogni numero, dimmi da quali righe viene”, o l’equivalente per il tuo compito.'],
        ['h1', '2. La nota sugli errori (10’)'],
        ['table', [3200, 3219, 3219], [
            ['Dove ha sbagliato Claude', 'Come me ne sono accorta', 'Cosa ho cambiato (prompt o dati)'],
            [' ', ' ', ' '], [' ', ' ', ' ']]],
        ['p', 'Se non ha sbagliato niente, scrivi come hai verificato: anche questo è un risultato.'],
        ['h1', 'Cosa non dare mai a Claude'],
        ['b', 'Dati di candidati e dipendenti non anonimizzati.'],
        ['b', 'Dati particolari: salute, provvedimenti disciplinari, appartenenza sindacale.'],
        ['b', 'Documenti riservati che non sono tuoi da usare.'],
        ['b', 'Password e credenziali.'],
        ['h1', 'Cosa porti alla lezione 8'],
        ['b', 'La nota sugli errori.'],
        ['b', 'Il prompt che hai usato.']]}
