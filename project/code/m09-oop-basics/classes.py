# Eine eigene Klasse: Bauplan für Studierende mit Namen und Noten


class Student:
    """Bauplan: Jede Studentin, jeder Student hat Namen, Semester und Noten."""

    def __init__(self, name, semester):
        # self = das Objekt, das gerade gebaut wird
        self.name = name  # Instanzattribut: gehört nur zu diesem Objekt
        self.semester = semester
        self.grades = []  # jedes Objekt bekommt seine eigene, leere Liste

    def add_grade(self, grade):
        """Hängt eine Note an die Notenliste dieses Objekts an."""
        self.grades.append(grade)

    def average(self):
        """Gibt den Notendurchschnitt zurück, ohne Noten 0.0."""
        if len(self.grades) == 0:
            return 0.0
        return round(sum(self.grades) / len(self.grades), 2)

    def describe(self):
        """Gibt einen Satz über dieses Objekt aus."""
        print(f"{self.name}, {self.semester}. Semester, Schnitt {self.average()}")


# Zwei Objekte nach demselben Bauplan
anna = Student("Anna", 3)  # ruft __init__ auf, self ist das neue Objekt
cem = Student("Cem", 1)

anna.add_grade(1.7)  # Python macht daraus: Student.add_grade(anna, 1.7)
anna.add_grade(2.3)
cem.add_grade(3.0)

anna.describe()
cem.describe()

# Attribute lesen und ändern mit Punkt
print(anna.grades, cem.grades)  # jede Liste gehört zu ihrem Objekt
cem.semester = 2
print(cem.name, "ist jetzt im Semester", cem.semester)

# Ein Objekt direkt ausgeben: Python zeigt nur Klasse und Speicheradresse
print(anna)
print(type(anna))

# Objekte in einer Liste sammeln
course = [anna, cem, Student("Lena", 5)]
for student in course:
    print(student.name, student.average())
