# Alles in Python ist ein Objekt: Daten und passendes Verhalten in einem Wert

# 1. Jeder Wert hat einen Typ – type() nennt seine Klasse (aus Lab 2.2)
values = [5, 2.5, "anna", [5, 8, 10], {"leicht": (1, 10, 5)}, None]
for value in values:
    print(value, "->", type(value))


# 2. Funktion: die Daten werden von außen übergeben
def shout(text):
    """Gibt den Text in Großbuchstaben mit Ausrufezeichen zurück."""
    return text.upper() + "!"


print(shout("hallo"))

# 3. Methode: der Wert bringt sein Verhalten selbst mit (Punkt-Schreibweise)
name = "anna"
print(name.upper())  # der String weiß selbst, wie er groß wird
print(name.count("n"))  # ... und wie oft ein Buchstabe vorkommt

guesses = [5, 8]
guesses.append(10)  # die Liste ändert sich selbst
print(guesses)

# 4. Dieselbe Methode, verschiedene Objekte: jedes kennt seine eigenen Daten
first = "anna"
second = "jürgen"
print(first.title(), second.title())

# 5. Auch Funktionen sind Objekte
print(type(shout))
