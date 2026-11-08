# Automatisierungsskript: wertet alle game*.log eines Ordners aus
# Start: python log_report.py <ordner> --since 2026-11-01
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
    for path in paths:
        with open(path, encoding="utf-8") as file:
            for line in file:
                result = parse_log_line(line)  # None bei allen anderen Zeilen
                if result is None:
                    continue
                if since is not None and date.fromisoformat(result["date"]) < since:
                    continue
                results.append(result)
    return results


def build_report(results, since, paths):
    """Baut den Bericht als Liste von Zeilen aus den Ergebnis-Dictionaries."""
    outcomes = Counter([result["result"] for result in results])
    levels = Counter([result["level"] for result in results])
    winners = Counter(
        [result["name"] for result in results if result["result"] == "Gewonnen"]
    )
    period = f"seit {since}" if since is not None else "alle Einträge"
    lines = [f"Bericht Zahlenraten ({period})", f"Log-Dateien: {len(paths)}"]
    if not results:
        lines.append("Keine Spiele gefunden.")
        return lines
    level, count = levels.most_common(1)[0]  # [("mittel", 20)] -> erstes Paar
    lines.append(
        f"{len(results)} Spiele, {outcomes['Gewonnen']} gewonnen, "
        f"häufigste Stufe: {level} ({count} Spiele)"
    )
    lines.append("Meiste Gewinne:")
    for name, wins in winners.most_common(3):
        lines.append(f"  {name}: {wins}")
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
    if not args.folder.is_dir():
        logger.error(f"Ordner fehlt: {args.folder}")
        print(f"Ordner nicht gefunden: {args.folder}")
        sys.exit(1)
    paths = sorted(args.folder.glob("game*.log"))
    if not paths:
        logger.warning(f"Keine game*.log in {args.folder}")
        print(f"Keine game*.log in {args.folder} gefunden.")
        sys.exit(1)
    results = read_results(paths, args.since)
    lines = build_report(results, args.since, paths)
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        for line in lines:
            print(line)
            file.write(line + "\n")
    print(f"Gespeichert in {REPORT_FILE}")
    logger.info(f"{len(paths)} Dateien, {len(results)} Spiele, Bericht {REPORT_FILE}")


if __name__ == "__main__":
    main()
