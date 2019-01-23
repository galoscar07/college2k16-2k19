from controller.UndoController import FunctionCall, Operation
from controller.RentalController import RentalController

class RentalControllerWithUndo(RentalController):
    """
    Controller for rental operations
    """
    def __init__(self, undoController, validator, rentalRepo, carRepo, clientRepo):
        RentalController.__init__(self, validator, rentalRepo, carRepo, clientRepo)
        self._validator = validator
        self._repository = rentalRepo

        self._undoController = undoController 

    def createRental(self, rentalId, client, car, start, end):
        '''
            NB! Undo/redo is also needed here
        '''
        pass 

    def deleteRental(self, rentalId):
        '''
            NB! Undo/redo is also needed here
        '''
        pass




