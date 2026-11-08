# Zuweisungsausdruck := ("Walross"): Wert speichern und prüfen in einer Zeile

# Vorher: input() steht zweimal, vor der Schleife und am Ende des Blocks
items = []
text = input("Eintrag (leer = fertig): ").strip()
while text != "":
    items.append(text)
    text = input("Eintrag (leer = fertig): ").strip()
print("Liste:", items)

# Nachher: := speichert die Eingabe in text und vergleicht sie sofort
items = []
while (text := input("Eintrag (leer = fertig): ").strip()) != "":
    items.append(text)
print("Liste:", items)

# Auch in if: Ergebnis einmal berechnen, prüfen und danach weiterverwenden
if (count := len(items)) > 2:
    print(f"{count} Einträge, das reicht für einen Großeinkauf.")
