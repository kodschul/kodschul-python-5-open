# Zahlenraten – Starter für Lab 13.2 (Stand nach Lab 13.1)
# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import csv
import json
from dataclasses import asdict
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

    # TODO Lab 13.2: __enter__ lädt die Datei, __exit__ speichert (Context Manager)

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

    def save(self):
        """Schreibt alle Ergebnisse als JSON in die Datei."""
        data = []
        for score in self.scores:
            data.append(asdict(score))  # Dataclass -> Dictionary für JSON
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def add(self, score):
        """Fügt ein Score-Objekt hinzu und speichert sofort."""
        self.scores.append(score)
        # TODO Lab 13.2: nicht mehr sofort speichern, das erledigt __exit__
        self.save()

    def top(self, by="versuche", count=5):
        """Gibt die besten Ergebnisse zurück: nach Versuchen, Zeit oder Punkten."""
        if by == "zeit":
            ranked = sorted(self.scores, key=lambda score: score.seconds)
        elif by == "punkte":
            ranked = sorted(self.scores, key=lambda score: score.points(), reverse=True)
        else:  # "versuche": sorted vergleicht mit Score.__lt__
            ranked = sorted(self.scores)
        return ranked[:count]


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
