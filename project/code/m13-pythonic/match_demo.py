# match/case: Literal-, Sequenz-, Klassen- und Dictionary-Muster

from dataclasses import dataclass


# 1. Literalmuster: Wert direkt vergleichen, | heißt "oder"
def day_type(day):
    """Ordnet ein Tageskürzel ein."""
    match day:
        case "sa" | "so":
            return "Wochenende"
        case "mo" | "di" | "mi" | "do" | "fr":
            return "Werktag"
        case _:  # Platzhalter: passt auf alles, was oben nicht passte
            return "unbekannt"


# 2. Sequenzmuster: Liste nach Länge und Inhalt zerlegen, if = Bedingung (Guard)
def shopping(command):
    """Wertet einen Befehl für eine Einkaufsliste aus."""
    match command.split():  # "neu Milch 2" -> ["neu", "Milch", "2"]
        case ["liste"]:
            return "zeige die Liste"
        case ["neu", item]:  # genau zwei Wörter, das zweite heißt jetzt item
            return f"1 x {item} dazu"
        case ["neu", item, amount] if amount.isdigit():
            return f"{amount} x {item} dazu"
        case []:  # leere Eingabe
            return "nichts eingegeben"
        case _:
            return f"unbekannter Befehl: {command}"


# 3. Klassenmuster: Objekt nach Klasse und Attributen prüfen
@dataclass
class Point:
    x: int
    y: int


def where(point):
    """Beschreibt die Lage eines Punkts."""
    match point:
        case Point(x=0, y=0):
            return "im Ursprung"
        case Point(x=0, y=y):  # y wird mit dem Attribut belegt
            return f"auf der y-Achse bei {y}"
        case Point(x=x, y=0):
            return f"auf der x-Achse bei {x}"
        case Point():
            return "irgendwo anders"


# 4. Dictionary-Muster: Schlüssel müssen vorhanden sein, weitere sind egal
def describe(person):
    """Beschreibt eine Person aus einem Dictionary wie in persons.json."""
    match person:
        case {"name": name, "age": age} if age >= 18:
            return f"{name} ist volljährig"
        case {"name": name, "age": age}:
            return f"{name} ist {age}"
        case {"name": name}:
            return f"{name}, Alter unbekannt"


print("1. Literal:", day_type("sa"), "|", day_type("mi"), "|", day_type("xy"))
for text in ["liste", "neu Milch", "neu Eier 6", "neu Eier viele", ""]:
    print("2. Sequenz:", repr(text), "->", shopping(text))
print("3. Klasse:", where(Point(0, 0)), "|", where(Point(0, 5)))
print("3. Klasse:", where(Point(4, 0)), "|", where(Point(3, 4)))
print("4. Dictionary:", describe({"name": "Anna", "age": 21, "city": "Köln"}))
print("4. Dictionary:", describe({"name": "Ben", "age": 16}))
print("4. Dictionary:", describe({"name": "Cem"}))
