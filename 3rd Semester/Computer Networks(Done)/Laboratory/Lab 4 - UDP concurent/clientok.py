import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
nr = input("Give me a number: ")
s.sendto(str(nr),("127.0.0.1",7777))                 
port = s.recvfrom(100)
print port
for i in range(0,nr):
    x = input("Da ba un nr: ")
    s.sendto(str(x),("127.0.0.1",int(port[0])))
