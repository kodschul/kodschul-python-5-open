# Geld abheben: ungültige Beträge früh mit raise ablehnen (Lab 7.3)


def withdraw(balance, amount):
    """Gibt den Kontostand nach dem Abheben zurück; ungültig → ValueError."""
    if amount <= 0:
        raise ValueError(f"Betrag muss größer als 0 sein, nicht {amount}.")
    if amount > balance:
        raise ValueError(f"Nicht genug Guthaben: nur {balance} Euro verfügbar.")
    return balance - amount


balance = 100
for amount in [30, -20, 500, 50]:
    try:
        balance = withdraw(balance, amount)
    except ValueError as error:  # Meldung aus raise anzeigen
        print(f"Abgelehnt: {error}")
    else:
        print(f"{amount} Euro abgehoben. Kontostand: {balance} Euro")
