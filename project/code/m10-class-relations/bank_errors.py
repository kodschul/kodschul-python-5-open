# Eigene Fehlerklassen: gezielt abfangen statt nur ValueError (Lab 10.1)


class InvalidAmountError(ValueError):
    """Der Betrag ist kein gültiger Wert, z. B. 0 oder negativ."""


class InsufficientFundsError(ValueError):
    """Auf dem Konto ist nicht genug Geld."""


def withdraw(balance, amount):
    """Gibt den Kontostand nach dem Abheben zurück; löst eigene Fehler aus."""
    if amount <= 0:
        raise InvalidAmountError(f"Betrag muss größer als 0 sein, nicht {amount}.")
    if amount > balance:
        raise InsufficientFundsError(f"Nur {balance} Euro verfügbar.")
    return balance - amount


# Die eingebauten Fehler bilden selbst eine Vererbungs-Hierarchie
print("ValueError ist eine Exception:", issubclass(ValueError, Exception))
print("Eigener Fehler ist ein ValueError:", issubclass(InvalidAmountError, ValueError))

balance = 100
for amount in [30, -20, 500, 50]:
    try:
        balance = withdraw(balance, amount)
    except InsufficientFundsError as error:  # gezielt: eigener Hinweis
        print(f"Zu wenig Geld: {error} Kleineren Betrag wählen.")
    except ValueError as error:  # fängt alle übrigen ValueErrors
        print(f"Abgelehnt: {error}")
    else:
        print(f"{amount} Euro abgehoben. Kontostand: {balance} Euro")
