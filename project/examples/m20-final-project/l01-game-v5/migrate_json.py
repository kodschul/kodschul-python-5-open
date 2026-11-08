# Migration: übernimmt highscores.json einmalig in die Tabelle scores von game.db
# Start im Ordner mit guess_game/ und highscores.json: python migrate_json.py
# Mehrfach starten schadet nicht: vorhandene Einträge werden übersprungen.

import sys

from guess_game import storage


def main():
    old_board = storage.Scoreboard("highscores.json")  # die JSON-Bestenliste
    if not old_board.path.exists():
        print("Keine highscores.json gefunden, nichts zu übernehmen.")
        sys.exit(1)
    old_scores = old_board.load()  # nur lesen, die JSON-Datei bleibt unverändert
    with storage.SqliteScoreboard("game.db") as board:
        # == vergleicht alle Felder (Dataclass): gleicher Eintrag = schon da
        new_scores = [score for score in old_scores if score not in board.scores]
        board.add_many(new_scores)
        total = len(board.scores)
    skipped = len(old_scores) - len(new_scores)
    print(f"highscores.json: {len(old_scores)} Einträge gelesen")
    print(f"Übernommen: {len(new_scores)} · schon vorhanden: {skipped}")
    print(f"game.db enthält jetzt {total} Einträge in der Tabelle scores.")


if __name__ == "__main__":
    main()
