import sys


def main():
    if len(sys.argv) != 2:
        exit(1)
    ipt_city = sys.argv[1]
    print(get_state(ipt_city))


def get_state(city):
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

    try:
        code = get_key(capital_cities, city)
        state = get_key(states, code)
        return state
    except ValueError:
        return 'Unknown capital city'


def get_key(dic, value):
    for key, val in dic.items():
        if val == value:
            return key
    raise ValueError()


if __name__ == '__main__':
    main()
