# Startpunkt: python -m guess_game führt diese Datei aus
# Beispiel: python -m guess_game --level schwer --name Anna

import argparse
import logging
import sys

from guess_game import export, logic, players, storage, ui

LOG_FILE = "game.log"
# __name__ wäre hier "__main__"; deshalb der Paketname als fester Logger-Name
logger = logging.getLogger("guess_game")


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
    parser.add_argument(
        "--verbose", action="store_true", help="Protokoll auch im Terminal zeigen"
    )
    parser.add_argument(
        "--export", choices=["html", "excel"], help="Bestenliste als Datei speichern"
    )
    parser.add_argument(
        "--resume", action="store_true", help="gespeichertes Spiel fortsetzen"
    )
    args = parser.parse_args()  # liest sys.argv
    if args.name is not None and not logic.is_valid_name(args.name):
        parser.error("--name braucht 2 bis 20 Buchstaben, z. B. Anna.")
    if args.keep < 1:
        parser.error("--keep muss mindestens 1 sein.")  # beendet mit Exit-Code 2
    return args


def setup_logging(verbose):
    """Schreibt alles ab DEBUG in game.log; mit --verbose auch ins Terminal."""
    handlers = [logging.FileHandler(LOG_FILE, encoding="utf-8")]
    if verbose:
        handlers.append(logging.StreamHandler())  # Terminal (Fehlerausgabe)
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
    )


def run_backup(args):
    """Sichert die Spieldateien; Exit-Code 1, wenn es nichts zu sichern gibt."""
    target, files, old_folders = storage.backup(args.keep, args.dry_run)
    if not files:
        logger.warning("Backup: keine Spieldateien gefunden")
        print("Keine Spieldateien gefunden, nichts zu sichern.")
        sys.exit(1)  # 1 = Fehler, z. B. für Aufgabenplanung oder cron
    ui.show_backup(target, files, old_folders, args.dry_run)
    if args.dry_run:
        logger.info(f"Backup-Trockenlauf: {len(files)} Dateien, Ziel {target}")
    else:
        logger.info(f"Backup: {len(files)} Dateien nach {target}")
        logger.info(f"Backup: {len(old_folders)} alte Backups gelöscht")


def run_export(args):
    """Speichert die Top 10 der Bestenliste als Datei, ohne zu spielen."""
    with storage.SqliteScoreboard("game.db") as board:
        scores = board.top(count=10)
    if args.export == "excel":
        path = export.export_excel(scores)
    else:
        path = export.export_html(scores)
    ui.show_export(path, len(scores))
    logger.info(f"Export: {len(scores)} Einträge nach {path}")


def main():
    """Hauptablauf: Optionen lesen, fehlende Angaben fragen, Runden spielen."""
    args = parse_args()
    setup_logging(args.verbose)
    logger.info(f"Programm gestartet mit {sys.argv[1:]}")
    if args.backup:  # Werkzeug-Modus: sichern und fertig, ohne Spiel
        run_backup(args)
        return
    if args.export is not None:  # Werkzeug-Modus: exportieren und fertig
        run_export(args)
        return
    saved_game = None  # bleibt None, wenn kein Spiel fortgesetzt wird
    if args.resume:
        if not storage.SAVEGAME_FILE.exists():
            print(f"Kein gespeichertes Spiel gefunden ({storage.SAVEGAME_FILE}).")
            sys.exit(1)
        saved_game = storage.load_game()
        logger.info(f"Spiel fortgesetzt aus {storage.SAVEGAME_FILE}")
    ui.show_banner()
    if saved_game is not None:  # Name und Spieler stecken im Spielstand
        player = saved_game.player
        name = player.name
    else:
        if args.name is None:  # nur fragen, was nicht beim Start angegeben wurde
            name = ui.ask_name()
        else:
            name = args.name.title()
        player_type = args.player
        if player_type is None:
            player_type = ui.ask_player_type()
        if player_type == "computer":
            player = players.ComputerPlayer()
        else:
            player = players.HumanPlayer(name)
    logger.info(f"Spiel gestartet: {name}, es rät {player.name}")
    played = []  # Scores aller Runden dieser Sitzung
    all_guesses = []  # alle Tipps dieser Sitzung
    # with: öffnet game.db beim Betreten, schließt die Verbindung beim Verlassen
    with storage.SqliteScoreboard("game.db") as board:
        if saved_game is not None:
            saved_game.scoreboard = board  # wurde nicht mitgespeichert
        # eine Runde pro Durchlauf; ein fortgesetztes Spiel läuft als erste
        for game in ui.rounds(player, board, args.level, saved_game):
            logger.info(f"Neue Runde: Stufe {game.level}")
            score = ui.play_round(game)  # @timed hat score.seconds eingetragen
            ui.show_result(game, score)
            if game.saved:  # Befehl speichern: Runde geht beim nächsten Start weiter
                logger.info(f"Spielstand gespeichert in {storage.SAVEGAME_FILE}")
                break
            if game.stopped:  # Befehl quit: Runde zählt nicht
                logger.info("Spiel mit quit beendet")
                break
            if score.won:  # Format passt zu logic.LOG_PATTERN (Lab 15.2)
                logger.info(f"Gewonnen: {score} · {score.level}")
            else:
                logger.info(f"Verloren: {score} · {score.level}")
            played.append(score)
            all_guesses.extend(game.guesses)  # hängt alle Tipps der Runde an
            storage.append_history(score)  # jede Runde, auch verlorene
            board.add_round(score)  # jede Runde auch in game.db (Tabelle rounds)
            game.save_score(score)  # nur ein Gewinn kommt in die Bestenliste
            if score.won:
                by = ui.ask_ranking()
                ui.show_highscores(board.top(by), by)
        ui.show_statistics(logic.statistics(board.scores))
    favourites = logic.favourite_numbers(all_guesses)
    ui.show_session(favourites, logic.tries_per_level(played))
    ui.show_goodbye(name, [score.tries for score in played])
    logger.info("Programm beendet")


if __name__ == "__main__":  # nur beim Start, nicht beim Import
    try:
        main()
    except KeyboardInterrupt:  # Strg+C; fertige Runden stehen schon in game.db
        logger.info("Mit Strg+C abgebrochen")
        print("\nSpiel abgebrochen. Bis zum nächsten Mal!")
    except Exception:  # alles Unerwartete: Traceback ins Log, kurze Meldung
        logger.exception("Unerwarteter Fehler")
        print(f"Ein Fehler ist aufgetreten. Details stehen in {LOG_FILE}.")
        sys.exit(1)
