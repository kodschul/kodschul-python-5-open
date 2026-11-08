# Zahlenraten – Starter für Lab 8.3 (Stand nach Lab 8.2)
# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import json
from pathlib import Path

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
HIGHSCORES_FILE = Path("highscores.json")
# TODO Lab 8.3: HISTORY_FILE und HISTORY_COLUMNS für history.csv festlegen


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


# TODO Lab 8.3: append_history(result) hängt jede Runde an history.csv an
