#!/usr/bin/python3
"""
Script that sends a get request using OAuth basic authentication
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    my_user = argv[1]
    my_token = argv[2]

    req = requests.get(url, auth=HTTPBasicAuth(my_user, my_token))

    print(req.json()['id']) if req.status_code == 200 else print('None')
