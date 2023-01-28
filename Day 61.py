# Inheritance in classes.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print("Name:", self.name)
        print("ID:", self.id)

class Manager(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def showDetails(self):
        super().showDetails()
        print("Salary:", self.salary)

e1 = Employee("Himanshu",123)
e1.showDetails()

m1 = Manager("Nitin",231,50000)
m1.showDetails()