# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

from rich.console import Console

from guess_game import logic

console = Console()  # druckt farbig, wenn das Terminal Farben kann

# Sortierung -> Überschrift der Bestenliste
RANKINGS = {"versuche": "Versuchen", "zeit": "Zeit", "punkte": "Punkten"}


def show_banner():
    """Zeigt den Titel des Spiels und den Hinweis auf die Befehle."""
    print("=" * 40)
    print("Zahlenraten")
    print("=" * 40)
    print("Beim Tipp versteht das Spiel auch Befehle, z. B. hilfe.")


def show_help():
    """Zeigt alle Befehle, die beim Tipp funktionieren."""
    print("Befehle:")
    print("  7             Zahl tippen")
    print("  hilfe         diese Übersicht")
    print("  stufe schwer  Stufe der nächsten Runde (leicht/mittel/schwer)")
    print("  bestenliste   Bestenliste zeigen")
    print("  quit          Spiel beenden")


def ask_name():
    """Fragt nach dem Namen und gibt ihn aufgeräumt zurück."""
    return input("Name: ").strip().title()


def ask_level():
    """Fragt so lange nach der Stufe, bis es sie gibt, und gibt sie zurück."""
    prompt = "Stufe (leicht/mittel/schwer): "
    # := speichert die Eingabe und prüft sie in derselben Zeile
    while (level := input(prompt).strip().lower()) not in logic.LEVELS:
        print("Diese Stufe gibt es nicht.")
    return level


def ask_player_type():
    """Fragt, ob ein Mensch oder der Computer rät, und gibt die Antwort zurück."""
    prompt = "Wer rät? (mensch/computer): "
    while (player_type := input(prompt).strip().lower()) not in ["mensch", "computer"]:
        print("Bitte mensch oder computer eingeben.")
    return player_type


def ask_command(prompt):
    """Fragt nach einem Tipp oder Befehl und gibt den Text aufgeräumt zurück."""
    return input(prompt).strip().lower()


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


def ask_ranking():
    """Fragt, wonach die Bestenliste sortiert wird; Enter = nach Versuchen."""
    by = input("Bestenliste nach (versuche/zeit/punkte): ").strip().lower()
    if by not in RANKINGS:  # leer oder unbekannt
        by = "versuche"
    return by


def show_highscores(scores, by="versuche"):
    """Zeigt die Bestenliste mit Platz, Score, Stufe und Punkten."""
    print(f"\nBestenliste (Top 5 nach {RANKINGS[by]})")
    if not scores:  # Befehl bestenliste vor dem ersten Gewinn
        print("Noch keine Einträge.")
    place = 1
    for score in scores:
        # f-String nutzt Score.__str__
        print(f"{place}. {score} · {score.level} · {score.points()} Punkte")
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


def rounds(player, scoreboard):
    """Generator: liefert Runde für Runde ein neues Spiel, bis niemand mehr will."""
    level = ask_level()  # nur einmal; wechseln mit dem Befehl "stufe schwer"
    while True:
        game = logic.Game(player, scoreboard, level)
        yield game  # pausiert, bis die for-Schleife weitermacht
        level = game.next_level
        if ask_play_again() != "j":
            return  # Generator endet, die for-Schleife hört auf


def make_guess(game, number):
    """Gibt einen Tipp an das Spiel weiter und zeigt den Hinweis an."""
    try:
        hint = game.guess(number)  # das Spiel wertet aus
    except logic.InvalidGuessError as error:  # kein Versuch verbraucht
        print(error)
        return
    game.player.on_hint(number, hint)  # Computer lernt daraus, Mensch liest es

    if hint == "schon getippt":
        print("Diese Zahl wurde schon getippt.")
    elif hint != "richtig":
        show_hint(hint)
        if not game.is_over():
            print(f"Verbleibende Versuche: {game.attempts_left}")


@logic.timed  # misst die Dauer der Runde, ohne Messcode in der Funktion
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
        text = player.next_guess()  # Zahl oder Befehl, als Text
        match text.split():  # "stufe schwer" -> ["stufe", "schwer"]
            case [number] if number.isdigit():  # genau ein Wort aus Ziffern
                make_guess(game, int(number))
            case ["hilfe"]:
                show_help()
            case ["stufe", level] if level in logic.LEVELS:
                game.next_level = level
                print(f"Die nächste Runde läuft auf Stufe {level}.")
            case ["stufe", _]:
                print("Diese Stufe gibt es nicht.")
            case ["bestenliste"]:
                show_highscores(game.scoreboard.top())
            case ["quit"]:
                game.stop()
            case _:  # alles andere, auch leere Eingabe
                print("Bitte eine ganze Zahl oder einen Befehl eingeben (hilfe).")
    return game.score()


def show_result(game, score):
    """Zeigt nach der Runde Gewinn oder Geheimzahl und die bisherigen Tipps."""
    player = game.player
    if score.won:
        duration = format_seconds(score.seconds)  # gemessen von @timed
        console.print(
            f"Richtig, {player.name}! Benötigte Versuche: {len(game.guesses)}"
            f" · Dauer: {duration} s",
            style="green",
        )
    elif game.stopped:
        print(f"Spiel beendet. Die Zahl war {game.reveal_secret()}.")
    else:
        print(f"Keine Versuche mehr. Die Zahl war {game.reveal_secret()}.")
    print("Bisherige Tipps:", game.guesses)
