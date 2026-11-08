# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

from pathlib import Path

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
SCORES_FILE = Path("scores.txt")


def append_score(result):
    """Hängt ein Ergebnis als Zeile „Name;Versuche;Sekunden;Datum“ an scores.txt an."""
    line = f"{result['name']};{result['tries']};{result['seconds']};{result['date']}\n"
    # "a": anhängen; gibt es die Datei noch nicht, wird sie angelegt
    with open(SCORES_FILE, "a", encoding="utf-8") as file:
        file.write(line)
