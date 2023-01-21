# Map, Filter and Reduce functions.

from functools import reduce

# Map function.
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.The iterable argument can be a list, tuple, or any other iterable object.
l = [1, 2, 4, 6, 4, 3]
newl = []

newl = list(map(lambda x: x*x*x, l))
print(newl)

# Filter Function.
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.


def filter_function(a):
    return a > 2


newnewl = list(filter(filter_function, l))
print(newnewl)

# Reduce Function.
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value.It is important to note that the reduce function requires the functools module.
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function


def mysum(x, y):
    return x + y


sum = reduce(mysum, numbers)

# Print the sum
print(sum)
