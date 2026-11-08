# Lab 8.2 – Übung: Bestenliste in highscores.json

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `highscores.json` ersetzt `scores.txt`; nach jedem Gewinn zeigt das Spiel die Top 5, auch nach einem Neustart. Lab 8.3 ergänzt `history.csv`.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `storage.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m08-l02-guess_game/` mit `__main__.py`, `storage.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 8.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m08-files/l01-text-files/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m08-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Eine vorhandene `playground/scores.txt` wird nicht mehr gebraucht und darf gelöscht werden.

## Aufgaben

1. Ersetze in `storage.py` die Konstante `SCORES_FILE` und die Funktion `append_score` durch `HIGHSCORES_FILE = Path("highscores.json")` und `import json`. Schreibe `load_highscores()`: Gibt es die Datei nicht, liefert sie eine leere Liste, sonst den Inhalt per `json.load`.
2. Schreibe `save_highscore(result)`: alle Ergebnisse laden, `result` anhängen, die ganze Liste mit `json.dump(..., indent=2, ensure_ascii=False)` im Modus `"w"` zurückschreiben.
3. Schreibe `get_tries(score)` (liefert `score["tries"]`) und `top_five()`: lädt alle Ergebnisse, sortiert sie mit `sorted(..., key=get_tries)` und gibt die ersten fünf zurück.
4. Schreibe in `ui.py` die Funktion `show_highscores(scores)`: Die Funktion gibt eine Leerzeile und `Bestenliste (Top 5)` aus, danach je Ergebnis eine Zeile `1. Anna · Versuche: 3 · 12,4 s · leicht`. Zähle den Platz mit einer eigenen Variable `place` hoch; die Dauer formatiert `format_seconds`.
5. Ersetze in `__main__.py` bei einem Gewinn den Aufruf von `append_score` und die Meldung `Gespeichert in …` durch `storage.save_highscore(result)` und `ui.show_highscores(storage.top_five())`. Gewinne zwei Runden, beende das Spiel, starte neu, gewinne erneut und öffne `playground/highscores.json`.

## Checkpoint

- Nach jedem Gewinn erscheint die Bestenliste, sortiert nach den wenigsten Versuchen.
- Nach dem Neustart enthält die Bestenliste auch die Runden der vorherigen Sitzung.
- `highscores.json` ist eingerückt, Umlaute erscheinen als Umlaute, jedes Ergebnis hat die Felder `name`, `level`, `tries`, `seconds`, `won`, `date`.
- Mit mehr als fünf Gewinnen zeigt die Liste genau fünf Zeilen.

## Abschlusskriterien

- `storage.py` enthält `HIGHSCORES_FILE`, `load_highscores`, `save_highscore`, `get_tries` und `top_five`; `scores.txt` kommt im Code nicht mehr vor.
- `ui.show_highscores` zeigt Platz, Name, Versuche, Dauer und Stufe.

## Erweiterung

Lege `playground/oldest.py` an: Das Skript lädt `../data/persons.json` (vom Ordner `playground/` aus gesehen), sortiert die Personen mit einer eigenen Funktion `get_age` absteigend nach Alter und gibt die drei ältesten als `Jülide (31)` aus. Start im Ordner `playground/` mit `python oldest.py`.
