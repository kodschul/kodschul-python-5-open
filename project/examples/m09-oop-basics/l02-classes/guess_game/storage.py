# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import csv
import json
from pathlib import Path

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
HIGHSCORES_FILE = Path("highscores.json")
HISTORY_FILE = Path("history.csv")
HISTORY_COLUMNS = ["Datum", "Name", "Stufe", "Versuche", "Dauer", "gewonnen"]


def load_highscores():
    """Gibt alle gespeicherten Ergebnisse als Liste von Dictionaries zurück."""
    if not HIGHSCORES_FILE.exists():  # erster Start: noch keine Datei
        return []
    with open(HIGHSCORES_FILE, encoding="utf-8") as file:
        return json.load(file)


def save_highscore(result):
    """Fügt ein Ergebnis zur Bestenliste hinzu und speichert sie als JSON."""
    scores = load_highscores()
    scores.append(result)
    with open(HIGHSCORES_FILE, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=2, ensure_ascii=False)


def get_tries(score):
    """Sortierschlüssel: die Anzahl der Versuche eines Ergebnisses."""
    return score["tries"]


def top_five():
    """Gibt die fünf Ergebnisse mit den wenigsten Versuchen zurück."""
    scores = load_highscores()
    return sorted(scores, key=get_tries)[:5]  # Funktion als Schlüssel, ohne ()


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
