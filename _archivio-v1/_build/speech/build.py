"""python3 build.py NN -> L{NN}-speech.docx da speech/sNN.txt
Markup: '# ' sezione (h1), '## ' slide (h2), '> ' indicazione di regia (quote), riga vuota separa i paragrafi."""
import sys, json, subprocess, os, re
N = int(sys.argv[1])
BASE = '/tmp/claude-0/-home-user/6bc0d0f6-e1c3-52f7-92ec-9fb486a20c2c/scratchpad'
src = open('%s/speech/s%02d.txt' % (BASE, N), encoding='utf-8').read()
head, body = src.split('\n===\n', 1)
meta = dict(l.split(': ', 1) for l in head.strip().splitlines())
blocks = [['h1', 'Come usare questo testo'],
          ['p', 'È il parlato delle parti frontali, scritto per essere detto ad alta voce, slide per slide. Non va letto parola per parola: leggilo un paio di volte prima della lezione e in aula tieni d’occhio la prima frase di ogni paragrafo, che porta il punto. Il resto è appoggio. Le righe in blu sono indicazioni di regia: cosa fai, non cosa dici. I tempi seguono la scaletta del facilitatore.']]
para = []
def flush():
    if para:
        blocks.append(['p', ' '.join(para)]); para.clear()
for line in body.splitlines():
    l = line.rstrip()
    if not l:
        flush(); continue
    if l.startswith('## '): flush(); blocks.append(['h2', l[3:]])
    elif l.startswith('# '): flush(); blocks.append(['h1', l[2:]])
    elif l.startswith('> '): flush(); blocks.append(['quote', l[2:]])
    else: para.append(l.strip())
flush()
words = sum(len(b[1].split()) for b in blocks if b[0] == 'p')
spec = {'title': 'Lezione %d · %s' % (N, meta['titolo']),
        'subtitle': 'Speech del facilitatore · %s · circa %d parole parlate' % (meta['data'], round(words, -2)),
        'blocks': blocks, 'footer': 'Percorso AI per Talent · Lezione %d · Speech' % N}
jf = '%s/speech/spec_%02d.json' % (BASE, N)
json.dump(spec, open(jf, 'w', encoding='utf-8'), ensure_ascii=False)
out = '/mnt/project-files/percorso-ai-talent/lezione-%02d/L%02d-speech.docx' % (N, N)
env = dict(os.environ, NODE_PATH=subprocess.check_output(['npm', 'root', '-g']).decode().strip())
subprocess.run(['node', BASE + '/doc/kit.js', jf, out], check=True, env=env)
print(out, words, 'parole')
