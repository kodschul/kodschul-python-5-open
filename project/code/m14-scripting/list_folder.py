# Inhalt eines Ordners mit Name, Endung, Größe und Datum auflisten (nur lesen)

from datetime import datetime
from pathlib import Path

folder = Path("data/messy_downloads")

for path in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
    if path.is_dir():
        print(f"[Ordner] {path.name}/")
        continue
    info = path.stat()  # Angaben des Betriebssystems zur Datei
    changed = datetime.fromtimestamp(info.st_mtime)  # Sekunden -> Datum
    print(
        f"{path.name} | Endung: {path.suffix} | {info.st_size} Bytes"
        f" | geändert {changed.strftime('%d.%m.%Y')}"
    )
