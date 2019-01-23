'''
Created on Oct 29, 2016

@author: oscar
'''
from src.Apartment_administrator.domain.operations import undoMemo, addApartmentInOrder, deleteApartmentNr, deleteApartmentsFromTo, \
    deleteApartmenttyp, replaceApartmentValue, getApartmentNr,filterApartmentByAmount, filterApartmentByTyp,sortApartmentByNumber, \
    sortApartmentByTyp,maximValueApartment,sumatyp,listGSE
    
def createApartment(number,typ,amount):
    """
    Resume: This function will create a dictionary.
    Arguments: The 3 arguments are the one that will be put into a dictionary, representing the apartment number, typ and amount.
    Return: The function will return a dictionary whit 3 elements.
    """
    return{"number":number,"typ":typ,"amount":amount}
    
def runAppList():
    """
    Resume: The function will run the principle menu, it will read a command from keyboard and decide to which use interface function to send, or it will break 
            the and stop the program, at the same time it will announce you if you typd wrong something.
    Arguments: There is no arguments.
    Return: It will not return nothing because it will send you to another function, or it will break if you hit the X key.
    """
    options = {1:uiAddApartmentList,2:runModifyMenu,3:runListMenu,4:uiSumList,5:uiMaxList,6:runSortMenu,7:runFilterMenu,9:printHelp}
    undolist = []
    building = startUp()
    undolist.append(list(building))
    while True:
        try:
            printOptions()
            option = input("Option: ")
            if option == "x" or option == "X":
                break
            elif int(option) == 8:
                building = uiUndo(undolist, building)
            else:
                try:
                    option = int(option)
                    options[option](undolist,building)
                except ValueError as ve:
                    print("Invalid Input: ",ve)
                except KeyError as ke:
                    print("Option is not implemented yet: ",ke)
        except ValueError as ve:
            print("Option not implemented yet. ")
            
def runModifyMenu(undolist,building):
    """
    Resume: The function will run another menu which is the modification menu, it will send you to other user interface functions, depends on what key you hit.
    Arguments: Building is the list which will be modified.
    Return: It will return only if you typed wrong.
    """
    modoptions={1:uiDeleteApartmentList,2:uiDeleteApartmentFromToList,3:uiDeleteApartmenttypList,4:uiReplaceValueFromtypList,5:printHelp}
    while True:
        printModifyOptions()
        modoption = input("Option: ")
        if modoption == "X" or modoption == "x":
            break
        try:
            modoption = int(modoption)
            modoptions[modoption](undolist,building)
        except ValueError as ve:
            print("Invalid Input: ",ve)
        except KeyError as ke:
            print("Option is not implemented yet: ",ke)
            
def runListMenu(undolist,building):
    """
    """
    listoptions = {1:uiListAll,2:uiListApartmentList,3:uiListGSEList,4:printHelp}
    while True:
        printListOptions()
        listoption = input("Option: ")
        if listoption == "x" or listoption == "X":
            break
        try:
            listoption = int(listoption)
            listoptions[listoption](undolist,building)
        except ValueError as ve:
            print("Invalid input: ",ve)
        except KeyError as ke:
            print("Option is not yet implemented: ",ke)
            
def runSortMenu(undolist,building):
    sortoptions = {1:uiSortApartment,2:uiSortType,3:printHelp}
    while True:
        printSortOptions()
        sortoption = input("Option: ")
        if sortoption == "x" or sortoption == "X":
            break
        try:
            sortoption = int(sortoption)
            sortoptions[sortoption](undolist,building)
        except ValueError as ve:
            print("Invalid input: ",ve)
        except KeyError as ke:
            print("Option is not yet implemented: ",ke)
            
def runFilterMenu(undolist,building):
    filteroptions = {1:uiFilterType,2:uiFilterAmount,3:printHelp}
    while True:
        printFilterOptions()
        filteroption = input("Option: ")
        if filteroption == "x" or filteroption == "X":
            break
        try:
            filteroption = int(filteroption)
            filteroptions[filteroption](undolist,building)
        except ValueError as ve:
            print("Invalid input: ",ve)
        except KeyError as ke:
            print("Option is not yet implemented: ",ke)
            
def runUndo(undolist,building):
    building = uiUndo(undolist, building)
            
def printOptions():
    """
    Resume: The function will print the principal menu. 
    """
    print("    1. Add an apartment.\n\
    2. Modify Options \n\
    3. List Options \n\
    4. Sum \n\
    5. Maximum \n\
    6. Sort Options \n\
    7. Filter Options \n\
    8. Undo \n\
    9. Help \n\
    x. Exit")
    
def printModifyOptions():
    """
    Resume: The function will print the menu for modifications.
    """
    print("    1. Remove one apartment from the program.\n\
    2. Remove all expenses from an apartment to another. \n\
    3. Remove an expenses from all apartments. \n\
    4. Replace the amount of an expense from an apartment. \n\
    5. Help \n\
    X. Back to the menu.")
    
def printListOptions():
    """
    """
    print("    1. Print all apartments from the program \n\
    2. Print an apartment expenses \n\
    3. List all apartments that have expenses greater, smaller or equal to a value \n\
    4. Help \n\
    X. Back to the menu")
    
def printSortOptions():
    print("    1. Sort Apartment \n\
    2. Sort Type \n\
    3. Help \n\
    X. Back to the menu")
    
def printFilterOptions():
    print("    1. Filter a type \n\
    2. Filter by an amount of money \n\
    3. Help \n\
    X. Back to the menu") 
    
def uiAddApartmentList(undolist,building):
    """
    Resume: The function will insert into the list an apartment read from the keyboard.
    Arguments: Building is the list which will be modified.
    Return: It will return the list modified.
    """
    apartment_nr = int(input("Apartment's number: "))
    typ = input("Type: ")
    amount = int(input("Amount: "))
    apartment = createApartment(apartment_nr, typ, amount) 
    addApartmentInOrder(building, apartment)
    undoMemo(undolist, building)
    
def uiPrintApartment(apartment):
    """
    Resume: The function will print a dictionary with a specific from.
    Argument: Apartment is a dictionary which is going to be print.
    Return: It will return nothing.
    """
    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")  
      
def uiPrintAllApartments(building):
    """
    Resume: The function is going to print the list building with the specific form of the previous function, if the list is empty, the program is going
            to print a message.
    Argument: Building is the list which is going to be printed.
    Return: The function will return a message if the list is empty.
    """
    if len(building) == 0:
        print("The list is empty.")
    for s in building:
        uiPrintApartment(s)
    print()
    
def uiDeleteApartmentList(undolist,building):
    """
    Resume: The function is a user interface one, and will delete an apartment.  
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    apartment_nr = int(input("Apartment Number: "))
    deleteApartmentNr(building, apartment_nr)
    undoMemo(undolist, building)
    
def uiDeleteApartmentFromToList(undolist,building):
    """
    Resume: The function will delete apartments from a specific number to another.
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    try:
        print("Delete apartment")
        i = int(input("From: "))
        j = int(input("To: "))
        deleteApartmentsFromTo(building, i, j)
        undoMemo(undolist, building)
    except ValueError as ve:
        print("Invalid Input: ",ve)
        
def uiDeleteApartmenttypList(undolist,building):
    """
    Resume: The function will delete a typ from all apartments that have that typ.
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    try:
        c = input("What expense should be deleted: ")
        deleteApartmenttyp(building, c)
        undoMemo(undolist, building)
    except ValueError as ve:
        print("Invalid Input: ", ve)
        
def uiReplaceValueFromtypList(undolist,building):
    """
    Resume: The function will modify the amount of a typ in a specific apartment.
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    try:    
        apartmentnr = int(input("At what apartment you want to change the value: "))
        typnr = input("What expense you what to change: ")
        value = int(input("And what's the replace amount: "))
        replaceApartmentValue(building, apartmentnr, typnr, value)
        undoMemo(undolist, building)
    except ValueError as ve:
        print("Invalid Input: ",ve)
        
def uiListAll(undolist,building):
    """
    Resume: The function is going to print the list building with the specific form of the previous function, if the list is empty, the program is going
            to print a message.
    Argument: Building is the list which is going to be printed.
    Return: The function will return a message if the list is empty.
    """
    if len(building) == 0:
        print("The list is empty.")
    else:
        for apartment in building:    
            uiPrintApartment(apartment)
            
def uiListApartmentList(undolist,building):
    try:
        c = input("What apartment should be printed: ")
        c = int(c)
        for apartment in building:
            if getApartmentNr(apartment) == c:
                uiPrintApartment(apartment) 
    except:
        ("Invalid Input")

def uiListGSEList(undolist,building):
    params = []
    sign = input("You want to list apartment with value >,<,=: ")
    value = input("And the value: ")
    params.append(sign)
    params.append(value)
    listGSE(building, params)
        
def uiSumList(undolist,building):
    try:
        typ = input("At what type of expense I should make the sum: ")
        suma,c = sumatyp(building, typ)
        if c == 0 :
            print("There is no apartment with the type: ",typ," in the apartments list.")
        else:
            print("The sum of the apartments with type: ",typ," is ",suma)
    except ValueError as ve:
        print("Invalid input: ",ve)

def uiMaxList(undolist,building):
    try:
        number = int(input("At what apartment I should print the maximum expenses: "))
        maximValueApartment(building, number)
    except ValueError as ve:
        print("Invalid Input: ",ve)
    except IndexError as ie:
        print("Invalid Input: ",ie)
        
def uiSortApartment(undolist,building):
    listsort = sortApartmentByNumber(building)
    if len(listsort) == 0:
        print("The list is empty.")
    else:   
        for apartment in listsort:    
            print("( Apartment Number = {0}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")

def uiSortType(undolist,building):
    listsort = sortApartmentByTyp(building)
    if len(listsort) == 0:
        print("The list is empty.")
    else:   
        for apartment in listsort:    
            print("( Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")

def uiFilterType(undolist,building):
    try:
        typ = input("What type you want to filter: ")
        building = filterApartmentByTyp(undolist,building, typ)
    except IndexError as ie:
        print("Invalid input, ",ie)

def uiFilterAmount(undolist,building):
    try:
        amount = int(input("What amount you want to filter: "))
        building = filterApartmentByAmount(undolist,building, amount)
    except IndexError as ie:
        print("Invalid input, ",ie)
    
def uiUndo(undolist, building):
    try:
        c = startUp()
        undolist[0] = c 
        undolist.pop()
        building = undolist[len(undolist)-1]
        return building
    except IndexError as ie:
        print("You don't have anything to undo, ",ie)
        building = startUp()
        return building
        
def printHelp(undolist,building):
    """
    Resume: The function will print all commands that can be given to the program
    """
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
    print("\t 11. sort <apartment> ")
    print("\t 12. sort <type>")
    print("\t 13. filter <type>")
    print("\t 14. filter <amount>")
    print("\t 15. undo")
    print("\t 16. help")
    print("\t 17. exit")
    print("")
    print("")

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