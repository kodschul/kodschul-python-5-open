# Namensliste aus data/names.txt lesen, aufräumen und sortiert speichern

from pathlib import Path

source = Path("data") / "names.txt"
target = Path("playground") / "names_sorted.txt"

names = []
with open(source, encoding="utf-8") as file:
    for line in file:
        name = line.strip().title()  # Leerzeichen weg, groß beginnen
        if name != "":  # leere Zeilen überspringen
            names.append(name)

names.sort()

with open(target, "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

print(f"{len(names)} Namen gelesen:", names)
print("Sortiert gespeichert in", target)
