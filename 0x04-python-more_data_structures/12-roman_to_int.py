#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if type(roman_string) is not str:
        return 0

    d_roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    value = 0
    for i in range(len(roman_string)):
        if i > 0 and d_roman[roman_string[i]] > d_roman[roman_string[i - 1]]:
            value += d_roman[roman_string[i]] - 2*d_roman[roman_string[i - 1]]
        else:
            value += d_roman[roman_string[i]]
    return value
