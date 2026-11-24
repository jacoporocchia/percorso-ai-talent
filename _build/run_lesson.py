"""python3 run_lesson.py NN  -> deck, scaletta e consegna in /mnt/project-files/percorso-ai-talent/lezione-NN/"""
import sys, json, subprocess, os
N = int(sys.argv[1])
BASE = '/tmp/claude-0/-home-user/fb6aa437-ef98-50a4-a83e-9179b450ba71/scratchpad'
DIR = '/mnt/project-files/percorso-ai-talent/lezione-%02d' % N
os.makedirs(DIR, exist_ok=True)
OUTDECK = '%s/L%02d-deck-aula.pptx' % (DIR, N)
sys.argv = ['x', '/mnt/project-files/templates/template_TS.pptx', OUTDECK]
exec(open(BASE + '/ts/tslib.py', encoding='utf-8').read())
exec(open(BASE + '/ts/kitfns.py', encoding='utf-8').read())
G = {}
exec(open(BASE + '/ts/lessons/l%02d.py' % N, encoding='utf-8').read())
p.save(OUTDECK)
print('deck', len(p.slides))


def vid_blocks(intro):
    bl = [['h1', 'Per approfondire (facoltativo)' if intro == 'c' else 'Video di approfondimento']]
    if intro == 's':
        bl.append(['p', 'Sono nella penultima slide e nella scheda della consegna. Li ho trovati con una ricerca: prima della lezione aprili e guardane almeno l’inizio, per controllare che il link funzioni e che il tono vada bene per le colleghe.'])
    for (h, d, url, lang) in VIDEOS:
        bl.append(['b', [{'text': h, 'bold': True}, ' · %s · %s ' % (lang, d.rstrip('.') + '.'), url]])
    if EXTRA:
        for (h, url) in EXTRA[1]:
            bl.append(['b', [{'text': h, 'bold': True}, ' · %s. ' % EXTRA[0], url]])
    return bl


for kind, spec in [('scaletta-facilitatore', SCALETTA), ('consegna-colleghe', CONSEGNA)]:
    spec = dict(spec)
    spec['footer'] = 'Percorso AI per Talent · Lezione %d' % N
    if kind.startswith('scaletta'):
        # i video prima di "Cosa entra nel basket" se c'è, altrimenti in coda
        bl = spec['blocks']
        idx = next((i for i, b in enumerate(bl) if b[0] == 'h1' and b[1].startswith('Cosa entra nel basket')), len(bl))
        spec['blocks'] = bl[:idx] + vid_blocks('s') + bl[idx:]
    else:
        bl = spec['blocks']
        idx = next((i for i, b in enumerate(bl) if b[0] == 'h1' and b[1].startswith('Cosa porti')), len(bl))
        spec['blocks'] = bl[:idx] + vid_blocks('c') + bl[idx:]
    jf = '%s/doc/spec_%02d_%s.json' % (BASE, N, kind[:4])
    json.dump(spec, open(jf, 'w', encoding='utf-8'), ensure_ascii=False)
    env = dict(os.environ, NODE_PATH=subprocess.check_output(['npm', 'root', '-g']).decode().strip())
    subprocess.run(['node', BASE + '/doc/kit.js', jf, '%s/L%02d-%s.docx' % (DIR, N, kind)], check=True, env=env)
