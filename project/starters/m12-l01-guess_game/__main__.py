# Zahlenraten – Starter für Lab 12.1 (Stand nach Lab 11.3)
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
        score = ui.play_round(game)
        all_tries.append(score.tries)
        storage.append_history(score)  # jede Runde, auch verlorene
        game.save_score()  # Game entscheidet, ob das Ergebnis in die Liste kommt
        if score.won:
            ui.show_highscores(scoreboard.top_five())
        play_again = ui.ask_play_again()
    # TODO Lab 12.1: Statistik der Bestenliste vor dem Abschied anzeigen
    ui.show_goodbye(name, all_tries)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
