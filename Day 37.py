# Finally Keyword in Python.

try:
    l = [1, 2, 3, 4, 5]
    i = int(input("Enter a number: "))
    print(l[i])
except:
    print("Error Occured")
# Finally will execute no what is happening in try and except block.
finally:
    print("I will be executed always no matter what")


# We use finally keyword because if we are using try except inside a function and in try and except block something is returned then rest of the code will not be executed so to overcome this we use finally keyword.

def func1():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter a number: "))
        print(l[i])
        return 1
    except:
        print("Error Occured")
        return 0
# Finally will execute no what is happening in try and except block.
    finally:
        print("I will be executed always no matter what")

    print("I will not be printed.")


x = func1()
print(x)
