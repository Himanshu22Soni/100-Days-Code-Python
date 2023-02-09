# Super Keyword.

class Parent:
    def __init__(self, name):
        self.name = name

    def get_parent(self):
        print("Parent Class Method")


class Child(Parent):
    def __init__(self, name):
        self.name = name

    def get_child(self):
        print("Child Class Method")
        # Super keyword is calling the method of parent class with object as argument.
        super().get_parent()


class GrandChild(Child, Parent):
    def __init__(self, name):
        # We can even call constructor of super class passing object as argument.
        super().__init__(name)

    def get_grand_child(self):
        print("Grand Child Method")
        super().get_child()
        super().get_parent()


child1 = Child("Himanshu")
child1.get_child()

grandChild1 = GrandChild("Nitin")
grandChild1.get_grand_child()
