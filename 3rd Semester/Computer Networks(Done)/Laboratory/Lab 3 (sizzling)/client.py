import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    a=int(input("Number:"))
    s.sendto(str(a),("127.0.0.1",5555))
    b,addr=s.recvfrom(10);
    print b
    if b!="<" and b!=">":
        break
