# Zahlenraten – Starter für Lab 15.2 (Stand nach Lab 14.3)
# Startpunkt: python -m guess_game führt diese Datei aus
# Beispiel: python -m guess_game --level schwer --name Anna

import argparse
import sys

from guess_game import logic, players, storage, ui


def parse_args():
    """Liest die Optionen aus der Kommandozeile; --help erzeugt argparse selbst."""
    parser = argparse.ArgumentParser(
        prog="python -m guess_game",
        description="Zahlenraten im Terminal. Fehlende Angaben fragt das Spiel ab.",
        epilog="Beispiel: python -m guess_game --level schwer --name Anna",
    )
    parser.add_argument("--name", help="Name der Person, z. B. Anna")
    parser.add_argument(
        "--level", choices=list(logic.LEVELS), help="Stufe der ersten Runde"
    )
    parser.add_argument(
        "--player", choices=["mensch", "computer"], help="wer rät (Standard: fragen)"
    )
    parser.add_argument(
        "--backup", action="store_true", help="Spieldateien sichern, nicht spielen"
    )
    parser.add_argument(
        "--keep", type=int, default=5, help="so viele Backups behalten (Standard: 5)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="mit --backup: nur anzeigen"
    )
    args = parser.parse_args()  # liest sys.argv
    # TODO Lab 15.2: ungültigen --name mit parser.error(...) ablehnen
    if args.keep < 1:
        parser.error("--keep muss mindestens 1 sein.")  # beendet mit Exit-Code 2
    return args


def run_backup(args):
    """Sichert die Spieldateien; Exit-Code 1, wenn es nichts zu sichern gibt."""
    target, files, old_folders = storage.backup(args.keep, args.dry_run)
    if not files:
        print("Keine Spieldateien gefunden, nichts zu sichern.")
        sys.exit(1)  # 1 = Fehler, z. B. für Aufgabenplanung oder cron
    ui.show_backup(target, files, old_folders, args.dry_run)


def main():
    """Hauptablauf: Optionen lesen, fehlende Angaben fragen, Runden spielen."""
    args = parse_args()
    if args.backup:  # Werkzeug-Modus: sichern und fertig, ohne Spiel
        run_backup(args)
        return
    ui.show_banner()
    if args.name is None:  # nur fragen, was nicht beim Start angegeben wurde
        name = ui.ask_name()
    else:
        name = args.name.strip().title()
    player_type = args.player
    if player_type is None:
        player_type = ui.ask_player_type()
    if player_type == "computer":
        player = players.ComputerPlayer()
    else:
        player = players.HumanPlayer(name)
    played = []  # Scores aller Runden dieser Sitzung
    all_guesses = []  # alle Tipps dieser Sitzung
    # with: lädt highscores.json beim Betreten, speichert beim Verlassen
    with storage.Scoreboard("highscores.json") as board:
        for game in ui.rounds(player, board, args.level):  # eine Runde pro Durchlauf
            score = ui.play_round(game)  # @timed hat score.seconds eingetragen
            ui.show_result(game, score)
            if game.stopped:  # Befehl quit: Runde zählt nicht
                break
            played.append(score)
            all_guesses.extend(game.guesses)  # hängt alle Tipps der Runde an
            storage.append_history(score)  # jede Runde, auch verlorene
            game.save_score(score)  # nur ein Gewinn kommt in die Bestenliste
            if score.won:
                by = ui.ask_ranking()
                ui.show_highscores(board.top(by), by)
        ui.show_statistics(logic.statistics(board.scores))
    favourites = logic.favourite_numbers(all_guesses)
    ui.show_session(favourites, logic.tries_per_level(played))
    ui.show_goodbye(name, [score.tries for score in played])


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C; die Bestenliste hat __exit__ schon gesichert
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
