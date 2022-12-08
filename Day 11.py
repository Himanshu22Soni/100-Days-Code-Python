# Strings

name = "Himanshu Soni"
print("Hi,"+name)

welcome = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas vel augue libero. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam sit amet augue quis lorem efficitur lobortis vel sit amet dolor. Integer maximus, lectus '''

# Can enclose a string between ''' and it will take long string without pressing enter.

print(welcome)

# Index of characters

print(name[3])

# Can use loop also to print index of characters

index = 0
for characters in welcome:
    index += 1
print(index)
