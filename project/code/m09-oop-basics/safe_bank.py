# Bankkonto mit Kapselung: Kontostand nur lesbar, Regeln prüfen jede Änderung


class BankAccount:
    """Ein Bankkonto, dessen Kontostand nie unter 0 fällt."""

    def __init__(self, owner, balance=0):  # Standardwert statt Überladung
        self.owner = owner  # nutzt schon den Setter unten (prüft den Namen)
        self.__balance = balance  # privat: nur die Methoden ändern ihn

    @property
    def balance(self):
        """Kontostand: lesbar wie ein Attribut, aber ohne Setter nicht änderbar."""
        return self.__balance

    @property
    def owner(self):
        """Inhaber des Kontos."""
        return self.__owner

    @owner.setter
    def owner(self, name):
        """Prüft den neuen Namen, bevor er gespeichert wird."""
        if name.strip() == "":
            raise ValueError("Der Inhaber braucht einen Namen.")
        self.__owner = name.strip()

    def deposit(self, amount):
        """Zahlt einen positiven Betrag ein."""
        if amount <= 0:
            raise ValueError("Einzahlungen müssen größer als 0 sein.")
        self.__balance += amount

    def withdraw(self, amount):
        """Hebt ab; ein negativer Kontostand löst ValueError aus."""
        if amount > self.__balance:
            raise ValueError(f"Nicht genug Guthaben: {self.__balance} €.")
        self.__balance -= amount


# Zwei Arten, ein Konto zu eröffnen – eine Methode, ein Standardwert
empty = BankAccount("Cem")
account = BankAccount("Anna", 100)
print(empty.owner, empty.balance, "€ |", account.owner, account.balance, "€")

account.deposit(50)
account.withdraw(30)
print("Kontostand:", account.balance, "€")  # ohne (): sieht aus wie ein Attribut

# Regel 1: Abheben ins Minus ist nicht möglich
try:
    account.withdraw(500)
except ValueError as error:
    print("ValueError:", error)

# Regel 2: Kontostand ist nur lesbar
try:
    account.balance = 1000000
except AttributeError as error:
    print("AttributeError:", error)

# Regel 3: Der Setter prüft jeden neuen Namen
account.owner = "Anna Schmidt"
print("Neuer Inhaber:", account.owner)
try:
    account.owner = "   "
except ValueError as error:
    print("ValueError:", error)

print("Kontostand am Ende:", account.balance, "€")
