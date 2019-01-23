from controller.CarControllerWithUndo import CarControllerWithUndo
from controller.ClientControllerWithUndo import ClientControllerWithUndo
from controller.RentalControllerWithUndo import RentalControllerWithUndo
from controller.UndoController import UndoController
from domain.Car import CarValidator
from domain.Client import ClientValidator
from domain.Rental import RentalValidator
from repository.Repository import Repository
from datetime import date

def printReposWithMessage(msg, clientRepo, carRepo, rentRepo):
    print("-"*15 + msg + "-"*15)
    print("Clients:\n" + str(clientRepo))
    print("Cars:\n" + str(carRepo))
    print("Rentals:\n" + str(rentRepo))  

def undoExample():
    """
    An example for doing multiple undo operations. 
    This is a bit more difficult than in Lab2-4 due to the fact that there are now several controllers, 
    and each of them can perform operations that require undo support.
     
    Follow the code below and figure out how it works!
    """
   
    undoController = UndoController()
    clientRepo = Repository()
    carRepo = Repository()

    '''
    Start rental Controller
    '''
    rentRepo = Repository()
    rentValidator = RentalValidator()
    rentController = RentalControllerWithUndo(undoController, rentValidator, rentRepo, carRepo, clientRepo)
    
    '''
    Start client Controller
    '''
    clientValidator = ClientValidator()
    clientController = ClientControllerWithUndo(undoController, rentController, clientValidator, clientRepo)
    
    '''
    Start car Controller
    '''
    carValidator = CarValidator()
    carController = CarControllerWithUndo(undoController, rentController, carValidator, carRepo)

    '''
    We add 1 client, 1 car and 2 rentals
    '''
    undoController.newOperation()
    clientSophia = clientController.create(103, "2990511035588", "Sophia")

    undoController.newOperation()
    carHyundaiTucson = carController.create(201, "CJ 02 TWD", "Hyundai", "Tucson")

    undoController.newOperation()
    rentController.createRental(301, clientSophia, carHyundaiTucson, date(2016, 11, 1), date(2016, 11, 30))
    
    undoController.newOperation()
    rentController.createRental(302, clientSophia, carHyundaiTucson, date(2016, 12, 1), date(2016, 12, 31))
    
    printReposWithMessage(" We added 1 client, 1 car and 2 rentals", clientRepo, carRepo, rentRepo)
    
    print(" We delete the car, it should also delete its rentals")
    undoController.newOperation()
    carController.delete(201)

    '''
    At this point we've performed 5 operations that can we can undo/redo
    '''
    printReposWithMessage("", clientRepo, carRepo, rentRepo)
  
    
    '''
    Now undo the performed operations, one by one
    '''
    undoController.undo()
    printReposWithMessage(" First undo should get the car and rentals back ", clientRepo, carRepo, rentRepo)

    undoController.undo()
    printReposWithMessage(" Second undo should delete the second rental ", clientRepo, carRepo, rentRepo)
     
    undoController.undo()
    printReposWithMessage(" Third undo should delete the first rental ", clientRepo, carRepo, rentRepo)
 
    undoController.undo()
    printReposWithMessage(" Fourth undo deletes the car ", clientRepo, carRepo, rentRepo)

    '''
    After 5 undos, all repos should be empty, as we did 5 operations in total
    '''
    undoController.undo()
    printReposWithMessage(" Fifth undo - so long, Sophia! ", clientRepo, carRepo, rentRepo)

    '''
    Redos start here
    '''
    undoController.redo()
    printReposWithMessage(" First redo gets Sophia back! Is she the same however? ", clientRepo, carRepo, rentRepo)

    undoController.redo()
    printReposWithMessage(" Second redo, we get our Hyundai back ", clientRepo, carRepo, rentRepo)

    undoController.redo()
    printReposWithMessage(" Third redo, the first rental ", clientRepo, carRepo, rentRepo)

    undoController.redo()
    printReposWithMessage(" Fourth redo, the second rental ", clientRepo, carRepo, rentRepo)

    undoController.redo()
    printReposWithMessage(" Fifth redo, the car and rentals are (again) deleted ", clientRepo, carRepo, rentRepo)

    '''
    Let's do a few undos again...
    '''
    undoController.undo()
    undoController.undo()
    undoController.undo()

    printReposWithMessage(" After 3 undos, we have the client and car ", clientRepo, carRepo, rentRepo)

    '''
    Now we try something new - let's add another car!
    
    NB!
        A new operation must invalidate the history for redo() operations
    '''
    undoController.newOperation()
    carController.create(202, "CJ 02 SSE", "Dacia", "Sandero")

    print("\n Do we have a redo? -", undoController.redo(), "\n")
    
    '''
    Now we should have 2 cars
    '''
    printReposWithMessage(" After a new operation, there is no redo ", clientRepo, carRepo, rentRepo)
    
    '''
    However, undos is still available !
    '''
    undoController.undo()
    printReposWithMessage(" Undo deletes the newly added car ", clientRepo, carRepo, rentRepo)
    
    undoController.undo()
    printReposWithMessage(" The first car is gone too :) ", clientRepo, carRepo, rentRepo)

undoExample()
