#!/usr/bin/python3
"""
Script that get header variable using request
"""
from sys import argv
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = argv[1]

    req = Request(url)

    with urlopen(req) as response:
        print(response.headers['X-Request-Id'])
