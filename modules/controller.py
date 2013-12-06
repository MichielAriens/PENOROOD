import lowLevelController as llci
import math
import time
import thread

#Set implementation for nodes.
class NodeSet:
    def __init__(self):
        self.nodes = []
        
    def addAll(self, multi):
        for x in multi:
            self.add(x)
            
    def get(self, stage):
        for elem in self.nodes:
            if elem.number == stage:
                return elem
        return None
    
    def add(self, node):
        for elem in self.nodes:
            if elem.equals(node):
                self.nodes.remove(elem)
            self.nodes.append(node)
            
    #node is a node
    def contains(self, node):
        for elem in self.nodes:
            if elem.equals(node):
                return True
        return False
    
    #stage is an int
    def containsStage(self, stage):
        for elem in self.nodes:
            if elem.number == stage:
                return True
        return False

#Controller class is responible for taking image data, storing and updating it and fulfilling the commands within the image data and
class Controller:
    def __init__(self, sens = None):
        self.llc = llci.LowLevelController(dists = sens)
        self.nodes = NodeSet() #Nodes is a set where each node is unique in its number and is mutable.
        self.stage = 0
        
    def _start(self):
        while(True):
            self.updateInput()
            activeNode = self.nodes.get(self.stage)
            if activeNode != None:
                while(activeNode.execute(self.llc)):
                    pass
            else:
                pass #Current node not vivible
            
            if self.nodes.containsStage(self.stage +1):
                nextNode = self.nodes.get(self.stage +1)
                if abs(nextNode.x) < 50 and abs(nextNode.y) < 50:
                    self.stage += 1
                    print "stage changed: " + str(self.stage)
                else:
                    pass #try to rotate to target.
                
            
        
    def getRotToNextStage(self):
        nextNode = self.nodes.get(self.stage + 1)
        if nextNode == None:
            return
        return math.atan2(nextNode.x, nextNode.y)
    
    def start(self):
        thread.start_new(self._start, ())
        
    def updateOutput(self):
        #if the next stage is visible
        if NodeSet.containsStage(self.stage + 1):
            pass #orient to the stage and go there
        else:
            pass #execute the commands in order of their priority untill the next stage is in view.
        
    def updateInput(self):
        #Take a picture
        self.llc.camera.click()
        #get data
        params = self.llc.camera.getQR()
        #update the nodes and add new ones
        foundNodes = []
        for x in params:
            foundNodes.append(Node(x[0], x[1], x[2]))
        for x in foundNodes:
            self.nodes.add(x)
        
#This class represents a command. type is = {mov, rot, asc, nr}. Invoke(llc) invokes a command on the low level controller
class Command:
    def __init__(self, string):
        self.string = string
        self.type
        self.priority
        self.param
        self.decode()
        
        #types = {mov, rot, asc, nr}
        
    def decode(self):
        parts = self.string.split(":")
        cmd = parts[0]
        self.param = float(parts[1])
        if cmd == "V" or cmd == "A":
            self.type = "MOV"
            self.priority = 2
        elif cmd == "S" or cmd == "D":
            self.type = "ASC"
            self.priority = 0
        elif cmd == "L" or cmd == "R":
            self.type = "ROT"
            self.priority = 1
        else:
            self.type = "NR"
            self.priority = 4
            
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
                
        
    
    

class Node():
    def __init__(self, x, y, command_list):
        commandstrings = self.splitstrings(command_list)
        self.commands = self.toCommands(commandstrings)
        self.x = x
        self.y = y
        self.stage = 0
        
        self.command_counter = 0
        self.active = False
        self.number
        
    def equals(self, other):
        return other.number == self.number
    
    def execute(self, llc):
        if self.stage < len(self.commands):
            self.commands[self.stage].invoke(llc)
            self.stage += 1
            return True
        else:
            return False
        
    #Fills the returnvalue with the command objects from the list of command strings.
    #If the command is of the type "NR" then the command is skipped and the node number is updated
    def toCommands(self, listOfStrings):
        result = []
        for string in listOfStrings:
            cmd = Command(string)
            if cmd.type == "NR":
                self.number = cmd.getParam()
            else:
                result.append(cmd)
        return result
    
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
    




