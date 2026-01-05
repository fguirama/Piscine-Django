import sys

import requests
from bs4 import BeautifulSoup


class WikiPage:
    WIKI = '/wiki/'
    BASE_URL = 'https://en.wikipedia.org' + WIKI + '{title}'

    class NoLinkFound(Exception):
        pass

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
        if bs.find(id='noarticletext'):
            raise WikiPage.NoLinkFound
        for link in bs.select('#bodyContent p a, #bodyContent ul a'):
            if (
                    not link.has_attr('href') or
                    not link['href'].startswith(self.WIKI) or
                    link.find_parent('table')
            ):
                continue

            paragraph = link.find_parent('p')
            if paragraph:
                text_before_link = ''
                for elem in paragraph.descendants:
                    if elem == link:
                        break
                    if isinstance(elem, str):
                        text_before_link += elem
                
                open_parens = text_before_link.count('(') - text_before_link.count(')')
                if open_parens > 0:
                    continue
            
            return self.BASE_URL.format(title=link['href'].removeprefix(self.WIKI))
        raise WikiPage.NoLinkFound


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 roads_to_philosophy.py <query>')

    query = sys.argv[1]
    url = WikiPage.BASE_URL.format(title=query.replace(' ', '_'))
    roads = []

    while True:
        try:
            page = WikiPage(url)
        except WikiPage.NoLinkFound:
            print('It leads to a dead end !')
            return
        print(page.title)
        if page in roads:
            print('It leads to an infinite loop !')
            return
        if page.title == 'Philosophy':
            break
        roads.append(page)
        url = page.first_link

    print(f'{len(roads)} roads from {query} to philosophy')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)
