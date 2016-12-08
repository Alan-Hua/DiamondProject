import socket
import ssl
import json
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5329))
serversocket.listen(5) # become a server socket, maximum 5 connections

import pysftp

run=True

# #ssl receive and create file
def do_something(connstream, data):
        print ("Received: ", data)
        data1 = str(data)
        data = data1
        file = open('payload.json', 'w')
        file.write(data1)
        file.close()
        run=False
        return False

def deal_with_client(connstream):
        data = connstream.read()
        while data:
                if not do_something(connstream, data):
                        break
                data = connstream.read()

print("WAITING FOR LOAD")
while run:
        newsocket, fromaddr = serversocket.accept()
        connstream = ssl.wrap_socket(newsocket, server_side=True, certfile="server.csr", keyfile="server.key")
        try:
                deal_with_client(connstream)
        finally:
                connstream.shutdown(socket.SHUT_RDWR)
                connstream.close()
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

cinfo = {'cnopts' : cnopts, 'host' : 'oz-ist-linux.abington.psu.edu', 'username': 'ftpuser', 'password': 'test1234', 'port': 109}
try:
    with pysftp.Connection(**cinfo) as sftp:
        try:
            sftp.cd('/home/ftpuser')
            sftp.put('thePayload.json', '/home/AlanHua/ProjectDiamond/thePayload.json')
            #sftp.get('Alanfile2')
        except:
            print ("File transfer issue")
except Exception:
    print(Exception)
