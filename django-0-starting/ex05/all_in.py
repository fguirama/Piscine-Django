import sys


def main():
    ipt = sys.argv[1]
    for query in ipt.split(','):
        normalize_query = query.strip()
        if normalize_query:
            try_ = get_state(normalize_query)
            if not try_:
                try_ = get_capital_city(normalize_query)
            if not try_:
                print(f'{normalize_query} is neither a capital city nor a state')
                continue
            print('{city} is the capital of {state}'.format_map(try_))


def get_capital_city(state):
    code = get_value('states', state, 0)
    if not code:
        return None
    city = get_value('capital_cities', code[1], 0)
    return {'city': city[1], 'state': code[0]}


def get_state(city):
    code = get_value('capital_cities', city, 1)
    if not code:
        return None
    state = get_value('states', code[0], 1)
    return {'state': state[0], 'city': code[1]}


def get_value(dic, search_value, index):
    normalize_search_value = search_value.lower()
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    search_dic = states if dic == 'states' else capital_cities
    for item in search_dic.items():
        if item[index].lower() == normalize_search_value:
            return item
    return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    main()
