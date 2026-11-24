#!/bin/sh
# UTF-8-Quelle in den GEOS-Zeichensatz (Mac Roman) wandeln
iconv -f UTF-8 -t MACINTOSH ../quelle-utf8/gtsfree.goc > ../GTSFree/gtsfree.goc
