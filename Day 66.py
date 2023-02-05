# Instance vs Class Variables.

class Employee:
    country = "India"  # Class variable associated to Class.f

    def __init__(self, name, salary):
        self.name = name  # Instance Variable associated to objects.
        self.salary = salary
        self.company = "Google"

    def showDetails(self):
        print(
            f"Name: {self.name}\nSalary: {self.salary}\nCompany: {self.company}\nCountry: {self.country}")


emp1 = Employee("Himanshu", 500)
emp2 = Employee("Nitin", 600)

emp1.showDetails()
# We can change particular class variable according to the object.
emp1.country = "USA"
emp2.showDetails()
emp1.showDetails()
