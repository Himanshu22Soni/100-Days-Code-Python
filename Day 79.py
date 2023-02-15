# Multiple Inheritance.

class LivingEntity:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species


class Dog(Animal, LivingEntity):
    def __init__(self, name, age, species):
        super().__init__(name, age, species)


d = Dog("Shanky", 23, "XYZ")
print(d.species)
print(Dog.mro())
