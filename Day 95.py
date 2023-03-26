# Regular Expressions.

# To Practice.
# https://regexr.com/

import re

pattern = r"[A-Z]+orem"

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus eget nunc scelerisque viverra mauris in. Enim neque volutpat ac tincidunt. Nibh ipsum consequat nisl vel pretium lectus. Ultrices dui sapien eget mi.
'''
matches = re.finditer(pattern, text)

for match in matches:
    print(match)

# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs
