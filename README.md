# FreeGEOS Test

**Systeminformation und Vorführung des FreeGEOS-SDK** – geschrieben in GOC/C für FreeGEOS (PC/GEOS 2.x und neuer).

FreeGEOS Test liest aus, auf welchem Rechner oder Emulator FreeGEOS läuft (DOSBox, Basebox, 86Box, QEMU …), zeigt alles auf zehn Seiten an, speichert, kopiert und druckt den Bericht und führt dabei vor, was mit dem FreeGEOS-SDK möglich ist.

Es ist die FreeGEOS-Ausgabe von *GeoWorks 1.x Test* (GWTEST.GEO) für GeoWorks Ensemble 1.2.

## Seiten

| Taste | Seite | Inhalt |
|---|---|---|
| 1 | Übersicht | Rechner/Emulator, Prozessor, Speicher, Grafik, Versionen, Datum |
| 2 | System | CPU (auch CPUID), Koprozessor, BIOS-Kennung, Emulator, Schnittstellen, DOS |
| 3 | Speicher | INT 12h, CMOS, INT 15h, XMS, EMS, GEOS-Speicherverwaltung |
| 4 | Bildschirm | GEOS-Bildschirmtreiber, VESA-BIOS, Auflösung, Farbtiefe |
| 5 | GEOS | Kernel-/UI-Version, Verzeichnis, Oberfläche, Geräte aus der GEOS.INI |
| 6 | Leistung | Schleifen/s, Geschwindigkeitsindex, Gleitkomma, Grafik, Speicher, Datei – mit Animation |
| 7 | Grafik | 16 Farben, RGB-Verläufe, Formen, Muster, Schriften, gedrehter Text, Bitmaps 1/4/24 Bit |
| 8 | Eingabe | Tastencodes, Maus, Mausrad, Malfläche (eigene Vis-Klasse mit Mausgriff) |
| 9 | Schriften | alle Schriften mit Datei, ID, Art (Bitmap/Nimbus/TrueType) und Muster |
| 0 | Klang | Ton, Tonleiter, Melodie, Akkord über die Sound-Bibliothek |

Weitere Tasten: N/P blättern, Pfeile, +/-, Mausrad rollen, M messen, S speichern, K kopieren, H/?/F1 Hilfe, I Info, Esc Übersicht.

## Vorgeführte SDK-Teile

- eigene Vis-Klasse mit Mausgriff in einer GenView, skaliert auf die Fenstergröße, mit Rollbalken
- GenPrimary mit Menüs, Info-Dialog mit Logo, Programmsymbole aus einem PCX
- PrintControl (mehrseitiger Bericht), Zwischenablage, Datei-Ein-/Ausgabe
- GEOS.INI, Laendereinstellungen (`LocalFormatDateTime`, `LocalGetNumericFormat`)
- `GrEnumFonts`, Bitmap-Größen aus den `.FNT`-Dateien, TrueType-Namen aus den `.TTF`-Dateien
- Sound-Bibliothek (`SoundAllocMusic`), Math-Bibliothek, Timer
- echte FreeGEOS-Hilfe (Kontexte je Seite), alle Texte in einer Ressource für den ResEdit
- BIOS-, DOS-, VESA-, XMS- und EMS-Abfragen, CPUID per Watcom `#pragma aux`

## Installation

`fertig/gtsfree.geo` (oder die Fehlerprüf-Version `gtsfreeec.geo`) in den Ordner `WORLD` der FreeGEOS-Installation kopieren. Gebaut gegen FreeGEOS CI-latest (Nov. 2026).

## Bauen

Mit dem FreeGEOS-SDK aus [bluewaysw/pcgeos](https://github.com/bluewaysw/pcgeos):

```
copy GTSFree %LOCAL_ROOT%\Appl\GTSFree
cd %LOCAL_ROOT%\Appl\GTSFree
mkmf
pmake                (gtsfreeec.geo)
pmake gtsfree.geo    (normale Version)
```

`GTSFree/gtsfree.goc` ist im GEOS-Zeichensatz (Mac Roman) gespeichert. Zum Lesen und Bearbeiten liegt dieselbe Datei in UTF-8 unter `quelle-utf8/`; `tools/to_geos.sh` wandelt sie zurück.

## Ordner

| Ordner | Inhalt |
|---|---|
| `GTSFree/` | Projekt für das SDK (gtsfree.goc, gtsfree.gp, Icons, Logo) |
| `quelle-utf8/` | Quelltext in UTF-8 |
| `fertig/` | fertige gtsfree.geo und gtsfreeec.geo |
| `hilfe/` | Vorschlag für die Hilfedatei „FGTest Hilfe“ mit allen Kontexten |
| `icon/` | Programmsymbol GTS1ICON.PCX |
| `tools/` | pcx2goc.py (PCX → GEOS-Moniker), to_geos.sh |

Ausführliche Beschreibung: [LIESMICH.TXT](LIESMICH.TXT)

## Kennung

Token `GTSF`, Hersteller-ID 16506.

## Lizenz

MIT – © 2026 by Möllerjaner, Johannes Möller, Syhra
