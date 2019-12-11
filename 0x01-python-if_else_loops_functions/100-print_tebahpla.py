#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:s}".format(chr(i) if (not(i % 2)) else chr(i).upper()), end='')
