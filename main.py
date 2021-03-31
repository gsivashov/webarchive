import json

from requests_html import HTMLSession
from argparse import ArgumentParser
from datetime import datetime


def get_response(url):
    session = HTMLSession()
    response = session.get(url)
    # print(url.strip())
    return response


def api_url(url):
    return f'http://archive.org/wayback/available?url={url}'


def main(file):
    '''
    https://archive.org/help/wayback_api.php
    '''

    with open(file) as start_file:
        for url in start_file:
            response = get_response(api_url(url.strip()))
            parse = response.json()
            if len(parse['archived_snapshots']) != 0:
                archive_url = parse['archived_snapshots']['closest']['url']
                timestamp = parse['archived_snapshots']['closest']['timestamp']
                formated_date = datetime.strptime(timestamp, "%Y%m%d%H%M%S")
                print(f'{url.strip()}|{formated_date}|{archive_url}')
            else:
                print(f'{url.strip()}|no date|no url')


if __name__ == '__main__':
    main('urls.txt')
