import sys
import time

import requests
from bs4 import BeautifulSoup


class WikiPage:
    BASE_URL = 'https://en.wikipedia.org/wiki/{title}'

    def __init__(self, url):
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        self.title = bs.find('h1').text
        self.first_link = self.__get_first_link(bs)

    def __eq__(self, other):
        if not isinstance(other, WikiPage):
            return False
        return self.title == other.title

    def __get_first_link(self, bs):
        for link in bs.select('#bodyContent p a'):
            if link['href'].startswith('/wiki/'):
                return self.BASE_URL.format(title=link['href'].removeprefix('/wiki/'))
        raise Exception


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 roads_to_philosophy.py <query>')

    query = sys.argv[1]
    url = WikiPage.BASE_URL.format(title=query.replace(' ', '_'))
    roads = []

    while True:
        try:
            page = WikiPage(url)
        except Exception:
            raise Exception(f'fetching {url}')
        print(page.title)
        if page in roads:
            print('It leads to an infinite loop !')
            return
        if page.first_link is None:
            print('It leads to a dead end !')
            return
        if page.title == 'Philosophy':
            break
        roads.append(page)
        url = page.first_link
        time.sleep(2)

    print(f'{len(roads)} roads from {query} to philosophy')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)
