# dir, __dict__ and help methods in Python.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

    @classmethod
    def fromString(cls, string):
        name, salary = string.split(",")[0], string.split(",")[1]
        return cls(name, int(salary))


emp1 = Employee("Himanshu", 20000)
emp1.showDetails()
emp2 = Employee.fromString("Renu,50000")
emp2.showDetails()

# To know about all the function and methods available for any data type or object we can use dir.
print(dir(emp1))

# To know about all the properties in a class we use dir __dict__ it returns a dictionary.
print(emp1.__dict__)

# To know everything about any class or object we can use help.
print(help(Employee))
