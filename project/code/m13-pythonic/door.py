# Tür auf – arbeiten – Tür zu: __enter__ und __exit__ einer eigenen Klasse


class Door:
    """Context Manager: öffnet beim Betreten, schließt beim Verlassen."""

    def __init__(self, room):
        self.room = room

    def __enter__(self):
        print(f"Tür zu {self.room} auf")
        return self  # wird zur Variablen hinter "as"

    def __exit__(self, exc_type, exc_value, traceback):
        # exc_type: Art des Fehlers im Block, None ohne Fehler
        print(f"Tür zu {self.room} zu (Fehler: {exc_type})")
        return False  # Fehler nicht verschlucken


with Door("Labor") as door:
    print("arbeite in", door.room)

try:
    with Door("Küche"):
        print("koche ...")
        raise ValueError("Topf übergelaufen")
except ValueError as error:
    print("abgefangen:", error)
