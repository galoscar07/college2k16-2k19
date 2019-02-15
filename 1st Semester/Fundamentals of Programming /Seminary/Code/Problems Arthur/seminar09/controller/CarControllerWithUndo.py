from controller.UndoController import FunctionCall, Operation
from controller.CarController import CarController

class CarControllerWithUndo(CarController):
    def __init__(self, undoController, rentalController, validator, repository):
        CarController.__init__(self, validator, repository)
        self._rentalController = rentalController
        self._undoController = undoController
        
    def create(self, carId, licensePlate, carMake, carModel):
        car = CarController.create(self, carId, licensePlate, carMake, carModel)
        
        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        redo = FunctionCall(self.create, carId, licensePlate, carMake, carModel) 
        undo = FunctionCall(self.delete, carId)
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)   

        return car
        
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