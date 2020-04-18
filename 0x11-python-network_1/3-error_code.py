#!/usr/bin/python3
"""
Script that handle errors generates in the request
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = argv[1]

    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
