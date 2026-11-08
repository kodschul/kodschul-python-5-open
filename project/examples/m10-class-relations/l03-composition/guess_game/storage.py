# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import csv
import json
from pathlib import Path

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
HIGHSCORES_FILE = Path("highscores.json")
HISTORY_FILE = Path("history.csv")
HISTORY_COLUMNS = ["Datum", "Name", "Stufe", "Versuche", "Dauer", "gewonnen"]


def get_tries(score):
    """Sortierschlüssel: die Anzahl der Versuche eines Ergebnisses."""
    return score["tries"]


class Scoreboard:
    """Bestenliste: hält alle Ergebnisse und speichert sie in einer JSON-Datei."""

    def __init__(self, path=HIGHSCORES_FILE):
        self.path = path
        self.scores = self.load()  # beim Erzeugen einmal aus der Datei laden

    def load(self):
        """Gibt alle gespeicherten Ergebnisse als Liste von Dictionaries zurück."""
        if not self.path.exists():  # erster Start: noch keine Datei
            return []
        with open(self.path, encoding="utf-8") as file:
            return json.load(file)

    def save(self):
        """Schreibt alle Ergebnisse als JSON in die Datei."""
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.scores, file, indent=2, ensure_ascii=False)

    def add(self, result):
        """Fügt ein Ergebnis hinzu und speichert sofort."""
        self.scores.append(result)
        self.save()

    def top_five(self):
        """Gibt die fünf Ergebnisse mit den wenigsten Versuchen zurück."""
        return sorted(self.scores, key=get_tries)[:5]


def append_history(result):
    """Hängt jede Runde, ob gewonnen oder nicht, als Zeile an history.csv an."""
    is_new = not HISTORY_FILE.exists()  # Kopfzeile nur beim ersten Mal
    row = {
        "Datum": result["date"],
        "Name": result["name"],
        "Stufe": result["level"],
        "Versuche": result["tries"],
        "Dauer": str(result["seconds"]).replace(".", ","),  # Komma für deutsches Excel
        "gewonnen": "ja" if result["won"] else "nein",
    }
    # newline="": das csv-Modul setzt die Zeilenenden selbst
    # utf-8-sig: Excel erkennt so die Umlaute
    with open(HISTORY_FILE, "a", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HISTORY_COLUMNS, delimiter=";")
        if is_new:
            writer.writeheader()
        writer.writerow(row)
