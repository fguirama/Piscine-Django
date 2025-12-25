import sys


def get_capital_city(state):
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
        code = states[state]
        city = capital_cities[code]
        return city
    except KeyError:
        return 'Unknown state'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)
    ipt_state = sys.argv[1]
    print(get_capital_city(ipt_state))
