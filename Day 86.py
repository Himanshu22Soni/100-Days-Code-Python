# Walrus Operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression
a = True
print(a := False)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while (n := len(list1) > 0):
    print(list1.pop() * 2)

# This is a normal method to implement this while loop and append of items without walrus operator.
food = list()
while True:
    name = input("Name of food: ")
    if name == "quit":
        break
    food.append(name)

# If I implement same thing with walrus it will look like this.
food = list()
while (foodName := input("Name of food: ")) != "quit":
    food.append(foodName)

print(food)
