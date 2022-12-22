# Tuple Methods.

# There is no direct method to operate on tuple. First we have to change the tuple to list. Then perform operations on list and after that convert that list to a tuple.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

num = list(numbers)
num.append(10)
num.reverse()
num[0] = 0
numbers = tuple(num)
print(numbers)

# There are some methods that we can apply to tuple.

# Will return the no. of occurence of given number.
numbers.count(6)

# Will return first occurence of given number.
numbers.index(4)
