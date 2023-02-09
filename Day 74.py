# Method Overriding.

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)

    # Here we are creating a method as same name of parent class method but here working is different. This is called Method Overriding.
    def getArea(self):
        return 3.14 * super().getArea()


circle1 = Circle(5)
print(circle1.getArea())
