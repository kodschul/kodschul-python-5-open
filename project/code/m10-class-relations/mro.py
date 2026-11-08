# Mehrfachvererbung und MRO: Mitarbeiterin und Kundin zugleich (Lab 10.4)


class Person:
    def __init__(self, name):
        self.name = name

    def discount(self):
        return 0  # Prozent Rabatt

    def greet(self):
        print("  Person.greet")


class Employee(Person):
    def discount(self):
        return 20  # Mitarbeiterrabatt

    def greet(self):
        print("  Employee.greet")
        super().greet()  # nächste Klasse in der MRO, nicht unbedingt Person


class Customer(Person):
    def discount(self):
        return 5  # Kundenkarte

    def greet(self):
        print("  Customer.greet")
        super().greet()


class EmployeeCustomer(Employee, Customer):
    """Zwei Basisklassen: erst Employee, dann Customer."""


anna = EmployeeCustomer("Anna")
print(f"{anna.name} bekommt {anna.discount()} % Rabatt")  # Employee gewinnt

print("Suchreihenfolge (MRO):")
for cls in EmployeeCustomer.__mro__:  # Tupel aller Klassen in Suchreihenfolge
    print(" ", cls.__name__)  # __name__: Name der Klasse als Text

print("greet() mit super() läuft die MRO entlang:")
anna.greet()

print(EmployeeCustomer.mro())  # dieselbe Reihenfolge als Liste
