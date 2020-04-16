#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
import urllib.request
from sys import argv

url = argv[1]

with urllib.request.urlopen(url) as response:
    val_header = response.getheader('X-Request-ID')

print(val_header)
