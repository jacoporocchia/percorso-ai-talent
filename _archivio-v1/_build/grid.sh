#!/bin/bash
# grid.sh NN -> ts/gNN.jpg  (slide 2..penultima)
N=$1; D=/mnt/project-files/percorso-ai-talent/lezione-$N
cd /tmp/claude-0/-home-user/6bc0d0f6-e1c3-52f7-92ec-9fb486a20c2c/scratchpad/ts
rm -f gg-*; soffice --headless --convert-to pdf $D/L$N-deck-aula.pptx >/dev/null 2>&1 && pdftoppm -r 45 -jpeg L$N-deck-aula.pdf gg && python3 -c "
from PIL import Image; import glob
fs=sorted(glob.glob('gg-*.jpg'))[1:-1]
ims=[Image.open(f) for f in fs]; w,h=ims[0].size; r=(len(ims)+1)//2
g=Image.new('RGB',(w*2,h*r),'white')
for k,im in enumerate(ims): g.paste(im,((k%2)*w,(k//2)*h))
g.save('g$N.jpg')"
