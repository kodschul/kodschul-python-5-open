# Lab 4.2 – Lösung: Tupel und Sets

Fertiger Stand: [examples/m04-collections/l02-tuples-sets/guess_game.py](../../project/examples/m04-collections/l02-tuples-sets/guess_game.py)

## Aufgabe 1: Bereich als Tupel

```python
MAX_TRIES = 3
NUMBER_RANGE = (1, 10)  # Tupel: Bereich ändert sich nicht
...
name = input("Name: ").strip().title()
low, high = NUMBER_RANGE  # Tupel entpacken
```

Der Name in Großbuchstaben zeigt wie bei `MAX_TRIES`: Dieser Wert ändert sich im Programm nicht.

## Aufgabe 2: Bereich verwenden

```python
    secret = random.randint(low, high)
    ...
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen {low} und {high}.")
```

Eine Änderung an `NUMBER_RANGE` wirkt jetzt an beiden Stellen.

## Aufgabe 3: Leeres Set pro Runde

```python
    guesses = []    # Reihenfolge der Tipps für die Ausgabe
    tried = set()   # schnelle Prüfung: schon getippt?
```

`set()` statt `{}`, denn `{}` wäre ein leeres Dictionary.

## Aufgabe 4: Doppelte Tipps erkennen

```python
    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue  # kein Versuch abziehen, gleich neu fragen

        tried.add(guess)
        guesses.append(guess)
        tries += 1
```

Die Prüfung steht vor `tries += 1`. Dadurch kostet ein doppelter Tipp keinen Versuch und landet nicht ein zweites Mal in `guesses`.

## Aufgabe 5: Testlauf

```bash
python playground/guess_game.py
```

Beispiellauf (Geheimzahl 7, die 5 zweimal getippt):

```text
========================================
Zahlenraten
========================================
Name: Anna

Neue Runde, Anna! Rate eine Zahl zwischen 1 und 10.
Tipp: 5
Zu niedrig.
Verbleibende Versuche: 2
Tipp: 5
Diese Zahl wurde schon getippt.
Tipp: 8
Zu hoch.
Verbleibende Versuche: 1
Tipp: 7
Richtig, Anna! Benötigte Versuche: 3.
Bisherige Tipps: [5, 8, 7]
Nochmal spielen? (j/n): n
Danke fürs Spielen, Anna!
```

Vollständiger Code:

```python
# Zahlenraten – Stand Lab 4.2: Bereich als Tupel, doppelte Tipps per Set

import random

MAX_TRIES = 3
NUMBER_RANGE = (1, 10)  # Tupel: Bereich ändert sich nicht

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
low, high = NUMBER_RANGE  # Tupel entpacken

play_again = "j"
while play_again == "j":
    secret = random.randint(low, high)
    tries = 0
    guesses = []    # Reihenfolge der Tipps für die Ausgabe
    tried = set()   # schnelle Prüfung: schon getippt?
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen {low} und {high}.")

    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue  # kein Versuch abziehen, gleich neu fragen

        tried.add(guess)
        guesses.append(guess)
        tries += 1

        if guess == secret:
            print(f"Richtig, {name}! Benötigte Versuche: {tries}.")
            break
        elif guess > secret:
            print("Zu hoch.")
        else:
            print("Zu niedrig.")

        if tries < MAX_TRIES:
            print(f"Verbleibende Versuche: {MAX_TRIES - tries}")
        else:
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")

    print("Bisherige Tipps:", guesses)
    play_again = input("Nochmal spielen? (j/n): ").strip().lower()

print(f"Danke fürs Spielen, {name}!")
```

Alternative: Statt eines Sets funktioniert auch `if guess in guesses:` mit der vorhandenen Liste. Das Ergebnis ist gleich; das Set ist bei vielen Werten schneller und macht die Absicht „schon gesehen?“ sichtbar.

## Erweiterung

```python
# playground/emails.py
emails = [
    "lena@uni-beispiel.de",
    "tom@uni-beispiel.de",
    " Lena@Uni-Beispiel.DE",
    "mia@uni-beispiel.de",
    "tom@uni-beispiel.de",
]

unique = set()
for email in emails:
    unique.add(email.strip().lower())

print("Verschiedene Adressen:", len(unique))
for email in sorted(unique):
    print("-", email)
```

Ausgabe:

```text
Verschiedene Adressen: 3
- lena@uni-beispiel.de
- mia@uni-beispiel.de
- tom@uni-beispiel.de
```

Vergleich: [code/m04-collections/unique_emails.py](../../project/code/m04-collections/unique_emails.py)
