# Constructor in Classes.

class Company:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def geEmployee(self):
        print(
            f"Hi my name is {self.name} and my department is {self.department}")


emp1 = Company("Himanshu", "HR")
emp2 = Company("Nitin", "Sales")
emp1.geEmployee()
emp2.geEmployee()
