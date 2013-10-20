class Motor:
    #Pins to be provided by parameters.
    def __init__(self):
        self.thrust
    
    #Set the desired trust. thrust element of [-100:100] (float)
    def setThrust(self,thrust):
        self.thrust = thrust
        self._actuate()
        
    def _actuate(self):
        return
        #-- IO to set thrust