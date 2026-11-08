# Zahlenraten – Starter für Lab 10.3 (Stand nach Lab 10.2)
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
    # TODO Lab 10.3: storage.Scoreboard() erzeugen, game.save_score() nutzen
    all_tries = []
    play_again = "j"
    while play_again == "j":
        level = ui.ask_level()
        game = logic.Game(player.name, level)  # ein neues Spiel-Objekt pro Runde
        result = ui.play_round(game, player)
        all_tries.append(result["tries"])
        storage.append_history(result)  # jede Runde, auch verlorene
        if result["won"]:  # nur gewonnene Runden kommen in die Bestenliste
            storage.save_highscore(result)
            ui.show_highscores(storage.top_five())
        play_again = ui.ask_play_again()
    ui.show_goodbye(name, all_tries)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
