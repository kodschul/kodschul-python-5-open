# Lab 7.2 – Übung: Spiel ohne Absturz bei falscher Eingabe

**Dauer:** ca. 18 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `ui.py` bekommt `ask_number()`, `__main__.py` fängt Strg+C ab; Lab 7.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/ui.py` und `playground/guess_game/__main__.py`
**Starter:** `starters/m07-l02-guess_game/` mit `__main__.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code im Ordner `project/`, `.venv` aktiv, dann einmal `cd playground`.
- Das eigene Spiel aus Lab 6.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m06-modules/l03-datetime/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m07-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Start jeweils mit `python -m guess_game`.

## Aufgaben

1. Lege in `ui.py` über `show_hint` die Funktion `ask_number(prompt)` an: In einer `while True:`-Schleife liest sie mit `input(prompt)` einen Text und gibt in einem `try`-Block `int(text)` mit `return` zurück.
2. Fange in `ask_number` den `ValueError` ab und gib dann `Bitte eine ganze Zahl eingeben, z. B. 7.` aus. Ergänze einen Docstring in einem Satz.
3. Ersetze in `play_round` die Zeile `guess = int(input("Tipp: "))` durch einen Aufruf von `ask_number("Tipp: ")`.
4. Umschließe in `__main__.py` den Aufruf `main()` unter `if __name__ == "__main__":` mit `try`/`except KeyboardInterrupt` und gib dort in einer neuen Zeile `Spiel abgebrochen. Bis zum nächsten Mal!` aus.
5. Teste: Spiele eine Runde mit den Tipps `abc`, `7.5`, einer leeren Eingabe (nur Enter) und danach gültigen Zahlen. Starte erneut und drücke bei `Nochmal spielen? (j/n):` die Tasten Strg+C (macOS: control+C).

## Checkpoint

- `abc`, `7.5` und eine leere Eingabe ergeben je `Bitte eine ganze Zahl eingeben, z. B. 7.` und eine neue Frage `Tipp:`; kein Versuch wird abgezogen.
- Strg+C zeigt `Spiel abgebrochen. Bis zum nächsten Mal!` ohne Traceback, an jeder Eingabestelle (Name, Stufe, Tipp, Nochmal).
- Gültige Tipps funktionieren wie vorher.

## Abschlusskriterien

- `ui.py` enthält `ask_number` mit gezieltem `except ValueError`, kein nacktes `except:`.
- `play_round` ruft `ask_number("Tipp: ")` auf.
- `__main__.py` fängt `KeyboardInterrupt` ab.

## Erweiterung

Schreibe `playground/safe_age.py`: Das Skript fragt `Alter: ` so lange, bis eine ganze Zahl kommt, und gibt dann das Geburtsjahr aus (`2026 - Alter`, wie in Lab 2.2). Ergänze einen `finally`-Block, der nach jedem Versuch `Eingabe geprüft.` ausgibt. Teste mit `zwanzig` und `20`.
