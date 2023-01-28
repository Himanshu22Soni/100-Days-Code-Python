# Getters and setters.

class Numbers:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value is {self.value}")

    @property
    # We are using this property because we can use it as a property by object.
    def ten_value(self):
        return 10 * self.value

    @ten_value.setter
    # This will set the value of the property.
    def ten_value(self, new_value):
        self.value = new_value/10

num1 = Numbers(10)

num1.show()
num1.value = 30
num1.ten_value = 200
print(num1.ten_value)
num1.show()

