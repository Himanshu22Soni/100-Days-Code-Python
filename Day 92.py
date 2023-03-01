# Function Caching.

# Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

# In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.

from functools import lru_cache
import time


@lru_cache(maxsize=None)
def delayedFunctions(n):
    time.sleep(3)
    return n*5


print(delayedFunctions(20))
print("Done for 20")
print(delayedFunctions(4))
print("Done for 4")
print(delayedFunctions(10))
print("Done for 10")

print(delayedFunctions(20))
print("Done for 20")
print(delayedFunctions(4))
print("Done for 4")
print(delayedFunctions(10))
print("Done for 10")
print(delayedFunctions(30))
print("Done for 30")
