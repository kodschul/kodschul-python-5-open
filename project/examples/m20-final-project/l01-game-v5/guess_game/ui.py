# Ein- und Ausgabe im Terminal: alles, was mit input() und print() zu tun hat

import logging

from rich.console import Console

from guess_game import logic, storage

console = Console()  # druckt farbig, wenn das Terminal Farben kann
logger = logging.getLogger(__name__)  # Name "guess_game.ui"

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
    names = "/".join(logic.LEVELS)  # "leicht/mittel/schwer" aus levels.xml
    print(f"  stufe schwer  Stufe der nächsten Runde ({names})")
    print("  bestenliste   Bestenliste zeigen (Top 10)")
    print("  statistik     Spiele, Gewinnquote und Versuche pro Stufe")
    print("  speichern     Spiel speichern und beenden (weiter mit --resume)")
    print("  quit          Spiel beenden")


def ask_name():
    """Fragt so lange nach dem Namen, bis er gültig ist, und gibt ihn zurück."""
    while not logic.is_valid_name(name := input("Name: ").strip()):
        print("Der Name braucht 2 bis 20 Buchstaben, z. B. Anna.")
    return name.title()


def ask_level():
    """Fragt so lange nach der Stufe, bis es sie gibt, und gibt sie zurück."""
    names = "/".join(logic.LEVELS)  # Stufen aus levels.xml, mit / verbunden
    prompt = f"Stufe ({names}): "
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
    print(f"\nBestenliste (Top 10 nach {RANKINGS[by]})")
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


def show_level_stats(rows):
    """Zeigt die Statistik aus game.db: gesamt und pro Stufe."""
    print("\nStatistik aller Runden (game.db)")
    if not rows:
        print("Noch keine Runden gespielt.")
        return
    games = sum(row["games"] for row in rows)  # Summe über alle Stufen
    wins = sum(row["wins"] for row in rows)
    rate = round(100 * wins / games)  # ganze Prozent
    print(f"Gesamt: {wins} von {games} Spielen gewonnen ({rate} %)")
    for row in rows:
        average = str(row["avg_tries"]).replace(".", ",")
        print(
            f"  {row['level']}: {row['wins']} von {row['games']} gewonnen "
            f"({round(row['win_rate'])} %) · Ø {average} Versuche"
        )


def show_session(favourites, groups):
    """Zeigt Lieblingszahl und Versuche pro Stufe der laufenden Sitzung."""
    print("\nDiese Sitzung")
    if favourites:  # leer, wenn niemand eine Zahl getippt hat
        number, count = favourites[0]
        print(f"Lieblingszahl: {number} ({count}-mal getippt)")
        print("Meistgetippt (Zahl, Anzahl):", favourites)
    print("Versuche pro Stufe:")
    for level in sorted(groups):
        print(f"  {level}: {groups[level]}")


def show_backup(target, files, old_folders, dry_run):
    """Zeigt, was das Backup kopiert und löscht (oder im Trockenlauf täte)."""
    if dry_run:
        print("Trockenlauf: Es wird nichts kopiert und nichts gelöscht.")
    for path in files:
        print(f"Kopieren: {path} -> {target}")
    for folder in old_folders:
        print(f"Löschen:  {folder}")
    if not dry_run:
        print(f"Backup fertig: {len(files)} Dateien in {target}")


def show_export(path, count, images):
    """Meldet, wohin die Bestenliste und die Diagramme exportiert wurden."""
    word = "Eintrag" if count == 1 else "Einträge"
    print(f"Bestenliste exportiert: {path} ({count} {word})")
    for image, title in images:
        print(f"Diagramm: {image} ({title})")


def show_goodbye(name, all_tries):
    """Zeigt die Versuche aller Runden und verabschiedet sich."""
    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")


def format_seconds(seconds):
    """Gibt Sekunden mit einer Nachkommastelle und deutschem Komma zurück: 12,4."""
    return f"{seconds:.1f}".replace(".", ",")


def rounds(player, scoreboard, level=None, game=None):
    """Generator: liefert Runde für Runde ein Spiel, bis niemand mehr will.

    game: ein fortgesetztes Spiel (--resume), das als erste Runde läuft.
    """
    if game is None:  # kein gespeichertes Spiel: neu anfangen
        if level is None:  # keine Stufe beim Start angegeben (--level)
            level = ask_level()  # nur einmal; wechseln mit dem Befehl "stufe schwer"
        game = logic.Game(player, scoreboard, level)
    while True:
        yield game  # pausiert, bis die for-Schleife weitermacht
        if ask_play_again() != "j":
            return  # Generator endet, die for-Schleife hört auf
        game = logic.Game(player, scoreboard, game.next_level)


def make_guess(game, number):
    """Gibt einen Tipp an das Spiel weiter und zeigt den Hinweis an."""
    try:
        hint = game.guess(number)  # das Spiel wertet aus
    except logic.InvalidGuessError as error:  # kein Versuch verbraucht
        logger.debug(f"Tipp {number} ungültig: {error}")
        print(error)
        return
    logger.debug(f"Tipp {number}: {hint}")
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
    if game.guesses:  # fortgesetztes Spiel: zeigen, wo es weitergeht
        print("Fortsetzung. Bisherige Tipps:", game.guesses)
        print(f"Verbleibende Versuche: {game.attempts_left}")
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
                show_highscores(game.scoreboard.top())  # Top 10 per SQL
            case ["statistik"]:
                show_level_stats(game.scoreboard.level_stats())  # GROUP BY
            case ["speichern"]:
                storage.save_game(game)  # zuerst speichern, dann beenden
                game.saved = True
                game.stop()
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
    elif game.saved:  # Geheimzahl nicht verraten, das Spiel geht weiter
        print(f"Spielstand gespeichert in {storage.SAVEGAME_FILE}.")
        print("Weiter beim nächsten Start: python -m guess_game --resume")
    elif game.stopped:
        print(f"Spiel beendet. Die Zahl war {game.reveal_secret()}.")
    else:
        print(f"Keine Versuche mehr. Die Zahl war {game.reveal_secret()}.")
    print("Bisherige Tipps:", game.guesses)
