# Startpunkt: python -m guess_game führt diese Datei aus
# Beispiel: python -m guess_game --level schwer --name Anna

import argparse

from guess_game import logic, players, storage, ui


def parse_args():
    """Liest die Optionen aus der Kommandozeile; --help erzeugt argparse selbst."""
    parser = argparse.ArgumentParser(
        prog="python -m guess_game",
        description="Zahlenraten im Terminal. Fehlende Angaben fragt das Spiel ab.",
        epilog="Beispiel: python -m guess_game --level schwer --name Anna",
    )
    parser.add_argument("--name", help="Name der Person, z. B. Anna")
    parser.add_argument(
        "--level", choices=list(logic.LEVELS), help="Stufe der ersten Runde"
    )
    parser.add_argument(
        "--player", choices=["mensch", "computer"], help="wer rät (Standard: fragen)"
    )
    return parser.parse_args()  # liest sys.argv


def main():
    """Hauptablauf: Optionen lesen, fehlende Angaben fragen, Runden spielen."""
    args = parse_args()
    ui.show_banner()
    if args.name is None:  # nur fragen, was nicht beim Start angegeben wurde
        name = ui.ask_name()
    else:
        name = args.name.strip().title()
    player_type = args.player
    if player_type is None:
        player_type = ui.ask_player_type()
    if player_type == "computer":
        player = players.ComputerPlayer()
    else:
        player = players.HumanPlayer(name)
    played = []  # Scores aller Runden dieser Sitzung
    all_guesses = []  # alle Tipps dieser Sitzung
    # with: lädt highscores.json beim Betreten, speichert beim Verlassen
    with storage.Scoreboard("highscores.json") as board:
        for game in ui.rounds(player, board, args.level):  # eine Runde pro Durchlauf
            score = ui.play_round(game)  # @timed hat score.seconds eingetragen
            ui.show_result(game, score)
            if game.stopped:  # Befehl quit: Runde zählt nicht
                break
            played.append(score)
            all_guesses.extend(game.guesses)  # hängt alle Tipps der Runde an
            storage.append_history(score)  # jede Runde, auch verlorene
            game.save_score(score)  # nur ein Gewinn kommt in die Bestenliste
            if score.won:
                by = ui.ask_ranking()
                ui.show_highscores(board.top(by), by)
        ui.show_statistics(logic.statistics(board.scores))
    favourites = logic.favourite_numbers(all_guesses)
    ui.show_session(favourites, logic.tries_per_level(played))
    ui.show_goodbye(name, [score.tries for score in played])


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C; die Bestenliste hat __exit__ schon gesichert
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
