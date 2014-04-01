#!/usr/bin/python

import socketserver
import subprocess
import sys
from threading import Thread
import time

HOST = 'localhost'
PORT = 21567

############################################################################

def reverse_string(my_str):
    if my_str:
        return my_str[::-1]

############################################################################
'''  One instance per connection.
     Override handle(self) to customize action. '''

class ZepBase():
    
    def __init__(self):
        self.zeppelins = []
        
    def addZeppelin(self, ID):
        self.zeppelins.append(((0,0),ID))
        
    def updatePosition(self, ID, position):
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[1] == ID):
                self.zeppelins.remove(zep)
                self.zeppelins.append(position,ID)
    
    def getZeppelin(self, ID):
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[1] == ID):
                return zep
        return ((-1,-1),-1)
    
    def formRequest(self,data):
        print("@formrequest, data= " + str(data))
        splitted = data.rsplit("=");
        print(splitted)
        if(data[0] == "G"):
            string = str(self.getZeppelin(int(splitted[1])))
            print("Got zep position: ")
            return string
        else:
            self.updatePosition(int(splitted[1]),int(splitted[2]))
            print("did update")
        return "updated"
        
class TCPConnectionHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        
        print("SingleTCPHandler::handle()")

        # self.request is the client connection
        data = self.request.recv(1024)  # clip input at 1Kb
        stuff = data.decode("utf-8")

        reply = self.formRequest(stuff)
        
        print((reply))

        if reply is not None:
            self.request.send(bytes(reply, 'UTF-8'))

    
    
############################################################################

class Server(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(\
        self,\
        server_address,\
        RequestHandlerClass)
    
    
    
############################################################################

if __name__ == "__main__":
    server = Server((HOST, PORT), TCPConnectionHandler)
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)

############################################################################