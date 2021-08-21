#!/usr/bin/python3
""" Show Status """


if __name__ == "__main__":
    """ Python script that fetches """
    import urllib.request as request
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf content: {}'.format(html.decode('utf-8')))
