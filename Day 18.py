# While Loop in Python.

i = 0
while (i <= 5):
    print(i, end=" ")
    i = i+1
else:
    print("\nI am in else loop")

# Do while loop.

i = 0
while True:  # Infinte while loop.
    # This print will be printed at least once. After that condition will be checked.
    print(i, end=" ")
    i = i+1
    if (i % 100 == 0):
        break
