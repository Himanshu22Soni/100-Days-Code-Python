# File IO in Python.

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist.This is default mode if no parameter is passed.

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist. Difference between write and append is that if we write on a file using w then its old contents will be deleted and the new contents will be created.

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images,pdfs etc)

# r means we are opening the file and can only read from it.
f = open("index.txt", 'r')
text = f.read()
print(text)
f.close()

# Closing is mandatory. But instead of writing close every time we can use this:
with open('index.txt', 'r') as f:
    text = f.read()

print(text)
