# Sets Methods.

s1 = {1, 2, 3, 5, 6}
s2 = {3, 7, 8}

# Union will merge these two sets. By this it will not change orginal sets.
print(s1.union(s2))

# To change original sets we will use update method.
s1.update(s2)
print(s1)

# Intersection will give the values that are present in both sets.
print(s1.intersection(s2))

# To change original sets we will use update method.
s1.intersection_update(s2)
print(s1)

# Symmetric difference will give the values that are unique in both sets.
print(s1.symmetric_difference(s2))

# To change original sets we will use update method.
s1.symmetric_difference_update(s2)
print(s1)

# Difference will return the values that are present in calling set and not in called set.It return new set.
print(s1.difference(s2))

# To change original sets we will use update method.
s1.difference_update(s2)
print(s1)

# isDisjoint will return true if the values in calling set are not present in called set.Otherwise False.
print(s1.isdisjoint(s2))

# isSuperset will return false if the values in called set are not present in calling set.Otherwise True.
print(s1.issuperset(s2))

# isSubset will return true if the values in calling set are present in called set.Otherwise False.
print(s2.issubset(s1))

# To add an element.
s2.add(9)

# To add more than one element.
s3 = {11, 12, 13, 14}
s2.update(s3)

# To remove or discard an element.
s2.remove(11)  # It will generate error if element is not found.
s1.discard(1)  # It will not generate any error if element is not found.

# To pop last element from set. The catch is we dont know that which element will be popped as sets are unordered.
item = s2.pop()
print(item)

# To delete a set completely we use del keyword.
del s1
del s2
print(s1, s2)

# But if we dont want to delete the set completely but just want to delete all elements.
s3.clear()
print(s3)
