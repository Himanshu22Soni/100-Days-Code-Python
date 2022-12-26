# Doc Strings in Python.

# Doc strings are working as comment but they have different functionality. We can access the doc string directly. It is treated specially by Python.

# Doc strings are always declared before function definition and just after function declaration.
def square(n):
    '''It takes a number and returns a square and prints.'''
    print(n*n)


square(25)
print(square.__doc__)
