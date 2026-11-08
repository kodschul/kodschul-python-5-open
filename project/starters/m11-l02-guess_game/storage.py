# Zahlenraten – Starter für Lab 11.2 (Stand nach Lab 11.1)
# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import csv
import json
from pathlib import Path

from guess_game import logic

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
HIGHSCORES_FILE = Path("highscores.json")
HISTORY_FILE = Path("history.csv")
HISTORY_COLUMNS = ["Datum", "Name", "Stufe", "Versuche", "Dauer", "gewonnen"]


class Scoreboard:
    """Bestenliste: hält Score-Objekte und speichert sie in einer JSON-Datei."""

    def __init__(self, path=HIGHSCORES_FILE):
        self.path = path
        self.scores = self.load()  # beim Erzeugen einmal aus der Datei laden

    def load(self):
        """Liest die JSON-Datei und gibt eine Liste von Score-Objekten zurück."""
        if not self.path.exists():  # erster Start: noch keine Datei
            return []
        with open(self.path, encoding="utf-8") as file:
            data = json.load(file)  # Liste von Dictionaries
        scores = []
        for item in data:
            score = logic.Score(
                item["name"],
                item["level"],
                item["tries"],
                item["seconds"],
                item["won"],
                item["date"],
            )
            scores.append(score)
        return scores

    # TODO Lab 11.2: save() wandelt jeden Score mit asdict(score) um
    def save(self):
        """Schreibt alle Ergebnisse als JSON in die Datei."""
        data = []
        for score in self.scores:
            data.append(score.to_dict())  # JSON kennt keine Score-Objekte
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def add(self, score):
        """Fügt ein Score-Objekt hinzu und speichert sofort."""
        self.scores.append(score)
        self.save()

    def top_five(self):
        """Gibt die fünf besten Ergebnisse zurück."""
        return sorted(self.scores)[:5]  # sorted vergleicht mit Score.__lt__


def append_history(score):
    """Hängt jede Runde, ob gewonnen oder nicht, als Zeile an history.csv an."""
    is_new = not HISTORY_FILE.exists()  # Kopfzeile nur beim ersten Mal
    row = {
        "Datum": score.date,
        "Name": score.name,
        "Stufe": score.level,
        "Versuche": score.tries,
        "Dauer": str(score.seconds).replace(".", ","),  # Komma für deutsches Excel
        "gewonnen": "ja" if score.won else "nein",
    }
    # newline="": das csv-Modul setzt die Zeilenenden selbst
    # utf-8-sig: Excel erkennt so die Umlaute
    with open(HISTORY_FILE, "a", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HISTORY_COLUMNS, delimiter=";")
        if is_new:
            writer.writeheader()
        writer.writerow(row)
