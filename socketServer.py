import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" %(err))

port = 60

s.bind(("",port))
print("socket is binded to port: ",port)


s.listen(1)
print("socket is listening ")

while True:
    c, addr = s.accept()
    print("got connection from ",addr)

    c.send('thanks for connecting!'.encode())

    c.close()









