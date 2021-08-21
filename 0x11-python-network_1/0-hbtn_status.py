#!/usr/bin/python3
""" Show Status """


if __name__ == "__main__":
    """ Python script that fetches """
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf content: {}'.format(html.decode('utf-8')))
