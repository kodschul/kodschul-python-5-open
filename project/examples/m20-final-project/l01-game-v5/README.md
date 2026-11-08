# Zahlenraten v5

Zahlenratespiel im Terminal: Das Programm denkt sich eine Zahl, ein Mensch oder der Computer rät, das Spiel antwortet „zu hoch“ oder „zu niedrig“. Bestenliste und alle Runden stehen in einer SQLite-Datenbank (`game.db`), die Bestenliste lässt sich als HTML-Seite mit Diagrammen oder als Excel-Datei exportieren.

## Voraussetzungen

- Python 3.14
- Pakete aus `requirements.txt`

## Installation

Im Ordner, der `guess_game/` enthält:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Spielen

```bash
python -m guess_game                                          # fragt Name, Spieler und Stufe
python -m guess_game --name Anna --level schwer --player mensch
python -m guess_game --resume                                 # gespeichertes Spiel fortsetzen
python -m guess_game --help                                   # alle Optionen
```

Beim Tipp versteht das Spiel auch Befehle:

| Befehl | Wirkung |
| --- | --- |
| `7` | Zahl tippen |
| `hilfe` | alle Befehle zeigen |
| `stufe schwer` | Stufe der nächsten Runde |
| `bestenliste` | Top 10 aus `game.db` |
| `statistik` | Spiele, Gewinnquote und Durchschnittsversuche pro Stufe |
| `speichern` | Spiel in `savegame.pkl` sichern und beenden |
| `quit` | Spiel beenden |

Die Stufen stehen in `guess_game/levels.xml` und lassen sich dort ändern oder ergänzen.

## Werkzeuge

| Befehl | Ergebnis |
| --- | --- |
| `python -m guess_game --export html` | `highscores.html` mit Top 10 und zwei Diagrammen (`chart_tries.png`, `chart_win_rate.png`) |
| `python -m guess_game --export excel` | `highscores.xlsx` |
| `python -m guess_game --backup` | Kopie der Spieldateien in `backups/` (`--dry-run` zeigt nur an) |
| `python migrate_json.py` | alte `highscores.json` einmalig nach `game.db` übernehmen |
| `python import_log.py` | Runden aus `game.log` in die Tabelle `log_rounds` von `game.db` |
| `python analyze.py` | Auswertung mit pandas: Gewinnquote und Median der Versuche pro Stufe und Spieler |
| `python log_report.py . --since 2026-11-01` | Bericht aus den Log-Dateien in `report.txt` |

## Dateien, die beim Spielen entstehen

`game.db`, `game.log`, `history.csv`, `savegame.pkl`, `highscores.html`, `highscores.xlsx`, `chart_tries.png`, `chart_win_rate.png`, `backups/`. Alle stehen in `.gitignore`.

`savegame.pkl` nur selbst erzeugte Dateien laden: pickle kann beim Laden Code ausführen.

## Aufbau

```text
guess_game/
  __main__.py   Start, Optionen (argparse), Logging, Ablauf
  logic.py      Spielregeln: Game, Score, Stufen aus levels.xml
  players.py    HumanPlayer und ComputerPlayer
  ui.py         Ein- und Ausgabe, Befehlsmenü
  storage.py    SQLite-Bestenliste, history.csv, Spielstand, Backup
  export.py     HTML- und Excel-Export
  charts.py     Diagramme mit matplotlib
  levels.xml    Schwierigkeitsstufen
```
