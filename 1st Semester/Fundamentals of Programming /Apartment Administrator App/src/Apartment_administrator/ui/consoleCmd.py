'''
Created on Oct 27, 2016

@author: oscar
'''
from src.Apartment_administrator.domain.operations import undoMemo, addApartmentInOrder, deleteApartmentNr, deleteApartmentsFromTo, \
    deleteApartmenttyp, replaceApartmentValue, getApartmentNr,filterApartmentByAmount, filterApartmentByTyp,sortApartmentByNumber, \
    sortApartmentByTyp,maximValueApartment,sumatyp,listGSE
from src.Apartment_administrator.ui.consoleList import runAppList

def createApartment(number,typ,amount):
    """
    Resume: This function will create a dictionary.
    Arguments: The 3 arguments are the one that will be put into a dictionary, representing the apartment number, typ and amount.
    Return: The function will return a dictionary whit 3 elements.
    """
    return{"number":number,"typ":typ,"amount":amount}
        
def runApp():
    print("The program can run in menu mode, or in command mode, so in what you want to work? \n\
    menu - if you want the menu mode \n\
    cmd - if you want the program to work in command mode")
    start = 0
    while start == 0:
        c = input("Menu or cmd: ")
        if c == "cmd":
            runAppCMD()
            start = 1
        elif c =="menu":
            runAppList()
            start = 1
        else:
            print("Invalid input; you can only writhe menu or cmd.")

def readCommand():
    """
    Resume: Read and parse user commands
    Arguments: There is no arguments.
    Return: (command, params) tuple, where, command is user command and params are parameters
    """
    cmd = input("Command: ")
    cmd = cmd.split(" ")
    command = cmd[0]
    params = cmd[1:]
    return (command, params)

def runAppCMD():
    """
    Resume: The function will run the principle menu, it will read a command from keyboard and decide to which use interface 
            function to send, or it will break the and stop the program, at the same time it will announce you if you type 
            wrong something.
    Arguments: There is no arguments.
    Return: It will not return nothing because it will send you to another functions, or it will break if you hit the X key.
    """
    undolist = []
    building = startUp()
    undolist.append(list(building))
    while True:
        (command,params) = readCommand()
        if command == "add":
            uiAddApartment(undolist,building,params)
        elif command == "remove":
            uiRemoveApartment(undolist,building,params)
        elif command == "replace":
            uiReplaceApartment(undolist,building,params)
        elif command == "list" and params == []:
            building = uiListAll(building)
        elif command == "list" and params != []:
            uiListMenu(building,params)
        elif command == "sum":
            uiSumaType(building, params)
        elif command == "max":
            uiMaxim(building, params)
        elif command == "filter":
            uiFilter(undolist, building,params)
        elif command == "sort":
            uiSort(building,params)
        elif command == "undo":
            building = uiUndo(undolist,building,params)
        elif command == "help":
            uiPrintHelp(params)
        elif command == "exit":
            break
        else:
            print(" † option not implemented yet.")
    
def uiPrintHelp(params):
    """
    Resume: The function will print all commands that can be given to the program
    """
    if len(params) != 0:
        print("Invalid Input: you don't have to write any parameter after help.")
    else: 
        print("Valid commands: ")
        print("\t 1. add <apartment> <type> <amount>") 
        print("\t 2. remove <apartment>") 
        print("\t 3. remove <type>")
        print("\t 4. remove <start apartment> to <end apartment>") 
        print("\t 5. replace <apartment> <type> with <amount>") 
        print("\t 6. list")
        print("\t 7. list <apartment>")
        print("\t 8. list [ < | = | > ] <amount>")
        print("\t 9. sum <type>")
        print("\t 10. max <apartment> ")
        print("\t 11. sort apartment ")
        print("\t 12. sort type")
        print("\t 13. filter <type>")
        print("\t 14. filter <amount>")
        print("\t 15. undo")
        print("\t 16. help")
        print("\t 17. exit")

def uiAddApartment(undolist,building,params):
    if len(params) < 3:
        print("Invalid input. Apartment was not added")
        return
    try:
        number = int(params[0])
        typ = params[1]
        amount = int(params[2])
        apartment = createApartment(number, typ, amount) 
        addApartmentInOrder(building, apartment)
        undoMemo(undolist,building)
    except ValueError as ve:
        print("Invalid input: ",ve)
    
def uiRemoveApartment(undolist,building,params):
    try:
        if len(params) >= 2:
            start = int(params[0])
            end = int(params[2])
            if params[1] == "to":
                deleteApartmentsFromTo(building, start, end)
                undoMemo(undolist,building)
            else:
                print("Invalid input, between the values you have to write to")
        else: 
            int(params[0])
            number = int(params[0])
            deleteApartmentNr(building, number)
            undoMemo(undolist,building)
    except ValueError:
        deleteApartmenttyp(building, params[0])
        undoMemo(undolist,building)

def uiReplaceApartment(undolist,building,params):
    try:
        apartmentnr = int(params[0])
        typnr = params[1]
        value = int(params[3])
        if params[2] == "with":
            replaceApartmentValue(building, apartmentnr, typnr, value)
            undoMemo(undolist,building)
        else:
            print("Invalid input, you have to write with not anything else.")
    except KeyError as ke:
        print("Option not yet implemented: ",ke)
    except IndexError as ie:
        print("Invalid input, you need to have at least 3 parameters at the command: ",ie)
    except ValueError as ve:
        print("Invalid input: ",ve)
        
def uiPrintApartment(apartment):
    """
    Resume: The function will print a dictionary with a specific from.
    Argument: Apartment is a dictionary which is going to be print.
    Return: It will return nothing.
    """
    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
        
def uiListAll(building):
    """
    Resume: The function is going to print the list building with the specific form of the previous function, if the list is empty, the program is going
            to print a message.
    Argument: Building is the list which is going to be printed.
    Return: The function will return a message if the list is empty.
    """
    try:
        if len(building) == 0:
            print("The list is empty.")
        else:
            for apartment in building:    
                uiPrintApartment(apartment)
        return building
    except TypeError:
        building = startUp()
        uiListAll(building)
        return building
            
def uiListMenu(building,params):
    try:
        if len(params) == 1:
            for apartment in building:
                if getApartmentNr(apartment) == int(params[0]):
                    uiPrintApartment(apartment)
        elif len(params) == 2:
            listGSE(building, params)
    except ValueError as ve:
        print("Invalid Input: ",ve)
    except KeyError as ke:
        print("Invalid Input: ",ke)
            
def uiSumaType(building,params):
    """
    Resume: The function will return the sum of the elements that have at key typ a value read from keyboard 
    Argument: building is the list in which we search for elements that have as key typ the value read from the keyboard
              which is saved in params list
    Return: The list building modified
    """
    try:
        typ = params[0]
        suma,c = sumatyp(building, typ)
        if c == 0 :
            print("There is no apartment with the type: ",typ," in the apartments list.")
        else:
            print("The sum of the apartments with type: ",typ," is ",suma)
    except ValueError as ve:
        print("Invalid input: ",ve)

def uiMaxim(building,params):
    try:
        number = int(params[0])
        maximValueApartment(building, number)
    except ValueError as ve:
        print("Invalid Input: ",ve)
    except IndexError as ie:
        print("Invalid Input: ",ie)
        
def uiSort(building, params):
    if params[0] == "apartment":
        listsort = sortApartmentByNumber(building)
        if len(listsort) == 0:
            print("The list is empty.")
        else:   
            for apartment in listsort:    
                print("( Apartment Number = {0}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
    elif params[0] == "type":
        listsort = sortApartmentByTyp(building)
        if len(listsort) == 0:
            print("The list is empty.")
        else:   
            for apartment in listsort:    
                print("( Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
    else:
        print("Invalid input, no sort was done.")
          
def uiFilter(undolist,building,params):
    try:
        number = int(params[0])
        building = filterApartmentByAmount(undolist,building, number)
    except ValueError:
        building = filterApartmentByTyp(undolist,building, params[0])
    except IndexError as ie:
        print("Invalid Input: ",ie)

def uiUndo(undolist, building, params):
    try:
        if len(params) != 0:
            print("Invalid input, you don't need to introduce any parameter after undo")
        else:
            c = startUp()
            undolist[0] = c 
            undolist.pop()
            building = undolist[len(undolist)-1]
            return building
    except IndexError as ie:
        print("You don't have anything to undo, ",ie)
        building = startUp()
        return building
        
def startUp():
    """
    Resume: The function is setting up the list building. The purpose for that is to have items for testing the program.
    Arguments: There is no argument.
    Return: Returns a list of dictionaries.  
    """
    building = []
    building.append(createApartment(1, "gas", 100))
    building.append(createApartment(1, "gas", 200))
    building.append(createApartment(1, "gas", 150))
    building.append(createApartment(1, "electricity", 300))
    building.append(createApartment(1, "electricity", 98))
    building.append(createApartment(1, "electricity", 110))
    building.append(createApartment(1, "electricity", 160))
    building.append(createApartment(1, "water", 180))
    building.append(createApartment(1, "water", 300))
    building.append(createApartment(1, "water", 1000))
    building.append(createApartment(1, "water", 1400))
    building.append(createApartment(8, "gas", 800))
    building.append(createApartment(9, "heating", 60))
    building.append(createApartment(10, "gas", 300))
    building.append(createApartment(11, "water", 200))
    building.append(createApartment(12, "gas", 10))
    building.append(createApartment(13, "water", 9))  
    building.append(createApartment(14, "heating", 2))
    return building


            