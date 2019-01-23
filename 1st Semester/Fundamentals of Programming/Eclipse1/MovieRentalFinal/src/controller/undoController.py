from src.domain.validators import UndoException, RedoException


class UndoController:
    def __init__(self):
        self.__operations = []
        self.__index = -1
        self.__recorded = True

    def recordOperation(self, operation):
        if self.isRecorded() == True:
            self.__operations[-1].append(operation)

    def newOperation(self):
        if self.isRecorded() == False:
            return

        self.__operations = self.__operations[0:self.__index + 1]
        self.__operations.append([])
        self.__index += 1


    def isRecorded(self):
        return self.__recorded


    def undo(self):
        if self.__index < 0:
            raise UndoException("Nothing to undo")

        self.__recorded = False

        for oper in self.__operations[self.__index]:
            oper.undo()

        self.__recorded = True

        self.__index -= 1
        return True

    def redo(self):
        if self.__index >= len(self.__operations) - 1:
            raise RedoException("Nothing to redo")

        self.__recorded = False

        for oper in self.__operations[self.__index]:
            oper.redo()

        self.__recorded = True

        self.__index += 1
        return True



class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)


class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()
