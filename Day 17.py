# Loops in Python.

# For Loops in Python.

name = "Himanshu Soni"

for i in name:
    print(i, end=" ")

# Starts from 1 and will print upto 99. Last parameter is step which means it will skip k-1 element in range. Suppose k is 2 so it will skip 1 element in range.
for k in range(1, 100, 2):
    print(k, end=" ")
