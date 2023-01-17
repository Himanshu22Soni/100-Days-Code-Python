# Local & Global variables.

x = 5
print(f"Global x is {x}")


def func():
    x = 3  # This x will be deleted as the function ends.
    print(f"Local x is {x}")

# To create a global variable inside a function, we can use the global keyword.
def func2():
    # Global keyword is holding the global variable x and now any updation we do on x in this function this will also updated globally.
    global x
    x = 10
    print(f"Global x is {x}")


func()
func2()
print(x)
