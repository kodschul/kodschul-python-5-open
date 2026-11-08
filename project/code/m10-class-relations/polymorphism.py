# Polymorphie: derselbe Aufruf vehicle.move(), unterschiedliches Verhalten (Lab 10.2)


class Vehicle:
    """Basisklasse für alles, was fährt."""

    def __init__(self, name):
        self.name = name

    def move(self):
        return "bewegt sich irgendwie"

    def honk(self):
        """Standard: kein Laut. pass = leerer Block, hier passiert nichts."""
        pass


class Car(Vehicle):
    def move(self):
        return "fährt auf der Straße, 4 Räder"

    def honk(self):
        print(f"{self.name}: Hup hup!")


class Bicycle(Vehicle):
    def move(self):
        return "rollt auf dem Radweg, 2 Räder"


class Ferry:
    """Erbt NICHT von Vehicle, hat aber auch move() und honk(): Duck Typing."""

    def __init__(self, name):
        self.name = name

    def move(self):
        return "fährt über den Rhein"

    def honk(self):
        print(f"{self.name}: Tuuut!")


def start_trip(vehicle):
    """Kennt nur die Methoden move() und honk(), nicht die Klasse."""
    print(f"{vehicle.name} {vehicle.move()}")
    vehicle.honk()


vehicles = [Car("Auto"), Bicycle("Fahrrad"), Ferry("Fähre")]
for vehicle in vehicles:
    start_trip(vehicle)  # eine Zeile, drei Verhaltensweisen
