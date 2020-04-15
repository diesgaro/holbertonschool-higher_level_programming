#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

my_url = 'https://intranet.hbtn.io/status'

with urlopen(my_url) as response:
    data = response.read()

print(
    "Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".
    format(
        type(data),
        data,
        data.decode('utf-8')
    )
)
