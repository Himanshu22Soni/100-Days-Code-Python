# More File IO Methods.

with open('file.txt', 'r') as f:
    # Move to the 10th byte in the file.
    # The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)


with open('file.txt', 'r') as f:
    # Read the first 10 bytes
    data = f.read(10)

    # Save the current position.
    # The tell() function returns the current position within the file, in bytes.
    current_position = f.tell()

    # Seek to the saved position
    f.seek(current_position)

with open('sample.txt', 'w') as f:
    f.write('Hello World!')
    # When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.
    f.truncate(5)

with open('sample.txt', 'r') as f:
    print(f.read())
