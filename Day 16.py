# Match Case Statements. Only available in latest versions of Python.

x = int(input("Enter te value of X: "))

match x:
    case 0:
        print("X value is 0")
    case 1:
        print("X value is 1")
    # For default cases _ is used. No need to add break statement as we do in C++.
    case _ if x == 90:
        print("X value is 90")
    # I can use condition statement with default case also.
    case _ if x == 80:
        print("X value is 80")
    case _:
        print("X value is ", x)
