# Lab 7.3 – Übung: Tipps außerhalb des Bereichs ablehnen

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `logic.py` bekommt `check_guess()`, `play_round` in `ui.py` fängt deren Fehler ab; Lab 8.1 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/logic.py` und `playground/guess_game/ui.py`
**Starter:** `starters/m07-l03-guess_game/` mit `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code im Ordner `project/playground/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 7.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m07-exceptions/l02-try-except/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m07-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Lege in `logic.py` die Funktion `check_guess(guess, low, high)` mit Docstring an. Liegt `guess` unter `low` oder über `high`, löst sie `ValueError` mit der Meldung `Der Tipp muss zwischen <low> und <high> liegen.` aus (f-String).
2. Prüfe die Funktion im REPL: In `playground/` `python` starten, dann `from guess_game import logic` und `logic.check_guess(500, 1, 10)` sowie `logic.check_guess(7, 1, 10)` eingeben. Beende den REPL mit `exit`.
3. Rufe in `play_round` (`ui.py`) direkt nach `guess = ask_number("Tipp: ")` die Funktion `logic.check_guess(guess, low, high)` in einem `try`-Block auf.
4. Fange dort `ValueError as error` ab, gib `error` aus und springe mit `continue` zum nächsten Tipp.
5. Teste mit `python -m guess_game` auf Stufe `leicht`: Tipps `500`, `0`, `abc`, danach gültige Zahlen bis zum Ende der Runde.

## Checkpoint

- Der REPL zeigt für `500` den Traceback mit `ValueError: Der Tipp muss zwischen 1 und 10 liegen.`, für `7` keine Ausgabe.
- Im Spiel erscheint bei `500` und `0` die Meldung `Der Tipp muss zwischen 1 und 10 liegen.`, bei `abc` weiterhin `Bitte eine ganze Zahl eingeben, z. B. 7.`.
- Ungültige Tipps stehen nicht in `Bisherige Tipps` und kosten keinen Versuch: Nach dem ersten gültigen Fehltipp steht `Verbleibende Versuche: 4`.

## Abschlusskriterien

- `logic.py` enthält `check_guess` mit `raise ValueError(...)`, ohne `print` und ohne `input`.
- `ui.py` fängt den Fehler mit `except ValueError as error:` und zeigt die Meldung aus `logic.py`.

## Erweiterung

Schreibe `playground/bank_deposit.py` mit einer Funktion `deposit(balance, amount)`: Sie lehnt Beträge ≤ 0 und Beträge über 10 000 Euro mit `ValueError` ab und gibt sonst den neuen Kontostand zurück. Teste mit den Beträgen `50`, `0`, `20000` und `250` bei einem Startguthaben von 100 Euro.
