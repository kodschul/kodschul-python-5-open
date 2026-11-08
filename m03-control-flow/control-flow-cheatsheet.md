# Programmfluss-Cheatsheet

Schnellreferenz für Modul 3 (Bedingungen, Zufall, Schleifen, Kombinieren).

## Bedingungen

| Syntax | Wirkung |
| --- | --- |
| `if x > 5:` | Block nur ausführen, wenn die Bedingung wahr ist |
| `elif x > 0:` | weitere Prüfung, nur wenn alle vorherigen falsch waren |
| `else:` | Block, wenn keine Bedingung passte |
| `if a and b:` | beide Bedingungen müssen wahr sein |
| `if a or b:` | eine wahre Bedingung genügt |
| `if not done:` | Bedingung umkehren |
| `if name:` | wahr, wenn der String nicht leer ist |
| `wert_a if bedingung else wert_b` | Bedingungsausdruck: einen von zwei Werten liefern |

## Wahrheitswerte

| Wert | gilt als |
| --- | --- |
| `0`, `0.0`, `""`, `None`, `False` | falsch |
| alle anderen Zahlen und Strings, `True` | wahr |
| `bool(wert)` | zeigt den Wahrheitswert an |

## Zufall

| Syntax | Wirkung |
| --- | --- |
| `import random` | Modul `random` aus der Standardbibliothek laden (oben in der Datei) |
| `random.randint(1, 6)` | ganze Zahl von 1 bis 6, beide Grenzen eingeschlossen |
| `random.choice("KZ")` | zufälliges Zeichen aus einem String |
| `random.random()` | Kommazahl von 0.0 bis unter 1.0 |
| `random.seed(42)` | fester Startwert: gleiche Zahlenfolge bei jedem Start (Tests) |
| `random.seed()` | wieder unvorhersehbarer Startwert |

## Schleifen

| Syntax | Wirkung |
| --- | --- |
| `while count <= 3:` | wiederholen, solange die Bedingung wahr ist |
| `while True:` | wiederholen, bis `break` die Schleife beendet |
| `while True:` … `if ereignis: break` | wiederholen, bis etwas eintritt (z. B. Antwort `n`, Würfel zeigt 6) |
| `for i in range(5):` | `i` = 0, 1, 2, 3, 4 |
| `for i in range(1, 6):` | `i` = 1 bis 5, Ende nicht enthalten |
| `for i in range(10, 0, -2):` | `i` = 10, 8, 6, 4, 2 |
| `for char in "Anna":` | jedes Zeichen eines Strings |
| `break` | Schleife sofort verlassen (nur die innerste) |
| `continue` | Rest des Durchlaufs überspringen, nächster Durchlauf |
| `else:` unter einer Schleife | läuft nur, wenn kein `break` kam |
| `count += 1` | Zähler erhöhen |
| `total += number` | Summe mitführen |
| `"*" * 5` | String wiederholen: `*****` |

## Programm kombinieren

| Muster | Wirkung |
| --- | --- |
| `MAX_TRIES = 3` | Konstante in GROSSBUCHSTABEN: Einstellung, die sich nicht ändert |
| `while play_again == "j":` außen, `while tries < MAX_TRIES:` innen | Runden außen, Tipps innen |
| `secret = …` und `tries = 0` am Anfang der äußeren Schleife | jede Runde beginnt frisch |
| `input(…).strip().lower()` | Antwort `J`, ` j ` und `j` gleich behandeln |

## Terminal und Fehlersuche

| Aktion | Wirkung |
| --- | --- |
| `python code/m03-control-flow/loops.py` | Beispiel im Ordner `project/` starten |
| `Strg+C` (macOS: `control+C`) | laufendes Programm abbrechen, z. B. Endlosschleife |
| `KeyboardInterrupt` | Meldung nach `Strg+C`, kein Fehler im Code |
| `SyntaxError: expected ':'` | Doppelpunkt nach `if`/`elif`/`else`/`while`/`for` fehlt |
| `IndentationError: expected an indented block …` | Zeile unter der Doppelpunkt-Zeile nicht eingerückt |
| `IndentationError: unindent does not match …` | Einrückung uneinheitlich (immer 4 Leerzeichen) |
| Programm läuft, tut aber das Falsche | Logikfehler: Einrückung der verdächtigen Zeile prüfen |
