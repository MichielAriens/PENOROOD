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

class TCPConnectionHandler(socketserver.BaseRequestHandler):

    def handle(self):
        
        print("SingleTCPHandler::handle()")

        # self.request is the client connection
        data = self.request.recv(1024)  # clip input at 1Kb
        print(data.decode("utf-8"))

        reply = reverse_string(data)

        print((reply))

        if reply is not None:
            self.request.send(reply)
        self.request.close()

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