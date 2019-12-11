#!/usr/bin/python3
separator = ", "
for i in range(0, 10):
    for x in range(i + 1, 10):
        print("{}{}".format(i, x), end="")
        if (i != 8 or x != 9):
            print(separator, end="")
print("")
