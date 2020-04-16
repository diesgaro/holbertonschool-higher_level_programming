#!/usr/bin/python3
"""
Script that get response header X-Request-Id
"""
import sys
import urllib.request

my_url = sys.argv[1]
req = urllib.request.Request(my_url)

with urllib.request.urlopen(req) as response:
    print(response.headers['X-Request-Id'])
