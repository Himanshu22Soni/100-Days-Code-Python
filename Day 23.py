# List Methods.

names = ['Himanshu', "Kanika", "Shrasti", "Renu", "Vijay", "Vaibhav"]
names2 = ["Joseph", "Smith", "Williamson", "Warner"]

# Add Element at the end of the list.
names.append("Prakhar")

# Sort the list.
names.sort()
names.sort(reverse=True)

# Returns the given index element.
print(names.index("Vijay"))

# Returns the occurence of given element.
print(names.count("Vaibhav"))

# Copies old list in new list.
new_names = names.copy()

# Insert given element at given index.
new_names.insert(1, "Nitin")

# It just add the new list at the end of old list.
names.extend(names2)

# Concatinating two lists.
names3 = names+names2

print(names)
print(new_names)
print(names3)
