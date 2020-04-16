#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    val_header = response.getheader('X-Request-ID')

print(val_header)
