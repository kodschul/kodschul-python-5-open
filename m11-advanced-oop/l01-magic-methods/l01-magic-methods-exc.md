# Lab 11.1 – Übung: Score mit __str__ und __lt__

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — Ergebnisse sind `Score`-Objekte, die Bestenliste sortiert mit `sorted(scores)`; Lab 11.2 macht daraus eine Dataclass.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `storage.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m11-l01-guess_game/` mit `__main__.py`, `logic.py`, `storage.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 10.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m10-class-relations/l03-composition/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m11-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. Die Stellen zum Ändern tragen `# TODO Lab 11.1`.
- Eine vorhandene `playground/highscores.json` bleibt liegen: Sie soll nach dem Umbau weiter laden. Ohne Datei vorher eine Runde gewinnen.

## Aufgaben

1. Lege in `logic.py` über `Game` die Klasse `Score` an: `__init__(self, name, level, tries, seconds, won, date)` speichert die sechs Werte als Attribute, `to_dict()` gibt sie als Dictionary mit denselben Schlüsseln zurück. Ersetze `Game.result()` durch `score()`, das ein `Score` mit denselben Werten liefert, und rufe in `save_score()` jetzt `self.score()` auf.
2. Schreibe `__str__`: Ergebnis wie `Anna – 3 Versuche – 12,4 s`, bei genau einem Versuch `1 Versuch`. Die Sekunden mit einer Nachkommastelle und Komma (wie `format_seconds` in `ui.py`).
3. Schreibe `__lt__(self, other)`: weniger Versuche ist kleiner; bei gleich vielen Versuchen entscheidet die kürzere Zeit. Prüfe im REPL (`python` im Ordner `playground/`): `from guess_game import logic`, drei Scores Anna (3, 20.0), Ben (4, 5.0), Cem (3, 12.4) anlegen und je Element von `sorted([anna, ben, cem])` ausgeben.
4. Stelle `storage.py` um: `from guess_game import logic`; `load()` baut aus jedem Dictionary der Datei ein `logic.Score` (Schleife mit `append`), `save()` schreibt `score.to_dict()` jedes Ergebnisses, `top_five()` gibt `sorted(self.scores)[:5]` zurück, `get_tries` entfällt. `append_history(score)` liest Attribute (`score.tries`) statt Schlüssel.
5. Lass in `ui.py` `play_round` `game.score()` zurückgeben und `show_highscores` je Zeile `f"{place}. {score} · {score.level}"` drucken. Ändere `__main__.py` auf `score = ui.play_round(game)`, `score.tries` und `score.won`. Starte mit `python -m guess_game` und gewinne eine Runde. Die Einzahl prüft im REPL `print(logic.Score("Jürgen", "leicht", 1, 0.0, True, "2026-11-08"))`.

## Checkpoint

- Im REPL ergibt `sorted` die Reihenfolge Cem, Anna, Ben.
- `print` eines Scores mit einem Versuch zeigt `Jürgen – 1 Versuch – 0,0 s`.
- Die Bestenliste zeigt Zeilen wie `1. Jürgen – 1 Versuch – 0,0 s · leicht` und `2. Anna – 3 Versuche – 0,0 s · leicht`.
- Die alte `highscores.json` lädt ohne Fehler; neue Einträge haben dieselben sechs Felder.

## Abschlusskriterien

- `logic.py` enthält `Score` mit `__init__`, `__str__`, `__lt__`, `to_dict`; `Game` hat `score()` statt `result()`.
- `storage.py` sortiert ohne `key=`; `get_tries` kommt nicht mehr vor.

## Erweiterung

Lege `playground/prices.py` an: eine Klasse `Price` mit dem Betrag in Cent (`Price(1250)`), `__str__` gibt `12,50 €` aus, `__add__` addiert zwei Preise zu einem neuen `Price`, `__lt__` vergleicht die Beträge. Sortiere drei Preise mit `sorted` und gib die Summe der drei aus. Start im Ordner `playground/` mit `python prices.py`.
