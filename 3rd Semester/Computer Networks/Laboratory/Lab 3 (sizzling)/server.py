import socket
import random

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5555))
number = random.randint(0, 100)
while(True):
    buff,addr=s.recvfrom(4)
    print("The number that was random generated is: ", number)
    print ("From ", addr, " I received the number", buff)
    something = buff
    something = int(something)
    if (something == number):
        s.sendto("Bravo ba", addr)
        break
    elif (something > number ):
        s.sendto(">", addr)
    else:
        s.sendto("<", addr)
    print("The new number is: ", something)
