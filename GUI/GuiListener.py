

class GuiListener:
    def __init__(self):
        self.zepListener = None
        self.gui = None
        
    def link(self,zepListener):
        self.zepListener = zepListener
        
    def send(self,stuff):
        self.zepListener.receive(stuff)
        
    def getPosition(self):
        pos = self.zepListener.getPosition()
        return pos
    
    def refactor(self,message):
        print()
        
    def encode(self,message):
        print()
        
    def sendMovementToFakeZep(self, movement): #1 = up ,2 = down, ...
        self.zepListener.sendMovementToFakeZep(movement)
        
    def sendGoalDirection(self,direction):
        print(direction)
        self.zepListener.sendGoalDirection(direction)