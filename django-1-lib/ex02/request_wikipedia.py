import sys

import dewiki
import requests


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 request_wikipedia.py <query>')

    query = sys.argv[1]

    try:
        response = wikipedia_search(query)
    except requests.exceptions.RequestException:
        raise Exception('Wikipedia API request failed')

    try:
        content = list(response['query']['pages'].items())[0][1]['revisions'][0]['*']
    except Exception:
        raise Exception('no results found')
    new_content = format_content(content)
    filename = f'{to_snakecase(query)[:50]}.wiki'
    with open(filename, 'w') as f:
        f.write(new_content)


def to_snakecase(query):
    return query.lower().replace(' ', '_')


def wikipedia_search(query):
    url = 'https://en.wikipedia.org/w/api.php'

    params = {
        'action': 'query',
        'titles': query,
        'prop': 'revisions',
        'rvprop': 'content',
        'format': 'json'
    }

    response = requests.get(url, headers={'User-Agent': 'DjangoPiscine-d04/1.0'}, params=params)
    return response.json()


def format_content(content):
    content = dewiki.from_string(content)
    content = remove_ref(content)
    content = content.strip()
    content = content.replace('<code>', '')
    content = content.replace('</code>', '')
    return content


def remove_ref(content):
    while True:
        idx_start = content.find('<ref')
        if idx_start == -1:
            break
        idx_end_close = content[idx_start:].find('</ref>')
        idx_end_selfclose = content[idx_start:].find('/>')
        if idx_end_close == -1 and idx_end_selfclose == -1:
            break
        if idx_end_close == -1 or idx_end_selfclose < idx_end_close:
            idx_end, len_rm = idx_end_selfclose, 2
        else:
            idx_end, len_rm = idx_end_close, 6
        idx_end += idx_start
        content = content[:idx_start] + content[idx_end + len_rm:]
    return content


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')
        exit(1)
