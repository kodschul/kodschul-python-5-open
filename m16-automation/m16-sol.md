# Modul 16 – Transferlösung: Lernzeit-Bericht

Vollständige Lösung für `playground/study_report.py`. Die Aufgaben sind im Code mit Kommentaren markiert; danach folgen die Testläufe. Der Aufbau folgt `log_report.py` aus Lab 16.3: Argumente → Dateien finden → Zeilen auswerten → Bericht → Exit-Code.

## Aufgaben 1 bis 4: Vollständiges Skript

```python
# Lernzeit-Bericht: wertet alle study*.log eines Ordners aus
# Start im Ordner project/:
#   python playground/study_report.py data/study --since 2026-11-01
# Ablauf: Argumente -> Dateien finden -> Zeilen auswerten -> Bericht -> Exit-Code

import argparse
import logging
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

# Beispielzeile: 2026-11-03 19:00 Programmieren 90 min
LINE_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2}) \d{2}:\d{2} (?P<subject>\w+) (?P<minutes>\d+) min$"
)
logger = logging.getLogger("study_report")


# Aufgabe 1: Optionen
def parse_args():
    """Liest Ordner, --since und --subject aus der Kommandozeile."""
    parser = argparse.ArgumentParser(description="Summiert Lernzeiten aus study*.log.")
    parser.add_argument("folder", type=Path, help="Ordner mit den Lern-Logs")
    parser.add_argument(
        "--since", type=date.fromisoformat, help="nur Einträge ab JJJJ-MM-TT"
    )
    parser.add_argument("--subject", help="nur dieses Fach, z. B. Mathe")
    return parser.parse_args()


# Aufgabe 2: eine Zeile zerlegen
def parse_line(line):
    """Gibt (Datum, Fach, Minuten) zurück oder None, wenn die Zeile nicht passt."""
    match = LINE_PATTERN.search(line.strip())
    if match is None:
        return None
    day = date.fromisoformat(match.group("date"))
    return day, match.group("subject"), int(match.group("minutes"))


def as_hours(minutes):
    """135 -> '2 h 15 min'."""
    return f"{minutes // 60} h {minutes % 60} min"


def main():
    """Ablauf; Exit-Code 1, wenn es nichts auszuwerten gibt."""
    logging.basicConfig(
        filename="study_report.log",
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    args = parse_args()
    logger.info(f"Start: {args.folder}, seit {args.since}, Fach {args.subject}")

    # Aufgabe 3: Ordner prüfen, Dateien finden
    if not args.folder.is_dir():
        logger.error(f"Ordner fehlt: {args.folder}")
        print(f"Ordner nicht gefunden: {args.folder}")
        sys.exit(1)
    paths = sorted(args.folder.glob("study*.log"))
    if not paths:
        logger.warning(f"Keine study*.log in {args.folder}")
        print(f"Keine study*.log in {args.folder} gefunden.")
        sys.exit(1)

    # Aufgabe 4: Minuten pro Fach summieren
    minutes = Counter()
    for path in paths:
        with open(path, encoding="utf-8") as file:
            for line in file:
                entry = parse_line(line)
                if entry is None:
                    logger.warning(f"Zeile übersprungen in {path.name}: {line.strip()}")
                    continue
                day, subject, duration = entry
                if args.since is not None and day < args.since:
                    continue
                if args.subject is not None and subject != args.subject:
                    continue
                minutes[subject] += duration  # fehlendes Fach startet bei 0

    period = f"seit {args.since}" if args.since is not None else "gesamt"
    print(f"Lernzeit {period} ({len(paths)} Dateien)")
    for subject, total in minutes.most_common():  # meiste Zeit zuerst
        print(f"  {subject}: {as_hours(total)}")
    print(f"Summe: {as_hours(sum(minutes.values()))}")
    logger.info(f"{len(paths)} Dateien, {sum(minutes.values())} Minuten")


if __name__ == "__main__":
    main()
```

- `type=date.fromisoformat` prüft das Datum schon beim Start; `day < args.since` vergleicht zwei `date`-Objekte (Lab 6.3).
- Das Muster endet mit `$`: `2026-11-03 Mathe lange gelernt` passt nicht und landet als `WARNING` im Log, statt das Skript abzubrechen.
- `Counter()` beginnt leer; `minutes[subject] += duration` funktioniert auch beim ersten Eintrag eines Fachs, weil ein fehlender Schlüssel als 0 zählt (Lab 14.1).
- `study_report.log` passt nicht zu `study*.log`, solange das Skript im Ordner `project/` startet und die Daten in `data/study/` liegen. Läge das eigene Log im ausgewerteten Ordner, würde das Skript es mitlesen; deshalb ein Name, der nicht zum Muster passt, oder ein anderer Ordner.

## Testläufe (Aufgabe 5)

```text
$ python playground/study_report.py data/study --since 2026-11-01
Lernzeit seit 2026-11-01 (2 Dateien)
  Englisch: 3 h 40 min
  Programmieren: 3 h 15 min
  Mathe: 3 h 5 min
  Statistik: 2 h 10 min
Summe: 12 h 10 min
$ python playground/study_report.py data/study
Lernzeit gesamt (2 Dateien)
  Englisch: 5 h 45 min
  Programmieren: 4 h 45 min
  Statistik: 4 h 10 min
  Mathe: 3 h 25 min
Summe: 18 h 5 min
$ python playground/study_report.py data/study --subject Mathe
Lernzeit gesamt (2 Dateien)
  Mathe: 3 h 25 min
Summe: 3 h 25 min
$ python playground/study_report.py data/stduy
Ordner nicht gefunden: data/stduy
$ python playground/study_report.py data
Keine study*.log in data gefunden.
$ python playground/study_report.py data/study --since morgen
usage: study_report.py [-h] [--since SINCE] [--subject SUBJECT] folder
study_report.py: error: argument --since: invalid fromisoformat value: 'morgen'
```

| Aufruf | Exit-Code |
| --- | --- |
| `data/study --since 2026-11-01`, `data/study`, `data/study --subject Mathe` | `0` |
| `data/stduy` (Tippfehler), `data` (keine `study*.log`) | `1` |
| `--since morgen` | `2` (argparse) |

Der Ordner `data` enthält zwar Dateien, aber keine, die mit `study` beginnt: `glob` sucht nur im angegebenen Ordner, nicht in Unterordnern (dafür gäbe es `rglob`, Lab 14.3).

`study_report.log` nach den ersten fünf Läufen:

```text
2026-11-08 02:46:38 INFO study_report: Start: data/study, seit 2026-11-01, Fach None
2026-11-08 02:46:38 WARNING study_report: Zeile übersprungen in study_2026-11.log: 2026-11-03 Mathe lange gelernt
2026-11-08 02:46:38 INFO study_report: 2 Dateien, 730 Minuten
2026-11-08 02:46:38 INFO study_report: Start: data/study, seit None, Fach None
2026-11-08 02:46:38 WARNING study_report: Zeile übersprungen in study_2026-11.log: 2026-11-03 Mathe lange gelernt
2026-11-08 02:46:38 INFO study_report: 2 Dateien, 1085 Minuten
2026-11-08 02:46:38 INFO study_report: Start: data/study, seit None, Fach Mathe
2026-11-08 02:46:38 WARNING study_report: Zeile übersprungen in study_2026-11.log: 2026-11-03 Mathe lange gelernt
2026-11-08 02:46:38 INFO study_report: 2 Dateien, 205 Minuten
2026-11-08 02:46:39 INFO study_report: Start: data/stduy, seit None, Fach None
2026-11-08 02:46:39 ERROR study_report: Ordner fehlt: data/stduy
2026-11-08 02:46:39 INFO study_report: Start: data, seit None, Fach None
2026-11-08 02:46:39 WARNING study_report: Keine study*.log in data
```

Der Lauf mit `--since morgen` hinterlässt keine Zeile: argparse beendet das Skript, bevor die `Start:`-Zeile geschrieben wird.

## Erweiterung

```python
    parser.add_argument(
        "--report", action="store_true", help="Bericht auch in study_report.txt"
    )
```

Am Ende von `main()` entsteht der Bericht als Liste von Zeilen, die ausgegeben und bei `--report` gespeichert wird:

```python
    period = f"seit {args.since}" if args.since is not None else "gesamt"
    lines = [f"Lernzeit {period} ({len(paths)} Dateien)"]
    for subject, total in minutes.most_common():  # meiste Zeit zuerst
        lines.append(f"  {subject}: {as_hours(total)}")
    lines.append(f"Summe: {as_hours(sum(minutes.values()))}")
    for line in lines:
        print(line)
    if args.report:
        with open("study_report.txt", "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        print("Gespeichert in study_report.txt")
```

```text
$ python playground/study_report.py data/study --since 2026-11-01 --report
Lernzeit seit 2026-11-01 (2 Dateien)
  Englisch: 3 h 40 min
  Programmieren: 3 h 15 min
  Mathe: 3 h 5 min
  Statistik: 2 h 10 min
Summe: 12 h 10 min
Gespeichert in study_report.txt
```

`study_report.txt` enthält danach dieselben sechs Zeilen wie die Ausgabe ohne die letzte Meldung.
