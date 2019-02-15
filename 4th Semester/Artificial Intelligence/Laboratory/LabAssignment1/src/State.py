from copy import deepcopy


class State:
    '''
    holds a PATH of configurations
    '''

    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = deepcopy(values)

    def getValues(self):
        return self.__values

    def __str__(self):
        s = ''
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def __add__(self, something):
        aux = State()
        if isinstance(something, State):
            aux.setValues(self.__values + something.getValues())
        elif isinstance(something,list):
            aux.setValues(self.__values + [something])
        else:
            aux.setValues(self.__values)
        return aux

