cover('Lezione 5 · Dati e struttura', 'Lunedì 18 gennaio 2027')

agenda('Oggi i dati di Talent trovano un posto solo, a partire da quelli che servono all’agente', [
    ('0-15’', 'Il test', 'Cinque file da trovare, un minuto ciascuno'),
    ('15-30’', 'Pillola', 'Fonte unica contro copia, e quattro convenzioni'),
    ('30-50’', 'Struttura', 'La proposta, con al più due modifiche'),
    ('50-105’', 'Laboratorio', 'Le fonti nell’agente, i duplicati del tuo tema'),
    ('105-120’', 'Consegna', 'Migrare o indicizzare un tema vero')],
    'la struttura condivisa di Talent in uso, la cartella fonti del tuo agente già dentro, e un tempo di ricerca da battere lunedì prossimo.',
    notes='È il blocco dati in una lezione sola, dove la v1 ne usava due. Nella simulazione il blocco dati di tre settimane era il punto in cui tutte e tre le colleghe smettevano di fare le consegne vere: troppo lento per chi corre, rischioso per chi lavora sui fondi, estraneo per chi fa recruiting. Qui ogni minuto sui dati è un minuto sull’agente o sul lavoro reale.')

rows('Il test dei cinque file: un minuto ciascuno, cronometro alla mano', [
    ('Cinque richieste', 'Tu leggi una richiesta reale alla volta: “trovami l’ultima versione di…”. Una è di Talent Acquisition.'),
    ('Un minuto', 'Ognuna cerca dove cercherebbe davvero. Si ferma allo scadere.'),
    ('Si annota', 'Trovato sì o no, in quanto tempo, ed è la versione giusta?'),
    ('Si ripete', 'Lunedì prossimo, sulla struttura nuova. Stesse richieste.')],
    side=('Perché misuriamo', ['È il secondo KPI del percorso: un dato si trova in meno di un minuto.', 'I risultati restano in aula. Il punto è il sistema, non la persona.']),
    notes='Le cinque richieste le prepari tu, su file reali di Talent: almeno una di Talent Acquisition (per esempio il template JD in uso, il kit del career day). Con cinque persone anche un dato aggregato è riconoscibile: annota solo quante su cinque, in media, e non scriverlo nella demo al responsabile.')

cards3('Un dato vive in un solo posto: altrove si mette un link, non una copia', [
    ('La copia diverge', 'Appena qualcuno corregge l’originale, la copia è vecchia. E nessuno glielo dice.'),
    ('La copia non sa di esserlo', 'Un file “_def_v3” sembra l’ultimo. Lo era, forse, il giorno in cui è stato salvato.'),
    ('Ogni copia ha una ragione', 'Lavorarci senza disturbare, mandarla a qualcuno, tenerla per sicurezza. Nasce bene e muore dimenticata.')],
    R('Ricordi la lezione 1? ', 'Claude aveva fatto bene i conti sul file sbagliato. Il problema non era Claude, era la copia.'),
    notes='“Ogni copia nasce con una buona ragione” è la frase che toglie la colpa: nella simulazione è quella che apre al cambiamento la collega più esperta. Fonte unica non vuol dire un solo file per tutto: per ogni dato c’è un posto che fa fede, gli altri puntano lì.')

cards4('Quattro convenzioni bastano, se le rispettano tutte', [
    ('Il nome', 'AAAA-MM-GG_argomento. Si ordina da solo e si legge senza aprirlo.'),
    ('Niente “def” o “v3”', 'Le versioni le tiene lo strumento: la cronologia di OneDrive e SharePoint.'),
    ('Un LEGGIMI', 'Tre righe per cartella: cosa contiene, chi ne risponde, da dove arrivano i dati.'),
    ('Link, non copia', 'Se serve altrove, si mette il collegamento al file che fa fede.')],
    R('La cronologia delle versioni ', 'è già nel file: tasto destro, Cronologia versioni. Si torna indietro senza tenere copie.'),
    notes='Mostra dal vivo la cronologia delle versioni su un file condiviso: è la cosa che rende inutili le copie “per sicurezza”. Mostra anche come si copia un link di condivisione: nella simulazione “link, non copia” diventava una copia della scorciatoia.')

code_slide('La struttura: sette cartelle, già pronte sul tuo Mac', 'Talent/  (cartella condivisa del team)',
           '00_LEGGIMI.md       regole, conservazione, chi risponde\n01_fonti/           dati originali, sola lettura\n02_lavoro/<progetto>/  elaborazioni in corso\n03_output/          deliverable consegnati\n04_modelli/         template, file modello, skill\n05_agenti/<nome>/   fonti, core, skill, prove\n99_archivio/        chiuso, non si modifica\n\ncoach-<nome>/       sul tuo Mac, privata',
           'Oggi decidiamo poco, apposta', [
               ('Al più due modifiche:', 'una sottocartella in più, un nome diverso.'),
               ('Un owner per cartella,', 'scelto per tempo, con la sua conferma.'),
               ('Il 00_LEGGIMI', 'è già scritto: lo leggiamo ad alta voce e lo correggiamo.'),
               ('Si rivede alla lezione 12,', 'con un mese d’uso alle spalle.')],
           R('È già sincronizzata sul tuo Mac ', 'e visibile in Cowork: l’ha preparata l’IT. Se non la vedi, dillo adesso.'),
           notes='Nella simulazione la discussione sui nomi si mangiava mezz’ora. Qui la proposta si adotta con al più due modifiche. Facilita, ma tieni il tempo: 20 minuti in tutto, compresa la lettura del 00_LEGGIMI.')

cards3('Cosa non entra, e cosa entra solo come indice', [
    ('Dati di persone', 'Candidati e dipendenti restano nel gestionale, nell’ATS, nella piattaforma. Nella struttura solo con la matricola, per uno scopo dichiarato.'),
    ('Documenti vincolati', 'Rendicontazione dei fondi, documenti inviati a enti esterni: non si spostano e non si rinominano. Si indicizzano: LEGGIMI e link.'),
    ('La tua istanza del coach', 'Resta sul tuo Mac. Nella struttura entra solo quello che scegli di portare.')],
    R('Nessuna copia si cancella ', 'senza la owner della cartella e senza la regola di conservazione scritta nel 00_LEGGIMI.'),
    notes='Il punto sui documenti vincolati viene dalla simulazione: per chi lavora sui fondi, rinominare rompe i collegamenti tra Excel e cancellare “dopo un mese” va contro la conservazione. L’indice è la soluzione: il documento resta dov’è, la struttura sa dove trovarlo.')

steps('Laboratorio, parte 1: le fonti di ogni agente entrano nella sua cartella', [
    ('La cartella', '05_agenti/<nome-agente>/, dal modello in 04_modelli.'),
    ('L’elenco', 'Quello della settimana: documento, posizione, perché serve.'),
    ('Le fonti', 'In fonti/: link o copia unica del file che fa fede.'),
    ('Da pulire', 'I documenti con dati personali: si tolgono i nomi o restano fuori.'),
    ('Il LEGGIMI', 'Tre righe, dal modello.')],
    [R('Venti minuti, in gruppo. ', 'È la fase 1 del processo standard, anticipata: la lezione 8 parte da qui.'), R('Se un documento è vincolato, ', 'in fonti/ va il link, non il file.')],
    notes='Nella v1 le fonti restavano in una cartella temporanea fino alla lezione 9, ed erano finite in zip via mail. Qui il blocco dati lavora per l’agente.')

prompt_slide('Laboratorio, parte 2: la caccia ai duplicati sul tema che usi davvero', 'Il prompt, in Cowork sulla cartella del tuo tema',
             '“Guarda la cartella che ti ho dato. Elenca i file con nome, data di modifica e dimensione. Raggruppa quelli che sembrano lo stesso documento in versioni diverse. Segnala gli Excel con collegamenti ad altri file. Non spostare, non rinominare, non cancellare niente.”',
             'Poi decidi tu', 'Per ogni gruppo: quale è la versione vera? Claude propone, ma solo tu sai quale file è stato mandato al responsabile o al fondo.',
             'Il tuo tema, per esempio', [
                 ('Il template JD', 'e gli annunci'), ('I modelli', 'di convocazione'), ('I materiali', 'di onboarding'), ('Il kit', 'del career day')],
             foot='Un tema che usi ogni settimana, non uno a caso: è quello che migrerai.',
             notes='Il criterio è il lavoro che va fatto comunque. Nella simulazione il tema “a scelta” (la formazione 2026) produceva mappe fatte in fretta e migrazioni mai fatte; il tema usato ogni settimana si migra perché conviene.')

prompt_slide('Migrare: prima la proposta, poi lo spostamento, e niente si cancella subito', 'Il prompt, per la consegna',
             '“Ti ho dato la cartella del mio tema e la struttura Talent. Proponimi dove va ogni file, con il nome AAAA-MM-GG_argomento. Le copie che non sono la versione vera vanno in _copie-da-eliminare. Non toccare i file che ti indico come vincolati. Fammi vedere la proposta prima di spostare qualsiasi cosa.”',
             'Prima di dire ok', 'Negli Excel: Dati, Modifica collegamenti. Se un file ne ha, spostarlo li rompe: tienilo dov’è e indicizzalo.',
             'Due strade', [
                 ('Migrare', 'il tema libero'), ('Indicizzare', 'il vincolato'), ('LEGGIMI', 'in entrambi i casi'), ('Il test', 'lo trovi in 1 minuto?')],
             foot='Spostare file è un’azione: Claude la fa solo dopo il tuo ok.',
             notes='La regola “prima la proposta, poi l’azione” è la stessa della lezione 2 (prima la tabella, poi i conti). Il controllo dei collegamenti esterni viene dalla simulazione: è il punto in cui la migrazione rompe davvero qualcosa.')

cards2('Per lunedì 25: il tuo tema, migrato o indicizzato', [
    (1, 'Migra o indicizza', '35 minuti', 'Il tema di oggi. Versione vera nel posto giusto, copie in _copie-da-eliminare, link dove serviva la copia. Se è vincolato, solo indice.'),
    (2, 'Il LEGGIMI', '10 minuti', 'Dal modello in 04_modelli: cosa contiene, chi ne risponde, da dove arrivano i dati.')],
    [R('Settimana piena? ', 'Versione minima da 15: LEGGIMI e indice, senza spostare niente.'), R('E il diario? ', 'Se questa è la tua settimana, continua: due momenti al giorno.')],
    notes='Il test di reperibilità di lunedì prossimo si fa sulla struttura. Chi fa la versione minima vede comunque la differenza, perché l’indice è nella struttura.')

VIDEOS = [
    ('Come organizzo i file sul computer', 'Cinque regole per non perdere nulla.', 'https://www.youtube.com/watch?v=qzUO7GeIUjg', 'italiano'),
    ('Pillola Agile: la Prima Direttiva', 'Lavorare in gruppo su regole comuni partendo dalla fiducia.', 'https://www.youtube.com/watch?v=45w_LYaF4iQ', 'italiano'),
    ('The PARA method', 'Un sistema per organizzare file per progetti, aree, risorse, archivio.', 'https://www.youtube.com/watch?v=s8-wJ1RxWmY', 'inglese, sottotitoli'),
    ('Organize your Google Drive with PARA', 'La stessa logica su un drive condiviso.', 'https://www.youtube.com/watch?v=Txkn35XwwR4', 'inglese, sottotitoli')]
EXTRA = None
links('Per approfondire: organizzare i file perché si trovino', VIDEOS)

closing('Quante copie hai trovato del file che pensavi unico?', 'Prossima lezione: lunedì 25 gennaio')

SCALETTA = {
    'title': 'Lezione 5 · Dati e struttura',
    'subtitle': 'Scaletta del facilitatore · lunedì 18 gennaio 2027 · 2 ore · 5 colleghe',
    'blocks': [
        ['h1', 'In una riga'],
        ['p', 'Si apre e si chiude il blocco dati in una lezione. Le colleghe misurano quanto ci mettono a trovare cinque file reali, capiscono perché la copia è il nemico, adottano la struttura condivisa già pronta con al più due modifiche, portano le fonti di ogni agente nella sua cartella e contano i duplicati di un tema che usano davvero. A casa lo migrano, o lo indicizzano se è vincolato.'],
        ['h1', 'Obiettivi della lezione'],
        ['table', [2600, 7038], [
            ['Comportamento', 'Prima di salvare un file, chiedersi se esiste già e se basta un link. Prima di spostare un file, chiedersi se qualcosa ci punta.'],
            ['Output in aula', 'Base del test dei cinque file. Struttura condivisa adottata, con owner per cartella e 00_LEGGIMI riletto. Cartella fonti di ogni agente in 05_agenti. Duplicati contati sul proprio tema.'],
            ['Output per il 25/1', 'Il proprio tema migrato nella struttura, o indicizzato se vincolato, con il suo LEGGIMI.'],
            ['Segnale che ha funzionato', 'Ognuna trova almeno un documento con più di due copie e sa dire quale fa fede. Le due cartelle degli agenti hanno fonti e LEGGIMI.']]],
        ['h1', 'Prima del 18 gennaio'],
        ['b', [{'text': 'Struttura pronta, dall’IT. ', 'bold': True}, 'La cartella condivisa Talent con le sette cartelle, i permessi per le cinque, sincronizzata su tutti i Mac e visibile in Cowork. Nella v1 il setup si faceva in aula e chi era assente restava fuori dalla struttura per tutto il blocco.']],
        ['b', [{'text': 'Il 00_LEGGIMI già scritto, ', 'bold': True}, 'con il prompt sotto, comprese la regola di conservazione e la regola sui documenti vincolati. In aula si legge e si corregge, non si scrive.']],
        ['b', [{'text': 'I file modello in 04_modelli: ', 'bold': True}, 'LEGGIMI, cartella agente (fonti, core, casi di prova, revisione, registro usi in Excel).']],
        ['b', [{'text': 'Le cinque richieste del test. ', 'bold': True}, 'File reali che tutte dovrebbero saper trovare, almeno uno di Talent Acquisition: l’ultimo calendario corsi, il template JD in uso, il budget formazione, il kit del career day, una procedura. Tienile identiche per la lezione 6.']],
        ['b', 'Un caso reale per la caccia ai duplicati da mostrare tu: una cartella in cui sai che ci sono copie.'],
        ['b', 'Chi è nella settimana del diario: chiedilo in chat, per non caricare troppo quella settimana.'],
        ['h1', 'La scaletta'],
        ['table', [1250, 2300, 6088], [
            ['Tempo', 'Blocco', 'Cosa fai'],
            ['0-15’', 'Il test dei cinque file', 'Slide 3. Leggi una richiesta alla volta, cronometro un minuto. Ognuna annota trovato, tempo, versione giusta. Raccogli solo il dato aggregato, che resta in aula.'],
            ['15-30’', 'Pillola', 'Slide 4 e 5. Fonte unica contro copia, con il richiamo alla lezione 1 e “ogni copia nasce con una buona ragione”. Le quattro convenzioni, con la demo della cronologia delle versioni e di un link di condivisione.'],
            ['30-50’', 'La struttura', 'Slide 6 e 7. La proposta già pronta: al più due modifiche, un owner per cartella con la sua conferma, lettura ad alta voce del 00_LEGGIMI. Cosa non entra e i documenti vincolati.'],
            ['50-70’', 'Le fonti nell’agente', 'Slide 8. In gruppo: cartella dell’agente dal modello, fonti dall’elenco della settimana, LEGGIMI. I documenti da pulire si puliscono o restano fuori.'],
            ['70-105’', 'Caccia ai duplicati', 'Slide 9 e 10. Prima la tua demo su una cartella reale, poi ognuna sul suo tema. Elenco con Claude, giudizio loro, controllo dei collegamenti. Chi finisce presto avvia la proposta di migrazione e si ferma prima di dire ok.'],
            ['105-120’', 'Consegna', 'Slide 11, 12 e 13. Ognuna scrive in chat il suo tema e se lo migra o lo indicizza.']]],
        ['h1', 'Il prompt per il 00_LEGGIMI (da preparare prima)'],
        ['quote', 'Scrivi il file 00_LEGGIMI.md della cartella condivisa del team Talent, in una pagina. Contiene: a cosa serve ogni cartella, chi ne risponde, le quattro regole (nomi AAAA-MM-GG_argomento, niente def o v3, LEGGIMI di tre righe in ogni sottocartella, link e non copia), cosa non entra (dati personali di candidati e dipendenti, se non con la matricola e per uno scopo dichiarato), i documenti vincolati che si indicizzano e non si spostano (rendicontazione dei fondi, documenti inviati a enti esterni), la regola di conservazione (nessuna copia si cancella senza la owner della cartella), chi può scrivere in 01_fonti e chi svuota 99_archivio. Usa solo le decisioni che ti scrivo qui sotto, senza aggiungerne.'],
        ['h1', 'Il punto da far arrivare'],
        ['p', 'Il problema dei dati non è tecnico. Ogni copia nasce con una buona ragione e muore senza che nessuno se ne accorga. Una struttura condivisa funziona solo se rende il link più comodo della copia, e se serve a qualcosa subito: per questo oggi entrano per prime le fonti degli agenti e i temi che le colleghe usano ogni settimana.'],
        ['h1', 'Se qualcosa va storto'],
        ['table', [3300, 6338], [
            ['Situazione', 'Cosa fai'],
            ['Una collega non vede la cartella condivisa in Cowork', 'Lavora sul suo tema in locale per la caccia ai duplicati e tu segnali all’IT. La migrazione la fa a casa, quando la cartella è visibile. Non perdere tempo d’aula sul setup.'],
            ['Il gruppo vuole riprogettare la struttura', 'Al più due modifiche oggi. Il resto si annota e si rivede alla lezione 12, con un mese d’uso.'],
            ['Claude propone di cancellare o spostare', 'Ripeti nel prompt “non spostare, non cancellare niente”. Lo spostamento si fa dopo la proposta e dopo il tuo ok.'],
            ['Il tema di una collega è tutto vincolato (fondi)', 'Indicizza: LEGGIMI e link nella struttura, i file restano dove sono. È una consegna completa, non una scorciatoia.'],
            ['Emergono file con dati personali in posti sbagliati (per esempio CV in Download)', 'Annotali senza aprirli in aula. Restano fuori dalla struttura; per i CV vale la risposta concordata con il DPO.'],
            ['Il test mette in imbarazzo qualcuno', 'I risultati sono aggregati e restano in aula. Il punto è il sistema, non la persona.']]],
        ['h1', 'Cosa entra nel basket'],
        ['p', 'Il deck, la scheda della consegna, la struttura e il 00_LEGGIMI finali (sono già un modello per altri team), i prompt della caccia ai duplicati e della migrazione, il format del test dei cinque file (senza le richieste reali), la registrazione della pillola.']]}

CONSEGNA = {
    'title': 'Lezione 5 · Il lavoro per lunedì 25 gennaio',
    'subtitle': 'Percorso AI per Talent · 45 minuti nel tuo slot · versione minima: 15 minuti',
    'blocks': [
        ['p', [{'text': 'Settimana piena? Fai la versione minima: ', 'bold': True}, 'il LEGGIMI del tuo tema e un indice dei file con i link, senza spostare niente (15’).']],
        ['h1', '1. Migra o indicizza il tuo tema (35’)'],
        ['p', 'È il tema su cui hai fatto la caccia ai duplicati: uno che usi ogni settimana. Prima di tutto, decidi la strada.'],
        ['table', [2600, 7038], [
            ['Se il tema è…', 'Allora'],
            ['Libero (template, modelli, materiali)', 'Lo migri nella struttura con il prompt qui sotto.'],
            ['Vincolato (rendicontazione fondi, documenti inviati a enti esterni) o con Excel collegati tra loro', 'Lo indicizzi: i file restano dove sono, nella struttura metti il LEGGIMI e i link.']]],
        ['p', 'Per migrare, in Cowork dai a Claude la cartella del tema e la struttura Talent:'],
        ['quote', 'Ti ho dato la cartella del mio tema e la struttura Talent. Proponimi dove va ogni file, con il nome AAAA-MM-GG_argomento. Le copie che non sono la versione vera vanno in _copie-da-eliminare. Non toccare i file che ti indico come vincolati. Fammi vedere la proposta prima di spostare qualsiasi cosa.'],
        ['b', 'Prima di dire ok, apri gli Excel del tema: Dati, Modifica collegamenti. Se un file ne ha, tienilo dov’è e mettilo nell’indice.'],
        ['b', 'Controlla la proposta riga per riga, poi dai l’ok.'],
        ['b', 'Dove prima serviva una copia, metti un link al file vero (tasto destro, Copia link).'],
        ['b', 'Le copie restano in _copie-da-eliminare: si cancellano solo con l’ok della owner della cartella.'],
        ['b', 'Niente dati personali di candidati o dipendenti: restano nei sistemi di record.'],
        ['h1', '2. Il LEGGIMI (10’)'],
        ['p', 'Copia il modello LEGGIMI da 04_modelli nella cartella del tuo tema e compila le tre righe: cosa contiene, chi ne risponde, da dove arrivano i dati.'],
        ['h1', 'Prima di finire'],
        ['p', 'Cerca un file del tema nella struttura, come se non sapessi dov’è. Lo trovi in meno di un minuto? Annota il tempo.'],
        ['h1', 'Cosa porti alla lezione 6'],
        ['b', 'Il tema migrato o indicizzato, con il suo LEGGIMI.'],
        ['b', 'Quante copie sono finite in _copie-da-eliminare, e il tempo del tuo test.'],
        ['h1', 'Se hai saltato la lezione'],
        ['p', 'Le decisioni prese: la struttura Talent con le sue due modifiche, l’owner di ogni cartella, il 00_LEGGIMI, la cartella del tuo agente in 05_agenti con le fonti. Il passo minimo (20 minuti): apri la cartella Talent in Cowork (se non la vedi, scrivi a Max: la sistema l’IT, non tu), leggi il 00_LEGGIMI, guarda la cartella del tuo agente e fai la caccia ai duplicati sul tuo tema con il prompt della slide 9. La tua buddy ti dice quali sono le due modifiche e chi è owner di cosa. Nessuna cartella ti viene assegnata senza che tu lo confermi.']]}
