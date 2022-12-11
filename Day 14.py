# If else Statement.

a = int(input("Enter your age: "))

# Conditional operators >,<,>=,<=,==,!=

if (a > 18):
    print("You can drive")
elif (a == 18):
    print("Apply for driving license first")
else:
    print("You can not drive")

# Nested If else.

num = 18

if (num < 0):
    print("Negative number")
elif (num > 0):
    if (num <= 10):
        print("Number less than 10")
    elif (num >= 10 and num <= 20):
        print("Number less than 20 but greater than 10")
    else:
        print("Number greater than 20")
else:
    print("Number is zero")
