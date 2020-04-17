#!/usr/bin/python3
"""
Script that sends a POST request to a http service
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":
    url = argv[1]
    data = {}
    data['email'] = argv[2]
    parameters = urlencode(data)

    req = Request(url, parameters.encode('ascii'))

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
