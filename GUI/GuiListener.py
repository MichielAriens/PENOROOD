

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
    