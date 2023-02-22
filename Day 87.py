# Shutil Module in Python.

import shutil as shu

try:
    # Copy file from src to dest.
    shu.copy("Day 86.py", "C:/Users/hp/Desktop")
    # Copy complete folder from src to dest.
    shu.copytree("TestingPDF", "C:/Users/hp/Desktop/CopiedFromPython")
    # Deletes complete folder
    shu.rmtree("C:/Users/hp/Desktop/pdfs")
except:
    print("Error copying file")
print("Successfull")
