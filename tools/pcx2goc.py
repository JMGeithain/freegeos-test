#!/usr/bin/env python3
"""GTS1ICON.PCX (48x30, 16 Farben, Magenta = durchsichtig) -> GEOS-Bitmaps.
Erzeugt GTSFree/gtsicon.goh (Moniker) und GTSFree/gtsicon.h (C-Feld).
Aufruf:  python3 pcx2goc.py ../icon/GTS1ICON.PCX ../GTSFree"""
import sys
from PIL import Image

GEOS = [(0,0,0),(0,0,170),(0,170,0),(0,170,170),(170,0,0),(170,0,170),(170,85,0),
        (170,170,170),(85,85,85),(85,85,255),(85,255,85),(85,255,255),(255,85,85),
        (255,85,255),(255,255,85),(255,255,255)]

def near(c):
    return min(range(16), key=lambda i: sum((a-b)**2 for a,b in zip(c,GEOS[i])))

def bitmap(im):
    """4 Bit + Maske, unkomprimiert: je Zeile Maske, dann Pixel"""
    w,h = im.size
    out=[]
    for y in range(h):
        idx=[near(im.getpixel((x,y))) for x in range(w)]
        mask=[0 if i==13 else 1 for i in idx]
        for x in range(0,w,8):
            b=0
            for k in range(8):
                if x+k<w and mask[x+k]: b|=0x80>>k
            out.append(b)
        for x in range(0,w,2):
            a=idx[x] if mask[x] else 0
            b=(idx[x+1] if mask[x+1] else 0) if x+1<w else 0
            out.append((a<<4)|b)
    return out

def fmt(d, ind='\t\t'):
    return ',\n'.join(ind+', '.join('0x%02x'%v for v in d[i:i+16]) for i in range(0,len(d),16))

def moniker(name, size, style, w, h, d, note=''):
    return ('%s@visMoniker %s = {\n    size = %s;\n    style = %s;\n    aspectRatio = normal;\n'
            '    color = color4;\n    cachedSize = %d, %d;\n    gstring {\n'
            '\tGSDrawBitmapAtCP(%d),\n\tBitmap(%d, %d, BMC_UNCOMPACTED, (BMF_4BIT | BMT_MASK)),\n'
            '%s,\n\tGSEndString()\n    }\n}\n\n') % (note, name, size, style, w, h, len(d)+6, w, h, fmt(d))

src, dst = sys.argv[1], sys.argv[2]
big = Image.open(src).convert('RGB')
small = big.resize((32,20), Image.NEAREST)
mini = Image.new('RGB', (15,15), GEOS[13])
mini.paste(big.crop((1,0,47,30)).resize((15,10), Image.NEAREST), (0,2))

L, S, M = bitmap(big), bitmap(small), bitmap(mini)
with open(dst + '/gtsicon.goh', 'w') as f:
    f.write('/* Erzeugt von tools/pcx2goc.py aus icon/GTS1ICON.PCX */\n\n')
    f.write(moniker('GTLargeIconMoniker', 'large', 'icon', 48, 30, L))
    f.write(moniker('GTSmallIconMoniker', 'tiny', 'icon', 32, 20, S))
    f.write(moniker('GTMiniIconMoniker', 'tiny', 'tool', 15, 15, M,
        '/* Mini-Icon 15x15 - VORLAEUFIG aus dem PCX verkleinert.\n'
        ' * Im Icon-Editor neu zeichnen und diesen Moniker ersetzen. */\n'))
hdr = [48,0,30,0,0,0x11] + L
with open(dst + '/gtsicon.h', 'w') as f:
    f.write('/* Programmsymbol 48x30 als Bitmap (4 Bit + Maske) fuer GrDrawBitmap */\n')
    f.write('static const byte iconBitmap[%d] = {\n%s\n};\n' % (len(hdr), fmt(hdr, '    ')))
