# Zahlenraten – Starter für Lab 8.1 (Stand nach Lab 7.3)
# Startpunkt: python -m guess_game führt diese Datei aus

# TODO Lab 8.1: neues Modul storage.py anlegen und hier mit importieren
from guess_game import ui


def main():
    """Hauptablauf: Name fragen, Runden spielen, bis niemand mehr will."""
    ui.show_banner()
    name = ui.ask_name()
    all_tries = []
    play_again = "j"
    while play_again == "j":
        level = ui.ask_level()
        result = ui.play_round(name, level=level)
        all_tries.append(result["tries"])
        # TODO Lab 8.1: gewonnene Runde mit storage.append_score(result) speichern
        play_again = ui.ask_play_again()
    ui.show_goodbye(name, all_tries)


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
