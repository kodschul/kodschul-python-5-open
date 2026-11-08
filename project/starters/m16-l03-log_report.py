# Zahlenraten – Starter für Lab 16.3 (Stand nach Lab 16.2): Gerüst für log_report.py
# Automatisierungsskript: wertet alle game*.log eines Ordners aus
# Start im Ordner neben guess_game/: python log_report.py <ordner> --since 2026-11-01
# Ablauf: Argumente -> Dateien finden -> Zeilen auswerten -> Bericht -> Exit-Code

import argparse
import logging
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from guess_game.logic import parse_log_line  # Regex aus Lab 15.2

REPORT_FILE = Path("report.txt")
logger = logging.getLogger("log_report")


def parse_args():
    """Liest Ordner und --since aus der Kommandozeile."""
    parser = argparse.ArgumentParser(
        description="Erstellt einen Bericht aus den Spiel-Logs (game*.log)."
    )
    parser.add_argument("folder", type=Path, help="Ordner mit den Log-Dateien")
    parser.add_argument(
        "--since",
        type=date.fromisoformat,  # "2026-11-01" -> date; falsches Format -> Fehler
        help="nur Spiele ab diesem Datum (JJJJ-MM-TT)",
    )
    return parser.parse_args()


def read_results(paths, since):
    """Liest alle Ergebniszeilen der Dateien; ältere als since werden übersprungen."""
    results = []
    # TODO Lab 16.3: jede Datei Zeile für Zeile lesen, parse_log_line anwenden,
    # None und Spiele vor since überspringen, den Rest an results anhängen
    return results


def build_report(results, since, paths):
    """Baut den Bericht als Liste von Zeilen aus den Ergebnis-Dictionaries."""
    period = f"seit {since}" if since is not None else "alle Einträge"
    lines = [f"Bericht Zahlenraten ({period})", f"Log-Dateien: {len(paths)}"]
    # TODO Lab 16.3: mit Counter Ergebnisse, Stufen und Gewinner zählen und die
    # Zeilen "8 Spiele, 7 gewonnen, häufigste Stufe: ..." und "Meiste Gewinne:"
    # anhängen; ohne Ergebnisse nur "Keine Spiele gefunden."
    return lines


def main():
    """Ablauf des Skripts; Exit-Code 1, wenn es nichts auszuwerten gibt."""
    logging.basicConfig(
        filename="log_report.log",  # eigenes Log, passt nicht auf game*.log
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    args = parse_args()
    logger.info(f"Start: Ordner {args.folder}, seit {args.since}")
    # TODO Lab 16.3: Ordner fehlt -> Meldung, ERROR ins Log, sys.exit(1)
    paths = []
    # TODO Lab 16.3: paths = alle game*.log im Ordner (sortiert);
    # keine gefunden -> Meldung, WARNING ins Log, sys.exit(1)
    results = read_results(paths, args.since)
    lines = build_report(results, args.since, paths)
    # TODO Lab 16.3: jede Zeile ausgeben und in REPORT_FILE schreiben
    print(f"Noch kein Bericht: {len(lines)} Zeilen vorbereitet")  # TODO-Platzhalter
    logger.info(f"{len(paths)} Dateien, {len(results)} Spiele, Bericht {REPORT_FILE}")


if __name__ == "__main__":
    main()
