# Function Arguments and Return.

# Here we already defined default values. If no arguments are passed,then these values will be taken as default values.
def getAveraging(a=10, b=20):
    #print("The average of the numbers are:", (a+b)/2)
    return (a+b)/2


# Variable length arguments. Here numbers is iterable.
def getAverage(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("The average of the numbers are:", sum/len(numbers))


print("The average of the numbers are:", getAveraging())

# Here we are passing arguments according to parameters name. So here order of passing doesn't matter.
print("The average of the numbers are:", getAveraging(b=6, a=20))

getAverage(10, 20, 30, 32)
