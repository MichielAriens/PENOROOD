class Motor:
    #Pins to be provided by parameters.
    def __init__(self,thrustPin,postivePin,negativePin):
        self.thrust
        self.direction
        self.thrustPin = thrustPin
        self.positivePin = postivePin
        self.negativePin = negativePin

    
    #Set the desired trust. thrust element of [0:100] (float)
    #The thrust is either at maximum speed (fixed pin) or at a given speed (pwd pin).
    #All other motors connected to the pwd pin have the same speed.
    #
    #The direction is either 1 or -1 (depending on the pin), indicating which way the
    #  propellers are spinning and thus decide the direction of the thrust.
    def setThrust(self):
        self.thrust = thrustPin.getSignal()    #replace .getSignal() with appropiate input
        if self.positivePin.getSignal() != null:
            self.direction = positive
        elif self.negativePin.getSignal() != null:
            self.direction = negative
        else self.direction = null    #No direction has been given, write something to handle it if thrust isn't equal to 0
        self._actuate()
        
    def _actuate(self):
        return
        #Make motor perform action with self.thrust and self.direction
