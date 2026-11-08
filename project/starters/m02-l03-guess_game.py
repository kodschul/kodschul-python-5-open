# Zahlenraten – Starter für Lab 2.3 (Stand nach Lab 2.2)

# TODO Lab 2.3: feste Geheimzahl secret = 7 anlegen

print("=" * 40)
print("Zahlenraten")
print("Rate eine Zahl zwischen 1 und 10.")
print("=" * 40)

name = input("Name: ")
guess_text = input("Tipp: ")  # input() liefert immer Text (str)
guess = int(guess_text)  # Text in eine ganze Zahl umwandeln

print(f"{name} tippt {guess}")
# TODO Lab 2.3: Ergebnis des Vergleichs guess == secret ausgeben
