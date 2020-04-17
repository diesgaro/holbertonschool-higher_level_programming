#!/usr/bin/python3
"""
Script that get the response header of a request
"""
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    my_url = argv[1]

    with urlopen(my_url) as response:
        print(response.headers['X-Request-Id'])
