import json, subprocess, os
BASE='/tmp/claude-0/-home-user/fb6aa437-ef98-50a4-a83e-9179b450ba71/scratchpad'
spec={'title':'La regola dati del percorso','subtitle':'Percorso AI per Talent · valida dalla lezione 1 · una pagina da tenere accanto al Mac','footer':'Percorso AI per Talent · Regola dati','blocks':[
 ['p','Lavoriamo con dati di persone: candidati, colleghi, partecipanti ai corsi. Claude è uno strumento potente e non distingue un dato personale da un altro testo. La distinzione la facciamo noi, con quattro regole.'],
 ['h1','Le quattro regole'],
 ['table',[2900,6738],[
  ['Regola','Cosa vuol dire in pratica'],
  ['1. Niente account personali','Per dati di lavoro si usa solo il Claude aziendale. ChatGPT, Claude o altri strumenti con il tuo account personale non si usano, nemmeno “per provare”, nemmeno durante le feste.'],
  ['2. Niente dati nominativi','CV, valutazioni, piani di sviluppo, elenchi di neoassunti o di iscritti con nome e cognome non si danno a Claude. Vale anche per gli screenshot e per gli eventi di calendario con nomi di candidati.'],
  ['3. La matricola come chiave','Quando serve riferirsi a una persona, si usa la matricola. Il collegamento tra matricola e nome resta nel sistema di record (gestionale HR, ATS, piattaforma corsi).'],
  ['4. Nel dubbio, chiedi il metodo','Claude scrive la formula, i passi di Power Query, il modello di mail con i campi da riempire. Tu li applichi in Excel o in Outlook sui dati veri. Excel conta, Claude ragiona.']]],
 ['h1','Cosa si può fare, per esempio'],
 ['b','Confrontare due elenchi di iscrizioni con la matricola al posto del nome, oppure farsi scrivere la formula e applicarla in Excel.'],
 ['b','Scrivere una job description, un annuncio, una mail tipo con i campi [NOME] e [DATA] da riempire a mano.'],
 ['b','Sintetizzare una survey anonima, dopo aver tolto i commenti che nominano persone.'],
 ['b','Preparare una checklist di screening o una scorecard vuota: le usa e le compila una persona, non Claude.'],
 ['h1','Cosa non si fa'],
 ['b','Chiedere a Claude di valutare, confrontare o classificare candidati o colleghi. Per l’AI Act sono attività ad alto rischio: l’AI prepara, decide un umano, e i dati delle persone non entrano.'],
 ['b','Caricare un export intero “per comodità” quando bastano poche colonne senza nomi.'],
 ['h1','Se lo hai già fatto'],
 ['p','Non è una colpa: fino a oggi nessuno lo aveva scritto. Dillo a Max a fine lezione o in privato. Insieme vedete cosa smettere, cosa fare al posto, e cosa fare dei dati già caricati.']]}
jf=BASE+'/doc/spec_regola.json'; json.dump(spec,open(jf,'w',encoding='utf-8'),ensure_ascii=False)
env=dict(os.environ,NODE_PATH=subprocess.check_output(['npm','root','-g']).decode().strip())
subprocess.run(['node',BASE+'/doc/kit.js',jf,'/mnt/project-files/percorso-ai-talent/lezione-01/L01-regola-dati.docx'],check=True,env=env)
