# Python-Grundlagen-Cheatsheet

Schnellreferenz für Modul 2 (Syntax, Variablen, Operatoren, Strings).

## Programm starten

| Befehl | Wirkung |
| --- | --- |
| `python playground/guess_game.py` | eigenes Spiel starten (Terminal im Ordner `project/`, `.venv` aktiv) |
| `python code/m02-basics/<datei>.py` | Beispiel aus Modul 2 starten |
| `Strg`/`Cmd` + `S` | speichern; mit Format on save formatiert Ruff dabei |
| `Shift` + `Alt` + `F` (macOS: `Shift` + `Option` + `F`) | Datei einmalig formatieren |

## Syntax

| Schreibweise | Wirkung |
| --- | --- |
| eine Anweisung pro Zeile | Python führt Zeilen von oben nach unten aus |
| `# Text` | Kommentar bis Zeilenende, wird ignoriert |
| 4 Leerzeichen Einrückung | markieren einen Block (ab Lab 3.1); sonst beginnt jede Zeile ganz links |
| `print` vs. `Print` | Groß-/Kleinschreibung zählt |

## Ausgabe mit `print()`

| Aufruf | Ausgabe |
| --- | --- |
| `print("a", "b", 3)` | `a b 3` |
| `print("2026", "11", "08", sep="-")` | `2026-11-08` |
| `print("Laden", end="")` | kein Zeilenumbruch am Ende |
| `print()` | leere Zeile |
| `print("=" * 40)` | 40 Gleichheitszeichen |

## Variablen und Datentypen

| Schreibweise | Wirkung |
| --- | --- |
| `name = "Anna"` | Variable anlegen oder neu zuweisen |
| `int` | ganze Zahl: `7`, `-3` |
| `float` | Kommazahl mit Punkt: `1.68` |
| `str` | Text: `"Anna"`, `'7'` |
| `bool` | `True`, `False` |
| `None` | noch kein Wert |
| `type(x)` | Datentyp anzeigen, z. B. `<class 'int'>` |

## Eingabe und Umwandlung

| Aufruf | Ergebnis |
| --- | --- |
| `input("Name: ")` | Eingabe als `str`, immer |
| `int("7")` | `7` (`ValueError` bei `"sieben"`, `"7.5"`) |
| `float("1.5")` | `1.5` (Punkt, nicht Komma) |
| `str(42)` | `"42"` |
| `int(input("Tipp: "))` | Eingabe direkt als ganze Zahl |
| `f"{name} tippt {guess}"` | Werte in Text einsetzen (f-String) |
| `round(3.14159, 2)` | `3.14` |

## Rechnen

| Operator | Beispiel → Ergebnis |
| --- | --- |
| `+ - *` | `7 + 2` → `9` |
| `/` | `7 / 2` → `3.5` (immer `float`) |
| `//` | `7 // 2` → `3` |
| `%` | `7 % 2` → `1` (Rest; `0` heißt gerade) |
| `**` | `2 ** 3` → `8` |
| `x += 5`, `x -= 1` | `x = x + 5`, `x = x - 1` |

## Vergleichen und Verknüpfen

| Operator | Wirkung |
| --- | --- |
| `==`, `!=` | gleich, ungleich |
| `<`, `>`, `<=`, `>=` | kleiner, größer, kleiner gleich, größer gleich |
| `1 <= x <= 10` | liegt im Bereich |
| `a and b` | wahr, wenn beide wahr |
| `a or b` | wahr, wenn mindestens eines wahr |
| `not a` | kehrt um |
| Vorrang | `()` → `**` → `* / // %` → `+ -` → Vergleiche → `not` → `and` → `or` |

## Strings: Index und Slicing

| Ausdruck (`w = "Python"`) | Ergebnis |
| --- | --- |
| `w[0]`, `w[-1]` | `"P"`, `"n"` |
| `w[1:4]` | `"yth"` (Ende zählt nicht mit) |
| `w[:3]`, `w[3:]` | `"Pyt"`, `"hon"` |
| `w[::2]` | `"Pto"` |
| `len(w)` | `6` |
| `"th" in w` | `True` |

## String-Methoden

| Methode | Wirkung |
| --- | --- |
| `s.strip()` | Leerzeichen am Rand entfernen |
| `s.lower()`, `s.upper()` | klein, groß |
| `s.title()` | jedes Wort groß beginnen |
| `s.replace("a", "b")` | Teil ersetzen |
| `s.startswith("x")`, `s.endswith("x")` | beginnt / endet mit? → `True`/`False` |
| `s.find("@")` | Index des ersten Vorkommens, sonst `-1` |
| `s.split(";")` | zerlegen → Liste (Lab 4.1) |
| `s = s.strip()` | Ergebnis speichern; Strings sind unveränderlich |

## Sonderzeichen

| Schreibweise | Wirkung |
| --- | --- |
| `\n` | neue Zeile |
| `\t` | Tabulator |
| `\\` | ein Backslash |
| `'Er sagte: "Hallo"'` | andere Anführungszeichen außen |
| `"""..."""` | mehrzeiliger String |
| `t"Hallo {name}"` | Template-String (seit 3.14), liefert `Template`, keinen `str` |

## Fehlermeldungen in Modul 2

| Meldung | Bedeutung |
| --- | --- |
| `IndentationError: unexpected indent` | Leerzeichen am Zeilenanfang zu viel |
| `SyntaxError: '(' was never closed` | Klammer fehlt |
| `NameError: name '...' is not defined` | Name vertippt oder noch nicht zugewiesen |
| `TypeError: can only concatenate str (not "int") to str` | Text + Zahl; f-String oder `str()` nutzen |
| `ValueError: invalid literal for int() ...` | Text ist keine ganze Zahl |
| `IndexError: string index out of range` | Index zu groß |
