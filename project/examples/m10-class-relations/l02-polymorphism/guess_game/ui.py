# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

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


def ask_player_type():
    """Fragt, ob ein Mensch oder der Computer rät, und gibt die Antwort zurück."""
    player_type = input("Wer rät? (mensch/computer): ").strip().lower()
    while player_type not in ["mensch", "computer"]:
        print("Bitte mensch oder computer eingeben.")
        player_type = input("Wer rät? (mensch/computer): ").strip().lower()
    return player_type


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


def show_guess(guess):
    """Zeigt einen Tipp an, den nicht ein Mensch eingegeben hat."""
    print(f"Tipp: {guess}")


def show_hint(hint):
    """Gibt den Hinweis des Spiels farbig aus."""
    if hint == "zu hoch":
        console.print("Zu hoch.", style="red")
    else:
        console.print("Zu niedrig.", style="blue")


def show_highscores(scores):
    """Zeigt die Bestenliste mit Platz, Name, Versuchen, Dauer und Stufe."""
    print("\nBestenliste (Top 5)")
    place = 1
    for score in scores:
        seconds = format_seconds(score["seconds"])
        print(
            f"{place}. {score['name']} · Versuche: {score['tries']}"
            f" · {seconds} s · {score['level']}"
        )
        place += 1


def show_goodbye(name, all_tries):
    """Zeigt die Versuche aller Runden und verabschiedet sich."""
    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")


def format_seconds(seconds):
    """Gibt Sekunden mit einer Nachkommastelle und deutschem Komma zurück: 12,4."""
    return f"{seconds:.1f}".replace(".", ",")


def play_round(game, player):
    """Spielt eine Runde: player tippt, game wertet aus; gibt das Ergebnis zurück."""
    print(
        f"\nStufe {game.level}, {game.name}: "
        f"Rate eine Zahl zwischen {game.low} und {game.high}."
    )
    print(f"Start: {game.started.strftime('%d.%m.%Y, %H:%M')} Uhr")
    player.start_round(game.low, game.high)

    while not game.is_over():
        guess = player.next_guess()  # wer tippt, entscheidet das Spieler-Objekt
        try:
            hint = game.guess(guess)  # das Spiel wertet aus
        except logic.InvalidGuessError as error:  # kein Versuch verbraucht
            print(error)
            continue
        player.on_hint(guess, hint)  # Computer lernt daraus, Mensch liest es

        if hint == "schon getippt":
            print("Diese Zahl wurde schon getippt.")
        elif hint != "richtig":
            show_hint(hint)
            if not game.is_over():
                print(f"Verbleibende Versuche: {game.attempts_left}")

    if game.is_won:
        duration = format_seconds(game.seconds)
        console.print(
            f"Richtig, {game.name}! Benötigte Versuche: {len(game.guesses)}"
            f" · Dauer: {duration} s",
            style="green",
        )
    else:
        print(f"Keine Versuche mehr. Die Zahl war {game.reveal_secret()}.")
    print("Bisherige Tipps:", game.guesses)
    return game.result()
