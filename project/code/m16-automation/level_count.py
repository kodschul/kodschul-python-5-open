# Admin-Skript im Kleinen: zählt die Stufen INFO/WARN/ERROR in allen *.log eines Ordners
# Start im Ordner project/: python code/m16-automation/level_count.py data
# Exit-Code: 0 = keine ERROR-Zeile, 1 = ERROR-Zeilen gefunden oder nichts zu prüfen

import argparse
import re
import sys
from pathlib import Path

# Datum, Uhrzeit, dann die Stufe als Gruppe: "2026-11-08 08:05:22 ERROR ..."
LINE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} [\d:]+ (?P<level>[A-Z]+) ")

# 1. Argumente
parser = argparse.ArgumentParser(description="Zählt Log-Stufen in *.log-Dateien.")
parser.add_argument("folder", type=Path, help="Ordner mit .log-Dateien")
args = parser.parse_args()

# 2. Dateien finden
paths = sorted(args.folder.glob("*.log"))  # nur dieser Ordner, ohne Unterordner
if not paths:
    print(f"Keine .log-Dateien in {args.folder}")
    sys.exit(1)

# 3. Zeilen auswerten
counts = {}
for path in paths:
    with open(path, encoding="utf-8") as file:
        for line in file:
            match = LINE_PATTERN.search(line)
            if match is not None:
                level = match.group("level")
                counts[level] = counts.get(level, 0) + 1

# 4. Bericht
print(f"Ordner {args.folder}, Log-Dateien: {len(paths)}")
for level in sorted(counts):
    print(f"  {level}: {counts[level]}")

# 5. Exit-Code: Ein Zeitplaner oder ein anderes Skript erkennt so ein Problem
if counts.get("ERROR", 0) > 0:
    print("Ergebnis: ERROR-Zeilen gefunden")
    sys.exit(1)
print("Ergebnis: alles in Ordnung")
