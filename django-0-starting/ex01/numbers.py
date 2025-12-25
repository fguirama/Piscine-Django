def print_numbers():
    filename = 'numbers.txt'

    try:
        with open(filename) as f:
            for line in f.read().split(','):
                print(line)
    except FileNotFoundError:
        print(f'File not found `{filename}`')


if __name__ == '__main__':
    print_numbers()
