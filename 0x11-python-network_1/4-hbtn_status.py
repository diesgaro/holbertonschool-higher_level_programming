#!/usr/bin/python3
"""
Script that fetch url using request
"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    req = requests.get(url)

    print(
        'Body response:\n\t- type: {}\n\t- content: {}'.
        format(type(req.text), req.text)
    )
