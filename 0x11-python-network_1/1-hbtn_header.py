#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
from sys import argv
from urllib.request import urlopen

url = argv[1]

with urlopen(url) as response:
    val_header = response.getheader('X-Request-ID')

print(val_header)
