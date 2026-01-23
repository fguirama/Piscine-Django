import random

from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self):
        self._nb_serve_drink = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__()
            self.name = 'empty cup'
            self.price = 0.90
            self._description = 'An empty cup?! Gimme my money back'

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__('This coffee machine has to be repaired')

    def repair(self):
        self._nb_serve_drink = 0
        print('Machine successfully repaired!')

    def serve(self, drink):
        if self._nb_serve_drink == 10:
            raise self.BrokenMachineException()
        serve_drink = random.choice([drink, self.EmptyCup()])
        self._nb_serve_drink += 1
        return serve_drink


if __name__ == '__main__':
    machine = CoffeeMachine()

    for i in range(10):
        test_drink = random.choice([Coffee, Tea, Chocolate, Cappuccino])
        print(f'\n\nTest [{i + 1:02}] with drink {test_drink} :\n{machine.serve(test_drink())}')

    print(f'\n\nTest [11] with drink {Coffee} (it shouldn\'t work because it\'s the 11th drink) :')
    try:
        machine.serve(Coffee())
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Error: {e}')

    print(f'\n\nTest [12] with drink {Cappuccino} (still not work) :')
    try:
        machine.serve(Cappuccino())
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Error: {e}')

    print('\n\nTry to repair the machine and see if it works again :')
    machine.repair()
    print(machine.serve(Coffee()))

    print('\n\nGreat, the machine work again, let\'s take some drink again!')
    for i in range(9):
        test_drink = random.choice([Coffee, Tea, Chocolate, Cappuccino])
        print(f'\n\nTest [{i + 13:02}] with drink {test_drink} :\n{machine.serve(test_drink())}')

    print(f'\n\nTest [21] with drink {Coffee} (it shouldn\'t work because it\'s the 21th drink) :')
    try:
        machine.serve(Coffee())
    except CoffeeMachine.BrokenMachineException as e:
        print(f'Error: {e}')
