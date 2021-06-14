import threading
import socket

#Connection Part
client_socket = socket.socket() #by default it is SOCK_STREAM (TCP) and has porotocal AF_INET (IPv4) 
client_socket.connect(('127.0.0.1',9999)) #server machine's ip and port on which it will send and recieve connections from

number_to_send = None

def send():
    global number_to_send
    while True:
        if number_to_send!=None:
            client_socket.send(number_to_send)
            number_to_send = None

def recieve():
    while True:
        msg = client_socket.recv(2048)
        print(msg)

if __name__ == '__main__':
    sending_thread = threading.Thread(target=recieve)
    sending_thread.start()