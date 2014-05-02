import pika

class Listener:
    def __init__(self):
        self.simulators = []#tuple (ID, ZepListener)
        self.zeppelins = [] #tuple (ID, x, y, z)
        self.color_ids = [(1, "rood"), (2, "ijzer"), (3, "paars"), (4, "blauw")] #tuple (ID, color)
        self.messages = []
     
    def updateSimulators(self):
        pass
    
    def copyList(self, list):
        for i in range(len(list)):
            copy = []
            copy.append((list[i]))
        return copy
            
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

    def createZep(self, id):
        match = False
        for j in range(len(self.zeppelins)):
            zep = self.zeppelins[j]
            if(zep[0] == id):
                match = True
        if(match == False):
            self.zeppelins.append((id, 0, 0, 0))


    
    def getZeppelinPosition(self,id):
        for i in range(len(self.zeppelins)):
            tuple = self.zeppelins[i]
            if(tuple[0] == id):
                return ((tuple[1], tuple[2]))
        return None
    
    def getZeppelinHeight(self,id):
        for i in range(len(self.zeppelins)):
            tuple = self.zeppelins[i]
            if(tuple[0] == id):
                return (tuple[3])
        return None
    
    def updateHeight(self, id, value):
        match = False
        print(value)
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[0] == id):
                self.zeppelins.remove(zep)
                self.zeppelins.append((id, zep[1], zep[2], value))
        if(match == False):
            self.zeppelins.append((id, 0, 0, value))
        
    def updateLocation(self, id, value):
        match = False
        print(value)
        for i in range(len(self.zeppelins)):
            zep = self.zeppelins[i]
            if(zep[0] == id):
                self.zeppelins.remove(zep)
                self.zeppelins.append((id, int(value[0])/10, int(value[1])/10, zep[3]))
                match = True;
        if(match == False):
            self.zeppelins.append((id, value[0], value[1], 0))
    
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
    
    def callback(self, ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body,))
        command = str(method.routing_key)
        values = body
        self.decodeResponse(command, values)
    
    def decodeResponse(self, command, value):
        try:
            split = command.rsplit(".");
            color = split[0]
            id = self.getID(color)
            self.createZep(id)
            if(id is not None):
                if(split[1] == "info"):
                    if(split[2] == "height"):
                        print(str(value))
                        self.updateHeight(id, int(value))
                    elif(split[2] == "location"):
                        print(str(value))
                        values = value.rsplit(",")
                        self.updateLocation(id, values)
                    else:
                        pass
                elif(split[1] == "hcommand"):
                    if(split[2] == "move"):
                        pass
                    elif(split[2] == "elevate"):
                        pass
                    else:
                        pass
                elif(split[1] == "lcommand"):
                    if(split[2] == "motor1"):
                        pass
                    elif(split[2] == "motor2"):
                        pass
                    elif(split[2] == "motor3"):
                        pass
                elif(split[1] == "private"):
                    pass
                else:
                    pass
        except:
            print "command not parsed: " + command + ":" + value
