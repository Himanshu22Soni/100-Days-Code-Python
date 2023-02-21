# Time Module in Python.
import time

print("Hello World")
time.sleep(3)
print("Hello World after 3 seconds")

t = time.localtime()
# Fromating the returned time in seconds into a string.
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
