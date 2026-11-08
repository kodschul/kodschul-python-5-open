# Ordnerbaum anzeigen: python code/m14-scripting/show_tree.py <ordner>

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Aufruf: python code/m14-scripting/show_tree.py <ordner>")
    sys.exit(1)

folder = Path(sys.argv[1])
print(f"{folder.name}/")
# alle Einträge auf allen Ebenen, alphabetisch ohne Rücksicht auf Groß/klein
for path in sorted(folder.rglob("*"), key=lambda p: str(p).lower()):
    if path.name.startswith("."):
        continue  # versteckte Dateien wie .DS_Store weglassen
    depth = len(path.relative_to(folder).parts)  # 1 = direkt im Ordner
    name = path.name
    if path.is_dir():
        name += "/"
    print("    " * depth + name)
