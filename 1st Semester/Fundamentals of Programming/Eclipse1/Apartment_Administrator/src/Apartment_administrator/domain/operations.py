'''
Created on Oct 27, 2016

@author: oscar
'''
def addApartmentInOrder(building,apartment):
    """
    Resume: This function will insert in the list with dictionary, the dictionary apartment in it's right place. If in the list is no apartment then the dictionary 
            will be pun on the first element of the list, otherwise the function will search for it's place, if there are 2 apartments dictionary with the same 
            specification a message will be displayed.
    Arguments: The function have 2 arguments, building which is the list where we will insert a dictionary, and apartment which is the dictionary
    Return: The function will return the list modified
    """
    if len(building) == 0:
        building.append(apartment)    
    else:
        i = 0
        while i < len(building) and building[i]["number"] <= apartment["number"]:
            i += 1
        if i == len(building):
            building.append(apartment)
        else:
            building.insert(i,apartment)
            
def addSortInOrderByAmount(building,apsort):
    """
    Resume: The function will add in an ascending order into a list, a dictionary with three elements. The order will be given by
            the key "amount" at the same time into the list there will no be 2 elements with the same apartment number.
    Arguments: The function get as arguments a list into which it will insert a dictionary, also given.
    Return: The function will return the function modified.
    """
    if len(building) == 0:
        building.append(apsort)    
    else:
        i = 0
        while i < len(building) and building[i]["amount"] <= apsort["amount"]:
            i += 1
        if i == len(building) and building[i-1]["number"] != apsort["number"]:
            building.append(apsort)
        else:
            if building[i-1]["number"] != apsort["number"]:
                building.insert(i,apsort)
                
def addSortInOrderBytyp(building,apsort):
    """
    Resume: The function will add in an ascending order into a list, a dictionary with three elements. The order will be given by
            the key "amount" at the same time into the list there will no be 2 elements with the typ of expense.
    Arguments: The function get as arguments a list into which it will insert a dictionary, also given.
    Return: The function will return the function modified.
    """
    if len(building) == 0:
        building.append(apsort)    
    else:
        i = 0
        while i < len(building) and building[i]["amount"] <= apsort["amount"]:
            i += 1
        if i == len(building) and building[i-1]["typ"] != apsort["typ"]:
            building.append(apsort)
        else:
            if building[i-1]["typ"] != apsort["typ"]:
                building.insert(i,apsort)

def getApartmentNr(apartment):
    """
    Resume: The function will return the value of the key number from the apartment dictionary.
    Argument: Apartment is the dictionary from which we will return the value of number key.
    Return: The value of number key.
    """
    return apartment["number"]

def getApartmenttyp(apartment):
    """
    Resume: The function will return the value of the key typ from the apartment dictionary.
    Arguments: Apartment is the dictionary from which we will return the value of typ key.
    Return: The value of typ key.
    """
    return apartment["typ"]

def getApartmentAmount(apartment):
    """
    Resume: The function will return the value of the key amount from the apartment dictionary.
    Arguments: Apartment is the dictionary from which we will return the value of amount key.
    Return: The value of amount key.
    """
    return apartment["amount"]

def isValueThere(building, number, typ):
    """
    Resume: The function will return the position of the element in list building, which have at key number the value, value1 and at key typ the value, value2.
    Arguments: Building is the list in which we will search, number and typ are the key we are searching for which need to have the value value1 and value2.
    Return: False if such an element doesn't exist and i which is the position of the element we are looking for.
    """
    for dictio in building:
        if dictio["number"] == number  and dictio["typ"] == typ:
            return True
    return False

def deleteApartmentNr(building,number):
    """
    Resume: The function will delete all the apartments with the number number from the list building.
    Arguments: Building represent the list in which we will delete the apartments, and number is the apartment which will be deleted.
    Return: The function will return the list with the apartments with the number deleted.
    """
    building[:] = [s for s in building if getApartmentNr(s) != number]
    
def deleteApartmentsFromTo(building,start,end):
    """
    Resume: The function will delete the apartments from number i to j in the list building.
    Arguments: Building is the list in which we will delete the apartments, i,j are the numbers between which we will delete apartments.
    Return: The function will return the list with the apartments between i,j deleted.
    """
    for s in range(start,end+1):
        deleteApartmentNr(building, s)

def deleteApartmenttyp(building,typ):
    """
    Resume: The function will delete the apartments which have as expense typ.
    Arguments: Building is the list in which we will remove elements which have at the key "typ", the typ value.
    Return: The function will return the list buildings without elements that have at expenses the value typ.
    """
    building[:] = [s for s in building if getApartmenttyp(s) != typ ]

def replaceApartmentValue(building, apartmentnr, typnr, value):
    """
    Resume: The function will replace the value of the element situated in buildings with number key = apartmentnr and type key = typnr with value.
    Arguments: Building is the list in which we will modify, apartmentnr is the number, typnr is the type and value is the value that is supposed to replace the old value.
    Return:The function will return the list modified. 
    """
    try:
        for i in range(0,len(building)+1):
            if getApartmentNr(building[i]) == apartmentnr and getApartmenttyp(building[i]) == typnr:
                building[i] = {"number":apartmentnr,"typ":typnr,"amount":value}
                break
    except IndexError:
        print("There is no apartment ",apartmentnr," with expense ",typnr)

def listGSE(building,params):
    """
    Resume: The function will print elements of the list building with which are [>,<.=] with a value read from the keyboard.
    Arguments: The arguments function are the list in which we will search the elements with the condition that we want, params
               is a list with 2 elements which are a condition [>,<.=], and a value, read from the keyboard.
    Return: It will return nothing, it will only print the apartments with the condition given.
    """
    try:
        c = int(params[1])
        d = 0
        if params[0] == "=":
            for apartment in building:
                if getApartmentAmount(apartment) == c:
                    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
                    d = 1 
        elif params[0] == ">":
            for apartment in building:
                if getApartmentAmount(apartment) > c:
                    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
                    d = 1
        elif params[0] == "<":
            for apartment in building:
                if getApartmentAmount(apartment) < c:
                    print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(apartment["number"], apartment["typ"], apartment["amount"]), end="\n")
                    d = 1
        else:
            print("Invalid Input")
        if d == 0:
            print("There is no such an element to be listed. ")
    except ValueError as ve:
        print("Invalid input: ", ve)

def sumatyp(building,typ):
    """
    Resume: The function will return the suma of a typ given by the parameter "typ",which will be return by the variable s. We
            will search the elements with the condition in the list building. C is a variable that will return 1 if there is made a
            suma or 0 otherwise.
    Arguments: Building is the list in which we will search elements, and typ is a value that the elements of the list must have.
    Return: The function will return the pair (s,c), in which s is the suma of the elements from the list with the condition that at
            the key "typ" to have the value typ; and c is a value that will return 0 if there is no suma made or 1 otherwise.
    """
    s = 0
    c = 0
    for apartment in building:
        if getApartmenttyp(apartment) == typ:
            s = s + getApartmentAmount(apartment)
            c = 1
    return (s,c)

def findmaximAmount(building, number, typ):
    """
    Resume: The function will return the maximimum element of a list, that have as key "number", "typ" the value number respectively
            typ.
    Arguments: The function will get as arguments, the list in which we will search, and 2 values.
    Return: The function will return a dictionary that have at the key "typ" the value of the variable typ and at the key "number"
            the value of the variable number and have the maximimum amount of all the dictionary in the list with that condition.
    """
    maxim = 0
    for apartment in building:
        if getApartmentNr(apartment) == number and getApartmenttyp(apartment) == typ:
            if getApartmentAmount(apartment) > maxim:
                maxim = getApartmentAmount(apartment)
    return {"number":number,"typ":typ,"amount":maxim}

def listOfApartmentExpenses(number,building):
    """
    Resume: The function will return a list of expenses for an apartment number which is in the list building.
    Argument: As arguments we have the list in which we will search (building), and the apartment number for the apartment that
              we are going to extract the list of expenses.
    Return: The function will return the list of an apartment kinds of expenses.
    """
    exp = []
    for apartment in building:
        if getApartmentNr(apartment) == number:
            if not( getApartmenttyp(apartment) in exp):
                exp.append(getApartmenttyp(apartment))
    return exp
                
def maximValueApartment(building,number):
    """
    Resume: The function will print the max amount per each expense for the apartment number.
    Argument: The arguments are the list in which we will search(building), and the apartment for which we are suppose to write 
              the max amount for each expense (number).
    Return: The function doesn't return anything.
    """
    exp = listOfApartmentExpenses(number, building)
    if exp == []:
        print("there is no such apartment like your request")
    else:
        for i in exp:
            c = findmaximAmount(building, number, i)
            if c != 0:
                print("( Apartment Number = {0}, Type = {1}, Amount = {2} )".format(c["number"], c["typ"], c["amount"]), end="\n")
                
def filterApartmentByAmount(undolist,building, number):
    """
    Resume: The function will remove all the apartments from the list that have the amount key smaller than number.
    Argument: Building is the list in which we will search, and number is an integer that is a condition for solving the problem.
    Return: The function will return through building the list building modified.
    """
    building[:] = [s for s in building if getApartmentAmount(s) < number]
    undoMemo(undolist, building)

def filterApartmentByTyp(undolist,building, typ):
    """
    Resume: The function will remove all the apartments from the list that have the type key different than typ.
    Argument: Building is the list in which we will search, and typ is a string that is a condition for solving the problem.
    Return: The function will return through building the list building modified.
    """
    building[:] = [s for s in building if getApartmenttyp(s) == typ]
    undoMemo(undolist, building)

def totalAmountPerApartment(building,number):
    """
    Resume: The function will compute the addition of the values of all expenses for apartment number .
    Argument: Building is a list in which we will search, and number is the apartment number, being an integer.
    Return: The function will return the sum of all apartment that have at key number the value number through the variable s.
    """
    s = 0
    for apartment in building:
        if getApartmentNr(apartment) == number:
            s = s + getApartmentAmount(apartment)
        elif getApartmentNr(apartment) > number:
            break
    return s

def alltypSort(building):
    """
    Resume: The function will return a list of all types from the list taken from all the apartments.
    Argument: Building is a list in which we will search types.
    Return: The function will return a list of strings with all types from the list in it.
    """
    exp = []
    for apartment in building:
        exp1 = listOfApartmentExpenses(getApartmentNr(apartment), building)
        for i in exp1:
            if not(i in exp):
                exp.append(i)
    return exp

def totalAmountPerApartmenttyp(building,typ):
    """
    Resume: The function will compute the addition of all expenses for a type.
    Argument: Buildings is the list in which we will search and typ is the type for whose we will make an addition.
    Return: The function returns the the sum of expenses for the type typ.
    """
    s = 0
    for apartment in building:
        if getApartmenttyp(apartment) == typ:
            s = s + getApartmentAmount(apartment)
    return s  
  
def sortApartmentByNumber(building):
    """
    Resume: The function compute the sum of all apartment, order by apartment number.
    Argument: Building is the list in which we will search.
    Return: The function will return a list of dictionaries.
    """
    sortlist = []
    for apartment in building:
        s = totalAmountPerApartment(building, getApartmentNr(apartment))
        addSortInOrderByAmount(sortlist, {"number":getApartmentNr(apartment),"typ":"none","amount":s})
    return sortlist

def sortApartmentByTyp(building):
    """
    Resume: The function compute the sum of all apartment, order by apartment's type.
    Argument: Building is the list in which we will search.
    Return: The function will return a list of dictionaries.
    """
    sortlist = []
    exp = alltypSort(building)
    for i in exp:
        s = totalAmountPerApartmenttyp(building, i)
        addSortInOrderBytyp(sortlist, {"number":0,"typ":i,"amount":s})
    return sortlist

def undoMemo(undolist,building):
    """
    Resume: The function will memorize in undolist all modification of building by saving the list at every step.
    Argument: Undolist is the list of lists of dictionaries, and building is a list of dictionaries.
    Return: The function is going to return the list undolist modified by adding at it's end the list building.
    """
    undolist.append(list(building))
