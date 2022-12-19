# Lists in Python.

# Lists are mutable. Or we can say that we can change list items after declaration.
names = ["Himanshu", "Nitin", "Kanika", "Shrasti", "Renu"]

for name in names:
    for i in name:
        print(i, end=" ")

print(names[-3])  # Negative Indexing.
print(names[len(names)-3])  # Converting negative index to positive index.

if "Nitin" in names:
    print("Yes It is present")
else:
    print("No It is not present")

print(names[:])  # It means it will start from 0 and will print till the end.

print(names[1:])  # It means it will start from 1 and will print till the end.

# It means it will start from 0 and will print till the index 2.
print(names[:3])

# It means it will start from 0 and will print till the end and will jump by n-1 places where n is last value provided.
print(names[::2])

# List Comprehension. It means we can generate a list by giving some condition on the go. We can give any condition as per our requirements.
list2 = [i*i for i in range(20) if i % 2 == 0]
print(list2)

names_less_than4 = [name for name in names if len(name) < 4]
print(names_less_than4)
