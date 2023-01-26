# Decorators in Python.

# Taking function as argument.
def greet(fx):
    def inner():
        print("Hello, I am Inner function of Greet")
        # Calling argument function.
        fx()
        print("Goodbye")
    return inner


def addDecorator(fx):
    def inner(*args, **kwargs):
        print("Hello, I am Inner function of addDecorator")
        fx(*args, **kwargs)
        print("Goodbye")
    return inner


# Decorator
@greet
def hello():
    print("Hello World!!")

# Decorator
@addDecorator
def add_function(a, b, c):
    print(a+b+c)


hello()
add_function(4,5,6)

# Another way of writing it.
addDecorator(add_function(7,8,9))
