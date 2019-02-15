from collections import namedtuple

# structure where we will store the tokens
from consts import STOP_CONDITION
from production import ProductionSet

Token = namedtuple('Token', ('name', 'value'))
# structure for representing the nodes
Node = namedtuple('Node', ('name', 'items'))


# class that will act like a stack
class Stack(object):
    def __init__(self):
        self.items = []

    def __str__(self):
        string = ""
        for item in self.items:
            if item == STOP_CONDITION:
                continue
            string += str(item) + '->'
        return string[:-2]

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_input_completed(stack):
    for element in stack.items:
        if type(element) is not ProductionSet:
            return False
        if not element.get_current().is_production_checked():
            return False
    return True
