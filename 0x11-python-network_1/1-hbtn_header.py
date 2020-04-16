#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
from sys import argv
from urllib.request import urlopen, Request

my_url = argv[1]
req = Request(my_url)

with urlopen(req) as response:
    print(response.headers['X-Request-Id'])
