# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

# TODO Lab 6.3: time und datetime (aus dem Modul datetime) importieren

from rich.console import Console

from guess_game import logic

console = Console()  # druckt farbig, wenn das Terminal Farben kann


def show_banner():
    """Zeigt den Titel des Spiels."""
    print("=" * 40)
    print("Zahlenraten")
    print("=" * 40)


def ask_name():
    """Fragt nach dem Namen und gibt ihn aufgeräumt zurück."""
    return input("Name: ").strip().title()


def ask_level():
    """Fragt so lange nach der Stufe, bis es sie gibt, und gibt sie zurück."""
    level = input("Stufe (leicht/mittel/schwer): ").strip().lower()
    while level not in logic.LEVELS:
        print("Diese Stufe gibt es nicht.")
        level = input("Stufe (leicht/mittel/schwer): ").strip().lower()
    return level


def ask_play_again():
    """Fragt, ob noch eine Runde gespielt wird, und gibt die Antwort zurück."""
    return input("Nochmal spielen? (j/n): ").strip().lower()


def show_hint(guess, secret):
    """Gibt aus, ob der Tipp zu hoch oder zu niedrig ist."""
    if guess > secret:
        console.print("Zu hoch.", style="red")
    else:
        console.print("Zu niedrig.", style="blue")


def show_goodbye(name, all_tries):
    """Zeigt die Versuche aller Runden und verabschiedet sich."""
    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")


# TODO Lab 6.3: format_seconds(seconds) -> "12,4" (eine Nachkommastelle, Komma)


def play_round(name, level="leicht"):
    """Spielt eine Runde und gibt die Anzahl der Versuche zurück."""
    low, high, max_tries = logic.LEVELS[level]
    secret = logic.draw_secret(low, high)
    tries = 0
    guesses = []
    tried = set()
    # TODO Lab 6.3: Startzeit ausgeben (Start: 08.11.2026, 14:05 Uhr), Stoppuhr starten
    print(f"\nStufe {level}, {name}: Rate eine Zahl zwischen {low} und {high}.")

    while not logic.is_game_over(tries, max_tries):
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue

        tried.add(guess)
        guesses.append(guess)
        tries += 1

        # TODO Lab 6.3: bei Treffer nur won = True merken und die Schleife verlassen
        if logic.is_guess_correct(guess, secret):
            console.print(
                f"Richtig, {name}! Benötigte Versuche: {tries}.", style="green"
            )
            break

        show_hint(guess, secret)

        if logic.is_game_over(tries, max_tries):
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")
        else:
            print(f"Verbleibende Versuche: {max_tries - tries}")

    # TODO Lab 6.3: Stoppuhr anhalten; bei Gewinn grüne Zeile mit Versuchen und Dauer
    print("Bisherige Tipps:", guesses)
    # TODO Lab 6.3: Ergebnis-Dictionary (name, level, tries, seconds, won, date)
    return tries
