'''
Created on Oct 29, 2016

@author: oscar
'''
from src.Apartment_administrator.domain.entities import createApartment

def testcreateApartment():
    number = 1
    typ = "gas"
    amount = 400
    ap = createApartment(number, typ, amount)
    assert(ap[number] == number)
    assert(ap[typ] == typ)
    assert(ap[amount] == amount)