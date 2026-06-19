#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

if last_digit < 0:
    last_digit += 10
if number < 0 and last_digit > 0:
    last_digit -= 10

if last_digit > 5:
    extra = "and is greater than 5"
elif last_digit == 0:
    extra = "and is 0"
else:
    extra = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, extra))
