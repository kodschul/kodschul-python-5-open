# Lab 4.1 – Lösung: Listen

Fertiger Stand: [examples/m04-collections/l01-lists/guess_game.py](../../project/examples/m04-collections/l01-lists/guess_game.py)

## Aufgabe 1: Leere Liste pro Runde

```python
    tries = 0
    guesses = []  # leere Liste: noch kein Tipp
```

Die Zeile steht innerhalb der äußeren Schleife. So beginnt jede Runde mit einer leeren Liste.

## Aufgabe 2: Tipp anhängen

```python
        guess = int(input("Tipp: "))
        tries += 1
        guesses.append(guess)  # Tipp hinten anhängen
```

`append` hängt hinten an; die Liste behält dadurch die Reihenfolge der Eingaben.

## Aufgabe 3: Liste ausgeben

```python
    print("Bisherige Tipps:", guesses)
    play_again = input("Nochmal spielen? (j/n): ").strip().lower()
```

Die Zeile ist so weit eingerückt wie `play_again = …`: Sie läuft einmal pro Runde, nach der inneren Schleife. `print` zeigt die Liste mit eckigen Klammern und Kommas.

## Aufgabe 4: Spiel starten

```bash
python playground/guess_game.py
```

Beispiellauf (Geheimzahl 7):

```text
========================================
Zahlenraten
========================================
Name: Anna

Neue Runde, Anna! Rate eine Zahl zwischen 1 und 10.
Tipp: 5
Zu niedrig.
Verbleibende Versuche: 2
Tipp: 8
Zu hoch.
Verbleibende Versuche: 1
Tipp: 7
Richtig, Anna! Benötigte Versuche: 3.
Bisherige Tipps: [5, 8, 7]
Nochmal spielen? (j/n): n
Danke fürs Spielen, Anna!
```

## Aufgabe 5: Zweite Runde

Nach `j` zeigt die nächste Runde nur ihre eigenen Tipps, z. B. `Bisherige Tipps: [3]` bei einem Treffer im ersten Versuch. Stehen dort auch die Tipps der ersten Runde, liegt `guesses = []` vor `while play_again == "j":` statt darin.

Vollständiger Code:

```python
# Zahlenraten – Stand Lab 4.1: alle Tipps einer Runde in einer Liste

import random

MAX_TRIES = 3

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()

play_again = "j"
while play_again == "j":
    secret = random.randint(1, 10)
    tries = 0
    guesses = []  # leere Liste: noch kein Tipp
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen 1 und 10.")

    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))
        tries += 1
        guesses.append(guess)  # Tipp hinten anhängen

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

## Erweiterung

```python
# playground/grades.py
grades = [2.0, 1.3, 2.7, 1.0, 3.3]

average = sum(grades) / len(grades)
print("Anzahl:", len(grades))
print("Durchschnitt:", round(average, 2))
print("Beste Note:", min(grades))
print("Schlechteste Note:", max(grades))
print("Sortiert:", sorted(grades))
```

Ausgabe:

```text
Anzahl: 5
Durchschnitt: 2.06
Beste Note: 1.0
Schlechteste Note: 3.3
Sortiert: [1.0, 1.3, 2.0, 2.7, 3.3]
```

Vergleich: [code/m04-collections/average_grades.py](../../project/code/m04-collections/average_grades.py)
