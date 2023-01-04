# Raising custom errors in Python.

# In Python we can raise custom errors using Raise keyword.
i = input("Enter number between 1 to 10:")
try:
    if int(i) < 1 or int(i) > 10:
        raise ValueError("Enter number between 1 and 10")
except:
    if i != "quit":
        raise ValueError("String is not quit")
    else:
        print("OK Quitting.")
