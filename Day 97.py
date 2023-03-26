# MultiThreading in Python.

import threading
import time


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)


# This function is used to check time taken by a section of code.
time1 = time.perf_counter()

# # Normal Code
func(4)
func(3)
func(1)

time2 = time.perf_counter()
print(time2-time1)

# Code using threading
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

# This will wait to finish the first thread.
t1.join()
t2.join()
t3.join()

time3 = time.perf_counter()
print(time3-time1)
