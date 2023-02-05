# Class Methods in Python.

class Employee:
    country = "India"

    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f"Name: {self.name}\nCountry: {self.country}")

    @classmethod
    def change_country(cls, new_country):
        # This method is taking class as first argument and making changes to class variables.
        cls.country = new_country


emp1 = Employee("Himanshu")
emp1.print_details()
emp1.change_country("USA")
emp1.print_details()
print(Employee.country)
