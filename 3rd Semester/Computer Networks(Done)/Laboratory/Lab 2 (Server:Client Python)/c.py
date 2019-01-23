import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("chiul?",("172.20.10.5",5555))
print s.recvfrom(10)

