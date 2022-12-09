# String Methods

name = "Himanshu Soni"
# Starting Index and the ending index as no of characters. Here starting index will be included and ending index will be excluded.
print(name[0:8])

# Reducing 3 characters from end of string. It means  [0:len(name)-3]
print(name[0:-3])

# Reducing 2 characters from end of string and removing 3 characters from beginning. It means [len(name)-3:len(name)-2].
print(name[-3:-2])

print(len(name))  # length function.
