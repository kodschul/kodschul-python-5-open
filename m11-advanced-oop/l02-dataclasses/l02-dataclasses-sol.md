# Lab 11.2 – Lösung: Score als Dataclass

Fertiger Stand: [project/examples/m11-advanced-oop/l02-dataclasses/guess_game/](../../project/examples/m11-advanced-oop/l02-dataclasses/guess_game/)

## Aufgabe 1: Import und Decorator

```python
import random
import time
from dataclasses import dataclass
from datetime import datetime
```

```python
@dataclass  # erzeugt __init__, __repr__ und __eq__ aus den Feldern
class Score:
```

## Aufgabe 2: Felder statt __init__

```python
@dataclass  # erzeugt __init__, __repr__ und __eq__ aus den Feldern
class Score:
    """Ergebnis eines Spiels, das sich lesbar ausgeben und sortieren lässt."""

    # Feld: Typ (bei Dataclasses Pflicht, Python prüft ihn nicht)
    name: str
    level: str
    tries: int
    seconds: float
    won: bool
    date: str

    def __str__(self):
        """Text für print() und f-Strings: Anna – 3 Versuche – 12,4 s."""
        word = "Versuch" if self.tries == 1 else "Versuche"
        seconds = f"{self.seconds:.1f}".replace(".", ",")
        return f"{self.name} – {self.tries} {word} – {seconds} s"

    def __lt__(self, other):
        """Kleiner = besser: weniger Versuche, bei Gleichstand weniger Zeit."""
        if self.tries != other.tries:
            return self.tries < other.tries
        return self.seconds < other.seconds
```

Die Reihenfolge der Felder bestimmt die Reihenfolge der Parameter im erzeugten `__init__`. Sie ist dieselbe wie in Lab 11.1, deshalb bleiben `Game.score()` und `Scoreboard.load()` unverändert. Kein `order=True`: Es würde zuerst nach `name` vergleichen und verträgt sich nicht mit dem eigenen `__lt__`.

## Aufgabe 3: asdict statt to_dict

```python
import csv
import json
from dataclasses import asdict
from pathlib import Path
```

```python
    def save(self):
        """Schreibt alle Ergebnisse als JSON in die Datei."""
        data = []
        for score in self.scores:
            data.append(asdict(score))  # Dataclass -> Dictionary für JSON
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
```

`logic.py` ist damit um 9 Zeilen kürzer, die Klasse `Score` etwa halb so lang wie in Lab 11.1.

## Aufgabe 4: Prüfung im REPL

```text
>>> from guess_game import logic, storage
>>> score = storage.Scoreboard().scores[0]
>>> print(score)
Anna – 3 Versuche – 0,0 s
>>> score
Score(name='Anna', level='leicht', tries=3, seconds=0.0, won=True, date='2026-11-08')
>>> score == logic.Score("Anna", "leicht", 3, 0.0, True, "2026-11-08")
True
```

`print` nutzt das eigene `__str__`, die REPL zeigt das erzeugte `__repr__`. In Lab 11.1 hätte `==` hier `False` ergeben, weil es nur prüfte, ob es dasselbe Objekt ist. Name, Datum und Werte hängen vom eigenen Eintrag ab.

## Aufgabe 5: Testlauf

Die Bestenliste zeigt dieselben Zeilen wie in Lab 11.1, z. B.:

```text
Bestenliste (Top 5)
1. Jürgen – 1 Versuch – 0,0 s · leicht
2. Anna – 3 Versuche – 0,0 s · leicht
```

`highscores.json` behält das Format:

```json
[
  {
    "name": "Anna",
    "level": "leicht",
    "tries": 3,
    "seconds": 0.0,
    "won": true,
    "date": "2026-11-08"
  }
]
```

## Erweiterung

```python
from dataclasses import dataclass


@dataclass(order=True)
class Book:
    title: str
    author: str
    year: int


books = [
    Book("Momo", "Michael Ende", 1973),
    Book("Faust", "Johann Wolfgang von Goethe", 1808),
    Book("Die Verwandlung", "Franz Kafka", 1915),
]
for book in sorted(books):
    print(book)
```

```text
Book(title='Die Verwandlung', author='Franz Kafka', year=1915)
Book(title='Faust', author='Johann Wolfgang von Goethe', year=1808)
Book(title='Momo', author='Michael Ende', year=1973)
```

Mit `year` als erstem Feld (und `Book(1973, "Momo", "Michael Ende")` usw.):

```text
Book(year=1808, title='Faust', author='Johann Wolfgang von Goethe')
Book(year=1915, title='Die Verwandlung', author='Franz Kafka')
Book(year=1973, title='Momo', author='Michael Ende')
```

`order=True` vergleicht immer das erste Feld zuerst. Die Sortierung hängt also an der Reihenfolge in der Klasse, nicht an einer eigenen Regel.
