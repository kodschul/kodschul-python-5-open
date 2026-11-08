# Präfix vor alle Dateinamen eines Ordners setzen: rename.py <ordner> --prefix
# Nur an einer Testkopie ausprobieren, z. B. playground/rename_test/

import argparse
import sys
from pathlib import Path

COURSE_DATA = Path("data/messy_downloads")  # Original der Kursdaten: nie ändern


def parse_args():
    """Liest Ordner und Optionen aus der Kommandozeile."""
    parser = argparse.ArgumentParser(
        description="Setzt ein Präfix vor alle Dateinamen eines Ordners.",
        epilog="Beispiel: rename.py playground/rename_test --prefix 2026_",
    )
    parser.add_argument("folder", help="Ordner mit den Dateien (nur Testkopie)")
    parser.add_argument(
        "--prefix", default="alt_", help="Text vor jedem Namen (Standard: alt_)"
    )
    parser.add_argument(
        "--only", choices=["pdf", "jpg", "txt", "csv"], help="nur diese Endung"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    folder = Path(args.folder)
    if not folder.is_dir():
        print(f"Ordner nicht gefunden: {folder}")
        sys.exit(1)  # 1 = Fehler
    if folder.resolve() == COURSE_DATA.resolve():  # resolve: vollständiger Pfad
        print("Das ist das Original der Kursdaten. Bitte eine Kopie nutzen.")
        sys.exit(1)
    count = 0
    for path in sorted(folder.iterdir()):  # alle Einträge des Ordners
        if not path.is_file() or path.name.startswith(args.prefix):
            continue  # Unterordner und schon umbenannte Dateien überspringen
        if args.only is not None and path.suffix.lower() != "." + args.only:
            continue  # suffix: Endung mit Punkt, z. B. ".pdf"
        new_path = folder / (args.prefix + path.name)
        path.rename(new_path)  # Datei umbenennen
        print(f"{path.name} -> {new_path.name}")
        count += 1
    print(f"Umbenannt: {count}")


if __name__ == "__main__":
    main()
