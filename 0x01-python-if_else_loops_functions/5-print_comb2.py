#!/usr/bin/python3
separator = ", "
list = []
for i in range(0, 100):
    if i < 10:
        list.insert(i, "{}{}".format(0, i))
    else:
        list.insert(i, "{}".format(i))

print(separator.join(list))
