# Magic or Dunder methods.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # __str__ method will return a string representation of the employee. So we can print the employee.
    def __str__(self):
        return f"Employee first name: {self.first}\nlast name: {self.last}\nSalary: {self.pay}\nFull Name: {self.first} { self.last}"\

    # If I want length of first name so __len__ method will return the length of the first name which I can print directly.

    def __len__(self):
        x = 0
        for i in self.first:
            x += 1
        return x

    # Representation of employee class in a formal manner.
    def __repr__(self):
        rep = f"Employee({self.first},{self.last},{self.pay})"
        return rep

    # We can directly call the object and get these fields.
    def __call__(self):
        print(
            f"Object Name: {self.first} {self.last}\nObject Salary: {self.pay}")


emp1 = Employee("Himanshu", "Soni", 50000)
print(emp1)
print(len(emp1))
print(repr(emp1))
emp1()
