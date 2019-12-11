#!/usr/bin/python3
separator = ", "
list = []
for i in range(0, 10):
    for j in range(i + 1, 10):
        list.append("{}{}".format(i, j))

print(separator.join(list))
