# Komposition: ein Car hat einen Engine – es ist keiner (Lab 10.3)


class Engine:
    """Verbrennungsmotor mit Leistung in PS."""

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Brumm! {self.horsepower}-PS-Motor läuft."


class ElectricEngine:
    """Elektromotor: andere Klasse, aber dieselbe Methode start()."""

    def __init__(self, kilowatt):
        self.kilowatt = kilowatt

    def start(self):
        return f"Summ … {self.kilowatt}-kW-Elektromotor läuft."


class Horn:
    """Hupe: gehört fest zum Auto."""

    def honk(self):
        return "Hup hup!"


class Car:
    """Ein Auto hat einen Motor (von außen) und eine Hupe (selbst gebaut)."""

    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Aggregation: Motor kommt von außen, ist tauschbar
        self.horn = Horn()  # Komposition: Hupe entsteht mit dem Auto

    def start(self):
        """Delegiert: das Auto bittet seinen Motor, zu starten."""
        print(f"{self.brand}: {self.engine.start()}")

    def honk(self):
        print(f"{self.brand}: {self.horn.honk()}")


engine = Engine(150)
car = Car("Kombi", engine)
car.start()
car.honk()

car.engine = ElectricEngine(110)  # Motor tauschen, Car bleibt unverändert
car.start()

print("Auto ist ein Motor?", isinstance(car, Engine))  # nein: es HAT einen
print("Motor ist ein Elektromotor?", isinstance(car.engine, ElectricEngine))
