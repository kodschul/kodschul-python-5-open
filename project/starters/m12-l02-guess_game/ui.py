# Zahlenraten – Starter für Lab 12.2 (Stand nach Lab 12.1)
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


# TODO Lab 12.2: RANKINGS, ask_ranking() und show_highscores(scores, by)
def show_highscores(scores):
    """Zeigt die Bestenliste mit Platz, Score und Stufe."""
    print("\nBestenliste (Top 5)")
    place = 1
    for score in scores:
        print(f"{place}. {score} · {score.level}")  # f-String nutzt Score.__str__
        place += 1


def show_statistics(stats):
    """Zeigt Gewinner, Versuche pro Spieler und Durchschnitt pro Stufe."""
    print("\nStatistik der Bestenliste")
    if not stats["winners"]:
        print("Noch keine Einträge.")
        return
    print("Gewinner:", sorted(stats["winners"]))  # sorted: feste Reihenfolge
    print("Versuche pro Spieler:")
    for name in sorted(stats["tries_per_player"]):
        print(f"  {name}: {stats['tries_per_player'][name]}")
    print("Durchschnitt pro Stufe:")
    for level in sorted(stats["average_per_level"]):
        value = str(stats["average_per_level"][level]).replace(".", ",")
        print(f"  {level}: {value} Versuche")


def show_goodbye(name, all_tries):
    """Zeigt die Versuche aller Runden und verabschiedet sich."""
    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")


def format_seconds(seconds):
    """Gibt Sekunden mit einer Nachkommastelle und deutschem Komma zurück: 12,4."""
    return f"{seconds:.1f}".replace(".", ",")


def play_round(game):
    """Spielt eine Runde: Spieler tippt, Spiel wertet aus; gibt den Score zurück."""
    player = game.player
    print(
        f"\nStufe {game.level}, {player.name}: "
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
            f"Richtig, {player.name}! Benötigte Versuche: {len(game.guesses)}"
            f" · Dauer: {duration} s",
            style="green",
        )
    else:
        print(f"Keine Versuche mehr. Die Zahl war {game.reveal_secret()}.")
    print("Bisherige Tipps:", game.guesses)
    return game.score()
