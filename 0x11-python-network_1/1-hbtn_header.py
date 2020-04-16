#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    my_url = argv[1]

    with urlopen(my_url) as response:
        print(response.headers['X-Request-Id'])
