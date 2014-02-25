import GUI.GuiListener

class ZepListener:
	def __init__(self):
		self.zeppelin = None
		self.guiListener = None	
		
	def link(other):
		self.guiListener = other
		other.guiListener = self
		
	def getPosition(self):
		return self.zeppelin.getPosition()
	
	def getSpeed(self):
		return self.zeppelin.getSpeed()

		

		