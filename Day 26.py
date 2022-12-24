# Solution of Day 15 problem.

import datetime

current_time = datetime.datetime.now()

if (current_time.hour < 12):
    print("Good Morning Sir!")
elif (current_time.hour >= 12 and current_time.hour < 17):
    print("Good Afternoon Sir!")
else:
    print("Good Evening Sir!")
