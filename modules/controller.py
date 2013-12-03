import lowLevelController as llci

class NodeSet:
    def __init__(self):
        self.nodes = []
        
    def add(self, Node):
        
    

class Controller:
    def __init__(self, dist = None):
        self.llc = llci.LowLevelController(dist = dist)
        self.nodes #Nodes is a set where each node is unique in its number and is mutable.
        
        
        
    def _start(self):
        self.llc.camera.click()
        readNodes = self.llc.camera.getQR()
        
        
class Command:
    def __init__(self, string):
        self.string = string
        self.decode()
        
        #kinds = {mov, rot, asc, nr}
        
    def decode(self):
        parts = self.string.split(":")
        cmd = parts[0]
        self.param = float(parts[1])
        if cmd == "V" or cmd == "A":
            self.type = "MOV"
        elif cmd == "S" or cmd == "D":
            self.type = "ASC"
        elif cmd == "L" or cmd == "R":
            self.type = "ROT"
        else:
            self.type = "NR"
            
        if cmd == "A" or cmd == "D" or cmd == "R":
            self.param *= -1 
        
    def getKind(self):
        return self.kind
    
    def getParam(self):
        return self.param
    
    def invoke(self, llc):
        if self.type == "ASC":
            llc.setDesiredHeight(llc.dHeight + self.param)
        elif self.type == "MOV":
            if self.param < 0:
                llc.thrust.setThrust(-20)
            elif self.param > 0:
                llc.thrust.setThrust(20)
            else:
                pass
        elif self.type == "ROT":
            pass
                
        
    
    

class Node:
    def __init__(self, x, y, command_list):
        commandstrings = self.splitstrings(command_list)
        commandstrings 
        
        
        self.command_counter = 0
        self.active = False
        self.number = number
        
    def splitstrings(self, string):
        return string.replace(" ","").split(";")
        
    
    def readCommand(self, commandString):
        global commandDictionary
        
    def getNumber(self):
        return self.number
    
    def getActive(self):
        return self.active
    
    def setActive(self,status):
        self.active = status
        
    def getCommandList(self):
        return self.command_list
    
    def getCommandCounter(self):
        return self.command_counter
    
    def setCommandCounter(self, counter):
        self.command_counter = counter
    
    def incrementCounter(self):
        counter = self.getCommandCounter()
        counter = counter + 1
        
        self.setCommandCounter(counter)
    def getNextCommand(self):
        command = self.getCommandList(self.getCommandCounter())
        self.incrementCounter(self)
        return command
    




