



class Controller:
    
    
    
    
    def __init__(self, llc):
        self.llc = llc
        self.commandDictionary = {"V":self.forwards,
                                  "A":self.backwards}
    
    #Removes all spacing and splits ";" seperated values into a list.
    
        
    def forwards(self, dist):
        pass
    
    def backwards(self, dist):
        try:
            dist = float(dist)
            self.forwards(-dist)
        except:
            pass
        
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
        
    
    

class Node:
    def __init__(self, x, y, command_list):
        commandstrings = self.splitstrings(command_list)
        self.createCommands(commandstrings)
        commands = []
        self.command_counter = 0
        self.active = False
        self.number = -1
        
    def splitstrings(self, string):
        return string.replace(" ","").split(";")
        
    def readCommand(self, commandString):
        global commandDictionary
        
    def getNumber(self):
        return self.number

    def setNumber(self,number):
        self.number = number
    
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

    def getCommands(self):
        self.commands
    
    def createCommands(self, commandstrings):
        i = 0
        while i < len(commandstrings):
            command = Command(commandstrings[i])
            if command.cmd == "NR" :
                self.setNumber(command.getParam())
            self.getCommands().append(command)
            i = i + 1
            
                  


