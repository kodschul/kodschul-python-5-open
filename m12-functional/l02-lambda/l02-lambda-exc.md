# Lab 12.2 – Übung: Umschaltbare Bestenliste

**Dauer:** ca. 13 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — jeder Score hat Punkte je nach Stufe, die Bestenliste lässt sich nach Versuchen, Zeit oder Punkten sortieren; Lab 12.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `storage.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m12-l02-guess_game/` mit `__main__.py`, `logic.py`, `storage.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 12.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m12-functional/l01-comprehensions/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m12-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Damit die Sortierung nach Zeit etwas zeigt: `data/highscores_sample.json` als `playground/highscores.json` kopieren (eine eigene Datei vorher umbenennen). Sie enthält Zeiten von 0,0 s bis 95,3 s.

## Aufgaben

1. Lege in `logic.py` unter `LEVELS` das Dictionary `LEVEL_POINTS` an: Stufe → `lambda`, die aus den Versuchen Punkte macht. `leicht`: `(6 - tries) * 10`, `mittel`: `(8 - tries) * 20`, `schwer`: `(8 - tries) * 30`. Prüfe im Ordner `playground/`:

   ```bash
   python -c "from guess_game import logic; print(logic.LEVEL_POINTS['leicht'](1))"
   ```

2. Ergänze in der Dataclass `Score` die Methode `points(self)`: Sie holt die Funktion zur eigenen Stufe aus `LEVEL_POINTS` und gibt deren Ergebnis für `self.tries` zurück.
3. Ersetze in `storage.py` die Methode `top_five(self)` durch `top(self, by="versuche", count=5)`: Bei `"zeit"` sortiert sie mit `key=lambda` nach `seconds`, bei `"punkte"` mit `key=lambda` nach `points()` absteigend, sonst wie bisher mit `sorted(self.scores)`. Zurück kommen die ersten `count` Einträge.
4. Lege in `ui.py` die Konstante `RANKINGS = {"versuche": "Versuchen", "zeit": "Zeit", "punkte": "Punkten"}` an und schreibe `ask_ranking()`: Sie fragt `Bestenliste nach (versuche/zeit/punkte): ` und gibt die Antwort zurück; leer oder unbekannt ergibt `"versuche"`. Erweitere `show_highscores(scores, by="versuche")`: Überschrift `Bestenliste (Top 5 nach Zeit)` (Wort aus `RANKINGS`), jede Zeile endet mit `· 30 Punkte`.
5. Ändere in `__main__.py` den Gewinnfall: erst `by = ui.ask_ranking()`, dann `ui.show_highscores(scoreboard.top(by), by)`. Gewinne eine Runde und probiere `zeit`, in einer zweiten Runde `punkte`, in einer dritten nur Enter.

## Checkpoint

- Der `python -c`-Befehl gibt `50` aus (leicht, 1 Versuch).
- Nach einem Gewinn erscheint `Bestenliste nach (versuche/zeit/punkte):`.
- `zeit`: Die Liste beginnt mit den kleinsten Sekunden (`0,0 s`), die Überschrift lautet `Bestenliste (Top 5 nach Zeit)`.
- `punkte`: Die höchsten Punkte stehen oben (`60 Punkte`).
- Enter oder eine unbekannte Eingabe sortiert nach Versuchen wie in Lab 11.1.

## Abschlusskriterien

- `LEVEL_POINTS` enthält drei Lambdas, `Score.points()` ruft die passende auf.
- `Scoreboard.top` nutzt `key=lambda` für Zeit und Punkte und `reverse=True` für Punkte; `top_five` kommt im Code nicht mehr vor.

## Erweiterung

Lege `playground/adults.py` an: Das Skript lädt `../data/persons.json` (vom Ordner `playground/` aus gesehen), wählt mit `filter` und einer Lambda die Personen ab 18 Jahren aus, macht daraus mit `map` eine Liste der Namen und gibt sie aus. Zusätzlich gibt es mit `max(..., key=lambda ...)` den Namen der größten Person (Feld `height`) aus. Start im Ordner `playground/` mit `python adults.py`.
