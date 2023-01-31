# Access Specifiers.

# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable
        # Private variable by using '__' before variable name.
        self.__class = "IT"
        self.__clg = "BVDU"


obj = Student(22, "Himanshu")
print(obj.age)
print(obj.name)

# Can't access like this. It will raise error.
# print(obj.__class)
# Class name befor variable name.
print(obj._Student__class)
print(obj._Student__clg)


class StudentNew:
    def __init__(self):
        self._name = "Himanshu"

    def _funName(self):      # protected method
        return "Himanshu Soni"


class Subject(StudentNew):  # inherited class
    pass


obj = StudentNew()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
