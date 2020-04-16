#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
from sys import argv
from urllib.request import urlopen

my_url = argv[1]

with urlopen(my_url) as response:
    print(response.headers['X-Request-Id'])
