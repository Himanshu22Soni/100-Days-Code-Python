# Sets in Python.

# Sets contains only unique values. If user gives repeated value then sets will automatically remove it.Sets are immutable means cannot be changed after creation.
set1 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
print(set1)

# We can not access items directly like array. Because sets doesn't maintain order.
for num in set1:
    print(num, end=' ')

# We cannot make empty set like this. Because set and dictionary have same syntax {} so to declare empty set we will use set() instead.
set2 = {}
set3 = set()
print(type(set2))
print(type(set3))
