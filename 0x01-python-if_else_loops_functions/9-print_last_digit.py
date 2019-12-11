#!/usr/bin/python3
def print_last_digit(number):
    v_digit = (abs(number) % 10)
    print("{:d}".format(v_digit), end="")
    return v_digit
