#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10

if (number >= 0):
    last_digit = number % 10
else:
    last_digit = (number * -1) % 10
    last_digit *= -1

print(f"Last digit of {number} is {lastdigit}", end="")

if lastdigit > 5 :
    print(" and is greater than 5")

elif lastdigit < 6 and lastdigit != 0 :
    print(" and is less than 6 and not 0")

elif lastdigit == 0 :
    print(" and is 0")


