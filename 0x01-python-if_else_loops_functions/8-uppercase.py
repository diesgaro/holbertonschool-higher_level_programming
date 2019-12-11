#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        value = ord(str[i])
        print("{}"
              .format(chr(value - 32) if (value >= 97 and value <= 122)
                      else chr(value)), end="")

    print("")
