# Pythonic Code – Cheatsheet

Schnellreferenz für Modul 13: Decorators, Context Manager, `match`/`case` und `:=`.

## Decorator schreiben (Lab 13.1)

| Syntax | Wirkung |
| --- | --- |
| `def deco(func): ... return wrapper` | Decorator: bekommt eine Funktion, gibt den Wrapper zurück |
| `def wrapper(*args, **kwargs):` | Wrapper nimmt jede Art von Argumenten an |
| `result = func(*args, **kwargs)` | Originalfunktion mit denselben Argumenten aufrufen (auspacken) |
| `return result` | Ergebnis weitergeben, sonst liefert die Funktion `None` |
| `@functools.wraps(func)` über `def wrapper` | Name und Docstring von `func` behalten |
| `@deco` über `def f` | Kurzform für `f = deco(f)` |
| `f.__name__`, `f.__doc__` | Name und Docstring einer Funktion als Text |

## Decorator mit Parameter

| Syntax | Wirkung |
| --- | --- |
| `def repeat(times): def decorator(func): ... return decorator` | drei Ebenen: Parameter, Decorator, Wrapper |
| `@repeat(times=3)` | erst `repeat(times=3)` aufrufen, das Ergebnis dekoriert |

## Bekannte Decorators

| Decorator | Wirkung |
| --- | --- |
| `@property` | Methode lesbar wie ein Attribut (Lab 9.3) |
| `@dataclass`, `@dataclass(order=True)` | Klasse bekommt `__init__`, `__repr__`, `__eq__` (Lab 11.2) |
| `@abstractmethod` | Pflichtmethode für Unterklassen (Lab 11.3) |
| `@functools.cache` | Ergebnis je Argument merken, nur für reine Funktionen |
| `@contextmanager` | Generatorfunktion → Context Manager (Lab 13.2) |
| `@logic.timed` | Spiel: misst `play_round` und füllt `score.seconds` |

## Context Manager (Lab 13.2)

| Syntax | Wirkung |
| --- | --- |
| `with ausdruck as name:` | `__enter__` beim Betreten, `__exit__` beim Verlassen, auch nach Fehlern |
| `def __enter__(self): ... return self` | vorbereiten; Rückgabe wird `name` |
| `def __exit__(self, exc_type, exc_value, traceback):` | aufräumen; ohne Fehler sind alle drei `None` |
| `return False` in `__exit__` | Fehler weiterreichen (Normalfall) |
| `return True` in `__exit__` | Fehler verschlucken (selten sinnvoll) |
| `file.closed` | `True`, wenn die Datei geschlossen ist |

## Context Manager mit contextlib

| Syntax | Wirkung |
| --- | --- |
| `from contextlib import contextmanager` | Decorator importieren |
| `@contextmanager` über `def timer(label):` | Funktion wird zum Context Manager |
| Code vor `yield` | läuft beim Betreten |
| `yield` / `yield wert` | hier läuft der `with`-Block; `wert` wird zu `as` |
| `try: yield` + `finally:` | Aufräumen auch nach einem Fehler im Block |

## Typische with-Einsätze

| Syntax | Wirkung |
| --- | --- |
| `with open(path, encoding="utf-8") as file:` | Datei öffnen, danach schließen |
| `with Timer("Import"):` | Abschnitt messen |
| `with tempfile.TemporaryDirectory() as folder:` | temporärer Ordner, danach gelöscht |
| `with storage.Scoreboard("highscores.json") as board:` | Spiel: Bestenliste laden, am Ende speichern |

## match und case (Lab 13.3)

| Syntax | Wirkung |
| --- | --- |
| `match wert:` | Fallunterscheidung beginnen |
| `case "hilfe":` | Literal: genau dieser Wert |
| `case "sa" \| "so":` | eines von mehreren Literalen |
| `case ["stufe", level]:` | Liste mit zwei Elementen, erstes `"stufe"`, zweites in `level` |
| `case [number] if number.isdigit():` | Muster plus Bedingung (Guard) |
| `case ["stufe", _]:` | `_` passt auf jedes Element, speichert nichts |
| `case []:` | leere Liste |
| `case Point(x=0, y=y):` | Klassenmuster: Klasse und Attribute prüfen |
| `case {"name": name}:` | Dictionary-Muster: Schlüssel muss vorhanden sein |
| `case _:` | alles Übrige, immer als letzter Fall |
| `match text.split():` | Text in Wörter zerlegen und nach Form unterscheiden |

## Reihenfolge der Muster

| Regel | Grund |
| --- | --- |
| genaue Muster zuerst | der erste passende `case` gewinnt |
| `case _` zuletzt | fängt alles, danach läuft kein `case` mehr |
| feste Werte in Anführungszeichen | `case quit:` fängt jeden Wert (`SyntaxError` bei weiteren Fällen) |

## Zuweisungsausdruck :=

| Syntax | Wirkung |
| --- | --- |
| `while (text := input("> ").strip()) != "":` | Eingabe speichern und prüfen, `input` steht nur einmal |
| `while (level := input(prompt)) not in LEVELS:` | so lange fragen, bis die Antwort passt |
| `if (count := len(items)) > 2:` | Ergebnis prüfen und danach weiterverwenden |
| Klammern um `(name := ...)` | ohne Klammern speichert `name` das Ergebnis des Vergleichs |

## Spiel-Befehle beim Tipp (Stand Lab 13.3)

| Eingabe | Wirkung |
| --- | --- |
| `7` | Zahl tippen |
| `hilfe` | Befehle zeigen |
| `stufe schwer` | Stufe der nächsten Runde |
| `bestenliste` | Bestenliste zeigen |
| `quit` | Runde und Spiel beenden, Runde zählt nicht |
