# Lab 9.2 – Lösung: Eine Runde als Game-Objekt

Fertiger Stand: [project/examples/m09-oop-basics/l02-classes/guess_game/](../../project/examples/m09-oop-basics/l02-classes/guess_game/). Test im Ordner `project/`: `cd examples/m09-oop-basics/l02-classes`, dann `python -m guess_game`.

## Aufgabe 1: Importe und `__init__`

Kopf von `logic.py` (die Importe sind aus `ui.py` hierher gewandert, `LEVELS`, `draw_secret` und `check_guess` bleiben unverändert):

```python
# Spielregeln: Stufen, Geheimzahl, Prüfungen und die Klasse Game – ohne Ein- und Ausgabe

import random
import time
from datetime import datetime
```

Am Ende von `logic.py`:

```python
class Game:
    """Ein Spiel: Geheimzahl, verbleibende Versuche und bisherige Tipps."""

    def __init__(self, name, level="leicht"):
        self.name = name
        self.level = level
        self.low, self.high, self.max_tries = LEVELS[level]
        self.secret = draw_secret(self.low, self.high)
        self.attempts_left = self.max_tries
        self.guesses = []
        self.won = False
        self.started = datetime.now()  # Datum und Uhrzeit des Starts
        self.start_time = time.perf_counter()  # Stoppuhr starten
        self.seconds = 0.0
```

`self.low, self.high, self.max_tries = LEVELS[level]` entpackt das Tupel aus Lab 4.2 direkt in drei Attribute. Die Geheimzahl wird gezogen, wenn das Objekt entsteht: Jedes neue `Game` hat seine eigene.

## Aufgabe 2: `is_over()` und `result()`

```python
    def is_over(self):
        """Gibt True zurück, wenn gewonnen oder alle Versuche verbraucht sind."""
        return self.won or self.attempts_left == 0

    def result(self):
        """Gibt das Ergebnis des Spiels als Dictionary zurück."""
        return {
            "name": self.name,
            "level": self.level,
            "tries": len(self.guesses),
            "seconds": self.seconds,
            "won": self.won,
            "date": self.started.strftime("%Y-%m-%d"),
        }
```

Das Dictionary hat dieselben Schlüssel wie an Tag 2. Deshalb funktionieren `storage.save_highscore` und `storage.append_history` ohne Änderung.

## Aufgabe 3: `guess(number)`

```python
    def guess(self, number):
        """Wertet einen Tipp aus und gibt den Hinweis als Text zurück."""
        check_guess(number, self.low, self.high)  # löst ValueError aus
        if number in self.guesses:
            return "schon getippt"  # kostet keinen Versuch
        self.guesses.append(number)
        self.attempts_left -= 1
        if number == self.secret:
            self.won = True
        if self.is_over():  # Stoppuhr anhalten
            self.seconds = round(time.perf_counter() - self.start_time, 1)
        if self.won:
            return "richtig"
        if number > self.secret:
            return "zu hoch"
        return "zu niedrig"
```

Die Methode druckt nichts: Sie gibt einen Text zurück, und `ui.py` entscheidet, wie er erscheint. `self.is_over()` ruft eine andere Methode desselben Objekts auf, ebenfalls über `self`.

## Aufgabe 4: `ui.py`

`ui.py` importiert `time` und `datetime` nicht mehr.

```python
def show_hint(hint):
    """Gibt den Hinweis des Spiels farbig aus."""
    if hint == "zu hoch":
        console.print("Zu hoch.", style="red")
    else:
        console.print("Zu niedrig.", style="blue")
```

```python
def play_round(game):
    """Spielt eine Runde mit einem Game-Objekt und gibt das Ergebnis zurück."""
    print(
        f"\nStufe {game.level}, {game.name}: "
        f"Rate eine Zahl zwischen {game.low} und {game.high}."
    )
    print(f"Start: {game.started.strftime('%d.%m.%Y, %H:%M')} Uhr")

    while not game.is_over():
        guess = ask_number("Tipp: ")
        try:
            hint = game.guess(guess)  # das Spiel wertet aus
        except ValueError as error:  # Regel verletzt: kein Versuch verbraucht
            print(error)
            continue

        if hint == "schon getippt":
            print("Diese Zahl wurde schon getippt.")
        elif hint != "richtig":
            show_hint(hint)
            if not game.is_over():
                print(f"Verbleibende Versuche: {game.attempts_left}")

    if game.won:
        duration = format_seconds(game.seconds)
        console.print(
            f"Richtig, {game.name}! Benötigte Versuche: {len(game.guesses)}"
            f" · Dauer: {duration} s",
            style="green",
        )
    else:
        print(f"Keine Versuche mehr. Die Zahl war {game.secret}.")
    print("Bisherige Tipps:", game.guesses)
    return game.result()
```

`play_round` hat keine eigenen Variablen für Geheimzahl, Versuche oder Stoppuhr mehr; alles steckt im Objekt `game`.

## Aufgabe 5: `__main__.py` und Testlauf

```python
from guess_game import logic, storage, ui


def main():
    """Hauptablauf: Name fragen, Runden spielen, bis niemand mehr will."""
    ui.show_banner()
    name = ui.ask_name()
    all_tries = []
    play_again = "j"
    while play_again == "j":
        level = ui.ask_level()
        game = logic.Game(name, level)  # ein neues Spiel-Objekt pro Runde
        result = ui.play_round(game)
        all_tries.append(result["tries"])
        # ... Rest unverändert: history.csv, Bestenliste, Nochmal spielen?
```

Testlauf (Eingaben `anna leicht 500 abc 5 8 10 j leicht 5 5 10 7 8 6 n`), Ausgabe identisch mit Lab 8.3:

```text
Stufe leicht, Anna: Rate eine Zahl zwischen 1 und 10.
Start: 08.11.2026, 02:18 Uhr
Tipp: 500
Der Tipp muss zwischen 1 und 10 liegen.
Tipp: abc
Bitte eine ganze Zahl eingeben, z. B. 7.
Tipp: 5
Zu niedrig.
Verbleibende Versuche: 4
Tipp: 8
Zu niedrig.
Verbleibende Versuche: 3
Tipp: 10
Richtig, Anna! Benötigte Versuche: 3 · Dauer: 0,0 s
Bisherige Tipps: [5, 8, 10]

Bestenliste (Top 5)
1. Anna · Versuche: 3 · 0,0 s · leicht
Nochmal spielen? (j/n): j
Stufe (leicht/mittel/schwer): leicht

Stufe leicht, Anna: Rate eine Zahl zwischen 1 und 10.
Start: 08.11.2026, 02:18 Uhr
Tipp: 5
Zu niedrig.
Verbleibende Versuche: 4
Tipp: 5
Diese Zahl wurde schon getippt.
Tipp: 10
Zu hoch.
Verbleibende Versuche: 3
Tipp: 7
Zu niedrig.
Verbleibende Versuche: 2
Tipp: 8
Zu niedrig.
Verbleibende Versuche: 1
Tipp: 6
Zu niedrig.
Keine Versuche mehr. Die Zahl war 9.
Bisherige Tipps: [5, 10, 7, 8, 6]
Nochmal spielen? (j/n): n
Versuche pro Runde: [3, 5]
Danke fürs Spielen, Anna!
```

Checkpoint in der Python-Konsole (Geheimzahl zufällig, daher kann der Hinweis anders lauten):

![Python-Konsole im Ordner playground: logic.Game("Anna") erzeugt, guess(5) liefert 'zu niedrig', attempts_left ist 4, guesses ist [5], is_over() ist False, game zeigt <guess_game.logic.Game object at 0x…>, ein zweites Spiel für Cem auf schwer hat 7 Versuche und high 100](https://raw.githubusercontent.com/kodschul/kodschul-python-5-open/assets/m09/game-l02-repl.png)

_Quelle: eigener Screenshot, Kurs-Repo, 08.11.2026._

Das zweite Objekt `other` zeigt die Antwort auf Leitfrage 1: Zwei Spiele existieren gleichzeitig, jedes mit eigener Stufe und eigenen Versuchen.

## Erweiterung

```python
# Sparschwein als Klasse: merkt sich jeden Einwurf


class PiggyBank:
    """Ein Sparschwein mit Besitzer und eingeworfenen Beträgen."""

    def __init__(self, owner):
        self.owner = owner
        self.coins = []  # jedes Sparschwein hat seine eigene Liste

    def insert(self, amount):
        """Wirft einen Betrag ein."""
        self.coins.append(amount)

    def total(self):
        """Gibt die Summe aller Einwürfe zurück."""
        return sum(self.coins)


anna = PiggyBank("Anna")
cem = PiggyBank("Cem")

anna.insert(2)
anna.insert(1.5)
cem.insert(0.5)

for piggy in [anna, cem]:
    print(f"Sparschwein von {piggy.owner}: {piggy.total()} €")
```

```text
Sparschwein von Anna: 3.5 €
Sparschwein von Cem: 0.5 €
```
