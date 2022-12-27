# Recursion in Python.

def factorial(x):
    '''Returns the factorial of number'''
    if x == 0 or x == 1:
        return 1
    else:
        return (x*factorial(x-1))


y = int(input("Enter number: "))
print(factorial(y))


def fibonacci(x):
    '''Return fibonacci elements'''
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)


print(fibonacci(4))
