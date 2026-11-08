# Zahlenraten – Starter für Lab 8.2 (Stand nach Lab 8.1)
# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

import time
from datetime import datetime

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


def ask_number(prompt):
    """Fragt so lange, bis eine ganze Zahl eingegeben wird, und gibt sie zurück."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:  # z. B. "abc", "7.5" oder leere Eingabe
            print("Bitte eine ganze Zahl eingeben, z. B. 7.")


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


# TODO Lab 8.2: show_highscores(scores) gibt die Bestenliste mit Platz aus


def format_seconds(seconds):
    """Gibt Sekunden mit einer Nachkommastelle und deutschem Komma zurück: 12,4."""
    return f"{seconds:.1f}".replace(".", ",")


def play_round(name, level="leicht"):
    """Spielt eine Runde und gibt das Ergebnis als Dictionary zurück."""
    low, high, max_tries = logic.LEVELS[level]
    secret = logic.draw_secret(low, high)
    tries = 0
    guesses = []
    tried = set()
    won = False
    started = datetime.now()  # Datum und Uhrzeit des Starts
    print(f"\nStufe {level}, {name}: Rate eine Zahl zwischen {low} und {high}.")
    print(f"Start: {started.strftime('%d.%m.%Y, %H:%M')} Uhr")
    start = time.perf_counter()  # Stoppuhr starten

    while not logic.is_game_over(tries, max_tries):
        guess = ask_number("Tipp: ")
        try:
            logic.check_guess(guess, low, high)
        except ValueError as error:  # Regel verletzt: kein Versuch verbraucht
            print(error)
            continue

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue

        tried.add(guess)
        guesses.append(guess)
        tries += 1

        if logic.is_guess_correct(guess, secret):
            won = True
            break

        show_hint(guess, secret)

        if logic.is_game_over(tries, max_tries):
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")
        else:
            print(f"Verbleibende Versuche: {max_tries - tries}")

    seconds = round(time.perf_counter() - start, 1)  # Stoppuhr anhalten
    if won:
        duration = format_seconds(seconds)
        console.print(
            f"Richtig, {name}! Benötigte Versuche: {tries} · Dauer: {duration} s",
            style="green",
        )
    print("Bisherige Tipps:", guesses)
    return {
        "name": name,
        "level": level,
        "tries": tries,
        "seconds": seconds,
        "won": won,
        "date": started.strftime("%Y-%m-%d"),
    }
