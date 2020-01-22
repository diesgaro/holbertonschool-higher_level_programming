#!/usr/bin/python3
import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

argv = sys.argv
argl = len(argv)

my_list = []
filename = "add_item.json"

for i in range(argl):
    if i > 0:
        my_list.append(argv[i])

if os.path.isfile(filename):
    load_list = load_from_json_file(filename)
else:
    load_list = []

load_list.extend(my_list)

save_to_json_file(load_list, filename)
