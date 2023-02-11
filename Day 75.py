# Exercise 07 Solution of Day 68.

import os

files = os.listdir("testing")
print(files)
i = 1
for file in files:
    if file.endswith(".png"):
        os.rename(f"testing/{file}", f"testing/{i}.png")
        i = i+1
        print(files)
