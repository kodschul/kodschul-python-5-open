# Lab 8.1 – Übung: Gewonnene Runden in scores.txt

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neues Modul `storage.py`; jede gewonnene Runde landet als Zeile in `scores.txt`. Lab 8.2 ersetzt die Textdatei durch JSON.
**Arbeitsdatei:** `playground/guess_game/` (neu: `storage.py`, geändert: `__main__.py`)
**Starter:** `starters/m08-l01-guess_game/` mit `__main__.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, einmal `cd playground` (Start dann mit `python -m guess_game`).
- Das eigene Spiel aus Lab 7.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m07-exceptions/l03-raise/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m08-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Lege im Ordner `playground/guess_game/` die Datei `storage.py` an. Importiere oben `Path` aus `pathlib` und lege die Konstante `SCORES_FILE = Path("scores.txt")` an.
2. Schreibe in `storage.py` die Funktion `append_score(result)`. Die Funktion baut aus dem Ergebnis-Dictionary eine Zeile `Name;Versuche;Sekunden;Datum` mit `\n` am Ende und hängt sie im Modus `"a"` mit `encoding="utf-8"` in einem `with`-Block an `SCORES_FILE` an.
3. Ändere in `__main__.py` den Import zu `from guess_game import storage, ui`. Rufe nach jeder Runde, aber nur wenn `result["won"]` wahr ist, `storage.append_score(result)` auf und gib danach `Gespeichert in scores.txt.` aus (Dateiname aus `storage.SCORES_FILE`).
4. Starte das Spiel, gewinne zwei Runden und beende es. Öffne `playground/scores.txt` im Explorer von VS Code.
5. Starte das Spiel erneut, gewinne eine Runde und verliere eine. Prüfe, ob `scores.txt` gewachsen ist und welche Runde fehlt.

## Checkpoint

- Nach jedem Gewinn erscheint `Gespeichert in scores.txt.`
- `playground/scores.txt` enthält pro gewonnener Runde eine Zeile wie `Anna;3;12.4;2026-11-08`.
- Nach dem Neustart bleiben die alten Zeilen erhalten, neue kommen unten dazu.
- Verlorene Runden stehen nicht in der Datei.

## Abschlusskriterien

- `storage.py` enthält `SCORES_FILE` und `append_score(result)` mit `open(..., "a", encoding="utf-8")` in einem `with`-Block.
- `__main__.py` speichert nur gewonnene Runden.

## Erweiterung

Lege `playground/show_scores.py` an: Das Skript liest `scores.txt` Zeile für Zeile, zerlegt jede Zeile mit `split(";")` und gibt sie als `Anna · Versuche: 3 · 2026-11-08` aus. Fehlt die Datei, erscheint `Noch keine Ergebnisse gespeichert.` statt eines Absturzes. Start im Ordner `playground/` mit `python show_scores.py`.
