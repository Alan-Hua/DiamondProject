import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(1) # become a server socket, maximum 5 connections

while True:
    print("[*]Waiting for a connection")
    connection, address = serversocket.accept()
    print("[x]Connected")
    buf = connection.recv(3000)
    if len(buf) > 0:
        print ("[x] Received", buf)
