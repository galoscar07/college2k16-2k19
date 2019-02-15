'''
Created on Oct 29, 2016

@author: oscar
'''
from src.Apartment_administrator.domain.operations import addApartmentInOrder, deleteApartmentNr, deleteApartmentsFromTo, deleteApartmenttyp, \
    replaceApartmentValue
from src.Apartment_administrator.domain.entities import createApartment
    
    
def testaddApartmentInOrder():
    b = startUp()
    assert(len(b) == 18)
    ap = createApartment(15, "gas", 500)
    addApartmentInOrder(b, ap)
    assert(len(b) == 19)
    
def testdeleteApartmentNr():
    b = startUp()
    assert(len(b) == 18)
    deleteApartmentNr(b, 14)
    assert(len(b)) == 17
    
def testdeleteApartmentsFromTo():
    b = startUp()
    assert(len(b) == 18)
    deleteApartmentsFromTo(b, 10, 12)
    assert(len(b) == 15)
    
def testdeleteApartmenttyp():
    b = startUp()
    assert(len(b) == 18)
    deleteApartmenttyp(b, "gas")
    assert(len(b) == 12)
    
def testreplaceApartmentValue():
    b = startUp()
    assert(len(b) == 18)
    replaceApartmentValue(b, 13, "water", 200)
    assert(b[16]["amount"] == 200)

def testAllOperations():
    testaddApartmentInOrder()
    testdeleteApartmentNr()
    testdeleteApartmentsFromTo()
    testdeleteApartmenttyp()
    testreplaceApartmentValue()

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