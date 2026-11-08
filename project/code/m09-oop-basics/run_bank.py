# Mehrere Konten nach demselben Bauplan: Objekte importieren, verwalten, verbinden

from bank import BankAccount  # bank.py liegt im selben Ordner


def transfer(sender, receiver, amount):
    """Überweist einen Betrag von einem Konto auf ein anderes."""
    sender.withdraw(amount)  # Methode des einen Objekts
    receiver.deposit(amount)  # Methode des anderen Objekts


alice = BankAccount("Alice")
bob = BankAccount("Bob")

alice.deposit(1000)
transfer(alice, bob, 200)
transfer(bob, alice, 50)

alice.show_balance()  # 850 €: jedes Objekt hat seinen eigenen Kontostand
bob.show_balance()  # 150 €

# Objekte in einer Liste: alle Konten der Bank
accounts = [alice, bob, BankAccount("Cem")]
total = 0
for account in accounts:
    total += account.balance
print(f"{len(accounts)} Konten, zusammen {total} {BankAccount.currency}")
