# Single Inheritance in Classes.

class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    def sounds(self):
        print("Sound from Animal")


# Single Inheritance.
class Dog(Animal):
    def __init__(self, name, specie):
        super().__init__(name, specie)

    def sounds(self):
        print("Sound from Dog")


d = Dog("Shanky", "Golden Retriver")
d.sounds()
