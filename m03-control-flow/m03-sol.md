# Modul 3 – Transferübung, Lösung: Würfeln bis zur 6

## Aufgabe 1: Ein Wurf

```python
import random

number = random.randint(1, 6)
print(f"Wurf 1: {number}")
```

## Aufgabe 2: Würfeln bis zur 6

```python
rolls = 0
while True:                        # Bedingung steht im Block: break bei 6
    number = random.randint(1, 6)
    rolls += 1
    print(f"Wurf {rolls}: {number}")
    if number == 6:
        break

print(f"Würfe bis zur 6: {rolls}")
```

`while True:` läuft, bis `break` sie beendet. Das passt, weil erst nach dem Würfeln feststeht, ob Schluss ist.

Alternative ohne `break`: Startwert setzen, der sicher keine 6 ist.

```python
rolls = 0
number = 0
while number != 6:
    number = random.randint(1, 6)
    rolls += 1
    print(f"Wurf {rolls}: {number}")
```

## Aufgabe 3: Bewertung

```python
if rolls == 1:
    print("Sofort!")
elif rolls <= 3:
    print("Schnell.")
else:
    print("Geduld gebraucht.")
```

Die Reihenfolge zählt: `rolls == 1` muss vor `rolls <= 3` stehen, sonst bekäme ein einzelner Wurf nur „Schnell.“.

## Aufgabe 4: Schätzung

```python
estimate = int(input("Wie viele Würfe bis zur ersten 6? "))   # ganz oben
...
result = "getroffen" if estimate == rolls else "daneben"
print(f"Schätzung {estimate}: {result}")
```

Vollständige Datei:

```python
# Würfeln bis zur 6

import random

estimate = int(input("Wie viele Würfe bis zur ersten 6? "))

rolls = 0
while True:
    number = random.randint(1, 6)
    rolls += 1
    print(f"Wurf {rolls}: {number}")
    if number == 6:
        break

print(f"Würfe bis zur 6: {rolls}")

if rolls == 1:
    print("Sofort!")
elif rolls <= 3:
    print("Schnell.")
else:
    print("Geduld gebraucht.")

result = "getroffen" if estimate == rolls else "daneben"
print(f"Schätzung {estimate}: {result}")
```

## Aufgabe 5: Fester Seed

```python
import random

random.seed(4)  # nur zum Testen
```

Beide Starts liefern (Python 3.14):

```text
Wie viele Würfe bis zur ersten 6? 4
Wurf 1: 2
Wurf 2: 3
Wurf 3: 1
Wurf 4: 6
Würfe bis zur 6: 4
Geduld gebraucht.
Schätzung 4: getroffen
```

Ohne die Seed-Zeile ändert sich die Folge bei jedem Start, zum Beispiel `Würfe bis zur 6: 9`.

## Erweiterung

```python
import random

again = "j"
while again == "j":
    estimate = int(input("Wie viele Würfe bis zur ersten 6? "))

    rolls = 0
    while True:
        number = random.randint(1, 6)
        rolls += 1
        print(f"Wurf {rolls}: {number}")
        if number == 6:
            break

    print(f"Würfe bis zur 6: {rolls}")
    # ... Bewertung und Schätzung wie oben, eine Ebene eingerückt

    again = input("Nochmal würfeln? (j/n): ").strip().lower()
```

`rolls = 0` steht in der äußeren Schleife, damit jede Runde bei null beginnt.
