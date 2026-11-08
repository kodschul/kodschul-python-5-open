# Datensammlungen-Cheatsheet

Schnellreferenz für Modul 4 (Listen, Tupel, Sets, Dictionaries) und alle eingebauten Funktionen aus Tag 1.

## Welche Sammlung?

| Sammlung | Wann |
| --- | --- |
| Liste `[5, 8, 7]` | geordnete Reihe, die wächst oder sich ändert (Tipps, Noten) |
| Tupel `(1, 10)` | feste Gruppe mit Bedeutung je Platz (Bereich, Koordinate) |
| Set `{5, 8}` | jeder Wert nur einmal, schnelle Prüfung „schon gesehen?“ |
| Dictionary `{"leicht": (1, 10, 5)}` | Wert über einen Namen finden (Stufen, Telefonbuch) |

## Listen anlegen und lesen

| Syntax | Wirkung |
| --- | --- |
| `guesses = []` | leere Liste |
| `shopping = ["Milch", "Brot"]` | Liste mit zwei Elementen |
| `shopping[0]` | erstes Element |
| `shopping[-1]` | letztes Element |
| `shopping[1:3]` | Elemente mit Index 1 und 2 als neue Liste |
| `len(shopping)` | Anzahl der Elemente |
| `"Brot" in shopping` | `True`, wenn der Wert enthalten ist |
| `for item in shopping:` | jedes Element einzeln durchlaufen |

## Listen ändern

| Syntax | Wirkung |
| --- | --- |
| `shopping[1] = "Käse"` | Element an Index 1 ersetzen |
| `shopping.append("Kaffee")` | hinten anhängen |
| `shopping.insert(0, "Butter")` | an Index 0 einfügen |
| `shopping.remove("Milch")` | ersten passenden Wert entfernen |
| `last = shopping.pop()` | letztes Element herausnehmen und zurückgeben |
| `shopping.pop(0)` | Element an Index 0 herausnehmen |
| `shopping.sort()` | Liste selbst sortieren (gibt nichts zurück) |
| `shopping.count("Milch")` | wie oft der Wert vorkommt |

## Array (Modul `array`)

| Syntax | Wirkung |
| --- | --- |
| `import array` | Modul aus der Standardbibliothek laden |
| `array.array("d", [12.5, 9.8])` | Reihe nur aus Kommazahlen |
| `array.array("i", [1, 2, 3])` | Reihe nur aus ganzen Zahlen |
| `temps.append(13.1)` | anhängen wie bei einer Liste; falscher Typ → `TypeError` |

## Tupel

| Syntax | Wirkung |
| --- | --- |
| `point = (3, 5)` | Tupel anlegen |
| `point[0]` | Element lesen (ändern nicht möglich) |
| `low, high = (1, 10)` | entpacken: `low = 1`, `high = 10` |
| `for x, y in route:` | Tupel einer Liste beim Durchlaufen entpacken |

## Sets

| Syntax | Wirkung |
| --- | --- |
| `tried = set()` | leeres Set (`{}` wäre ein Dictionary) |
| `{1, 1, 2}` | Set anlegen, Duplikate fallen weg → `{1, 2}` |
| `tried.add(5)` | Element hinzufügen |
| `tried.remove(5)` | Element entfernen |
| `5 in tried` / `5 not in tried` | enthalten / nicht enthalten |
| `set(liste)` | Duplikate einer Liste entfernen |
| `a & b` | Schnittmenge: in beiden |
| `a \| b` | Vereinigung: in mindestens einem |
| `a - b` | Differenz: in `a`, aber nicht in `b` |

## Dictionaries

| Syntax | Wirkung |
| --- | --- |
| `phone_book = {}` | leeres Dictionary |
| `{"Anna": "0151 1234567"}` | Dictionary mit einem Paar Schlüssel: Wert |
| `phone_book["Anna"]` | Wert lesen; fehlt der Schlüssel → `KeyError` |
| `phone_book.get("Cem", "fehlt")` | Wert oder Standardwert |
| `phone_book["Cem"] = "0170 1112223"` | Paar anlegen oder Wert ersetzen |
| `del phone_book["Anna"]` | Paar löschen |
| `phone_book.pop("Ben")` | Paar entfernen, Wert zurückgeben |
| `"Anna" in phone_book` | prüft Schlüssel |
| `for name in phone_book:` | Schlüssel durchlaufen |
| `for number in phone_book.values():` | Werte durchlaufen |
| `for name, number in phone_book.items():` | Paare durchlaufen |
| `low, high, max_tries = LEVELS[level]` | Tupel-Wert lesen und entpacken |
| `contacts[0]["name"]` | verschachtelt: Feld eines Dictionaries in einer Liste |

## Alles auf einen Blick: eingebaute Funktionen aus Tag 1

### Ein- und Ausgabe

| Funktion | Wirkung |
| --- | --- |
| `print("A", "B")` | Werte mit Leerzeichen getrennt ausgeben |
| `print("A", "B", sep="-", end="!")` | eigenes Trennzeichen und Zeilenende |
| `input("Name: ")` | Eingabe lesen, Ergebnis ist immer ein String |

### Typen prüfen und umwandeln

| Funktion | Wirkung |
| --- | --- |
| `type(7)` | Typ eines Werts → `<class 'int'>` |
| `int("7")` | Text in ganze Zahl → `7` |
| `float("2.5")` | Text in Kommazahl → `2.5` |
| `str(7)` | Zahl in Text → `'7'` |
| `list(phone_book.keys())` | in eine Liste umwandeln |
| `set([6, 2, 6])` | in ein Set umwandeln → `{2, 6}` |

### Zählen, Rechnen, Sortieren

| Funktion | Wirkung |
| --- | --- |
| `len(x)` | Länge eines Strings oder einer Sammlung |
| `range(1, 6)` | Zahlen 1 bis 5 für `for` |
| `sum([1, 2, 3])` | Summe → `6` |
| `min([3, 1, 2])` / `max([3, 1, 2])` | kleinster / größter Wert |
| `sorted([3, 1, 2])` | neue, sortierte Liste → `[1, 2, 3]` |
| `round(2.0333, 2)` | runden auf 2 Nachkommastellen → `2.03` |
| `sum(grades) / len(grades)` | Durchschnitt einer Zahlenliste |

## Typische Fehlermeldungen

| Meldung | Bedeutung |
| --- | --- |
| `IndexError: list index out of range` | Index größer als die Liste |
| `ValueError: list.remove(x): x not in list` | Wert zum Entfernen fehlt |
| `TypeError: 'tuple' object does not support item assignment` | Tupel lässt sich nicht ändern |
| `TypeError: 'set' object is not subscriptable` | Set hat keinen Index |
| `KeyError: 'extrem'` | Schlüssel fehlt im Dictionary |
| `ValueError: too many values to unpack` | Anzahl Namen und Werte beim Entpacken ungleich |
