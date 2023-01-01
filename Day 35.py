# For loops with else statements.

for i in range(5):
    print(i)
    if i == 3:
        break
    # If break is appearing then else wil not be executed because loop is breaking here.
else:
    print("For loop exited")

# We can use else with while loop also.
x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("While loop exited")
