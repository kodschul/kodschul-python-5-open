# Dateien per Muster finden: glob nur im Ordner, rglob auch in allen Unterordnern

from pathlib import Path

folder = Path("data/messy_downloads")

print('glob("*.csv"):')
for path in sorted(folder.glob("*.csv")):  # * = beliebige Zeichen
    print("  ", path)

print('rglob("*.csv"):')
for path in sorted(folder.rglob("*.csv")):  # r = rekursiv, alle Ebenen
    print("  ", path)

total = sum(path.stat().st_size for path in folder.rglob("*") if path.is_file())
print("Alle Dateien zusammen:", total, "Bytes")
