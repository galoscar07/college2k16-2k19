from controller.UndoController import FunctionCall, Operation
from controller.ClientController import ClientController

class ClientControllerWithUndo(ClientController):
    def __init__(self, undoController, rentalController, validator, repository):
        ClientController.__init__(self, validator, repository)
        self._rentalController = rentalController
        self._undoController = undoController

    def create(self, clientId, clientCNP, clientName):
        client = ClientController.create(self, clientId, clientCNP, clientName)

        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        redo = FunctionCall(self.create, clientId, clientCNP, clientName) 
        undo = FunctionCall(self.delete, clientId)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)   

        return client

    def delete(self, clientId):
        '''
            NB! Undo/redo is also needed here
        '''
        pass

    def update(self, car):
        '''
            NB! Undo/redo is also needed here
        '''
        pass