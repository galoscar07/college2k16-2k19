from src.store.domain.redo import RedoOperation
from src.store.domain.undo import UndoOperation
from src.store.domain.validators import UndoExcept, RedoExcept


class UndoController(object):
    """
    The class is for the undo and redo function
    """
    def __init__(self):
        """
        The function is for initializing variables
        """
        self.__operations = []
        self.__redoController = []

    @property
    def operations(self):
        """
        The funtion is a property, it's return the value of the list operations
        """
        return self.__operations

    def registerOperation(self, sourceMethod, handler, *args):
        """
        The function will save the operation made for undo
        :param sourceMethod: is the operation that was applied
        :param handler: is the operation that needs to be done to do the undo
        :param args: are the parameters for handler
        """
        self.__operations.append(UndoOperation(sourceMethod, handler, *args))

    def undo(self):
        """
        The function will do the undo by doing the oposite thing that has been done on the dictionary
        """
        if len(self.__operations) == 0:
            raise UndoExcept("Nothing to undo")
        undoOperation = self.__operations.pop()
        self.registerOperationRedo(undoOperation.handler, undoOperation.sourceMethod, undoOperation.args)
        undoOperation.handler(*undoOperation.args)


    def registerOperationRedo(self,sourceMethod, handler, *args):
        """
        The function does the same thing as the one above, the difference is that this one is for redo
        """
        self.__redoController.append(RedoOperation(sourceMethod, handler, *args))


    def redo(self):
        """
        This function is the same as the one above, only this one is for redo
        """
        if len(self.__redoController) == 0:
            raise RedoExcept("Nothing to redo")
        redoOperation = self.__redoController.pop()
        redoOperation.handler(*redoOperation.args)