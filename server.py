import socket
import csv

#create a TCP/IP socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to port
server_address = ('localhost',1234)
print('starting up on %s port %s' % server_address)
my_socket.bind(server_address)


#listen for incoming connections
my_socket.listen(5)
with open('sent.csv','wb') as write_file:
    client_socket, address = my_socket.accept()
    row = client_socket.recv(10000)
    while True:
        write_file.write(row)
        row = client_socket.recv(10000)
print("finished")
client_socket.send("file transfer is complete")
client_socket.close()
