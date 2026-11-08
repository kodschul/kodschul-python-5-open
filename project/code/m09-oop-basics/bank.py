# Bankkonto als Klasse: Daten (Inhaber, Kontostand) und Verhalten (ein-, auszahlen)


class BankAccount:
    """Ein Bankkonto mit Inhaber und Kontostand."""

    currency = "€"  # Klassenattribut: gilt für alle Konten gemeinsam

    def __init__(self, owner):
        self.owner = owner  # Instanzattribute: jedes Konto hat eigene Werte
        self.balance = 0

    def deposit(self, amount):
        """Zahlt einen Betrag auf dieses Konto ein."""
        self.balance += amount

    def withdraw(self, amount):
        """Hebt einen Betrag von diesem Konto ab."""
        self.balance -= amount  # prüft nichts: Konto kann ins Minus gehen

    def show_balance(self):
        """Gibt Inhaber und Kontostand aus."""
        print(f"Konto von {self.owner}: {self.balance} {self.currency}")


if __name__ == "__main__":  # nur beim Start dieser Datei, nicht beim Import
    account = BankAccount("Anna")
    account.show_balance()

    account.deposit(1000)
    account.withdraw(200)
    account.show_balance()

    # Klassenattribut: über die Klasse und über jedes Objekt lesbar
    print("Währung:", BankAccount.currency, account.currency)

    # Problem für Lab 9.3: Jeder Code kann den Kontostand direkt ändern
    account.withdraw(5000)
    account.show_balance()
    account.balance = 1000000
    account.show_balance()
