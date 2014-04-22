from RabbitMQ import RMQreceiver as r
from RabbitMQ import RMQSender as s


class Listener:
    def __init__(self):
        self.simulators = []
        self.zeppelins = []
        self.color_ids = []

        
    def updateSimulators(self):
        pass
    
    def addZeppelinListener(self, listener, id):
        if(listener is not None):
            self.simulators.append((listener, id))
    
    def getSimulator(self, id):
        for i in range(len(self.simulators)):
            simulator_tuple = self.simulators[i]
            if(simulator_tuple[1] == id):
                return simulator_tuple[0]
        return None
    
    def getColor(self, id):
        for i in range(len(self.color_ids)):
            combo = self.color_ids[i]
            if(combo[0] == id):
                return combo[1]
        return None
    
    def getID(self, color):
        for i in range(len(self.color_ids)):
            combo = self.color_ids[i]
            if(combo[1] == color):
                return combo[0]
        return None
    
    def getZeppelinPosition(self,id):
        color = self.getColor(id)
        if(color is not None):
            command = self.getLocationMQ(0,0,color)
            self.sendCommand(command)
            answer = self.receiveAnswer()
            return answer
        else:
            return None
        
    def getZeppelinHeight(self,id):
        color = self.getColor(id)
        if(color is not None):
            command = self.getHeightMQ(0, color)
            elf.sendCommand(command)
            answer = self.receiveAnswer()
            return answer
        else:
            return None
            
    def sendCommand(self, command):
        pass 
    
    def receiveAnswer(self):
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
    
    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body,))
        command = method.routing_key
        values = body
        self.decodeResponse(command, values)
    
    def updateHeight(self, id, value):
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[0] == id):
                self.zeppelins.remove(zep)
                self.zeppelins.append((id, zep[1], zep[2], value))
    
    def updateLocation(self, id, value):
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[0] == id):
                self.zeppelins.remove(zep)
                self.zeppelins.append((id, value[0], value[1], zep[3]))
                
    
    def decodeResponse(self, command, value):
        split = command.string.rsplit(".");
        color = split[0]
        try:
            id = self.getID(color)
            if(id is not None):
                if(split[1] == "info"):
                    if(split[2] == "height"):
                        height = split[3]
                        print(color + ".info.height."+height)
                        self.updateHeight(self, id, value)
                    elif(split[2] == "location"):
                        location = split[3]
                        print(color + ".info.height."+location)
                        self.updateLocation(self,id, value)
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