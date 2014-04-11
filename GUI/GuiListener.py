
import CONNECTION.multithread_client as multithread_client
from CONNECTION.multithread_client import *



class GuiListener:
    def __init__(self):
        self.zepListener = None
        self.gui = None
        self.zepID = None
        self.socket = None
        try:
            HOST, PORT = 'localhost', 21567
            # SOCK_STREAM == a TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sock.setblocking(0)  # optional non-blocking
            print(sock)
            sock.connect((HOST, PORT))
            self.socket = sock
        except:
            print("Could not connect to server.")
        
    def link(self,zepListener):
        self.zepListener = zepListener
        
    def getPosition(self):
        if(self.zepListener is not None):
            pos = self.zepListener.getPosition()
            self.getPositionServer()
            return pos
        else:
            print("Could not get position of zep (ID=" + str(self.zepID) + ").")
        
    def sendMovementToFakeZep(self, movement): #1 = up ,2 = down, ...
        if(self.zepListener is not None):
            self.zepListener.sendMovementToFakeZep(movement)
        
    def sendGoalDirection(self,direction):
        print("Zep " + str(self.zepID) + ", direction: " + str(direction))
        if(self.zepListener is not None):
            self.zepListener.sendGoalDirection(direction)
        else:
            print("Could not send goal direction.")
            
    def setZepID(self, ID):
        self.zepID = ID
        
    def getPositionServer(self):
        if(self.socket is not None):
            try:
                #test
                sendMessage("G=1", self.socket)
                print("was able to send")
                reply = sock.recv(16384)  # limit reply to 16K
                print(reply.decode("utf-8"))
                print("SERVER REPLY: " + multithread_client.client("G==1"))
            except:
                print("not working")
                return (-1,-1)
            
    
        