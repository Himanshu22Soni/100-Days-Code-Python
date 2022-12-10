# More String Methods.

name = "Himanshu     Soni!!!!!!!!!!"  # Strings are immutable

# All these methods are not changing the existing string they are creating a new string and performing opertions on them.

print(name.upper())  # Upper case.

print(name.lower())  # Lower case.

print(name.rstrip("!"))  # It is striping the trailing "!".

# Replaces all the occurrences of string with given string.
print(name.replace("Himanshu", "Nitin"))

# It is spliting the string with " " and creating a list.
print(name.split(" "))

# Capitalize first character of the string and lowercase the remaining characters.
print(name.capitalize())

print(name.center(100))  # Brings string to the center by giving spaces.

# Counts the number of occurrences of particular string or character.
print(name.count("!"))

print(name.endswith("!"))  # Tell that if string is ending with "!".

print(name.endswith("Soni", 0, 13))  # We can also check in between string.

# Returns first occurrence of string or character. Returns -1 if not found.
print(name.find("s"))

# Completely works same as find but it doesn't return -1 it generates error.
print(name.index("s"))

print(name.isalnum())  # Checks if the string is alphanumeric.

print(name.isalpha())  # Checks if the string is only alphabetic.

print(name.islower())  # Checks if the string is only lowercase.

print(name.isspace())  # Checks if the string is having whitespace.

print(name.istitle())  # Checks if all the words in the string are capitalize.

print(name.swapcase())  # Upper Case to lower case and vice versa.

print(name.title())  # Capitalize each word in the string.
