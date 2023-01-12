# File only for testing purposes.

name = "Himanshu Soni"


def welcome():
    print('Welcome to the 100 Days of Code')


# In this file value of __name__will be __main__. If called from other file then its value will be that file's name.
print(__name__)

# This means it is checking that if this file is calling the function if yes then only run the function otherwise no.
if __name__ == '__main__':
    welcome()
