import socket
import csv


def server_recieving(filename):
    #create a TCP/IP socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind socket to port
    server_address = ('0.0.0.0',25565)
    print('starting up on %s port %s' % server_address)
    my_socket.bind(server_address)


    #listen for incoming connections
    my_socket.listen(5)
    with open(filename,'wb') as write_file:
        client_socket, address = my_socket.accept()
        row = client_socket.recv(10000)
        print("Starting to accept")
        while True:
            #row = row.decode("utf-8")
            write_file.write(row)
            row = client_socket.recv(10000)
            if not row: break
    print("finished")
    client_socket.send("file transfer is complete")
    client_socket.close()


def server_sending(filename):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('0.0.0.0', 25565)
    print('connecting to %s port %s' % server_address)
    my_socket.connect(server_address)

    with open(filename,'r') as open_file:
        csv_read = csv.reader(open_file)
        column_num = len(next(csv_read))
        open_file.seek(0)
        print(column_num)
        for row in csv_read:
            row_send = ''
            counter = 0;
            for ele in row:
                counter = counter + 1
                if(counter == column_num):
                    row_send += ele + '\n'
                else:
                    row_send += ele+','
            print(row_send)
            row_send = row_send.encode("utf-8")
            my_socket.send(row_send)

    print("file has been sent")
    my_socket.shutdown(socket.SHUT_WR)
    my_socket.close

#server_recieving("sent.csv")
server_sending("test.csv")
