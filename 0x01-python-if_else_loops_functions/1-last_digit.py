#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    ld = number % 10
else:
    ld = number % -10
print(f"Last digit of {number:d} is {ld:d}", end=" ")
if ld > 5:
    print("and is greater than 5")
elif ld == 0:
    print("and is 0")
elif ld < 6:
    print("and is less than 6 and not 0")
