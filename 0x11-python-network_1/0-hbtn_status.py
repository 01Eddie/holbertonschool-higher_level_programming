#!/usr/bin/python3
import urllib.request
""" Show Status """


if __name__ == "__main__":
    """ Python script that fetches """
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- utf content: {}'.
              format(type(html), html, html.decode('utf-8')))
