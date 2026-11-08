# Fortgeschrittene OOP-Cheatsheet

Schnellreferenz für Modul 11 (Magic Methods, Dataclasses, abstrakte Klassen, Code-Review).

## Magic Methods: was Python aufruft

| Schreibweise | Python ruft auf |
| --- | --- |
| `Point(1, 2)` | `__init__(self, x, y)` |
| `print(obj)`, `str(obj)`, `f"{obj}"` | `__str__(self)` → Text für Menschen |
| `repr(obj)`, `obj` im REPL, `print([obj])` | `__repr__(self)` → Text für Entwickler |
| `a == b` | `__eq__(self, other)` → `True`/`False` |
| `a < b`, `sorted(liste)` | `__lt__(self, other)` → `True`/`False` |
| `b > a` | ohne `__gt__`: Python prüft `a < b` |
| `a + b` | `__add__(self, other)` → neues Objekt |
| `len(obj)` | `__len__(self)` → ganze Zahl |

## Magic Methods schreiben

| Code | Wirkung |
| --- | --- |
| `def __str__(self): return f"{self.name} – {self.tries} Versuche"` | lesbare Ausgabe; immer `return`, nie `print` |
| `def __repr__(self): return f"Point({self.x}, {self.y})"` | eindeutige Ausgabe, möglichst wie der Code zum Erzeugen |
| `def __lt__(self, other): return self.tries < other.tries` | Sortierregel: „kleiner“ steht vorn |
| `if self.tries != other.tries: return self.tries < other.tries` | erste Stufe; danach `return self.seconds < other.seconds` |
| `def __add__(self, other): return Point(self.x + other.x, self.y + other.y)` | `+` liefert ein neues Objekt |
| `word = "Versuch" if self.tries == 1 else "Versuche"` | Einzahl/Mehrzahl in `__str__` |

## Dataclass

| Code | Wirkung |
| --- | --- |
| `from dataclasses import dataclass, asdict, field` | Import |
| `@dataclass` über `class Score:` | erzeugt `__init__`, `__repr__`, `__eq__` |
| `tries: int` | Feld mit Type Hint (Pflicht; Python prüft den Typ nicht) |
| `stock: int = 0` | Feld mit Standardwert; steht nach den Feldern ohne |
| `members: list = field(default_factory=list)` | eigene leere Liste je Objekt |
| `@dataclass(order=True)` | `<`, `>` usw. vergleichen Feld für Feld in Klassenreihenfolge |
| `@dataclass(frozen=True)` | Felder nach dem Erzeugen nicht änderbar |
| `asdict(score)` | Dataclass → Dictionary (z. B. für `json.dump`) |
| `def __str__(self):` in der Dataclass | eigene Methoden bleiben möglich |

## Type Hints

| Type Hint | Bedeutung |
| --- | --- |
| `name: str` | Text |
| `tries: int` | ganze Zahl |
| `seconds: float` | Kommazahl |
| `won: bool` | `True`/`False` |
| `members: list` | Liste |

## Abstrakte Klasse

| Code | Wirkung |
| --- | --- |
| `from abc import ABC, abstractmethod` | Import |
| `class Player(ABC):` | Klasse kann abstrakte Methoden haben |
| `@abstractmethod` über `def next_guess(self):` | Pflichtmethode; Körper nur Docstring |
| normale Methode in der abstrakten Klasse | fertig für alle Unterklassen (z. B. `start_round`) |
| `Player("Test")` | `TypeError: Can't instantiate abstract class Player without an implementation for abstract methods …` |
| Unterklasse mit allen Pflichtmethoden | lässt sich erzeugen |

## Welche Klassenart?

| Fall | Wahl |
| --- | --- |
| kurzlebige Daten ohne Regeln, JSON | Dictionary |
| Datensatz mit wenig Verhalten | Dataclass |
| Daten mit eigener Ausgabe oder Sortierregel | Dataclass + `__str__`/`__lt__` |
| Vorlage, die selbst nichts tun kann | abstrakte Klasse (`ABC`) |
| viel Verhalten, eigener `__init__` | normale Klasse |

## Code-Review

| Prüfen | Wie |
| --- | --- |
| `input`/`print` nur in `ui.py` | **Edit → Find in Files** (`Strg+Shift+F`): `input(`, `print(` |
| Dateizugriffe nur in `storage.py` | Suche `open(`, `json`, `Path` |
| kein Import im Kreis | Suche `import`, Pfeile notieren |
| gleiche Regel nur einmal | Suche nach dem Muster, z. B. `replace(".", ",")` |
| Suche auf einen Ordner begrenzen | Feld **files to include**, z. B. `playground/guess_game` |

## UML light

| Zeichen (Mermaid) | Bedeutung |
| --- | --- |
| `A <\|-- B` | B erbt von A („ist ein“) |
| `A *-- B` | A hat ein B (Komposition) |
| `A o-- B` | A hat ein B, B lebt auch allein (Aggregation) |
| `A ..> B : erzeugt` | A benutzt oder erzeugt B |
| `"1" *-- "*"` | eins hat viele |
| `<<abstract>>`, `methode()*` | abstrakte Klasse, abstrakte Methode |
