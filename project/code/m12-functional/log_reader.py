# Große Log-Datei Zeile für Zeile verarbeiten: nur eine Zeile liegt im Speicher

from pathlib import Path

LOG_FILE = Path("data/sample.log")  # Start im Ordner project/


def read_lines(path):
    """Generator: liefert die Zeilen einer Datei einzeln, ohne Zeilenumbruch."""
    with open(path, encoding="utf-8") as file:
        for line in file:  # die Datei selbst liest auch nur Zeile für Zeile
            yield line.rstrip("\n")  # rstrip: Zeilenumbruch rechts entfernen


def only_level(lines, level):
    """Generator: lässt nur Zeilen mit der gewünschten Stufe durch."""
    for line in lines:
        if line.split(" ")[2] == level:  # Datum, Uhrzeit, Stufe, Text
            yield line


errors = only_level(read_lines(LOG_FILE), "ERROR")  # noch nichts gelesen
print("Erste zwei Fehler:")
print(" ", next(errors))
print(" ", next(errors))
rest = sum(1 for line in errors)  # Generator-Ausdruck zählt den Rest
print("Weitere Fehler:", rest)
