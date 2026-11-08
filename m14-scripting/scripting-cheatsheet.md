# Scripting-Cheatsheet

Schnellreferenz für Modul 14: `collections`, `itertools`, Kommandozeilen-Programme mit `argparse`, Dateisystem mit `pathlib` und `shutil`.

## Zählen und gruppieren (Lab 14.1)

| Syntax | Wirkung |
| --- | --- |
| `from collections import Counter, defaultdict` | Werkzeuge laden |
| `Counter(["a", "b", "a"])` | `Counter({'a': 2, 'b': 1})` |
| `counter["x"]` | Anzahl; fehlender Schlüssel → `0` |
| `counter[x] += 1` | leeren `Counter()` Schritt für Schritt füllen |
| `counter.most_common(3)` | die drei häufigsten als `[(Ding, Anzahl), ...]` |
| `groups = defaultdict(list)` | fehlender Schlüssel → automatisch `[]` |
| `groups[key].append(wert)` | gruppieren ohne `if key in groups` |
| `defaultdict(int)` | fehlender Schlüssel → `0` |
| `liste.extend(andere)` | alle Elemente einzeln anhängen |

## Weitere Sammlungen (Lab 14.1)

| Syntax | Wirkung |
| --- | --- |
| `deque(maxlen=3)` | Warteschlange; beim Anhängen fällt das älteste Element hinaus |
| `Point = namedtuple("Point", ["x", "y"])` | Tupel-Typ mit Feldnamen anlegen |
| `p = Point(3, 4)`; `p.x` | Feld per Name, `p[0]` per Index |

## itertools (Lab 14.1)

| Syntax | Wirkung |
| --- | --- |
| `count(101)` | 101, 102, 103, … ohne Ende |
| `cycle(["Anna", "Ben"])` | Anna, Ben, Anna, … ohne Ende |
| `islice(it, 4)` | nur die ersten 4 Werte |
| `chain(a, b)` | erst alle aus `a`, dann alle aus `b` |
| `groupby(folge)` | direkt aufeinanderfolgende gleiche Werte als Gruppe |
| `combinations(folge, 2)` | alle Paare ohne Wiederholung |
| `product(a, b)` | jede Kombination aus `a` und `b` |
| `list(...)` | Iterator sichtbar machen (nicht bei `count`/`cycle` ohne `islice`) |

## Kommandozeile (Lab 14.2)

| Syntax | Wirkung |
| --- | --- |
| `import sys`; `sys.argv` | Liste der Wörter der Kommandozeile, `[0]` = Skriptname |
| `parser = argparse.ArgumentParser(description=..., epilog=...)` | Parser anlegen |
| `prog="python -m guess_game"` | Programmname in Hilfe und Fehlern |
| `parser.add_argument("folder")` | Positionsargument, Pflicht |
| `parser.add_argument("--name")` | Option; fehlt sie: `None` |
| `default="alt_"` | Standardwert, wenn die Option fehlt |
| `choices=["leicht", "schwer"]` | nur diese Werte erlaubt |
| `help="..."` | Text in `--help` |
| `type=int` | Text in Zahl umwandeln |
| `action="store_true"` | Schalter ohne Wert: `True`, wenn angegeben |
| `args = parser.parse_args()` | auslesen; `args.name`, `args.dry_run` (`-` wird `_`) |
| `parser.error("Text")` | eigene Fehlermeldung, Exit-Code 2 |
| `if args.name is None:` | Option fehlt → nachfragen |

## Exit-Codes und Start (Lab 14.2)

| Syntax | Wirkung |
| --- | --- |
| `sys.exit(1)` | sofort beenden mit Exit-Code 1 (Fehler) |
| `0` / `1` / `2` | Erfolg / eigener Fehler / falsche Kommandozeile (`argparse`) |
| `echo $?` | letzter Exit-Code (macOS/Linux) |
| `$LASTEXITCODE` | letzter Exit-Code (PowerShell) |
| `#!/usr/bin/env python3` + `chmod +x skript.py` | Skript direkt mit `./skript.py` starten (Linux/macOS) |
| `py skript.py` | Start über den Python-Befehl `py` (Windows) |
| `30 7 * * * python backup.py` | cron-Zeile: täglich 7:30 Uhr (Linux/macOS) |

## Ordner lesen und suchen (Lab 14.3)

| Syntax | Wirkung |
| --- | --- |
| `ordner.iterdir()` | alle Einträge, eine Ebene |
| `pfad.is_file()` / `pfad.is_dir()` | Datei? Ordner? |
| `ordner.glob("*.csv")` | Muster, nur dieser Ordner |
| `ordner.rglob("*.csv")` | Muster, alle Unterordner |
| `pfad.name` / `pfad.stem` / `pfad.suffix` | `a.pdf` / `a` / `.pdf` |
| `pfad.stat().st_size` | Größe in Bytes |
| `datetime.fromtimestamp(pfad.stat().st_mtime)` | Änderungszeit als `datetime` |
| `pfad.relative_to(ordner)` | Pfad unterhalb von `ordner` |
| `pfad.resolve()` | vollständiger Pfad ab dem Laufwerk |

## Anlegen, kopieren, verschieben, löschen (Lab 14.3)

| Syntax | Wirkung |
| --- | --- |
| `ordner.mkdir(parents=True, exist_ok=True)` | Ordner samt Eltern anlegen, kein Fehler, wenn vorhanden |
| `quelle.copy(ziel)` | Datei oder ganzen Ordner kopieren (seit 3.14) |
| `quelle.copy_into(ordner)` | in vorhandenen Ordner kopieren (seit 3.14) |
| `quelle.move(ziel)` | verschieben (seit 3.14) |
| `quelle.move_into(ordner)` | in vorhandenen Ordner verschieben (seit 3.14) |
| `quelle.rename(ziel)` | umbenennen |
| `datei.unlink()` | Datei löschen |
| `shutil.rmtree(ordner)` | Ordner samt Inhalt löschen, ohne Papierkorb |
| `shutil.make_archive("name", "zip", ordner)` | ZIP-Archiv eines Ordners |

## Ältere Schreibweisen (steht in älterem Code)

| Alt | Heute |
| --- | --- |
| `os.path.join(a, b)` | `Path(a) / b` |
| `os.path.exists(p)` | `Path(p).exists()` |
| `os.path.getsize(p)` | `Path(p).stat().st_size` |
| `os.listdir(p)` | `Path(p).iterdir()` |
| `shutil.copy(a, b)` | `Path(a).copy(b)` |
| `shutil.copytree(a, b)` | `Path(a).copy(b)` |
| `shutil.move(a, b)` | `Path(a).move(b)` |

## Sicher automatisieren

| Regel | Umsetzung |
| --- | --- |
| keine Rückfragen | alle Angaben als Optionen |
| erst zeigen, dann tun | `--dry-run` mit denselben Ausgabezeilen |
| erst an einer Kopie testen | z. B. `python code/m14-scripting/make_sandbox.py` |
| nichts still überschreiben | `if ziel.exists(): continue` |
| Ergebnis melden | `sys.exit(1)` bei Fehler |
