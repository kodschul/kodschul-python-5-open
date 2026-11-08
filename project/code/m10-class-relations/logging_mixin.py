# Mixin: kleine Fähigkeit (Protokollieren), die mehrere Klassen ausleihen (Lab 10.4)


class LoggingMixin:
    """Fähigkeit „protokollieren“: braucht nur ein Attribut name."""

    def log(self, text):
        print(f"[{self.name}] {text}")


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class LoggingBankAccount(LoggingMixin, BankAccount):
    """Konto mit Protokoll: Mixin zuerst, dann die eigentliche Basisklasse."""

    def deposit(self, amount):
        super().deposit(amount)  # das normale Einzahlen aus BankAccount
        self.log(f"{amount} Euro eingezahlt, Stand {self.balance} Euro")


class Thermostat(LoggingMixin):
    """Hat mit Konten nichts zu tun, nutzt aber dieselbe Fähigkeit."""

    def __init__(self, name):
        self.name = name
        self.temperature = 20

    def set_temperature(self, degrees):
        self.temperature = degrees
        self.log(f"Temperatur auf {degrees} °C gestellt")


account = LoggingBankAccount("Konto Anna", 100)
account.deposit(50)
heating = Thermostat("Heizung Bad")
heating.set_temperature(22)
print("MRO:", LoggingBankAccount.mro())
