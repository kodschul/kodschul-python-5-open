# Sortieren, kleinstes und größtes Element mit key=lambda

persons = [
    {"name": "Marie", "age": 40},
    {"name": "Fritz", "age": 18},
    {"name": "Paul", "age": 15},
    {"name": "Anna", "age": 22},
]


# Lab 8.2: benannte Funktion als Schlüssel
def get_age(person):
    """Sortierschlüssel: das Alter."""
    return person["age"]


print("def:      ", [p["name"] for p in sorted(persons, key=get_age)])

# lambda: derselbe Schlüssel ohne eigene def-Zeile
by_age = sorted(persons, key=lambda person: person["age"])
print("lambda:   ", [p["name"] for p in by_age])

# reverse=True: absteigend, der Älteste zuerst
oldest_first = sorted(persons, key=lambda person: person["age"], reverse=True)
print("absteigend:", [p["name"] for p in oldest_first])

# nach Namen: Schlüssel ist ein String, sortiert alphabetisch
print("nach Name:", [p["name"] for p in sorted(persons, key=lambda p: p["name"])])

# min und max kennen key= genauso
youngest = min(persons, key=lambda person: person["age"])
oldest = max(persons, key=lambda person: person["age"])
print("jüngste Person:", youngest["name"], "· älteste Person:", oldest["name"])
