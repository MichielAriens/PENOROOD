import GUI.GuiListener

class ZepListener:
	def __init__(self):
		self.zeppelin = None
		self.guiListener = None
		
	def link(self,other):
		self.guiListener = other
		other.zepListener = self
		
	def getPosition(self):
		return self.zeppelin.getPosition()
	
	def getSpeed(self):
		return self.zeppelin.getSpeed()

	def sendMovementToFakeZep(self,movement):
		self.zeppelin.acceptMovementFromListener(movement)
		
	def sendGoalDirection(self,direction):
		self.zeppelin.setMovementZeppelin(direction)