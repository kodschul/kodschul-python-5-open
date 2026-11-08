# Klassenbeziehungen-Cheatsheet

Schnellreferenz für Modul 10 (Vererbung, Polymorphie, Komposition, Mehrfachvererbung).

## Welche Beziehung?

| Prüfsatz | Beziehung |
| --- | --- |
| „Ein Kreis **ist eine** Form.“ | Vererbung: `class Circle(Shape):` |
| „Ein Auto **hat einen** Motor.“ | Komposition: `self.engine = engine` |
| „Beide haben `move()`.“ | Polymorphie / Duck Typing: gleicher Aufruf `obj.move()` |
| „Kann zusätzlich protokollieren.“ | Mixin: `class X(LoggingMixin, Basis):` |
| im Zweifel | Komposition vor Vererbung |

## Vererbung

| Syntax | Wirkung |
| --- | --- |
| `class Dog(Animal):` | `Dog` erbt alle Attribute und Methoden von `Animal` |
| `def speak(self):` in `Dog` | überschreibt `Animal.speak` |
| `super().__init__(name)` | ruft das `__init__` der Basisklasse auf |
| `super().deposit(amount)` | ruft die gleichnamige Methode der Basisklasse auf |
| kein `__init__` in der Unterklasse | das `__init__` der Basisklasse wird benutzt |
| `isinstance(bello, Animal)` | `True` auch für Objekte von Unterklassen |
| `issubclass(Dog, Animal)` | `True`, wenn `Dog` von `Animal` erbt |
| `raise NotImplementedError("…")` | „muss eine Unterklasse festlegen“ |

## Eigene Fehlerklassen

| Syntax | Wirkung |
| --- | --- |
| `class InvalidGuessError(ValueError):` + Docstring | eigener Fehlertyp, erbt Meldung und Traceback |
| `raise InvalidGuessError("…")` | eigenen Fehler auslösen |
| `except InvalidGuessError as error:` | nur diesen Fehler fangen |
| `except ValueError:` | fängt auch `InvalidGuessError` (Unterklasse) |
| speziellen `except`-Block zuerst | erste passende Klausel gewinnt |

## Polymorphie

| Syntax | Wirkung |
| --- | --- |
| `for v in vehicles: v.move()` | jede Klasse führt ihr eigenes `move()` aus |
| `def honk(self): pass` | leerer Block: Methode tut absichtlich nichts |
| Methode in fremder Klasse mit gleichem Namen | Duck Typing: passt ohne gemeinsame Basisklasse |
| `(low + high) // 2` | Mitte für die Intervallhalbierung |

## Komposition

| Syntax | Wirkung |
| --- | --- |
| `def __init__(self, engine): self.engine = engine` | Teil von außen (Aggregation), tauschbar |
| `self.horn = Horn()` im `__init__` | Teil entsteht mit dem Ganzen (Komposition) |
| `self.engine.start()` | Aufgabe an das Teil delegieren |
| `car.engine = ElectricEngine(110)` | Teil austauschen |
| `Scoreboard(path=HIGHSCORES_FILE)` | Standardwert für das Teil |

## Mehrfachvererbung und MRO

| Syntax | Wirkung |
| --- | --- |
| `class C(A, B):` | erbt von `A` und `B`; `A` gewinnt bei gleichen Namen |
| `C.__mro__` | Suchreihenfolge als Tupel |
| `C.mro()` | Suchreihenfolge als Liste |
| `cls.__name__` | Name einer Klasse als Text |
| MRO-Regeln | Klasse selbst, Kinder vor Eltern, links vor rechts, jede einmal, `object` zuletzt |
| `class Logging…(LoggingMixin, Basis):` | Mixin links von der Basisklasse |

## Im Spiel (Stand Lab 10.3)

| Klasse | Rolle |
| --- | --- |
| `Player` | Basisklasse: `name`, `start_round`, `next_guess`, `on_hint` |
| `HumanPlayer(Player)` | Tipp per `ui.ask_number` |
| `ComputerPlayer(Player)` | Tipp per Intervallhalbierung, höchstens 7 Versuche bei 1–100 |
| `InvalidGuessError(ValueError)` | Spielfehler: Tipp außerhalb des Bereichs |
| `Scoreboard` | lädt und speichert `highscores.json` |
| `Game` | hat einen `Player` und ein `Scoreboard` |
