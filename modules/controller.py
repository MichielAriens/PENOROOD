



class Controller:
    
    
    
    
    def __init__(self, llc):
        self.llc = llc
        self.commandDictionary = {"V":self.forwards,
                                  "A":self.backwards}
    
    #Removes all spacing and splits ";" seperated values into a list.
    def splitstrings(self, string):
        return string.replace(" ","").split(";")
        
    
    def readCommand(self, commandString):
        global commandDictionary
        
    def forwards(self, dist):
        pass
    
    def backwards(self, dist):
        try:
            dist = float(dist)
            self.forwards(-dist)
        
        
class Command:
    self.action #A function
    self.param  #The parameter

class Node:
    def __init__(self,no,commands):
        self.seqNo = no
        self.commands = commands
        
    




