"""Wahlaufgabe Zwei-Personen-Modus (Lab 20.1): zwei Menschen raten nacheinander.

Das Skript liegt neben dem Paket guess_game/ (wie log_report.py) und nutzt
es unverändert: Game, HumanPlayer, play_round und die SQLite-Bestenliste.
Start im Ordner, der guess_game/ enthält: python two_players.py --level leicht
"""

import argparse

from guess_game import logic, players, storage, ui


def parse_args():
    """Liest die Stufe aus der Kommandozeile; beide Runden laufen auf ihr."""
    parser = argparse.ArgumentParser(
        description="Zahlenraten zu zweit: jede Person rät eine Runde.",
        epilog="Beispiel: python two_players.py --level mittel",
    )
    parser.add_argument(
        "--level",
        choices=list(logic.LEVELS),
        default="leicht",
        help="Stufe beider Runden (Standard: leicht)",
    )
    return parser.parse_args()


def play_turn(name, board, level):
    """Spielt eine Runde für name und speichert sie; None bei quit/speichern."""
    game = logic.Game(players.HumanPlayer(name), board, level)
    score = ui.play_round(game)  # eigene Geheimzahl pro Person
    ui.show_result(game, score)
    if game.stopped:  # quit oder speichern: Runde zählt nicht
        return None
    board.add_round(score)  # jede Runde in die Tabelle rounds
    game.save_score(score)  # ein Gewinn zusätzlich in scores
    return score


def winner_text(first, second):
    """Vergleicht zwei Scores: Gewinn vor Verlust, dann weniger Versuche."""
    if not first.won and not second.won:
        return "Niemand hat die Zahl gefunden: unentschieden."
    if first.won and not second.won:
        return f"{first.name} gewinnt: nur {first.name} hat die Zahl gefunden."
    if second.won and not first.won:
        return f"{second.name} gewinnt: nur {second.name} hat die Zahl gefunden."
    # beide gewonnen: Score.__lt__ vergleicht Versuche, dann Zeit (Lab 11.1)
    if first < second:
        return f"{first.name} gewinnt: {first.tries} zu {second.tries} Versuchen."
    if second < first:
        return f"{second.name} gewinnt: {second.tries} zu {first.tries} Versuchen."
    return f"Unentschieden: beide brauchten {first.tries} Versuche."


def main():
    """Fragt zwei Namen, spielt zwei Runden und verkündet das Ergebnis."""
    args = parse_args()
    ui.show_banner()
    print(f"Zu zweit auf Stufe {args.level}: weniger Versuche gewinnt.")
    names = []
    for number in [1, 2]:
        print(f"Person {number}")
        names.append(ui.ask_name())
    scores = []
    with storage.SqliteScoreboard("game.db") as board:
        for name in names:
            score = play_turn(name, board, args.level)
            if score is None:
                print("Runde abgebrochen, kein Vergleich.")
                return
            scores.append(score)
    print()
    print(winner_text(scores[0], scores[1]))


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    main()
