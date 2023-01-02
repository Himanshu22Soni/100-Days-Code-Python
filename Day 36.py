# Exception Handeling.

a = input("Enter the number:")

# In this block if some error occurs then error will be printed and further execution of code will continue.
try:
    for i in range(1, 11):
        print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print(e)

print("End of code")

# We can also have multiple exceptions.
try:
    num = input("Enter the number:")
    a = [6, 4]
    print(a[int(num)])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Out of bounds")
