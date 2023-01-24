# Classes and Objects.

class Person:
    name = "Himanshu Soni"
    occupation = "System Engineer"
    age = 23

    # Here self is written because when we have multiple objects then the parameters of that particular object will be passed to the function which is responsible for calling this method.
    def getInfo(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.getInfo()

# If i want to change the name I can do it like this...
a.name = "John"
a.getInfo()

b = Person()
b.name = "Nitin"
b.occupation = "Customer Support"
b.getInfo()
