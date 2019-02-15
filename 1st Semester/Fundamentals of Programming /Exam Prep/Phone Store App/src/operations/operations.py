'''
Created on Nov 14, 2016

@author: oscar
'''
def createEntity(manufacturer,model,value):
    """
    Resume: The aplication will return a dictionary with the three elements given to the function
    Input: The function recive 3 values which will be put into a dictionary
    Output: The function returns a dictionary. 
    """
    return {"manufacturer":manufacturer,"model":model,"price":value}

def addPhone(phonelist,phone):
    """
    Resume: The function will add into a list a dictionary
    Input: The function will recive the list, and a dictionary
    Output: The function will return the list with a dictionary added.
    """
    phonelist.append(phone)
    
def startUp(phonelist):
    """
    Resume: The function will add 10 items into the list
    Input: The function recive the list in which will add
    Output: The list mofifyed
    """
    addPhone(phonelist,createEntity("Apple", "iPhone 7", 4000))
    addPhone(phonelist,createEntity("Apple", "iPhone 7 Plus", 5000))
    addPhone(phonelist,createEntity("Apple", "iPhone 6", 3000))
    addPhone(phonelist,createEntity("Apple", "iPhone 5", 2000))
    addPhone(phonelist,createEntity("Apple", "iPhone 5C", 1000))
    addPhone(phonelist,createEntity("Apple", "iPhone 5SE", 600))
    addPhone(phonelist,createEntity("Apple", "iPhone 5S", 700))
    addPhone(phonelist,createEntity("Samsung", "Galaxy S7", 4500))
    addPhone(phonelist,createEntity("Samsung", "Note 7", 350))
    addPhone(phonelist,createEntity("Samsung", "Galaxy S2", 600))
    return phonelist

def findManufacturer(phonelist,manufacturer):
    """
    Resume: The function will return a list with all phone that have a manufacturer given from the keyboard
    Input: phonelist - is the list in which we will search, manufacturer - is the manufacturer that we are searching
    output: The function will return a list in which all elements will have the same manufacturer
    """
    manulist = []
    for phone in phonelist:
        if phone["manufacturer"] == manufacturer:
            addPhone(manulist,phone)
    return manulist
    
def findPhoneByManuModel(phonelist,manufacturer,model):
    """
    Resume: The function will return True if there is an element with key manufacturer = manufacturer and model key = model
    Input: phonelist - is the list in with we will search the elements
    Output: True if the dictionary is in the list and False otherwise
    """
    for phone in phonelist:
        if phone["manufacturer"] == manufacturer and phone["model"] == model:
            return True
    return False
    
def replacePhoneValue(phonelist,manufacturer,model,amount):
    """
    Resume: The function will replace the value of the phone in the phonelist, and will return the list
    Input: phonelist is the list in which we will search to replace the dictionary that have at key manufacturer = manufacturer 
           and model key = model with the value amount
    output: The list phonelist modified
    """
    for i in range(0,len(phonelist)):
        if phonelist[i]["manufacturer"] == manufacturer and phonelist[i]["model"] == model:
            phonelist[i]["price"] = amount
            return phonelist
        
def incresePercentPerPhone(phone,amount):
    """
    Resume: The function will return the a dictionary with a key modified
    Input: Phone which is a dictionary, and amount which is a percent
    Output: The function will return the dictionary with a keu modified
    """
    
    if amount > 0:
        phone["price"] =(phone["price"] * (100 + amount)) // 100
    else:
        amount = amount * -1
        phone["price"] = (phone["price"]*amount) // 100
    return phone
         
def testStartUp():
    testlist = []
    testlist = startUp(testlist)
    testlist.append(10)

def testAddPhoneAndCreateEntity():
    testlist = []
    addPhone(testlist, createEntity("Samsung", "Vt5", 600))
    testlist.append(1)
    
def testAll():
    testStartUp
    testAddPhoneAndCreateEntity
    
    
    
    