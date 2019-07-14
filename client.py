import socket
import csv

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1234)
print('connecting to %s port %s' % server_address)
my_socket.connect(server_address)

with open('test.csv','rb') as open_file:
    csv_read = csv.reader(open_file)
    for row in csv_read:
        row_send = ''
        counter = 0;
        for ele in row:
            counter = counter + 1
            if(counter == 11):
                row_send += ele + '\n'
            else:
                row_send += ele+','
        print(row_send)
        my_socket.send(row_send)

print("file has been sent")
my_socket.shutdown(socket.SHUT_WR)
my_socket.close
