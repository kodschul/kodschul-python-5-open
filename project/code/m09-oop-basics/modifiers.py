# Sichtbarkeit: öffentlich, _intern (Konvention), __privat (Namensverschleierung)


class Locker:
    """Ein Schließfach mit Besitzer, Fehlversuchen und geheimer PIN."""

    def __init__(self, owner, pin):
        self.owner = owner  # öffentlich: darf jeder lesen und ändern
        self._failed_tries = 0  # _intern: „bitte nicht von außen anfassen“
        self.__pin = pin  # __privat: Python versteckt den Namen

    def open(self, pin):
        """Gibt True zurück, wenn die PIN stimmt; zählt Fehlversuche mit."""
        if pin == self.__pin:  # innerhalb der Klasse ganz normal nutzbar
            self._failed_tries = 0
            return True
        self._failed_tries += 1
        return False


locker = Locker("Anna", 4711)
print("Besitzer:", locker.owner)
print("Öffnen mit 1234:", locker.open(1234))
print("Öffnen mit 4711:", locker.open(4711))

# _intern: technisch erreichbar, nur eine Abmachung unter Programmierern
locker.open(1111)
print("Fehlversuche:", locker._failed_tries)

# __privat: unter diesem Namen von außen nicht erreichbar
try:
    print(locker.__pin)
except AttributeError as error:
    print("AttributeError:", error)

# Python hat den Namen nur umbenannt: _Klasse__name
print("Umweg:", locker._Locker__pin)  # funktioniert, aber nie so verwenden

# Eine Zuweisung von außen legt nur ein NEUES Attribut an
locker.__pin = 0
print("Öffnen mit 0:", locker.open(0))  # False: die echte PIN ist unverändert
