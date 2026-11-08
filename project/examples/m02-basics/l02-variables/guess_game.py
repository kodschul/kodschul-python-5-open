# Zahlenraten – Stand Lab 2.2: Name und Tipp abfragen

print("=" * 40)
print("Zahlenraten")
print("Rate eine Zahl zwischen 1 und 10.")
print("=" * 40)

name = input("Name: ")
guess_text = input("Tipp: ")  # input() liefert immer Text (str)
guess = int(guess_text)  # Text in eine ganze Zahl umwandeln

print(f"{name} tippt {guess}")
