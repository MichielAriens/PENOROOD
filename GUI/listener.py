from RabbitMQ import RMQreceiver as r
from RabbitMQ import RMQSender as s


class Listener:
    def __init__(self):
        self.simulators = []
        self.zeppelins = []
    
    def addZeppelinListener(self, listener, id):
        if(listener is not None):
            self.simulators.append((listener, id))
    
    def getSimulator(self, id):
        for i in range(len(self.simulators)):
            simulator_tuple = self.simulators[i]
            if(simulator_tuple[1] == id):
                return simulator_tuple[0]
        return None
    
    def getZeppelin(self, id):
        for i in range(len(self.zeppelins)):
            zeppelin_tuple = self.zeppelins[i]
            if(zeppelin_tuple[1] == id):
                return zeppelin_tuple[0]
        return None
    
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