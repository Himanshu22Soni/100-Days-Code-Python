# Operator Overloading.
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Using this dunder method to add two complex numbers.
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Using this dunder method to multiply two complex numbers.
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imag*other.imag, self.imag*other.real+other.imag*self.real)

    def __str__(self):
        return f"Results of Complexes are: {self.real} + {self.imag}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

# We can directly add or multiply two objects just using + or *.
print(c1+c2)
print(c1*c2)
