# Break and Continue Statement.

# Break means exit the particular loop and Continue means exit the particular iteration.

for i in range(1, 11):
    if (i == 3):
        # After this loop will break and no printing will be done.
        break
    print("5 X", i, "=", 5*i)

for i in range(1, 11):
    if (i == 3):
        # After this iteration will be skipped and printing will resume from next iteration.
        continue
    print("5 X", i, "=", 5*i)
