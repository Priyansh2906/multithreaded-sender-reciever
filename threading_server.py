import socket
import threading

def sendClient1():
    while True:
        msg = c1.recv(4096)
        if(msg!=None):
            print(msg)
            msg = msg.decode()
            c2.send(bytes(msg,"utf-8"))

def sendClient2():
    while True:
        msg = c2.recv(4096)
        if(msg!=None):
            print(msg)
            msg = msg.decode()
            c1.send(bytes(msg,"utf-8"))
   
c1 = None #Client socket1
addr1 = None #Client address1
c2 = None #Client socket2
addr2 = None #Client address2	
server_socket1 = socket.socket() #by default it is SOCK_STREAM (TCP) and has porotocal AF_INET (IPv4) 

server_socket1.bind(('127.0.0.1',9999)) #server machine's ip and port on which it will send and recieve connections from

server_socket1.listen(2) #We will only accept two connections as of now , one for each client
print("Server started successfully!!!")
print("Waiting for connections...\n\n")

while (((c1 is None)and(addr1 is None)) and ((c2 is None) and (addr2 is None))):
        
    if((c1 is None) and (addr1 is None)):
        c1,addr1 = server_socket1.accept()
        print("User connected to client1 socket!!")   

    if((c2 is None) and (addr2 is None)):
        c2,addr2 = server_socket1.accept()
        print("\n\nUser connected to client2 socket!!")

send_to_client1 = threading.Thread(target=sendClient1)
send_to_client2 = threading.Thread(target=sendClient2)

send_to_client1.start()
send_to_client2.start()

