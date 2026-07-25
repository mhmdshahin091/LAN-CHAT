import socket
import threading
client = socket.socket()
client.connect(("127.0.0.1",2222))
print("Connected to Server")
def receive_messages() :
 while True :
  message = client.recv(1024)
  print (message.decode())
thread=threading.Thread(target=receive_messages)
thread.start()
while True:
 message =input("You :")
 client.send(message.encode()) 