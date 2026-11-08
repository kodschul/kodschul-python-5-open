# Funktionen-Cheatsheet

Schnellreferenz für Modul 5 (eigene Funktionen, Parameter, Rückgabewerte, Laufzeitmodell).

## Definieren und aufrufen

| Syntax | Wirkung |
| --- | --- |
| `def greet(name):` | Funktion `greet` mit Parameter `name` definieren |
| `"""Gibt … zurück."""` | Docstring: erste Zeile im Funktionskörper, ein Satz |
| `greet("Anna")` | Funktion aufrufen, Argument `"Anna"` landet in `name` |
| `def show_banner():` | Funktion ohne Parameter; Aufruf mit leeren Klammern `show_banner()` |
| `return number % 2 == 0` | Funktion beenden und Wert zurückgeben |
| `result = is_even(4)` | Rückgabewert speichern |
| `if is_even(n):` | Rückgabewert direkt als Bedingung |
| kein `return` | Prozedur: bewirkt etwas, Aufruf liefert `None` |
| `main()` als letzte Zeile | Hauptablauf in `main()`, Datei startet ihn am Ende |

## Argumente übergeben

| Syntax | Wirkung |
| --- | --- |
| `book_room("B204", 2)` | nach Position: erstes Argument → erster Parameter |
| `book_room("A101", projector=True)` | nach Name (Schlüsselwortargument) |
| `book_room(hours=2, room="C3")` | nach Name ist die Reihenfolge egal |
| `book_room("C3", hours=2)` | gemischt: erst Position, dann Name |

## Parameter definieren

| Syntax | Wirkung |
| --- | --- |
| `def book_room(room, hours=1):` | `hours` hat Standardwert 1, Angabe beim Aufruf freiwillig |
| `def add(*numbers):` | beliebig viele Positionsargumente, im Körper ein Tupel |
| `def make_profile(name, **details):` | beliebig viele Schlüsselwortargumente, im Körper ein Dictionary |
| `def add_tip(tip, tips=None):` | veränderlichen Standardwert vermeiden: `None` + `if tips is None: tips = []` |
| `def play_round(level: str = "leicht") -> int:` | Type Hints: Typ von Parameter und Rückgabe, nur Dokumentation |

## Rückgabewerte

| Syntax | Wirkung |
| --- | --- |
| `return tries` | einen Wert zurückgeben |
| `return best, worst, average` | mehrere Werte als Tupel zurückgeben |
| `best, worst, average = grade_stats(grades)` | Tupel-Rückgabe direkt entpacken |
| `all_tries.append(play_round())` | Rückgabewert in einer Liste sammeln |

## Namen, Objekte, Vergleiche

| Syntax | Wirkung |
| --- | --- |
| `b = a` | zweiter Name für dasselbe Objekt, keine Kopie |
| `a == b` | gleicher Inhalt? |
| `a is b` | dasselbe Objekt? Nur für `x is None` verwenden |
| `id(a)` | Nummer des Objekts; gleich bei `is` → `True` |
| `items.append(x)` in einer Funktion | ändert die übergebene Liste, außen sichtbar |
| `n = n * 2` in einer Funktion | neues Objekt nur lokal; außen unverändert |

## Gültigkeitsbereiche

| Ort | Regel |
| --- | --- |
| Parameter und Zuweisung in einer Funktion | lokal: nur in diesem Aufruf bekannt |
| Name auf Modulebene | global: überall lesbar |
| Suchreihenfolge | LEGB: lokal → umschließende Funktion → global → eingebaut |
| `global counter` | globale Variable in einer Funktion ändern; vermeiden |
| `LEVELS = {...}` auf Modulebene | Konstante: global erlaubt, weil sie nur gelesen wird |

## Aufrufstapel und Rekursion

| Begriff | Bedeutung |
| --- | --- |
| Aufrufstapel | jeder Aufruf legt einen Rahmen mit eigenen Variablen oben auf, `return` nimmt ihn weg |
| Rekursion | Funktion ruft sich selbst mit kleinerer Aufgabe auf: `countdown(number - 1)` |
| Abbruchbedingung | `if number == 0: return`, ohne sie `RecursionError` |

## Werkzeuge

| Werkzeug | Wofür |
| --- | --- |
| [pythontutor.com](https://pythontutor.com/) | Code im Browser Schritt für Schritt mit Frames und Pfeilen ansehen |
| „Python › Analysis: Type Checking Mode“ in VS Code | `basic` statt `off`: Warnungen bei falschen Typen (Type Hints) |

## Typische Fehlermeldungen

| Meldung | Bedeutung |
| --- | --- |
| `NameError: name 'greet' is not defined` | Aufruf vor der Definition oder Name lokal in anderer Funktion |
| `TypeError: greet() missing 1 required positional argument: 'name'` | Argument fehlt |
| `TypeError: greet() takes 1 positional argument but 2 were given` | zu viele Argumente |
| `TypeError: … got an unexpected keyword argument 'level'` | Parametername falsch |
| `TypeError: … got multiple values for argument 'room'` | Parameter doppelt belegt |
| `SyntaxError: positional argument follows keyword argument` | Position nach Name beim Aufruf |
| `SyntaxError: parameter without a default follows parameter with a default` | Pflichtparameter nach Standardwert in `def` |
| `UnboundLocalError: cannot access local variable …` | Zuweisung macht Namen lokal, bevor er einen Wert hat |
| `RecursionError: maximum recursion depth exceeded` | Rekursion ohne Abbruch |
| `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'` | Funktion ohne `return` liefert `None` |
