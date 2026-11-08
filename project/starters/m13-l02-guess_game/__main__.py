# Zahlenraten – Starter für Lab 13.2 (Stand nach Lab 13.1)
# Startpunkt: python -m guess_game führt diese Datei aus

from guess_game import logic, players, storage, ui


def main():
    """Hauptablauf: Name fragen, Runden spielen, bis niemand mehr will."""
    ui.show_banner()
    name = ui.ask_name()
    if ui.ask_player_type() == "computer":
        player = players.ComputerPlayer()
    else:
        player = players.HumanPlayer(name)
    # TODO Lab 13.2: with storage.Scoreboard("highscores.json") as board: ...
    scoreboard = storage.Scoreboard()  # lädt highscores.json einmal
    all_tries = []
    for game in ui.rounds(player, scoreboard):  # eine Runde pro Durchlauf
        score = ui.play_round(game)  # @timed hat score.seconds eingetragen
        ui.show_result(game, score)
        all_tries.append(score.tries)
        storage.append_history(score)  # jede Runde, auch verlorene
        game.save_score(score)  # Game entscheidet, ob das Ergebnis in die Liste kommt

        if score.won:
            by = ui.ask_ranking()
            ui.show_highscores(scoreboard.top(by), by)
    ui.show_statistics(logic.statistics(scoreboard.scores))
    ui.show_goodbye(name, all_tries)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
