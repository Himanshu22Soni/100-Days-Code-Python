# Static Methods.

class Maths:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def add(a, b):
        # No need to pass self as argument. Now this method is no longer associated to any class or object. We can call it directly.
        return a + b


m = Maths(6)
print(m.add(7, 8))

# And we can call it like this.
print(Maths.add(6, 7))
