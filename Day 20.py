# Functions in Python.

# Function defined with parameters.
def getGeoMean(a, b):
    mean = (a*b)/(a+b)
    print("The mean of given no. are:", mean)


def getGreaterNumbers(a, b):
    if (a > b):
        print("a is greater than b")
    else:
        print("a is less than or equal to b")


def getLessNumbers(a, b):
    # Pass means We will define the body of the function later. You should carr on with program execution.
    pass


x = int(input("Enter 1st Number: "))

y = int(input("Enter 2nd Number: "))

# Function called with arguments.
getGeoMean(x, y)
getGreaterNumbers(x, y)
