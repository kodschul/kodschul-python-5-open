# Vererbung: Bird und Dog sind Animals und übernehmen deren Code (Lab 10.1)


class Animal:
    """Basisklasse: alles, was jedes Tier hat und kann."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Standard-Laut für Tiere ohne eigenen Laut."""
        return "..."

    def introduce(self):
        """Stellt das Tier vor; nutzt speak() der jeweiligen Klasse."""
        print(f"{self.name} sagt: {self.speak()}")


class Dog(Animal):
    """Ein Hund ist ein Tier: erbt __init__ und introduce, überschreibt speak."""

    def speak(self):
        return "Wuff!"


class Bird(Animal):
    """Ein Vogel ist ein Tier mit zusätzlicher Eigenschaft: kann er fliegen?"""

    def __init__(self, name, can_fly=True):
        super().__init__(name)  # Basisklasse setzt self.name
        self.can_fly = can_fly  # nur Vögel haben dieses Attribut

    def speak(self):
        return "Piep!"


fish = Animal("Nemo")
bello = Dog("Bello")
tweety = Bird("Tweety")
pingu = Bird("Pingu", can_fly=False)

fish.introduce()  # Animal.speak
bello.introduce()  # Dog.speak überschreibt Animal.speak
tweety.introduce()
print(f"{pingu.name} kann fliegen: {pingu.can_fly}")

print("Ist Bello ein Dog?   ", isinstance(bello, Dog))
print("Ist Bello ein Animal?", isinstance(bello, Animal))  # Unterklasse zählt mit
print("Ist Bello ein Bird?  ", isinstance(bello, Bird))
