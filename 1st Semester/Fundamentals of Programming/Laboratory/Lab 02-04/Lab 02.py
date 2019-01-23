'''
Created on Oct 16, 2016

@author: oscar
'''
#---------------------------------------------------------------------------Domain------------------------------------------------------------------

def createApartment(apartment_nr,type,amount):
    """
    Resume: This function will create a dictionary.
    Arguments: The 3 arguments are the one that will be put into a dictionary, representing the apartment number, type and amount.
    Return: The function will return a dictionary whit 3 elements.
    """
    return{"apartment_nr":apartment_nr,"type":type,"amount":amount}

    '''   
def addApartmentInOrder(building,apartment):
    if len(building) == 0:
        building.append(apartment)
    else:
        i = 0
        while i <= len(building) and getApartmentNr(building[i]) <= getApartmentNr(apartment):
            i += i
        if i == len(building) + 1:
            building.append(apartment)
        else:
            if getApartmentNr(building[i]) == getApartmentNr(apartment) and getApartmentType(b[i]) == getApartmentType(apartment):
                print("You can't give same apartment with same type. You can change the amount if you want in modify menu.")
            else:
                building.inser(i,apartment)
    '''
    
def addApartment(building,apartment):
    """
    Resume: The function will insert into the list building the dictionary apartment.
    Arguments: Building represent the list in which we will insert a dictionary, and apartment is the dictionary which will be inserted.
    Return: The function will return the list building with dictionary apartment inserted in the end.  
    """
    building.append(apartment)

def getApartmentNr(apartment):
    """
    Resume: The function will return the value of the key apartment_nr from the apartment dictionary.
    Argument: Apartment is the dictionary from which we will return the value of apartment_nr key.
    Return: The value of apartment_nr key.
    """
    return apartment["apartment_nr"]

def getApartmentType(apartment):
    """
    Resume: The function will return the value of the key type from the apartment dictionary.
    Arguments: Apartment is the dictionary from which we will return the value of type key.
    Return: The value of type key.
    """
    return apartment["type"]

def deleteApartmentNr(building,apartment_nr):
    """
    Resume: The function will delete all the apartments with the number apartment_nr from the list building.
    Arguments: Building represent the list in which we will delete the apartments, and apartment_nr is the apartment which will be deleted.
    Return: The function will return the list with the apartments with the apartment_nr deleted.
    """
    building[:] = [s for s in building if getApartmentNr(s) != apartment_nr]
    
def deleteApartmentsFromTo(building,i,j):
    """
    Resume: The function will delete the apartments from number i to j in the list building.
    Arguments: Building is the list in which we will delete the apartments, i,j are the numbers between which we will delete apartments.
    Return: The function will return the list with the apartments between i,j deleted.
    """
    for s in range(i,j+1):
        deleteApartmentNr(building, s)
        
def deleteApartmentType(building,type):
    """
    Resume: The function will delete the apartments which have as expense type.
    Arguments: Building is the list in which we will remove elements which have at the key "type", the type value.
    Return: The function will return the list buildings without elements that have at expenses the value type.
    """
    building[:] = [s for s in building if getApartmentType(s) != type ]
    
def find_value(building, apartament_nr, value1, type, value2):
    """
    Resume: The function will return the position of the element in list building, which have at key apartment_nr the value, value1 and at key type the value, value2.
    Arguments: Building is the list in which we will search, apartament_nr and type are the key we are searching for which need to have the value value1 and value2.
    Return: -1 if such an element doesn't exist and i which is the position of the element we are looking for.
    """
    for i, dict in enumerate(building):
          if dict[apartament_nr] == value1 and dict[type] == value2:
             return i
    return -1
 
def replaceApartmentValue(building, apartmentnr, typenr, value):
    """
    Resume: The function will replace the value of the element situated in buildings with apartment_nr key = apartmentnr and type key = typenr with value.
    Arguments: Building is the list in which we will modify, apartmentnr is the apartment_nr, typenr is the type and value is the value that is supposed to replace the old value.
    Return:The function will return the list modified. 
    """
    c = find_value(building,"apartment_nr",apartmentnr,"type",typenr)
    if c == -1:
        print("There is no apartment ",apartmentnr," with this expense ",typenr)
    else:
        building[c] = {"apartment_nr":apartmentnr,"type":typenr,"amount":value}

            
#---------------------------------------------------------------User Interface-----------------------------------------------------------

def printOptions():
    """
    Resume: The function will print the principal menu. 
    """
    print("    1. Add an apartment.\n\
    2. Print all apartments\n\
    3. Modify Options \n\
    X. Exit")
    
def printModifyOptions():
    """
    Resume: The function will print the meniu for modifications.
    """
    print("    1. Remove one apartment from the program.\n\
    2. Remove all expenses from an apartment to another. \n\
    3. Remove an expenses from all apartments. \n\
    4. Replace the amount of an expense from an apartment. \n\
    X. Back to the menu.")
    
def runMenu():
    """
    Resume: The function will run the principle menu, it will read a command from keyboard and decide to which use interface function to send, or it will break 
            the and stop the program, at the same time it will announce you if you typed wrong something.
    Arguments: There is no arguments.
    Return: It will not return nothing because it will send you to another function, or it will break if you hit the X key.
    """
    options = {1:uiAddApartment,2:uiPrintAllApartments,3:runModifyMenu}
    while True:
        printOptions()
        option = input("Option: ")
        if option == "x" or option == "X":
            break
        try:
            option = int(option)
            options[option](building)
        except ValueError as ve:
            print("Invalid Input: ",ve)
        except KeyError as ke:
            print("Option is not implemented yet: ",ke)
            
def runModifyMenu(building):
    """
    Resume: The function will run another menu which is the modification menu, it will send you to other user interface functions, depends on what key you hit.
    Arguments: Building is the list which will be modified.
    Return: It will return only if you typed wrong.
    """
    modoptions={1:uiDeleteApartment,2:uiDeleteApartmentFromTo,3:uiDeleteApartmentType,4:uiReplaceValueFromType}
    while True:
        printModifyOptions()
        modoption = input("Option: ")
        if modoption == "X" or modoption == "x":
            break
        try:
            modoption = int(modoption)
            modoptions[modoption](building)
        except ValueError as ve:
            print("Invalid Input: ",ve)
        except KeyError as ke:
            print("Option is not implemented yet: ",ke)

def uiAddApartment(building):
    """
    Resume: The function will insert into the list an apartment read from the keyboard.
    Arguments: Building is the list which will be modified.
    Return: It will return the list modified.
    """
    apartment_nr = int(input("Apartment's number: "))
    type = input("Type: ")
    amount = int(input("Amount: "))
    apartment = createApartment(apartment_nr, type, amount) 
    addApartment(building, apartment)
    """
    def apartmentInOrder(building,apartment)
    """
    
def uiPrintApartment(apartment):
    """
    Resume: The function will print a dictionary with a specific from.
    Argument: Apartment is a dictionary which is going to be print.
    Return: It will return nothing.
    """
    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["apartment_nr"], apartment["type"], apartment["amount"]), end="\n")

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
    
def uiDeleteApartment(building):
    """
    Resume: The function is a user interface one, and will delete an apartment.  
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    apartment_nr = int(input("Apartment Number: "))
    deleteApartmentNr(building, apartment_nr)
    
def uiDeleteApartmentFromTo(building):
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
    except ValueError as ve:
        print("Invalid Input: ")
        
def uiDeleteApartmentType(building):
    """
    Resume: The function will delete a type from all apartments that have that type.
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    try:
        c = input("What expense should be deleted: ")
        deleteApartmentType(building, c)
    except ValueError as ve:
        print("Invalid Input: ", ve)
        
def uiReplaceValueFromType(building):
    """
    Resume: The function will modify the amount of a type in a specific apartment.
    Argument: Building is the list which will be modified.
    Return: The function will return the list modified.
    """
    try:    
        apartmentnr = int(input("At what apartment you want to change the value: "))
        typenr = input("What expense you what to change: ")
        value = int(input("And what's the replace amount: "))
        replaceApartmentValue(building, apartmentnr, typenr, value)
    except ValueError as ve:
        print("Invalid Input: ",ve)
        
#------------------------------------------------------------------SetUp---------------------------------------------------------------------------------

def startUp():
    """
    Resume: The function is setting up the list building. The purpose for that is to have items for testing the program.
    Arguments: There is no argument.
    Return: Returns a list of dictionaries.  
    """
    building = []
    building.append(createApartment(1, "gas", 100))
    building.append(createApartment(1, "water", 200))
    building.append(createApartment(1, "heating", 150))
    building.append(createApartment(1, "electricity", 300))
    building.append(createApartment(2, "gas", 98))
    building.append(createApartment(2, "water", 110))
    building.append(createApartment(3, "gas", 160))
    building.append(createApartment(4, "gas", 180))
    building.append(createApartment(5, "heating", 300))
    building.append(createApartment(6, "gas", 1000))
    building.append(createApartment(7, "water", 1400))
    building.append(createApartment(8, "gas", 800))
    building.append(createApartment(9, "heating", 60))
    building.append(createApartment(10, "gas", 300))
    building.append(createApartment(11, "water", 200))
    building.append(createApartment(12, "gas", 10))
    building.append(createApartment(13, "water", 9))  
    building.append(createApartment(14, "heating", 2))
    return building
        
#-------------------------------------------------------------------Main---------------------------------------------------------------------------------
      
if __name__ == '__main__':
    print("Hello World!")
    building = startUp()
    runMenu()
    print("Bye Bye!")
    pass