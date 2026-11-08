# Kurs-Projekt: Zahlenraten

Ein Python-Projekt für den ganzen Kurs: das Zahlenratespiel in allen Ausbaustufen, die Starter-Dateien der Übungen, kurze Beispiele zu jedem Thema und ein Arbeitsbereich. Handouts und Aufgaben liegen eine Ebene höher: [`../README.md`](../README.md).

## Start

Voraussetzung: Python 3.14 und VS Code, siehe [`../00-setup-and-installation.md`](../00-setup-and-installation.md). Alle Befehle laufen im Terminal von VS Code im Ordner `project/`.

```bash
python -m venv .venv                 # virtuelle Umgebung anlegen (einmal)
source .venv/bin/activate            # macOS/Linux
.venv\Scripts\Activate.ps1           # Windows (PowerShell)
pip install -r requirements.txt      # alle Kurspakete installieren (einmal)
python playground/hello.py           # Test: gibt „Hallo“ aus
```

Nach dem Aktivieren steht `(.venv)` vor der Eingabezeile. Ab dann ist `python` auf allen Systemen derselbe Befehl.

## Ordner

```text
project/
├── code/<modul>/        kurze Beispiele zu jedem Thema, einzeln startbar
├── examples/<modul>/<lab>/  fertiger Spielstand nach jedem Lab (guess_game.py, ab 6.1 Paket guess_game/)
├── starters/            Starter je Übung: mNN-lNN-guess_game.py bzw. Ordner mNN-lNN-guess_game/
├── playground/          Arbeitsbereich: hier entsteht das eigene Spiel
├── data/                Beispieldateien der Demos
├── .vscode/launch.json  Debugger-Konfiguration (Lab 7.4)
└── requirements.txt     alle Pakete des Kurses, fest gepinnt
```

| Ordner | Regel |
| --- | --- |
| `code/` | lesen, starten, verändern; z. B. `python code/m03-control-flow/christmas_tree.py` |
| `starters/` | bis Lab 5.3 eine Datei mit dem ganzen Spiel, die nach `playground/guess_game.py` kopiert wird; Lab 6.1 ein Ordner mit dem neuen Paket, der als `playground/guess_game/` kopiert wird. Ab Lab 6.2 enthält ein Starter-Ordner nur die Dateien, die das Lab ändert oder neu anlegt (mit `TODO`-Kommentaren); sie werden in `playground/guess_game/` kopiert und ersetzen die vorhandenen. Ohne eigenen Stand vorher `guess_game/` aus `examples/` des vorherigen Labs nach `playground/` kopieren |
| `playground/` | eigene Arbeit; bis Lab 5.3 `python playground/guess_game.py`, ab Lab 6.1 `cd playground` und `python -m guess_game` |
| `examples/` | fertige Lösung zum Vergleichen; Einzeldatei: `python examples/m04-collections/l03-dictionaries/guess_game.py`; Paket: `cd examples/m08-files/l03-csv`, danach `python -m guess_game` |
| `data/` | Beispieldateien der Demos (Text, JSON, CSV, HTML, Excel, `store.db`, Logs, Testordner `messy_downloads/`); nicht verändern, die Demos arbeiten auf Kopien |
| `.vscode/launch.json` | Debug-Konfigurationen für Lab 7.4 (Spiel im `playground/` und aktuelle Datei) |

## Lab → Beispiel → Starter

Labs ohne Spielschritt (1.1, 1.2, 7.1, 7.4, 9.1, 10.4, 11.4, 15.1, 16.1, 18.1, 20.2) fehlen in der Tabelle; 7.4 nutzt den absichtlich fehlerhaften Starter `m07-l04-guess_game/ui.py`. Ab Lab 6.2 nennt die Spalte Starter nur die Dateien, die das Lab ändert oder neu anlegt; der vollständige Stand davor liegt in `examples/` eine Zeile weiter oben.

| Lab | Spiel kann danach | Beispiel (`examples/`) | Starter (`starters/`) |
| --- | --- | --- | --- |
| 2.1 | Begrüßungsbanner | `m02-basics/l01-syntax/` | `m02-l01-guess_game.py` |
| 2.2 | Name und Tipp abfragen | `m02-basics/l02-variables/` | `m02-l02-guess_game.py` |
| 2.3 | Tipp mit Geheimzahl vergleichen | `m02-basics/l03-operators/` | `m02-l03-guess_game.py` |
| 2.4 | Spielername aufräumen | `m02-basics/l04-strings/` | `m02-l04-guess_game.py` |
| 3.1 | „zu hoch / zu niedrig / richtig“ | `m03-control-flow/l01-conditions/` | `m03-l01-guess_game.py` |
| 3.2 | zufällige Geheimzahl | `m03-control-flow/l02-random/` | `m03-l02-guess_game.py` |
| 3.3 | drei Versuche | `m03-control-flow/l03-loops/` | `m03-l03-guess_game.py` |
| 3.4 | mehrere Runden, Versuchszähler | `m03-control-flow/l04-combining/` | `m03-l04-guess_game.py` |
| 4.1 | Liste der Tipps | `m04-collections/l01-lists/` | `m04-l01-guess_game.py` |
| 4.2 | Zahlenbereich, doppelte Tipps erkennen | `m04-collections/l02-tuples-sets/` | `m04-l02-guess_game.py` |
| 4.3 | **v1:** drei Schwierigkeitsstufen | `m04-collections/l03-dictionaries/` | `m04-l03-guess_game.py` |
| 5.1 | Spiel in Funktionen zerlegt | `m05-functions/l01-basics/` | `m05-l01-guess_game.py` |
| 5.2 | Runde als Funktion mit Rückgabewert | `m05-functions/l02-parameters/` | `m05-l02-guess_game.py` |
| 5.3 | ohne globale Variablen | `m05-functions/l03-runtime/` | `m05-l03-guess_game.py` |
| 6.1 | Paket `guess_game/`, Start mit `python -m guess_game` | `m06-modules/l01-modules/` | `m06-l01-guess_game`, `m06-l01-guess_game.py` |
| 6.2 | farbige Hinweise mit `rich` | `m06-modules/l02-pypi/` | `m06-l02-guess_game/`: `ui.py` |
| 6.3 | Spieldauer und Datum | `m06-modules/l03-datetime/` | `m06-l03-guess_game/`: `__main__.py`, `ui.py` |
| 7.2 | stürzt bei falscher Eingabe nicht ab | `m07-exceptions/l02-try-except/` | `m07-l02-guess_game/`: `__main__.py`, `ui.py` |
| 7.3 | Tipps außerhalb des Bereichs abgelehnt | `m07-exceptions/l03-raise/` | `m07-l03-guess_game/`: `logic.py`, `ui.py` |
| 8.1 | Ergebnisse in `scores.txt` | `m08-files/l01-text-files/` | `m08-l01-guess_game/`: `__main__.py` |
| 8.2 | Bestenliste in `highscores.json` | `m08-files/l02-json/` | `m08-l02-guess_game/`: `__main__.py`, `storage.py`, `ui.py` |
| 8.3 | **v2:** Spielverlauf in `history.csv` | `m08-files/l03-csv/` | `m08-l03-guess_game/`: `__main__.py`, `storage.py` |
| 9.2 | Klasse `Game` | `m09-oop-basics/l02-classes/` | `m09-l02-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 9.3 | geschützte Geheimzahl, Properties | `m09-oop-basics/l03-encapsulation/` | `m09-l03-guess_game/`: `logic.py`, `ui.py` |
| 10.1 | `Player`, `HumanPlayer`, eigene Exception | `m10-class-relations/l01-inheritance/` | `m10-l01-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 10.2 | `ComputerPlayer` rät mit | `m10-class-relations/l02-polymorphism/` | `m10-l02-guess_game/`: `__main__.py`, `players.py`, `ui.py` |
| 10.3 | `Scoreboard` übernimmt die Bestenliste | `m10-class-relations/l03-composition/` | `m10-l03-guess_game/`: `__main__.py`, `logic.py`, `storage.py`, `ui.py` |
| 11.1 | `Score` sortierbar und lesbar | `m11-advanced-oop/l01-magic-methods/` | `m11-l01-guess_game/`: `__main__.py`, `logic.py`, `storage.py`, `ui.py` |
| 11.2 | `Score` als Dataclass | `m11-advanced-oop/l02-dataclasses/` | `m11-l02-guess_game/`: `logic.py`, `storage.py` |
| 11.3 | abstrakter `Player` | `m11-advanced-oop/l03-abstraction/` | `m11-l03-guess_game/`: `players.py` |
| 12.1 | Statistik per Comprehension | `m12-functional/l01-comprehensions/` | `m12-l01-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 12.2 | Bestenliste umschaltbar sortiert | `m12-functional/l02-lambda/` | `m12-l02-guess_game/`: `__main__.py`, `logic.py`, `storage.py`, `ui.py` |
| 12.3 | **v3:** Runden als Generator | `m12-functional/l03-generators/` | `m12-l03-guess_game/`: `__main__.py`, `ui.py` |
| 13.1 | Zeitmessung per `@timed` | `m13-pythonic/l01-decorators/` | `m13-l01-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 13.2 | Bestenliste per `with` gespeichert | `m13-pythonic/l02-context-managers/` | `m13-l02-guess_game/`: `__main__.py`, `storage.py` |
| 13.3 | Befehlsmenü per `match` | `m13-pythonic/l03-pattern-matching/` | `m13-l03-guess_game/`: `__main__.py`, `logic.py`, `players.py`, `ui.py` |
| 14.1 | häufigste Tipps der Sitzung | `m14-scripting/l01-collections-itertools/` | `m14-l01-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 14.2 | Optionen `--name`, `--level`, `--player` | `m14-scripting/l02-argparse/` | `m14-l02-guess_game/`: `__main__.py`, `ui.py` |
| 14.3 | `--backup` mit Rotation | `m14-scripting/l03-filesystem/` | `m14-l03-guess_game/`: `__main__.py`, `storage.py`, `ui.py` |
| 15.2 | Namensprüfung per Regex | `m15-system/l02-regex/` | `m15-l02-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 15.3 | Log-Datei `game.log`, `--verbose` | `m15-system/l03-logging/` | `m15-l03-guess_game/`: `__main__.py`, `logic.py`, `ui.py` |
| 16.2 | Bestenliste per HTTP lesen (`fetch_scores.py`) | `m16-automation/l02-server/` | – (Paket unverändert) |
| 16.3 | **v4:** Auswertungsskript `log_report.py` | `m16-automation/l03-report/` | `m16-l03-log_report.py` |
| 17.1 | Stufen aus `levels.xml`, HTML-Export | `m17-data-formats/l01-xml-html/` | `m17-l01-guess_game/`: `__main__.py`, `export.py`, `levels.xml`, `logic.py`, `ui.py` |
| 17.2 | Excel-Export | `m17-data-formats/l02-excel/` | `m17-l02-guess_game/`: `__main__.py`, `export.py` |
| 17.3 | `speichern` und `--resume` | `m17-data-formats/l03-pickle/` | `m17-l03-guess_game/`: `__main__.py`, `logic.py`, `storage.py`, `ui.py` |
| 18.2 | Runden in `game.db` | `m18-sqlite/l02-sqlite3/` | `m18-l02-guess_game/`: `__main__.py`, `storage.py` |
| 18.3 | `bestenliste`, `statistik`, `migrate_json.py` | `m18-sqlite/l03-queries/` | `m18-l03-guess_game/`: `storage.py`, `ui.py` |
| 19.1 | Log-Import `import_log.py` | `m19-data-analysis/l01-multiline-regex/` | `m19-l01-import_log.py` |
| 19.2 | Auswertung `analyze.py` | `m19-data-analysis/l02-pandas/` | – (Paket unverändert) |
| 19.3 | Diagramme im HTML-Export | `m19-data-analysis/l03-matplotlib/` | – (`charts.py` entsteht ohne Vorlage) |
| 20.1 | **v5:** komplettes Spiel mit README | `m20-final-project/l01-game-v5/` | – (README und `requirements.txt` entstehen ohne Vorlage) |

## Pakete

| Paket | Wofür | ab Lab |
| --- | --- | --- |
| `rich` | farbige Ausgabe im Terminal | 6.2 |
| `requests` | HTTP-Anfragen | 16.1 |
| `beautifulsoup4` | HTML lesen | 17.1 |
| `openpyxl` | Excel-Dateien | 17.2 |
| `regex` | erweiterte reguläre Ausdrücke | 15.2 |
| `numpy`, `pandas` | Daten auswerten | 19.2 |
| `matplotlib` | Diagramme | 19.3 |

Versionen: [`requirements.txt`](requirements.txt), Stand 08.11.2026, getestet mit Python 3.14.
