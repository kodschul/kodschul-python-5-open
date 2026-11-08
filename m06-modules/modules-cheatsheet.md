# Module-Cheatsheet

Schnellreferenz für Modul 6 (eigene Module und Pakete, Standardbibliothek, PyPI und pip, Datum und Zeit).

## Importieren

| Syntax | Wirkung |
| --- | --- |
| `import math_tools` | ganzes Modul laden; Aufruf `math_tools.add(1, 2)` |
| `import math_tools as mt` | ganzes Modul unter Kurznamen; Aufruf `mt.add(1, 2)` |
| `from math_tools import add` | nur einen Namen holen; Aufruf `add(1, 2)` |
| `from math_tools import add, subtract` | mehrere Namen auf einmal |
| `from guess_game import logic` | Modul aus einem Paket; Aufruf `logic.LEVELS` |
| `from helpers.percent import percent_of` | Funktion aus einem Modul eines Pakets |
| Reihenfolge der Importe | Standardbibliothek, externe Pakete, eigenes Paket; je Gruppe eine Leerzeile |

## Modul, Paket, Startdatei

| Datei / Ordner | Rolle |
| --- | --- |
| `math_tools.py` | Modul: jede `.py`-Datei, Modulname = Dateiname ohne `.py` |
| `guess_game/` mit `__init__.py` | Paket: Ordner mit Modulen |
| `__init__.py` | macht den Ordner zum Paket; im Kurs nur ein Docstring |
| `__main__.py` | Startdatei des Pakets, läuft bei `python -m guess_game` |
| `__pycache__/` | vorübersetzte Dateien von Python; ignorieren, darf gelöscht werden |

## Start und Programmstruktur

| Syntax | Wirkung |
| --- | --- |
| `if __name__ == "__main__":` | Block läuft nur beim direkten Start, nicht beim Import |
| `__name__` | `"__main__"` beim Start, sonst der Modulname (`"math_tools"`) |
| Aufbau einer Datei | `import` → Konstanten → Funktionen → Startblock |

## Terminal

| Befehl | Wirkung |
| --- | --- |
| `cd playground` | Terminal wechselt in den Ordner `playground/` |
| `cd ..` | eine Ordner-Ebene zurück |
| `python -m guess_game` | Paket `guess_game` aus dem aktuellen Ordner starten |
| `python -c "from guess_game import logic; print(logic.LEVELS)"` | eine Zeile Python ohne Datei ausführen |
| `python -m rich` | Vorführung aller Fähigkeiten von `rich` |

## Standardbibliothek (ohne Installation)

| Modul | Beispiel |
| --- | --- |
| `math` | `math.sqrt(16)` → `4.0`, `math.pi` |
| `random` | `random.randint(1, 10)`, `random.choice(["a", "b"])` |
| `datetime` | `date.today()`, `datetime.now()` |
| `pathlib` | `Path("requirements.txt").exists()` |
| `json` | `json.dumps({"tries": 3})` → `'{"tries": 3}'` |
| `os` | `os.name` → `'nt'` (Windows) oder `'posix'` |
| `time` | `time.time()`, `time.perf_counter()` |
| `zoneinfo` | `ZoneInfo("Europe/Berlin")` |

## pip (venv aktiv)

| Befehl | Wirkung |
| --- | --- |
| `pip install rich` | neueste Version von PyPI installieren |
| `pip install rich==15.0.0` | genau diese Version installieren |
| `pip install -r requirements.txt` | alle Pakete aus der Datei installieren |
| `pip install --upgrade rich` | auf die neueste Version aktualisieren |
| `pip list` | installierte Pakete mit Version |
| `pip show rich` | Version, Lizenz, Speicherort, Abhängigkeiten |
| `pip freeze` | installierte Pakete im Format `name==version` |
| `pip freeze > requirements.txt` | diese Liste in eine Datei schreiben |
| `pip uninstall rich` | Paket entfernen |
| `python -m pip …` | wie `pip …`, sicher mit dem aktiven `python` |

## requirements.txt

| Zeile | Bedeutung |
| --- | --- |
| `rich==15.0.0` | Paket in genau dieser Version (gepinnt) |
| `# Kommentar` | wird ignoriert |
| eine Zeile pro Paket | Abhängigkeiten installiert pip automatisch mit |

## Paket vor der Installation prüfen

| Prüfen | Wo |
| --- | --- |
| exakter Name (kein Typo-Squatting) | Doku des Pakets, pypi.org |
| Downloads, aktuelle Version | pypi.org: Badges, „Release history“ |
| Quellcode, Lizenz | pypi.org: „Project links“, „Meta“ |

## rich

| Syntax | Wirkung |
| --- | --- |
| `from rich.console import Console` | Ausgabe-Werkzeug importieren |
| `console = Console()` | Ausgabe-Werkzeug anlegen (einmal pro Modul) |
| `console.print("Zu hoch.", style="red")` | ganze Zeile farbig |
| `style="bold green"` | Stile kombinieren: `bold`, `italic`, Farben `red`, `green`, `blue`, `yellow`, `cyan`, `magenta` |
| `console.print("[yellow]gelb[/yellow]")` | Markup: Teil einer Zeile färben (Vorsicht bei `[` im Text) |
| `from rich.table import Table` | Tabellen-Werkzeug importieren |
| `table = Table(title="…")` | Tabelle anlegen |
| `table.add_column("Stufe")` | Spalte anlegen |
| `table.add_row("leicht", "1 bis 10")` | Zeile anfügen (nur Text) |
| `console.print(table)` | Tabelle ausgeben |

## Datum und Zeit

| Syntax | Wirkung |
| --- | --- |
| `from datetime import date, datetime, timedelta` | Typen importieren |
| `datetime.now()` | jetzt: Datum und Uhrzeit |
| `date.today()` | heute: nur Datum |
| `date(2027, 2, 15)` | bestimmtes Datum |
| `today + timedelta(days=14)` | Datum verschieben |
| `(exam - today).days` | Tage zwischen zwei Daten |
| `now.strftime("%d.%m.%Y, %H:%M")` | Datum → Text: `08.11.2026, 14:05` |
| `datetime.strptime("03.04.2026", "%d.%m.%Y")` | Text → Datum |
| `today.isoformat()` | ISO-Format: `2026-11-08` |
| `dt.date()` | `datetime` → `date` |
| `birthday.replace(year=2027)` | neues Datum mit anderem Jahr |
| `d.weekday()` | Wochentag als Zahl, 0 = Montag |
| `datetime.now(ZoneInfo("Europe/Berlin"))` | jetzt in einer Zeitzone |
| `dt.astimezone(ZoneInfo("Asia/Tokyo"))` | gleicher Moment in anderer Zeitzone |

## Formatcodes (strftime, strptime)

| Code | Bedeutung |
| --- | --- |
| `%d` / `%m` / `%Y` | Tag / Monat / Jahr (vierstellig) |
| `%y` | Jahr zweistellig |
| `%H` / `%M` / `%S` | Stunde / Minute / Sekunde |
| `%A` / `%B` | Wochentag / Monatsname (englisch) |

## Dauer messen und Zahlen formatieren

| Syntax | Wirkung |
| --- | --- |
| `time.time()` | Unix-Zeit: Sekunden seit 01.01.1970 |
| `start = time.perf_counter()` | Stoppuhr starten |
| `time.perf_counter() - start` | vergangene Sekunden |
| `round(seconds, 1)` | Zahl auf eine Nachkommastelle runden |
| `f"{seconds:.1f}"` | Text mit genau einer Nachkommastelle: `'12.4'` |
| `f"{x:.2f}"` | Text mit zwei Nachkommastellen |
| `f"{seconds:.1f}".replace(".", ",")` | deutsches Dezimalkomma: `'12,4'` |
