# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

from guess_game import logic

# TODO Lab 6.1: ask_level, show_hint und play_round aus der alten Datei hierher;
#               Regeln dort mit logic. aufrufen (logic.LEVELS, logic.draw_secret, ...)


def show_banner():
    """Zeigt den Titel des Spiels."""
    print("=" * 40)
    print("Zahlenraten")
    print("=" * 40)


def ask_name():
    """Fragt nach dem Namen und gibt ihn aufgeräumt zurück."""
    return input("Name: ").strip().title()


def ask_play_again():
    """Fragt, ob noch eine Runde gespielt wird, und gibt die Antwort zurück."""
    return input("Nochmal spielen? (j/n): ").strip().lower()


def show_goodbye(name, all_tries):
    """Zeigt die Versuche aller Runden und verabschiedet sich."""
    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")
