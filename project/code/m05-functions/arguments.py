# Argumente: nach Position, nach Name (Schlüsselwort) und Standardwerte


def book_room(room, hours=1, projector=False):
    """Gibt eine Raumbuchung aus; hours und projector haben Standardwerte."""
    extra = "mit Beamer" if projector else "ohne Beamer"
    print(f"Raum {room}: {hours} h, {extra}")


book_room("B204")  # nur die Pflichtangabe, Rest Standard
book_room("B204", 2)  # nach Position: hours = 2
book_room("A101", projector=True)  # nach Name: hours bleibt 1
book_room(room="C3", hours=3, projector=True)  # alles nach Name
book_room(hours=2, room="C3")  # nach Name ist die Reihenfolge egal
