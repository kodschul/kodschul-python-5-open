# Auswertung mit pandas: liest die Tabelle rounds aus game.db und berechnet
# Gewinnquote und Median der Versuche pro Stufe und pro Spieler
# Start im Ordner mit game.db: python analyze.py

import sqlite3
import sys
from pathlib import Path

import pandas as pd

DB_FILE = Path("game.db")

# dieselbe Frage wie der Befehl statistik (Lab 18.3), hier als SQL für den Vergleich
SQL_STATS = """
SELECT level,
       COUNT(*) AS games,
       ROUND(100.0 * SUM(won) / COUNT(*)) AS win_rate,
       ROUND(AVG(tries), 1) AS avg_tries
FROM rounds
GROUP BY level
ORDER BY level
"""


def load_rounds(path=DB_FILE):
    """Lädt alle Runden als DataFrame (eine Zeile pro Runde)."""
    connection = sqlite3.connect(path)
    rounds = pd.read_sql("SELECT * FROM rounds", connection)  # SQL -> Tabelle
    connection.close()
    return rounds


def summary(rounds, column):
    """Gewinnquote und Versuche pro Gruppe, z. B. column="level" oder "name"."""
    groups = rounds.groupby(column)  # Zeilen nach Stufe bzw. Spieler bündeln
    return pd.DataFrame(
        {
            "Spiele": groups["won"].count(),
            "Gewinnquote %": (groups["won"].mean() * 100).round(),  # won: 1 oder 0
            "Median Versuche": groups["tries"].median(),
            "Ø Versuche": groups["tries"].mean().round(1),
        }
    )


def main():
    if not DB_FILE.exists():
        print(f"{DB_FILE} nicht gefunden. Erst spielen (SQLite ab Lab 18.2).")
        sys.exit(1)
    rounds = load_rounds()
    print(f"{len(rounds)} Runden aus {DB_FILE}")  # Checkpoint nach read_sql
    print(rounds.head())  # die ersten fünf Zeilen
    print("\nVersuche (alle Runden):")
    print(rounds["tries"].describe().round(1))  # Anzahl, Mittelwert, Min, Max ...
    print("\nPro Stufe (pandas):")
    print(summary(rounds, "level"))
    print("\nPro Spieler (pandas):")
    print(summary(rounds, "name").sort_values("Gewinnquote %", ascending=False))
    connection = sqlite3.connect(DB_FILE)
    print("\nPro Stufe (SQL wie in Lab 18.3, ohne Median):")
    print(pd.read_sql(SQL_STATS, connection))
    connection.close()


if __name__ == "__main__":
    main()
