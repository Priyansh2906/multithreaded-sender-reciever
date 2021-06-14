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
            client_socket.send(bytes(number_to_send,"utf-8"))
            number_to_send = None

def inputThread():
    global number_to_send
    while True:
        number_to_send = input("Enter a number : ")

def recieve():
    while True:
        msg = client_socket.recv(2048)
        print("Message recieved : ",msg)

if __name__ == '__main__':
    sending_thread = threading.Thread(target=send)
    inputThread = threading.Thread(target=inputThread)
    recieving_thread = threading.Thread(target=recieve)
    recieving_thread.start()
    inputThread.start()
    sending_thread.start()
    