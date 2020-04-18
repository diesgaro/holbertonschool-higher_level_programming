#!/usr/bin/python3
"""
Script that fetch url using request
"""
from urllib.request import urlopen, Request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    req = Request(url)

    with urlopen(req) as response:
        data = response.read().decode('utf-8')

    print(
        'Body response:\n\t- type: {}\n\t- content: {}'.
        format(type(data), data)
    )
