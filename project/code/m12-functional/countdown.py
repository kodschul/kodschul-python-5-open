# Gleiche Aufgabe zweimal: eigener Iterator als Klasse und als Generatorfunktion


class Countdown:
    """Iterator-Objekt: zählt von start bis 1 herunter."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # das Objekt ist selbst sein Iterator

    def __next__(self):
        if self.current < 1:
            raise StopIteration  # Ende melden
        value = self.current
        self.current -= 1
        return value


def countdown(start):
    """Generator: dasselbe in vier Zeilen, Python baut __iter__/__next__ selbst."""
    while start >= 1:
        yield start  # Wert abgeben und hier pausieren
        start -= 1


print("Klasse:   ", list(Countdown(3)))
print("Generator:", list(countdown(3)))
print("Typ:", type(countdown(3)))


def ticket_numbers():
    """Unendlicher Generator: liefert Wartenummern, so viele wie abgefragt werden."""
    number = 1
    while True:  # endet nie, rechnet aber nur auf Anfrage
        yield f"A-{number}"
        number += 1


tickets = ticket_numbers()
print(next(tickets), next(tickets), next(tickets))
