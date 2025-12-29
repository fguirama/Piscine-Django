import json
import requests
import sys


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 request_wikipedia.py <query>')

    query = sys.argv[1]

    try:
        response = wikipedia_search(query)
    except requests.exceptions.RequestException:
        response = {}

    filename = f'{to_snakecase(query)[:50]}.wiki'
    with open(filename, 'w') as f:
        json.dump(response, f, indent=2)


def to_snakecase(query):
    return query.lower().replace(' ', '_')


def wikipedia_search(query):
    url = 'https://en.wikipedisa.org/w/api.php'

    headers = {
        'User-Agent': 'PiscineDjango/django-1-lib/ex02/1.0 (fguirama@student.42berlin.de)'
    }

    params = {
        "action": "opensearch",
        "search": query,
        "format": "json"
    }

    response = requests.get(url, headers=headers, params=params)
    return response.json()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)
