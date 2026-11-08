# Testkopie anlegen: data/messy_downloads/ -> playground/messy_downloads/
# Beliebig oft startbar: eine alte Kopie wird vorher gelöscht.

import shutil
from pathlib import Path

SOURCE = Path("data/messy_downloads")  # Original der Kursdaten: nur lesen
TARGET = Path("playground/messy_downloads")  # hier darf aufgeräumt werden

if TARGET.exists():
    shutil.rmtree(TARGET)  # alte Kopie samt Inhalt löschen
SOURCE.copy(TARGET)  # seit Python 3.14: kopiert den ganzen Ordner
files = [path for path in TARGET.rglob("*") if path.is_file()]
print(f"Testkopie angelegt: {TARGET} (Dateien: {len(files)})")
