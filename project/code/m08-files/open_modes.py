# open() mit den Modi "w" (schreiben), "a" (anhängen) und "r" (lesen)

from pathlib import Path

shopping_file = Path("playground") / "shopping.txt"

# "w": Datei neu schreiben; ein vorhandener Inhalt wird gelöscht
with open(shopping_file, "w", encoding="utf-8") as file:
    file.write("Milch\n")  # \n = Zeilenumbruch, write setzt keinen selbst
    file.write("Brot\n")

# "a": hinten anhängen; der bisherige Inhalt bleibt
with open(shopping_file, "a", encoding="utf-8") as file:
    file.write("Käse\n")

# "r": lesen (Standard, darf fehlen); Zeile für Zeile mit for
with open(shopping_file, encoding="utf-8") as file:
    for line in file:
        print("Zeile:", line.strip())  # strip entfernt den Zeilenumbruch

# read: alles auf einmal; readlines: Liste aller Zeilen
with open(shopping_file, encoding="utf-8") as file:
    lines = file.readlines()
print("readlines:", lines)

# Datei fehlt: FileNotFoundError abfangen (try/except aus Lab 7.2)
try:
    with open(Path("playground") / "gibt_es_nicht.txt", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError as error:
    print("Fehler:", error)
