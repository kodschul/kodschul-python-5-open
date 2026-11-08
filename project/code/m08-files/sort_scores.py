# Sortieren mit key=: eine benannte Funktion bestimmt, wonach sortiert wird

scores = [
    {"name": "Anna", "tries": 3},
    {"name": "Cem", "tries": 1},
    {"name": "Lena", "tries": 5},
    {"name": "Jürgen", "tries": 2},
]


def get_tries(score):
    """Sortierschlüssel: die Anzahl der Versuche."""
    return score["tries"]


def get_name(score):
    """Sortierschlüssel: der Name."""
    return score["name"]


print("Nach Versuchen:")
for score in sorted(scores, key=get_tries):  # get_tries ohne (): Funktion übergeben
    print(" ", score["name"], score["tries"])

print("Nach Namen:")
for score in sorted(scores, key=get_name):
    print(" ", score["name"], score["tries"])

print("Die zwei Besten:", sorted(scores, key=get_tries)[:2])
print("Meiste Versuche zuerst:", sorted(scores, key=get_tries, reverse=True)[0])
