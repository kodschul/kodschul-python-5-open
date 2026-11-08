# Modul 11 – Transferlösung: Stadtbibliothek

Vollständige Lösung für `playground/library.py`. Die einzelnen Aufgaben sind im Code mit Kommentaren markiert; danach folgt der Lauf.

## Vollständiges Skript

```python
# Stadtbibliothek: Medien, Ausleihen und Fehler als Klassen

from abc import ABC, abstractmethod
from dataclasses import dataclass


# Aufgabe 4: eigener Fehler
class MediumNotFoundError(ValueError):
    """Fehler: Diesen Titel hat die Bibliothek nicht."""


# Aufgabe 1: abstrakte Basisklasse und zwei Unterklassen
class Medium(ABC):
    """Abstrakte Basisklasse: alles, was sich ausleihen lässt."""

    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def loan_days(self):
        """Gibt die Leihfrist in Tagen zurück."""

    # Aufgabe 2: Ausgabe und Sortierung
    def __str__(self):
        return f"{self.title} ({self.year}) · {self.loan_days()} Tage"

    def __lt__(self, other):
        """Älter ist kleiner; bei gleichem Jahr entscheidet der Titel."""
        if self.year != other.year:
            return self.year < other.year
        return self.title < other.title


class Book(Medium):
    def loan_days(self):
        return 28


class Dvd(Medium):
    def loan_days(self):
        return 7


# Aufgabe 4: Ausleihe als Dataclass
@dataclass
class Loan:
    """Eine Ausleihe: wer hat welchen Titel wie lange."""

    title: str
    member: str
    days: int


# Aufgabe 3 und 4: Bibliothek hat Medien und Ausleihen
class Library:
    """Bibliothek: hat Medien und Ausleihen (Komposition)."""

    def __init__(self):
        self.media = []
        self.loans = []

    def add(self, medium):
        self.media.append(medium)

    def __len__(self):
        return len(self.media)

    def sorted_media(self):
        return sorted(self.media)

    def lend(self, title, member):
        """Leiht einen Titel aus und gibt die Ausleihe zurück."""
        for medium in self.media:
            if medium.title == title:
                loan = Loan(title, member, medium.loan_days())
                self.loans.append(loan)
                return loan
        raise MediumNotFoundError(f"Titel nicht im Bestand: {title}")


# Aufgabe 5: Bibliothek benutzen
library = Library()
library.add(Book("Momo", 1973))
library.add(Dvd("Lola rennt", 1998))
library.add(Book("Die Verwandlung", 1915))
library.add(Dvd("Good Bye, Lenin!", 2003))

print(f"Bestand: {len(library)} Medien")
for medium in library.sorted_media():
    print(medium)

print(library.lend("Momo", "Anna"))
print(library.lend("Lola rennt", "Ben"))
try:
    library.lend("Harry Potter", "Cem")
except MediumNotFoundError as error:
    print(error)
```

Lauf mit `python playground/library.py` im Ordner `project/`:

```text
Bestand: 4 Medien
Die Verwandlung (1915) · 28 Tage
Momo (1973) · 28 Tage
Lola rennt (1998) · 7 Tage
Good Bye, Lenin! (2003) · 7 Tage
Loan(title='Momo', member='Anna', days=28)
Loan(title='Lola rennt', member='Ben', days=7)
Titel nicht im Bestand: Harry Potter
```

## Aufgabe 1: Medium, Book, Dvd

`Medium` ist abstrakt, weil es kein Medium „ohne Art“ gibt. Prüfung im REPL oder am Skriptende:

```text
>>> Medium("Ohne Art", 2000)
TypeError: Can't instantiate abstract class Medium without an implementation for abstract method 'loan_days'
```

## Aufgabe 2: __str__ und __lt__

`__str__` steht in `Medium` und ruft `self.loan_days()` auf: Jede Unterklasse liefert ihre eigene Frist (Polymorphie). `__lt__` vergleicht wie `Score.__lt__` im Spiel in zwei Stufen.

## Aufgabe 3: Library

`Library` erbt nicht von `list`, sondern **hat** zwei Listen (Komposition, Lab 10.3); `__len__` macht `len(library)` möglich, `sorted_media()` nutzt `__lt__`.

## Aufgabe 4: Loan, Fehler und lend

`Loan` ist eine Dataclass: reine Daten, `repr` und `==` erzeugt `@dataclass`. `Medium` ist keine Dataclass, weil es eine abstrakte Methode und eine eigene Vergleichsregel hat. `MediumNotFoundError` erbt von `ValueError`; ein `except ValueError` fängt ihn ebenfalls (wie `InvalidGuessError` im Spiel).

## Aufgabe 5: Lauf

Siehe Ausgabe oben: `len(library)` ist 4, die Liste ist nach Jahr sortiert, die dritte Ausleihe endet mit der Meldung statt mit einem Traceback.

## Erweiterung

Zusätzliche Importe oben im Skript:

```python
import json
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from pathlib import Path
```

Neue Methode in `Library`:

```python
    def save_loans(self, path):
        """Schreibt alle Ausleihen als JSON-Liste in die Datei path."""
        data = []
        for loan in self.loans:
            data.append(asdict(loan))
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
```

Aufruf am Ende: `library.save_loans(Path("playground/loans.json"))`. Inhalt von `playground/loans.json`:

```json
[
  {
    "title": "Momo",
    "member": "Anna",
    "days": 28
  },
  {
    "title": "Lola rennt",
    "member": "Ben",
    "days": 7
  }
]
```
