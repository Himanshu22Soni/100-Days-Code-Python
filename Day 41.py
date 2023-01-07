# If else in one line.

a = 10
b = 50

print("a") if a > b else print("=") if a == b else print("b")

# We can also do this.
c = 9 if a > b else 0
print(c)  # 0 Printed.
