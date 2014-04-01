import socket
import random

def client(string):
    HOST, PORT = 'localhost', 21567
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    sendMessage(string, sock)
    
    reply = sock.recv(16384)  # limit reply to 16K
    print(reply.decode("utf-8"))
    sock.close()
    #while(True):
     #  i = 1
    return reply

def main():
    client("this is a test")
    
def sendMessage(string, sock):
    sock.send(bytes(string, 'UTF-8'))
    
if __name__ == "__main__":
    main()
    