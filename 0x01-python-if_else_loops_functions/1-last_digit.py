#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
v_digit = (abs(number) % 10)

if number < 0:
    v_digit = v_digit * -1

if (v_digit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, v_digit))
elif (v_digit < 6 and v_digit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, v_digit))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, v_digit))
