from RabbitMQ import RMQreceiver as r
from RabbitMQ import RMQSender as s


class GuiListener:
    def __init__(self):
        self.zepListener = None
        self.gui = None
        self.zepID = None
        self.connected = False
        self.ip = None
        self.sender = None
        self.receiver = None
        
        
    def connect(self):
        self.ip = 'localhost'
        self.sender = s.Sender
        self.receiver = r.Receiver
        self.sendRequest = SendRequest
        self.connected = True
        
        self.startRMQ()

    def startRMQ(self):
        self.receiver.startReceiving()

    def sendCommand(self,command):
        print('command: ' + command)
        self.sender.sendCommand(command)
        
    def link(self,zepListener):
        self.zepListener = zepListener
        
    def getPosition(self):
        if(not self.connected):
            pos = self.zepListener.getPosition()
            
            #test
            testpos = self.getPositionMQ()
            
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
        
    def getPositionMQ(self):
        if(self.connected):
            try:
                pass
            except:
                print("not working")
                return (-1,-1)
    
    def communicateWithMQ(self):
        pass
    
    def getLocationMQ(self,x,y,color):
        return color + ".info.location" + str(x) + "," + str(y)  
    
    def getHeightMQ(self,z,color):
        return color + ".info.height" + str(z)
    
    def moveMQ(self,x,y, color):
        return color + ".hcommand.move" + str(x) + "," + str(y)  
    
    def elevateMQ(self,z, color):
        return color + ".hcommand.elevate" + "<" + str(z)
    
    def commandMotor1MQ(self, percentage, color):
        return color + ".lcommand.motor1" + str(percentage)
    
    def commandMotor2MQ(self, percentage, color):
        return color + ".lcommand.motor1" + str(percentage)
    
    def commandMotor3MQ(self, percentage, color):
        return color + ".lcommand.motor1" + str(percentage)
    
    def privateMQ(self, command, color):
        return color + "." + command
    
    def decodeResponse(self, command):
        split = command.string.rsplit(".");
        color = split[0]
        try:
            if(split[1] == "info"):
                if(split[2] == "height"):
                    height = split[3]
                    print(color + ".info.height."+height)
                elif(split[2] == "location"):
                    location = split[3]
                    print(color + ".info.height."+location)
                else:
                    pass
            elif(split[1] == "hcommand"):
                if(split[2] == "move"):
                    move = split[3]
                    print(color + ".hcommand.move."+ move)
                elif(split[2] == "elevate"):
                    elevate = split[3]
                    print(color + ".hcommand.elevate."+ elevate)
                else:
                    pass
            elif(split[1] == "lcommand"):
                if(split[2] == "motor1"):
                    power = split[3]
                    print(color + ".lcommand.motor1."+ power)
                elif(split[2] == "motor2"):
                    power = split[3]
                    print(color + ".lcommand.motor2."+ power)
                elif(split[2] == "motor3"):
                    power = split[3]
                    print(color + ".lcommand.motor3."+ power)
            elif(split[1] == "private"):
                pass
            else:
                pass
            
        except:
            print("Something wrong happened at decodeResponse() in GuiListener.")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            