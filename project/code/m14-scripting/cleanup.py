# Aufräum-Skript: sortiert Dateien nach Endung in Unterordner (pdf/, jpg/, ...)
# Erst mit --dry-run prüfen, dann ohne ausführen. Nur an einer Testkopie arbeiten:
# python code/m14-scripting/make_sandbox.py legt playground/messy_downloads/ an.

import argparse
import sys
from pathlib import Path

COURSE_DATA = Path("data/messy_downloads")  # Original der Kursdaten: nie ändern


def parse_args():
    """Liest Ordner und Optionen aus der Kommandozeile."""
    parser = argparse.ArgumentParser(
        description="Sortiert die Dateien eines Ordners nach Endung in Unterordner.",
        epilog="Beispiel: cleanup.py playground/messy_downloads --dry-run",
    )
    parser.add_argument("folder", help="Ordner, der aufgeräumt wird")
    parser.add_argument(
        "--dry-run", action="store_true", help="nur anzeigen, nichts verschieben"
    )
    return parser.parse_args()


def folder_name_for(path):
    """Unterordner für eine Datei: ".PDF" -> "pdf", ohne Endung -> "ohne_endung"."""
    if path.suffix == "":
        return "ohne_endung"
    return path.suffix.lower()[1:]  # Punkt abschneiden


def main():
    args = parse_args()
    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Ordner nicht gefunden: {folder}")
        sys.exit(1)
    if folder.resolve() == COURSE_DATA.resolve():
        print("Das ist das Original der Kursdaten. Bitte eine Kopie nutzen.")
        sys.exit(1)
    if args.dry_run:
        print("Trockenlauf: Es wird nichts verschoben.")
    count = 0
    for path in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
        if not path.is_file() or path.name.startswith("."):
            continue  # Unterordner und versteckte Dateien bleiben, wo sie sind
        target_dir = folder / folder_name_for(path)
        target = target_dir / path.name
        if target.exists():
            print(f"Übersprungen, existiert schon: {target}")
            continue  # nie eine vorhandene Datei überschreiben
        print(f"{path.name} -> {target_dir.name}/")
        if not args.dry_run:
            target_dir.mkdir(exist_ok=True)  # Unterordner anlegen, falls nötig
            path.move(target)  # seit Python 3.14; früher shutil.move
        count += 1
    if args.dry_run:
        print(f"Würde verschieben: {count}")
    else:
        print(f"Verschoben: {count}")


if __name__ == "__main__":
    main()
