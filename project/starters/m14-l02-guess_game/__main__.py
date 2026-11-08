# Zahlenraten – Starter für Lab 14.2 (Stand nach Lab 14.1)
# Startpunkt: python -m guess_game führt diese Datei aus

from guess_game import logic, players, storage, ui


# TODO Lab 14.2: parse_args() mit argparse: --name, --level, --player


def main():
    """Hauptablauf: Name fragen, Runden spielen, bis niemand mehr will."""
    # TODO Lab 14.2: Optionen lesen; nur fragen, was beim Start fehlt (is None)
    ui.show_banner()
    name = ui.ask_name()
    if ui.ask_player_type() == "computer":
        player = players.ComputerPlayer()
    else:
        player = players.HumanPlayer(name)
    played = []  # Scores aller Runden dieser Sitzung
    all_guesses = []  # alle Tipps dieser Sitzung
    # with: lädt highscores.json beim Betreten, speichert beim Verlassen
    with storage.Scoreboard("highscores.json") as board:
        # TODO Lab 14.2: Stufe aus --level an ui.rounds weitergeben
        for game in ui.rounds(player, board):  # eine Runde pro Durchlauf
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
