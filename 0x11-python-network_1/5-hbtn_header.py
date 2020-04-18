#!/usr/bin/python3
"""
Script that get header variable using request
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    req = requests.get(url)

    print(req.headers.get('X-Request-Id'))
