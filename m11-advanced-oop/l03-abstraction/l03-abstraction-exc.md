# Lab 11.3 – Übung: Player als abstrakter Vertrag

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `Player` wird abstrakt, `HumanPlayer` bekommt ein eigenes `on_hint`; das Spiel läuft wie vorher. Lab 12.1 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/players.py`
**Starter:** `starters/m11-l03-guess_game/` mit `players.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 11.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m11-advanced-oop/l02-dataclasses/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m11-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. Die Stellen zum Ändern tragen `# TODO Lab 11.3`.

## Aufgaben

1. Ergänze oben in `players.py` `from abc import ABC, abstractmethod` und lass `Player` von `ABC` erben.
2. Markiere `next_guess` und `on_hint` in `Player` mit `@abstractmethod`. Lösche ihren Code (`raise NotImplementedError(...)` und `pass`); als Körper bleibt nur ein Docstring. `start_round` bleibt unverändert.
3. Starte `python -m guess_game` und wähle `mensch`. Lies die letzte Zeile der Fehlermeldung.
4. Gib `HumanPlayer` eine eigene Methode `on_hint(self, guess, hint)` mit dem Körper `pass` und einem Docstring, der erklärt, warum sie nichts tut. Spiele je eine Runde als `mensch` und als `computer`.
5. Prüfe den Vertrag im REPL (`python` im Ordner `playground/`): `from guess_game import players`, dann `players.Player("Test")`. Lege danach eine Klasse `LazyPlayer(players.Player)` an, die nur `next_guess` mit `return 5` hat, und erzeuge `LazyPlayer("Test")`.

## Checkpoint

- Nach Aufgabe 3 endet das Spiel mit `TypeError: Can't instantiate abstract class HumanPlayer without an implementation for abstract method 'on_hint'`.
- Nach Aufgabe 4 laufen Mensch- und Computer-Runde wie in Lab 11.2.
- Im REPL scheitert `Player("Test")` mit beiden fehlenden Methoden, `LazyPlayer("Test")` nur mit `'on_hint'`.

## Abschlusskriterien

- `Player` erbt von `ABC`, `next_guess` und `on_hint` sind `@abstractmethod`; `NotImplementedError` kommt in `players.py` nicht mehr vor.
- `HumanPlayer` und `ComputerPlayer` haben je `next_guess` und `on_hint`.

## Erweiterung

Lege `playground/animals.py` an: eine abstrakte Klasse `Animal` mit `name`, der Pflichtmethode `sound()` und der fertigen Methode `speak()`, die `Bello sagt Wuff` zurückgibt. Schreibe `Dog` und `Cat` und eine unvollständige Klasse `Fish` ohne `sound()`. Lass Hund und Katze sprechen und fange den Fehler beim Erzeugen eines Fisches mit `try`/`except TypeError` ab.
