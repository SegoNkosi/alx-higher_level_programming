#!/usr/bin/python3
"""
A script that fetches an URL https://alx-intranet.hbtn.io/status with requests package
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
