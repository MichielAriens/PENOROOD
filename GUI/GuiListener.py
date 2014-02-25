

class GuiListener:
    def __init__(self):
        self.zepListener = None
        self.gui = None
        
    def link(self,zepListener,gui):
        self.zepListener = zepListener
        self.gui = gui
        
    def send(self,stuff):
        self.zepListener.receive(stuff)
        
    def getPosition(self):
        pos = self.zepListener.getPosition()
        return pos
    