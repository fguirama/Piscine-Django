class Intern:
    class Coffee:
        def __str__(self):
            return 'This is the worst coffee you ever tasted.'

    def __init__(self, name='My name? I’m nobody, an intern, I have no name.'):
        self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception('I’m just an intern, I can’t do that...')

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':
    mark = Intern('Mark')
    print(f'mark instance name : {mark.Name}')
    print(f'Mark pls make a coffee ?')
    coffee = mark.make_coffee()
    print(coffee)

    print('\n')

    random_intern = Intern()
    print(f'random_intern instance str : {random_intern}')
    print(f'random_intern instance name : {random_intern.Name}')
    try:
        random_intern.work()
    except Exception as e:
        print(e)
