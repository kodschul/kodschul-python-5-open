# Betriebssystem und Textwerkzeuge – Cheatsheet

Schnellreferenz für Modul 15: System abfragen, Umgebungsvariablen, `subprocess`, reguläre Ausdrücke mit `re` und `regex`, `logging`.

## System abfragen (Lab 15.1)

| Aufruf | Wirkung |
| --- | --- |
| `platform.system()`, `platform.release()` | Betriebssystem und Version: `'Windows'`, `'Darwin'`, `'Linux'` |
| `platform.python_version()` | Python-Version als Text, z. B. `'3.14.2'` |
| `sys.platform` | Kurzname für `if`: `'win32'`, `'darwin'`, `'linux'` |
| `sys.executable` | Pfad des laufenden Python (auch in `.venv`) |
| `os.getcwd()` | aktueller Arbeitsordner |
| `shutil.disk_usage(".")` | `total`, `used`, `free` in Byte für das Laufwerk |
| `os.pathsep` | Trenner in `PATH`: `;` (Windows) oder `:` |

## Umgebungsvariablen (Lab 15.1)

| Befehl | Wirkung |
| --- | --- |
| `os.environ["PATH"]` | Wert lesen; fehlt er: `KeyError` |
| `os.getenv("APP_MODE")` | Wert oder `None` |
| `os.getenv("APP_MODE", "normal")` | Wert oder Standardwert |
| `$env:DEMO_TOKEN = "abc12345"` | setzen in PowerShell (nur dieses Terminal) |
| `export DEMO_TOKEN=abc12345` | setzen in bash/zsh (nur dieses Terminal) |
| `Remove-Item Env:DEMO_TOKEN` / `unset DEMO_TOKEN` | entfernen |

## Programme starten (Lab 15.1)

| Syntax | Wirkung |
| --- | --- |
| `subprocess.run([sys.executable, "--version"])` | Programm starten und warten; Befehl als Liste |
| `capture_output=True, text=True` | Ausgabe als Text in `result.stdout` / `result.stderr` |
| `check=True` | Rückgabecode ≠ 0 → `subprocess.CalledProcessError` |
| `timeout=10` | nach 10 s abbrechen → `subprocess.TimeoutExpired` |
| `result.returncode` | Rückgabecode, `0` = Erfolg |
| `except FileNotFoundError` | Programm existiert nicht |
| `"-n" if sys.platform == "win32" else "-c"` | Option je System wählen |
| nie: `shell=True` mit Eingaben | Gefahr: Shell-Injection |

## Muster-Zeichen (Lab 15.2)

| Muster | passt auf |
| --- | --- |
| `.` | ein beliebiges Zeichen (außer Zeilenumbruch) |
| `\d` / `\D` | Ziffer / keine Ziffer |
| `\w` | Buchstabe (auch Umlaute), Ziffer, `_` |
| `\s` / `\S` | Leerraum / kein Leerraum |
| `[abc]`, `[A-Z]`, `[^0-9]` | ein Zeichen aus Liste, Bereich, nicht aus Liste |
| `+`, `*`, `?` | 1+-mal, 0+-mal, 0- oder 1-mal |
| `{4}`, `{2,20}`, `{5,}` | genau 4, 2 bis 20, mindestens 5 |
| `^`, `$`, `\b` | Anfang, Ende, Wortgrenze |
| `a\|b` | `a` oder `b` |
| `(...)`, `(?P<name>...)` | Gruppe, benannte Gruppe |
| `\.`, `\(`, `\+` | Sonderzeichen selbst |
| `r"\d+"` | Raw-String: Muster immer mit `r` |

## Funktionen aus re (Lab 15.2)

| Aufruf | Wirkung |
| --- | --- |
| `re.search(p, text)` | erster Treffer irgendwo oder `None` |
| `re.match(p, text)` | Treffer nur am Anfang oder `None` |
| `re.fullmatch(p, text)` | ganzer Text passt oder `None` (prüfen) |
| `re.findall(p, text)` | Liste aller Treffer (mit Gruppen: Tupel) |
| `re.finditer(p, text)` | Match-Objekte für `for` |
| `re.sub(p, "x", text)` | Treffer ersetzen |
| `re.compile(p)` | Muster-Objekt: `PATTERN.fullmatch(text)` |
| `re.findall(p, text, re.IGNORECASE)` | Groß/klein egal |
| `match.group()`, `match.group("year")` | ganzer Treffer, eine Gruppe |
| `match.groupdict()` | alle benannten Gruppen als Dictionary |
| `regex.findall(r"\p{L}+", text)` | Paket `regex`: Buchstaben aller Sprachen |

## Regex oder nicht? (Lab 15.2)

| Aufgabe | Werkzeug |
| --- | --- |
| fester Text enthalten | `"Fehler" in line` |
| fester Anfang/Ende | `startswith`, `endswith` |
| fester Trenner | `split`, `csv` |
| Form prüfen | `fullmatch` |
| Angaben aus Fließtext | `findall`, `finditer`, Gruppen |

## Im Spiel (Lab 15.2)

| Code | Wirkung |
| --- | --- |
| `NAME_PATTERN = re.compile(r"^[A-Za-zÄÖÜäöüß]{2,20}$")` | 2 bis 20 Buchstaben |
| `logic.is_valid_name("Anna1")` | `False` |
| `logic.parse_log_line(line)` | Dictionary aus einer Ergebniszeile oder `None` |

## logging einrichten (Lab 15.3)

| Code | Wirkung |
| --- | --- |
| `logging.basicConfig(level=logging.INFO)` | einmal am Start: Mindest-Level |
| `format="%(asctime)s %(levelname)s %(name)s: %(message)s"` | Zeile mit Zeit, Level, Logger, Text |
| `datefmt="%Y-%m-%d %H:%M:%S"` | Form des Zeitstempels |
| `filename="app.log", encoding="utf-8"` | in Datei statt Terminal |
| `handlers=[logging.FileHandler(...), logging.StreamHandler()]` | mehrere Ziele |
| `logger = logging.getLogger(__name__)` | ein Logger pro Modul |
| `handler.setLevel(logging.WARNING)` | eigenes Level pro Ziel |
| `RotatingFileHandler("app.log", maxBytes=..., backupCount=3)` | Datei begrenzen |

## Meldungen (Lab 15.3)

| Aufruf | Level, Einsatz |
| --- | --- |
| `logger.debug(...)` | DEBUG: Details zur Fehlersuche |
| `logger.info(...)` | INFO: Start, Ergebnis, Ende |
| `logger.warning(...)` | WARNING: unerwartet, läuft weiter |
| `logger.error(...)` | ERROR: Aufgabe gescheitert |
| `logger.critical(...)` | CRITICAL: Programm kann nicht weiter |
| `logger.exception(...)` | im `except`: ERROR plus Traceback |
| `python -m guess_game --verbose` | Spiel: Protokoll auch im Terminal |
