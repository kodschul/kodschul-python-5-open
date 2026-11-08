"""Wahlaufgabe eigene Stufe per CLI (Lab 20.1): Bereich und Versuche beim Start.

Das Skript liegt neben dem Paket guess_game/ (wie log_report.py) und nutzt
es unverändert. Die Stufen sind ein Dictionary (logic.LEVELS, Lab 4.3);
das Skript ergänzt dort für diesen einen Lauf die Stufe "eigene".
Start: python custom_level.py --name Anna --high 1000 --tries 10
"""

import argparse

from guess_game import logic, players, storage, ui


def parse_args():
    """Liest Name, Zahlenbereich und Versuche; prüft, ob sie zusammenpassen."""
    parser = argparse.ArgumentParser(
        description="Eine Runde Zahlenraten mit eigener Stufe.",
        epilog="Beispiel: python custom_level.py --name Anna --high 1000 --tries 10",
    )
    parser.add_argument("--name", help="Name der Person, z. B. Anna")
    parser.add_argument("--low", type=int, default=1, help="kleinste Zahl (1)")
    parser.add_argument("--high", type=int, default=1000, help="größte Zahl (1000)")
    parser.add_argument("--tries", type=int, default=10, help="Versuche (10)")
    args = parser.parse_args()
    if args.low >= args.high:
        parser.error("--low muss kleiner als --high sein.")  # Exit-Code 2
    if args.tries < 1:
        parser.error("--tries muss mindestens 1 sein.")
    if args.name is not None and not logic.is_valid_name(args.name):
        parser.error("--name braucht 2 bis 20 Buchstaben, z. B. Anna.")
    return args


def main():
    """Ergänzt die Stufe "eigene", spielt eine Runde und speichert sie."""
    args = parse_args()
    logic.LEVELS["eigene"] = (args.low, args.high, args.tries)  # nur für diesen Lauf
    ui.show_banner()
    if args.name is None:
        name = ui.ask_name()
    else:
        name = args.name.title()
    with storage.SqliteScoreboard("game.db") as board:
        game = logic.Game(players.HumanPlayer(name), board, "eigene")
        score = ui.play_round(game)
        ui.show_result(game, score)
        if not game.stopped:  # quit/speichern: Runde zählt nicht
            board.add_round(score)  # erscheint in statistik als Stufe eigene
            game.save_score(score)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    main()
