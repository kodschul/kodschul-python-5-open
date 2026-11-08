# Funktionale Werkzeuge – Cheatsheet

Schnellreferenz für Modul 12: Comprehensions, Funktionen als Werte, `lambda`, `map`/`filter`, Iteratoren und Generatoren.

## Comprehensions (Lab 12.1)

| Syntax | Wirkung |
| --- | --- |
| `[price * 1.19 for price in prices]` | neue Liste: jedes Element umgerechnet |
| `[p for p in prices if p >= 20]` | neue Liste: nur Elemente, für die die Bedingung gilt |
| `[round(p * 1.19, 2) for p in prices if p >= 20]` | umrechnen und filtern in einem |
| `{email.lower() for email in emails}` | Set: doppelte Werte fallen weg |
| `{email: email.split("@")[1] for email in emails}` | Dictionary: Schlüssel → Wert |
| `{name: p * 0.9 for name, p in prices.items()}` | Schlüssel-Wert-Paare beim Durchlaufen entpacken |
| `[g for grades in courses.values() for g in grades]` | zwei `for`: Liste von Listen flach machen |
| `{c: [g for g in gs if g < 2.5] for c, gs in courses.items()}` | Comprehension im Wert |

## Comprehension oder Schleife?

| Situation | Wahl |
| --- | --- |
| neue Sammlung aus einer Folge, ein `for`, höchstens ein `if` | Comprehension |
| mehrere `for` plus Bedingungen, Zwischenergebnisse | `for`-Schleife |
| `print`, Datei schreiben, Eingabe | `for`-Schleife |
| Reihenfolge eines Sets anzeigen | `sorted(menge)` |

## Funktionen als Werte (Lab 12.2)

| Syntax | Wirkung |
| --- | --- |
| `action = double` | Funktion in einer Variablen, ohne `()` kein Aufruf |
| `action(5)` | Funktion über die Variable aufrufen |
| `apply_to_all(double, numbers)` | Funktion als Argument übergeben |
| `operations = {"doppelt": double}` | Funktionen in einem Dictionary |
| `operations["doppelt"](7)` | Funktion holen, dann aufrufen |
| `def make_discount(p): ... return discount` | Funktion zurückgeben (Closure merkt sich `p`) |

## lambda

| Syntax | Wirkung |
| --- | --- |
| `lambda tries: (6 - tries) * 10` | Funktion ohne Namen, Ausdruck = Rückgabewert |
| `lambda a, b: a + b` | mehrere Parameter |
| `LEVEL_POINTS["leicht"](1)` | Lambda aus einem Dictionary aufrufen → `50` |

## Sortieren, Minimum, Maximum

| Syntax | Wirkung |
| --- | --- |
| `sorted(persons, key=lambda p: p["age"])` | aufsteigend nach Alter |
| `sorted(persons, key=lambda p: p["age"], reverse=True)` | absteigend |
| `sorted(scores, key=lambda s: s.points(), reverse=True)` | nach Methodenergebnis, höchster Wert zuerst |
| `min(persons, key=lambda p: p["age"])` | ganzes Element mit dem kleinsten Schlüssel |
| `max(persons, key=lambda p: p["height"])` | ganzes Element mit dem größten Schlüssel |
| `sorted(...)[:5]` | die ersten fünf |

## map und filter

| Syntax | Wirkung |
| --- | --- |
| `list(map(square_num, nums))` | Funktion auf jedes Element anwenden |
| `list(map(lambda n: n**2, nums))` | dasselbe mit Lambda |
| `list(filter(is_even, nums))` | nur Elemente mit `True` behalten |
| `list(filter(lambda p: p["age"] >= 18, persons))` | auswählen mit Lambda |
| `map(...)` ohne `list` | map-Objekt, rechnet erst auf Anfrage, nur einmal durchlaufbar |

## Iteratoren (Lab 12.3)

| Syntax | Wirkung |
| --- | --- |
| `iterator = iter(tips)` | Iterator für eine Liste, einen String, eine Datei holen |
| `next(iterator)` | nächstes Element |
| `except StopIteration:` | Ende abfangen (macht `for` automatisch) |
| `def __iter__(self): return self` | eigene Klasse wird iterierbar |
| `def __next__(self): ... raise StopIteration` | nächstes Element liefern, Ende melden |

## Generatoren

| Syntax | Wirkung |
| --- | --- |
| `def countdown(start): ... yield start` | Generatorfunktion: Wert abgeben, pausieren |
| `gen = countdown(3)` | erzeugt den Generator, startet noch keine Zeile |
| `next(gen)` | läuft bis zum nächsten `yield` |
| `for value in gen:` | alle Werte abrufen, endet bei `StopIteration` |
| `list(countdown(3))` | alle Werte als Liste → `[3, 2, 1]` |
| `return` im Generator | Generator beenden |
| `while True: ... yield ...` | unendlicher Generator, nur mit `next` oder `break` nutzen |
| `(n * n for n in numbers)` | Generator-Ausdruck |
| `sum(n * n for n in numbers)` | Generator-Ausdruck direkt in einer Funktion |
| `sum(1 for line in lines)` | Elemente zählen, ohne Liste |

## Im Spiel (Stand Lab 12.3)

| Stelle | Werkzeug |
| --- | --- |
| `logic.statistics(scores)` | Set-, Dict- und Listen-Comprehensions |
| `logic.LEVEL_POINTS`, `Score.points()` | Dictionary von Lambdas |
| `Scoreboard.top(by)` | `sorted(key=lambda ...)`, `reverse=True` |
| `ui.rounds(player, scoreboard)` | Generatorfunktion mit `yield` und `return` |
| `for game in ui.rounds(player, scoreboard):` | Hauptschleife in `__main__.py` |
