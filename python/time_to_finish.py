# Find out if a number is a square
# test time it takes to complete
# one-liner vs readable code

import math
import time


def my_square(n):
    if n < 0:
        return False
    number = int(math.sqrt(n))
    return number**2 == n


def is_square(n):
    return n >= 0 and math.sqrt(n) % 1 == 0


n = 25.0000000000
start_time = time.perf_counter()
print(my_square(n))
print(
    f"This took... {(time.perf_counter() - start_time)*1000:.2f} milliseconds to complete")
