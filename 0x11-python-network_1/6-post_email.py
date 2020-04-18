#!/usr/bin/python3
"""
Script that get header variable using request
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    send_parameters = {}
    send_parameters['email'] = email

    req = requests.post(url, data=send_parameters)

    print(req.text)
