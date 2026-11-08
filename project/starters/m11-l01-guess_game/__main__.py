# Zahlenraten – Starter für Lab 11.1 (Stand nach Lab 10.3)
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
    scoreboard = storage.Scoreboard()  # lädt highscores.json einmal
    all_tries = []
    play_again = "j"
    while play_again == "j":
        level = ui.ask_level()
        game = logic.Game(player, scoreboard, level)  # neues Spiel pro Runde
        # TODO Lab 11.1: score = ui.play_round(game), dann score.tries und score.won
        result = ui.play_round(game)
        all_tries.append(result["tries"])
        storage.append_history(result)  # jede Runde, auch verlorene
        game.save_score()  # Game entscheidet, ob das Ergebnis in die Liste kommt
        if result["won"]:
            ui.show_highscores(scoreboard.top_five())
        play_again = ui.ask_play_again()
    ui.show_goodbye(name, all_tries)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
