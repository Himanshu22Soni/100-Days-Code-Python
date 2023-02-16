# Multilevel Inheritance in Classes.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def show_details(self):
        super().show_details()
        print(f"Breed: {self.breed}")


class Puppy(Dog):
    def __init__(self, name, color):
        super().__init__(name, breed="puppy")
        self.color = color

    def show_details(self):
        super().show_details()
        print(f"Color: {self.color}")


d1 = Puppy("Shanky", "White")
d2 = Dog("Sheru", "BullDog")
d2.show_details()
print(Puppy.mro())
