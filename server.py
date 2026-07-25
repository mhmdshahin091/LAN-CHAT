import socket
import threading
clients=[]
def handle_client(client) :
 while True :
  message = client.recv(1024)
  for c in clients:
   if c !=client:
    c.send(message)
server = socket.socket()
server.bind(("0.0.0.0",2222))
server.listen()
while True:
 client , address= server.accept()
 print("Client Connected :" , address)
 clients.append(client)
 thread=threading.Thread(target=handle_client,args=(client,))
 thread.start()