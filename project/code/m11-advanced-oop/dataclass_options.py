# Dataclass-Optionen: order=True, frozen=True, field(default_factory=list)

from dataclasses import FrozenInstanceError, dataclass, field


@dataclass(order=True)  # erzeugt <, <=, >, >=: vergleicht Feld für Feld
class Grade:
    """Note: order=True vergleicht zuerst points, dann subject."""

    points: int
    subject: str


grades = [Grade(2, "Mathe"), Grade(1, "Deutsch"), Grade(2, "Englisch")]
print(sorted(grades))  # erst nach points, bei Gleichstand nach subject


@dataclass(frozen=True)  # eingefroren: Felder lassen sich nicht mehr ändern
class Coordinate:
    """Ein fester Ort, z. B. Köln."""

    lat: float
    lon: float


cologne = Coordinate(50.94, 6.96)
try:
    cologne.lat = 0.0
except FrozenInstanceError as error:  # Fehler beim Ändern eines frozen-Feldes
    print("Geht nicht:", error)


@dataclass
class Course:
    """Kurs mit Teilnehmerliste: jede Instanz bekommt eine eigene leere Liste."""

    title: str
    members: list = field(default_factory=list)  # nicht: members: list = []


python = Course("Python")
excel = Course("Excel")
python.members.append("Anna")
print(python)
print(excel)  # eigene Liste, Anna steht nur im Python-Kurs
