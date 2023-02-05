# Exercise 07 Clear the Clutter.

# Not my Solution.

import os


def to_raw(string):
    return fr"{string}"


def Change_fileName(extension, user_dir_path):
    if (os.path.exists(user_dir_path)):
        os.chdir(user_dir_path)

        print("***Welcome to the programme for changing a series of files***")
        print(
            f"\nThe current Directory where the operation is going to be performed is :: {os.path.abspath(user_dir_path)}"
        )

        # Finding the files with current extension user given extension
        dir_list = os.listdir()
        file_list = list(filter(lambda x: os.path.isfile(x) == True, dir_list))
        file_with_user_extension = list(
            filter(lambda x: os.path.splitext(x)[1] == extension, file_list))
        print(
            f'\nThe list of all the file in the current directory with user given extension {extension} are:: '
        )
        for index, i in enumerate(file_with_user_extension):
            print(f'{index+1}. {i}')
        choice = input(
            "Do you want to change the above files' name to Numerical order [y]/n :: "
        )
        status = True if (choice == 'y') else False
        if (status == True):
            print("get ready for chnages")
            for index, i in enumerate(file_with_user_extension):
                print(f"extension changed {index+1}")
                os.rename(i, fr"{index+1}_screenShot{extension}")
        else:
            exit
    else:
        exit


print("****Welcome to the programme to change the change file names****")
ch = int(
    input(
        "Chose the extension you want to change the file name for::\n1. '.pdf'\n2. '.jpg'\n3. '.png'\n4. '.txt'\nChoice :: "
    ))
extent = ".pdf" if (ch == 1) else ".jpg" if (ch == 2) else ".png" if (
    ch == 3) else ".txt"
print(f"The chosen extension for changes is :: {extent}")
print("\nSpecifiy the Directory to introduce changes into::")
dir_user = input(
    "Enter the file path with forward '/' if working in Linux-OS\nEnter the file path with backward '\' if working in Windows-OS\nOr press '.' for current directory \nChoice :: "
)
dir_user = to_raw(dir_user)
Change_fileName(extent, dir_user)
