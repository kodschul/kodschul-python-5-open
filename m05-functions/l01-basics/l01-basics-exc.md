# Lab 5.1 – Übung: Spielregeln als Funktionen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — drei Funktionen übernehmen die Spielregeln, der Hauptablauf ruft sie auf; Lab 5.2 baut darauf auf.

**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m05-l01-guess_game.py`

## Vorbereitung

- Terminal in VS Code im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel v1 aus Lab 4.3 liegt in `playground/guess_game.py`. Ohne eigenen Stand: `starters/m05-l01-guess_game.py` öffnen, alles markieren (Strg+A / Cmd+A), kopieren und damit den Inhalt von `playground/guess_game.py` ersetzen.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 5.1` markiert.

## Aufgaben

1. Definiere über dem Banner (`print("=" * 40)`) die Funktion `is_guess_correct(guess, secret)`. Sie gibt `True` zurück, wenn der Tipp die Geheimzahl trifft, sonst `False`. Ergänze einen Docstring in einem Satz.
2. Definiere darunter die Prozedur `show_hint(guess, secret)`, die „Zu hoch.“ oder „Zu niedrig.“ ausgibt. Übernimm dafür die passenden Zeilen der `if`-Kette aus der Schleife.
3. Definiere die Funktion `is_game_over(tries, max_tries)`, die `True` zurückgibt, sobald alle Versuche verbraucht sind.
4. Ersetze im Hauptablauf die Bedingungen durch Aufrufe: `while not is_game_over(...)`, Treffer mit `if is_guess_correct(...)`, den Hinweis mit `show_hint(...)`, die Prüfung nach dem Hinweis mit `if is_game_over(...)`. Achtung: Bei der letzten Prüfung tauschen die beiden Meldungen die Plätze.
5. Starte das Spiel mit `python playground/guess_game.py`. Spiele eine Runde, die gewonnen wird, und eine, in der alle Versuche verbraucht werden.

## Checkpoint

- Ganz oben in der Datei stehen drei `def`-Blöcke, jeder mit Docstring.
- Im Hauptablauf kommen `tries < max_tries`, `guess == secret` und `guess > secret` nicht mehr vor.
- Das Spiel gibt dieselben Meldungen aus wie vorher: „Zu hoch.“, „Verbleibende Versuche: 4“, „Richtig, Anna! Benötigte Versuche: 3.“, „Keine Versuche mehr. Die Zahl war …“.

## Abschlusskriterien

- `playground/guess_game.py` läuft ohne Fehlermeldung und verhält sich wie Spiel v1; die Regeln stecken in `is_guess_correct`, `show_hint` und `is_game_over`.

## Erweiterung

Lege `playground/functions_practice.py` an. Schreibe eine Funktion `is_adult(age)`, die ab 18 `True` liefert, und eine Prozedur `print_line(length)`, die eine Linie aus `length` Bindestrichen ausgibt. Rufe `print_line(20)` auf und gib danach für die Alter 17 und 18 jeweils das Ergebnis von `is_adult` aus.
