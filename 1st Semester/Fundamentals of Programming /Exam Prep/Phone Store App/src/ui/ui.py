'''
Created on Nov 14, 2016

@author: oscar
'''
from src.operations.operations import createEntity,addPhone,startUp,findManufacturer,findPhoneByManuModel,replacePhoneValue,incresePercentPerPhone

def printOptions():
    print("1. Add a new phone to the list")
    print("2. Display all the phones from a given manufacturer")
    print("3. Increase the price of a phone")
    print("4. Increase the price of all phone")
    print("5. Exit")
    
def runMenu():
    phonelist = []
    phonelist = startUp(phonelist)
    keepAlive = True
    while keepAlive:
        printOptions()
        command = input("Command = ")
        if command == "5":
            keepAlive = False
        elif command == "1":
            uiAddPhone(phonelist)
        elif command == "2":
            uiFindManufacturer(phonelist)
        elif command == "3":
            uiIncreseAPhone(phonelist)
        elif command == "4":
            uiIncresePercent(phonelist)
        elif command == "6":
            uiPrintAll(phonelist)

def uiAddPhone(phonelist):
    manufacturer = input("Give a manufacturer:")
    model = input("Give a model:")
    price = input("Give a price:")
    if len(manufacturer) < 3:
        print("Invalid input, the phone was not added")
    elif len(model) < 3:
        print("Invalid input, the phone was not added")
    elif len(price) < 3:
        print("Invalid input, the phone was not added")
    else:
        price = int(price)
        phone = createEntity(manufacturer,model,price)
        addPhone(phonelist,phone)
        
def uiFindManufacturer(phonelist):
    manufacturer = input("Give a manufacturer: ")
    manulist = findManufacturer(phonelist,manufacturer)
    uiPrintAll(manulist)

def uiIncreseAPhone(phonelist):
    manufacturer = input("Give a manufacturer:")
    model = input("Give a model:")
    amount = input("Give an amount:")
    if findPhoneByManuModel(phonelist,manufacturer,model) == False:
        print("There is no phone with such specifications")
    else:
        replacePhoneValue(phonelist,manufacturer,model,amount)

def uiIncresePercent(phonelist):
    amount = input("Give a percent: ")
    amount = int(amount)
    if amount > 100 or amount < -50:
        print("Invalid input!")
    else:
        for phone in phonelist:
            phone = incresePercentPerPhone(phone, amount)

def uiPrintAll(phonelist):
    if len(phonelist) == 0:
        print("There is no element to print")
    else:
        for phone in phonelist:
            print(phone)
        
        
        
        