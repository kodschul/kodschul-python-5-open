# Ältere Wege, die in vielen Skripten stehen: os.path und shutil

import os
import shutil
from pathlib import Path

folder = "data/messy_downloads"

# os.path: Pfade sind Strings, jede Aufgabe ist eine eigene Funktion
file = os.path.join(folder, "notizen.txt")
print("os.path.join:   ", file)
print("os.path.exists: ", os.path.exists(file))
print("os.path.getsize:", os.path.getsize(file), "Bytes")
print("os.listdir:     ", len(os.listdir(folder)), "Einträge")

# pathlib: dasselbe mit einem Path-Objekt
path = Path(folder) / "notizen.txt"
print("Path / ...:     ", path)
print("path.exists():  ", path.exists())
print("stat().st_size: ", path.stat().st_size, "Bytes")
print("iterdir():      ", len(list(Path(folder).iterdir())), "Einträge")

# shutil.make_archive: ZIP eines ganzen Ordners (dafür gibt es keine Path-Methode)
archive = shutil.make_archive("playground/messy_downloads_backup", "zip", folder)
print("ZIP erstellt:   ", Path(archive).name)
