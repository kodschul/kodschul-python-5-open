# Zahlenraten – Starter für Lab 2.4 (Stand nach Lab 2.3)

secret = 7  # vorerst fest; ab Lab 3.2 zufällig

print("=" * 40)
print("Zahlenraten")
print("Rate eine Zahl zwischen 1 und 10.")  # TODO Lab 2.4: Zeile entfernen, Begrüßung kommt nach der Namensabfrage
print("=" * 40)

name = input("Name: ")  # TODO Lab 2.4: Namen mit strip() und title() aufräumen
# TODO Lab 2.4: "Hallo <Name>! Rate eine Zahl zwischen 1 und 10." mit f-String ausgeben

guess = int(input("Tipp: "))

print(f"{name} tippt {guess}")
print("Treffer:", guess == secret)  # == liefert True oder False
