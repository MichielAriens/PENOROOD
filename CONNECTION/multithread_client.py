import socket
import random

def client(string):
    HOST, PORT = 'localhost', 21567
    # SOCK_STREAM == a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setblocking(0)  # optional non-blocking
    sock.connect((HOST, PORT))

    sock.send(bytes(string, 'UTF-8'))
    reply = sock.recv(16384)  # limit reply to 16K
    print(reply.decode("utf-8"))
    sock.close()
    while(True):
       i = 1
    return reply

def main():
    client('Python Rocks')

if __name__ == "__main__":
    main()