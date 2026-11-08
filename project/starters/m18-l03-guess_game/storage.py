# Zahlenraten – Starter für Lab 18.3 (Stand nach Lab 18.2)
# Speichern: Ergebnisse in Dateien im aktuellen Ordner ablegen

import csv
import json
import pickle
import shutil
import sqlite3
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from guess_game import logic

# relativer Pfad: die Datei landet im Ordner, in dem das Spiel startet
HIGHSCORES_FILE = Path("highscores.json")
HISTORY_FILE = Path("history.csv")
DB_FILE = Path("game.db")  # SQLite: Bestenliste und alle Runden in einer Datei
HISTORY_COLUMNS = ["Datum", "Name", "Stufe", "Versuche", "Dauer", "gewonnen"]
SAVEGAME_FILE = Path("savegame.pkl")  # laufendes Spiel, Befehl speichern
BACKUP_DIR = Path("backups")  # ein Unterordner pro Backup, z. B. 2026-11-08_1530


class Scoreboard:
    """Bestenliste als Context Manager: with lädt die Datei und speichert sie."""

    def __init__(self, path=HIGHSCORES_FILE):
        self.path = Path(path)  # erlaubt "highscores.json" und Path(...)
        self.scores = []

    def __enter__(self):
        """Beginn des with-Blocks: Datei laden; das Objekt wird zu "as board"."""
        self.scores = self.load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Ende des with-Blocks: immer speichern, auch nach Fehler oder Strg+C."""
        self.save()
        return False  # Fehler nicht verschlucken, sondern weiterreichen

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
        """Fügt ein Score-Objekt hinzu; gespeichert wird am Ende des with-Blocks."""
        self.scores.append(score)

    def top(self, by="versuche", count=5):
        """Gibt die besten Ergebnisse zurück: nach Versuchen, Zeit oder Punkten."""
        if by == "zeit":
            ranked = sorted(self.scores, key=lambda score: score.seconds)
        elif by == "punkte":
            ranked = sorted(self.scores, key=lambda score: score.points(), reverse=True)
        else:  # "versuche": sorted vergleicht mit Score.__lt__
            ranked = sorted(self.scores)
        return ranked[:count]


# Tabelle scores = Bestenliste (wie highscores.json), nur Gewinne
# Tabelle rounds = jede Runde (wie history.csv), auch verlorene
# IF NOT EXISTS: beim ersten Start anlegen, danach nichts tun
CREATE_SCORES = """
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    tries INTEGER NOT NULL,
    seconds REAL NOT NULL,
    won INTEGER NOT NULL,
    date TEXT NOT NULL
)
"""
CREATE_ROUNDS = """
CREATE TABLE IF NOT EXISTS rounds (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    tries INTEGER NOT NULL,
    seconds REAL NOT NULL,
    won INTEGER NOT NULL,
    date TEXT NOT NULL
)
"""

# ? = Platzhalter: sqlite3 setzt die Werte sicher ein (nie f-Strings in SQL)
INSERT_SCORE = """
INSERT INTO scores (name, level, tries, seconds, won, date)
VALUES (?, ?, ?, ?, ?, ?)
"""
INSERT_ROUND = """
INSERT INTO rounds (name, level, tries, seconds, won, date)
VALUES (?, ?, ?, ?, ?, ?)
"""

# TODO Lab 18.3: TOP_QUERIES (ORDER BY ... LIMIT ?) und LEVEL_STATS (GROUP BY level)


def score_values(score):
    """Gibt die Werte eines Scores als Tupel in der Reihenfolge der Spalten zurück."""
    return (score.name, score.level, score.tries, score.seconds, score.won, score.date)


class SqliteScoreboard:
    """Bestenliste in SQLite, gleiche Schnittstelle wie Scoreboard.

    with lädt, add() speichert, top() sortiert, scores enthält alle Gewinne.
    Neu: add_round() speichert jede Runde in der Tabelle rounds.
    """

    def __init__(self, path=DB_FILE):
        self.path = Path(path)
        self.connection = None  # Verbindung entsteht erst in __enter__
        self.scores = []

    def __enter__(self):
        """Beginn des with-Blocks: Datenbank öffnen, Tabellen anlegen, laden."""
        self.connection = sqlite3.connect(self.path)  # legt game.db notfalls an
        self.connection.row_factory = sqlite3.Row  # Zeilen mit Spaltennamen
        self.connection.execute(CREATE_SCORES)
        self.connection.execute(CREATE_ROUNDS)
        self.connection.commit()
        self.scores = self.load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Ende des with-Blocks: Verbindung schließen (gespeichert ist schon)."""
        self.connection.close()
        return False  # Fehler nicht verschlucken, sondern weiterreichen

    def load(self):
        """Liest alle Zeilen der Tabelle scores als Liste von Score-Objekten."""
        rows = self.connection.execute("SELECT * FROM scores").fetchall()
        scores = []
        for row in rows:  # row["name"] dank row_factory = sqlite3.Row
            score = logic.Score(
                row["name"],
                row["level"],
                row["tries"],
                row["seconds"],
                bool(row["won"]),  # SQLite speichert True als 1
                row["date"],
            )
            scores.append(score)
        return scores

    def add(self, score):
        """Speichert einen Gewinn sofort in der Tabelle scores."""
        self.scores.append(score)
        self.connection.execute(INSERT_SCORE, score_values(score))
        self.connection.commit()  # erst jetzt steht die Zeile sicher in game.db

    def add_round(self, score):
        """Speichert eine Runde, ob gewonnen oder nicht, in der Tabelle rounds."""
        self.connection.execute(INSERT_ROUND, score_values(score))
        self.connection.commit()

    # TODO Lab 18.3: add_many(scores) mit executemany (für migrate_json.py)
    # TODO Lab 18.3: top() mit count=10; versuche/zeit per SQL, punkte weiter per Python
    def top(self, by="versuche", count=5):
        """Gibt die besten Ergebnisse zurück: nach Versuchen, Zeit oder Punkten."""
        if by == "zeit":
            ranked = sorted(self.scores, key=lambda score: score.seconds)
        elif by == "punkte":
            ranked = sorted(self.scores, key=lambda score: score.points(), reverse=True)
        else:  # "versuche": sorted vergleicht mit Score.__lt__
            ranked = sorted(self.scores)
        return ranked[:count]

    # TODO Lab 18.3: level_stats() führt LEVEL_STATS aus


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


def save_game(game, path=SAVEGAME_FILE):
    """Speichert das laufende Game-Objekt mit pickle (Binärdatei: "wb")."""
    with open(path, "wb") as file:
        pickle.dump(game, file)  # Objekt -> Bytes, samt Player und Tipps


def load_game(path=SAVEGAME_FILE):
    """Lädt das gespeicherte Spiel und löscht die Datei danach.

    Sicherheitsregel: pickle.load kann beim Laden Code ausführen.
    Deshalb nur selbst gespeicherte Dateien laden, nie fremde.
    """
    with open(path, "rb") as file:
        game = pickle.load(file)  # Bytes -> wieder ein Game-Objekt
    path.unlink()  # ein Spielstand lässt sich nur einmal fortsetzen
    return game


def backup(keep=5, dry_run=False):
    """Kopiert die Spieldateien in backups/<Datum_Uhrzeit>/, behält nur keep Backups.

    Gibt Zielordner, kopierte Dateien und zu löschende Ordner zurück.
    Mit dry_run=True (Trockenlauf) wird nichts kopiert und nichts gelöscht.
    """
    game_files = [HIGHSCORES_FILE, HISTORY_FILE, DB_FILE]
    files = [path for path in game_files if path.exists()]
    target = BACKUP_DIR / datetime.now().strftime("%Y-%m-%d_%H%M")
    folders = []  # vorhandene Backup-Ordner
    if BACKUP_DIR.exists():
        folders = [path for path in BACKUP_DIR.iterdir() if path.is_dir()]
    if target not in folders:
        folders.append(target)
    # Namen wie 2026-11-08_1530 sortieren alphabetisch = zeitlich
    old_folders = sorted(folders)[:-keep]  # alle außer den neuesten keep
    if dry_run or not files:
        return target, files, old_folders
    target.mkdir(parents=True, exist_ok=True)  # legt auch backups/ an
    for path in files:
        path.copy_into(target)  # seit Python 3.14; früher shutil.copy
    for folder in old_folders:
        shutil.rmtree(folder)  # löscht den Ordner samt Inhalt
    return target, files, old_folders
