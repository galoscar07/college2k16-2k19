class UndoOperation(object):
    """
    This class will define the redo object, which atributes will remember the the function which was done, the function
    that needs to be done in order to redo an action and the arguments for the handler
    """
    def __init__(self, sourceMethod, handler, *args):
        self.__sourceMethod = sourceMethod
        self.__handler = handler
        self.__args = args

    @property
    def sourceMethod(self):
        return self.__sourceMethod

    @property
    def handler(self):
        return self.__handler

    @property
    def args(self):
        return self.__args
