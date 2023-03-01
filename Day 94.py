# Exercise 11 Water Drink Reminder.

import time
from plyer import notification

title = "Water Reminder"
message = "Drink Water Please.It's been an hour."

while True:
    notification.notify(
        title=title,
        message=message,
        timeout=10,
        toast=False
    )
    time.sleep(5)
