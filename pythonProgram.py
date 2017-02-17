import socket
import _thread

hostname = socket.gethostname()
buffersize = 1024
serverPort = 4411 #digits 1 thru 4 of SHA256("lost the game") in base 10

#SERVER
server = socket.socket() #to recieve data
server.bind((hostname,serverPort))
server.listen()
def serverfunc():
    while True:
        connection,address=server.accept()
        data = connection.recv(buffersize)
        print("Started connection, recieved data "+str(data))
        connection.send(b'r')
_thread.start_new_thread(serverfunc,())

#CLIENT
def clientfunc(recipient,port,data):
    client = socket.socket()
    client.connect((recipient,port))
    client.send(data)
    while True:
        data = client.recv(buffersize)
        if data:
            print("Recieved data "+str(data))
            return data
_thread.start_new_thread(clientfunc,(hostname,serverPort,b'h'))
