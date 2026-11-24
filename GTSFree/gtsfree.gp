##############################################################################
#
#  PROJEKT:   FreeGEOS Test 1.0
#             FreeGEOS-Ausgabe von "GeoWorks 1.x Test" (GWTEST.GEO)
#  DATEI:     gtsfree.gp  -  Geode-Parameter fuer den GLUE-Linker
#
##############################################################################

name     gtsfree.app
longname "FreeGEOS Test"

# Kennung GTSF mit eigener Hersteller-ID 16506 (Programm und Icon)
tokenchars "GTSF"
tokenid    16506

type   appl, process, single
class  GTProcessClass
appobj GTApp

heapspace 8000
stack     4000

library geos
library ui
library ansic
library text
library spool
library math
library sound

resource AppResource  ui-object
resource Interface    ui-object
resource Content      object
resource ICONRESOURCE ui-object
resource StringsUI    lmem read-only shared

export GTContentClass
export GTPageClass
