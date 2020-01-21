#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as f:
        list = f.readlines()

    if nb_lines <= 0 or nb_lines >= len(list):
        for line in list:
            print(line, end='')
    else:
        for i in range(nb_lines):
            print(list[i], end='')
