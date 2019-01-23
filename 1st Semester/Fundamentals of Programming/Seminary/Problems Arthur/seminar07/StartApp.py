'''
Created on Nov 12, 2016

@author: Arthur
'''

from repository.Repository import Repository
from domain.Car import Car
from domain.Client import Client

carRepo = Repository()
clientRepo = Repository()
rentalRepo = Repository()

carRepo.store(Car(1, "AB 01 RTY", "Mazda", "CX-3"))
carRepo.store(Car(2, "NT 99 PUX", "Dacia", "Dokker"))

clientRepo.store(Client(1001, "2850369887452", "Maria Popescu"))
clientRepo.store(Client(1002, "2880365882446", "Ion Andone"))

print("This is our car repo:")
print(carRepo)

print("This is our client repo:")
print(clientRepo)
 