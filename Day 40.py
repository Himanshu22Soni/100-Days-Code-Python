# Secret Code language Exercise.

import random


def encryption(st):
    if len(st) >= 3:
        # Taking out first character from string.
        st2 = st[0:1]
        # Putting it to the end of the string.
        st3 = st+st2
        # Having a new string without the first character.
        st = st3[1:]
        characters = []
        st4 = ""
        # Generating 6 random characters.
        for i in range(6):
            characters.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        # Placing 3-3 random characters at starting and ending of string.
        for i in range(6):
            if i < 3:
                st = st+characters.pop()
            else:
                st4 = st4+characters.pop()
        resultString = st4+st
        return resultString
    else:
        # Simply reversing the string.
        dumString = ""
        for i in range(len(st)):
            dumString = st[i]+dumString
        return dumString


def decryption(st):
    # Simply reversing the string.
    if len(st) < 3:
        dumString = ""
        for i in range(len(st)):
            dumString = st[i]+dumString
        return dumString
    else:
        # Popping 3-3 characters from start and end.
        st2 = st[3:-3]
        # Taking last character and adding it to the start of string.
        st3 = st2[len(st2)-1]
        st2 = st3+st2
        return st2[0:len(st2)-1]


inputStr = input("Enter the String to encrypt: ")
encryptedStr = encryption(inputStr.lower())
print(encryptedStr)
charY = input("Press Y if you want to decrypt: ")
if charY == 'y' or charY == 'Y':
    print(decryption(encryptedStr).capitalize())
