# Class Methods as Alternative Constructors in Python.

# In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.

# However, there are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor. This is where class methods can be used as alternative constructors.

# A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. For example, consider a class named "Person" that has two attributes: "name" and "age".

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def showDetails(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

    # But what if you want to create a Employee object from a string that contains the person's name and salary, separated by a comma? You can define a class method named "from_string" to do this:
    @classmethod
    def fromString(cls, string):
        name, salary = string.split(",")[0], string.split(",")[1]
        return cls(name, int(salary))


emp1 = Employee("Himanshu", 20000)
emp1.showDetails()
emp2 = Employee.fromString("Renu,50000")
emp2.showDetails()
print(dir(emp1))
