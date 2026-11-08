# Fehlerbehandlung-Cheatsheet

Schnellreferenz für Modul 7 (Fehlermeldungen, `try`/`except`, `raise`, Debugger).

## Traceback lesen

| Stelle | Bedeutung |
| --- | --- |
| letzte Zeile `ValueError: …` | Fehlertyp und Meldung: zuerst lesen |
| Block darüber `File "…/ui.py", line 72, in play_round` | Datei, Zeile, Funktion der Abbruchstelle |
| weitere Blöcke nach oben | Aufrufkette: wer hat wen aufgerufen |
| `Traceback (most recent call last):` | Überschrift: neuester Aufruf steht unten |
| `File "<frozen runpy>"` | Python-intern, überspringen |
| `~~~~^^^^` unter Code | genauer Ausdruck, der den Fehler ausgelöst hat |
| `Did you mean: 'total'?` | Vorschlag für einen ähnlichen Namen (prüfen, nicht blind übernehmen) |

## Häufige Fehlertypen

| Fehlertyp | Typische Ursache |
| --- | --- |
| `SyntaxError` | Klammer, Doppelpunkt oder Anführungszeichen fehlt; Programm startet nicht |
| `IndentationError` | Einrückung falsch |
| `NameError` | Name vertippt, nicht zugewiesen oder `import` fehlt |
| `TypeError` | Operation passt nicht zum Typ, z. B. `"Alter: " + 20` |
| `ValueError` | Typ richtig, Wert falsch, z. B. `int("sieben")`, `float("4,99")` |
| `IndexError` | Index zu groß, z. B. `liste[len(liste)]` |
| `KeyError` | Schlüssel fehlt im Dictionary (Groß-/Kleinschreibung!) |
| `ZeroDivisionError` | Division durch 0 |
| `ModuleNotFoundError` | venv nicht aktiv oder falscher Startordner |
| `KeyboardInterrupt` | Strg+C gedrückt |
| `AssertionError` | Bedingung eines `assert` war falsch |

## Fehler abfangen

| Syntax | Wirkung |
| --- | --- |
| `try:` | Block, in dem ein Fehler auftreten darf |
| `except ValueError:` | läuft nur bei `ValueError`, danach geht es normal weiter |
| `except ValueError as error:` | Ausnahme unter dem Namen `error`; `print(error)` zeigt die Meldung |
| `except (ValueError, TypeError):` | mehrere Typen gleich behandeln |
| `except ValueError, TypeError:` | dasselbe ohne Klammern, nur Python 3.14+ und nur ohne `as` |
| `else:` | läuft nur, wenn kein Fehler auftrat |
| `finally:` | läuft immer, mit und ohne Fehler |
| `except:` (nackt) | fängt alles, auch Tippfehler und Strg+C: vermeiden |

## Muster

| Code | Wirkung |
| --- | --- |
| `while True:` + `try: return int(input(prompt))` + `except ValueError: print(...)` | fragt, bis eine ganze Zahl kommt (`ask_number`) |
| `try: main()` + `except KeyboardInterrupt: print("\nAbgebrochen.")` | Strg+C ohne Traceback beenden |
| `try: … except ValueError: …` statt `if text.isdigit():` | EAFP: einfach versuchen statt vorher prüfen |

## Fehler auslösen

| Syntax | Wirkung |
| --- | --- |
| `raise ValueError("Betrag muss größer als 0 sein.")` | Fehler mit eigener Meldung auslösen, Funktion endet sofort |
| `if amount <= 0: raise ValueError(...)` | Eingabe früh prüfen (validieren) |
| `raise TypeError("…")` | Wert hat den falschen Typ |
| `assert balance >= 0, "Meldung"` | Annahme im eigenen Code prüfen; mit `python -O` abgeschaltet, nicht für Eingaben |

## Debugger in VS Code

| Aktion | Taste / Ort |
| --- | --- |
| Ansicht Run and Debug öffnen | Strg+Shift+D (macOS: Cmd+Shift+D) |
| Haltepunkt setzen/entfernen | Klick links neben die Zeilennummer oder F9 |
| bedingter Haltepunkt | Rechtsklick links neben die Zeile → **Add Conditional Breakpoint…** |
| Debuggen starten / Continue | F5 (**Run → Start Debugging**) |
| Step Over | F10 |
| Step Into | F11 |
| Step Out | Shift+F11 |
| Restart | Strg+Shift+F5 (macOS: Cmd+Shift+F5) |
| Stop | Shift+F5 |
| Debug Console | Strg+Shift+Y (macOS: Cmd+Shift+Y) |
| Ausdruck dauerhaft beobachten | Bereich **Watch** → **+** |
| Haltepunkt im Code | `breakpoint()` (ohne Debugger: `pdb`, `p name`, `n`, `c`, `q`) |

## launch.json (`project/.vscode/launch.json`)

| Feld | Wirkung |
| --- | --- |
| `"type": "debugpy"` | Python-Debugger der Erweiterung „Python“ |
| `"module": "guess_game"` | wie `python -m guess_game` |
| `"program": "${file}"` | die gerade geöffnete Datei |
| `"cwd": "${workspaceFolder}/playground"` | Startordner `project/playground` |
| `"console": "integratedTerminal"` | Eingaben und Ausgaben im Terminal |
| `"justMyCode": true` | nur im eigenen Code anhalten |
