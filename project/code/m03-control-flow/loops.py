# Schleifen: while, for mit range, for über einen String, break, continue

# 1) while: wiederholen, solange die Bedingung wahr ist
count = 1
while count <= 3:
    print(f"while-Durchlauf {count}")
    count += 1  # ohne diese Zeile endet die Schleife nie

# 2) for mit range(start, stop, step): stop selbst ist nicht dabei
for number in range(1, 6):
    print(number, end=" ")
print()  # Zeilenumbruch nach der Zahlenreihe

for number in range(10, 0, -3):  # rückwärts in Dreierschritten
    print(number, end=" ")
print()

# 3) Zähler mitführen: Summe von 1 bis 100
total = 0
for number in range(1, 101):
    total += number
print(f"Summe 1 bis 100: {total}")

# 4) for über die Zeichen eines Strings
for letter in "Anna":
    print(letter, end="-")
print()

# 5) break: Schleife sofort verlassen
for char in "Raum B204":
    if char in "0123456789":
        print(f"Erste Ziffer: {char}")
        break

# 6) continue: Rest des Durchlaufs überspringen
for char in "Programmieren":
    if char in "aeiou":
        continue  # Vokal überspringen, weiter mit dem nächsten Zeichen
    print(char, end="")
print()

# 7) else an einer Schleife: läuft nur, wenn kein break kam
for char in "Hallo":
    if char in "0123456789":
        print("Ziffer gefunden")
        break
else:
    print("Keine Ziffer in 'Hallo'")
