# Enumerate function in Python.

# When we are dealing with for loops we have to declare a seperate variable to watch index. But using enumerate function we can achieve this.
fruits = ["Apple", "Banana", "Orange", "Kiwi",
          "Grapes", "Guava", "Lichi", "Strawberry", "Papaya"]

for index, fruit in enumerate(fruits):
    print(f"Fruits in list are {index}: {fruit}")

# We can also change starting index.
for index, fruit in enumerate(fruits, start=1):
    print(f"Fruits in list are {index}: {fruit}")
