# Log-Import: zerlegt game.log in Runden (Start, Tipps, Ergebnis) und
# speichert sie in game.db, Tabelle log_rounds
# Start im Ordner mit game.log: python import_log.py
# Mehrfach starten schadet nicht: der Import ersetzt den vorherigen.

import re
import sqlite3
import sys
from pathlib import Path

LOG_FILE = Path("game.log")
DB_FILE = Path("game.db")

# Eine Runde im Log geht über mehrere Zeilen, z. B.:
# 2026-11-08 15:30:00 INFO guess_game: Neue Runde: Stufe leicht
# 2026-11-08 15:30:04 DEBUG guess_game.ui: Tipp 5: zu niedrig
# 2026-11-08 15:30:09 DEBUG guess_game.ui: Tipp 8: richtig
# 2026-11-08 15:30:09 DEBUG guess_game.logic: play_round dauerte 9.1 s
# 2026-11-08 15:30:09 INFO guess_game: Gewonnen: Anna – 2 Versuche – 9,1 s · leicht
ROUND_PATTERN = re.compile(
    r"""
    ^(?P<started>\d{4}-\d{2}-\d{2}\ [\d:]{8})      # Datum und Uhrzeit des Starts
    \ INFO\ guess_game:\ Neue\ Runde:\ Stufe\ (?P<level>\w+)\n
    (?P<body>(?:.*\ DEBUG\ .*\n)*?)               # nur DEBUG-Zeilen: die Tipps
    .*\ INFO\ guess_game:\ (?P<result>Gewonnen|Verloren):\ (?P<name>\w+)
    \ –\ (?P<tries>\d+)\ Versuche?\ –\ (?P<seconds>[\d,]+)\ s\ ·\ \w+$
    """,
    re.MULTILINE | re.VERBOSE,  # ^ und $ je Zeile; Leerzeichen und # im Muster
)
# eine Tipp-Zeile im body, z. B. "Tipp 5: zu niedrig" (ungültige Tipps nicht)
GUESS_PATTERN = re.compile(r"Tipp (\d+): (?:zu hoch|zu niedrig|richtig)")

CREATE_LOG_ROUNDS = """
CREATE TABLE IF NOT EXISTS log_rounds (
    id INTEGER PRIMARY KEY,
    started TEXT NOT NULL,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    tries INTEGER NOT NULL,
    seconds REAL NOT NULL,
    won INTEGER NOT NULL,
    guesses TEXT NOT NULL
)
"""
INSERT_LOG_ROUND = """
INSERT INTO log_rounds (started, name, level, tries, seconds, won, guesses)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""


def parse_rounds(text):
    """Gibt alle vollständigen Runden im Text als Liste von Dictionaries zurück."""
    rounds = []
    for match in ROUND_PATTERN.finditer(text):  # ein Treffer pro Runde
        record = match.groupdict()  # {"started": "...", "level": "leicht", ...}
        guesses = GUESS_PATTERN.findall(record.pop("body"))  # ["5", "8"]
        record["guesses"] = " ".join(guesses)  # "5 8"
        record["tries"] = int(record["tries"])
        record["seconds"] = float(record["seconds"].replace(",", "."))
        record["won"] = record.pop("result") == "Gewonnen"
        rounds.append(record)
    return rounds


def save_rounds(rounds, path=DB_FILE):
    """Ersetzt den Inhalt der Tabelle log_rounds durch die Runden aus dem Log."""
    rows = []
    for record in rounds:
        rows.append(
            (
                record["started"],
                record["name"],
                record["level"],
                record["tries"],
                record["seconds"],
                record["won"],
                record["guesses"],
            )
        )
    connection = sqlite3.connect(path)
    connection.execute(CREATE_LOG_ROUNDS)
    connection.execute("DELETE FROM log_rounds")  # alter Import raus
    connection.executemany(INSERT_LOG_ROUND, rows)  # ein INSERT pro Tupel
    connection.commit()
    connection.close()


def main():
    if not LOG_FILE.exists():
        print(f"{LOG_FILE} nicht gefunden. Erst spielen (Log ab Lab 15.3).")
        sys.exit(1)
    text = LOG_FILE.read_text(encoding="utf-8")  # die ganze Datei als ein Text
    rounds = parse_rounds(text)
    wins = len([record for record in rounds if record["won"]])
    print(f"{LOG_FILE}: {len(rounds)} Runden gefunden, davon {wins} gewonnen")
    for record in rounds:
        result = "gewonnen" if record["won"] else "verloren"
        print(
            f"  {record['started']} · {record['name']} · {record['level']} · "
            f"{result} · Tipps: {record['guesses']}"
        )
    save_rounds(rounds)
    print(f"Gespeichert in {DB_FILE}, Tabelle log_rounds.")


if __name__ == "__main__":
    main()
