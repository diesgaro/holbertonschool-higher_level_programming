#!/usr/bin/python3
"""
Script that sends post request and the service return a Json
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    parameter = ""
    send_parameters = {}

    if (len(argv) > 1):
        parameter = argv[1]

    send_parameters['q'] = parameter

    req = requests.post(url, data=send_parameters)

    try:
        print('No result') if req.json() == {} else print(
            '[{}] {}'.
            format(
                req.json()['id'],
                req.json()['name']
            )
        )
    except ValueError as e:
        print('Not a valid JSON')
