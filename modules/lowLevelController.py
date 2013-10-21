#Controls the positioning of the zeppelin at high level.
#You tell this class what results you wish to achieve instead of how to achieve them.


#--------------------------------------

import hardware.distSensor as ds
import hardware.motor as motor
import thread
import time
class LowLevelController:
    #initmethod variables (call start to invoke backround methods)
    def __init__(self):
        #Primary declarations.
        #
        #Motors:
        self.lift = Motor(thrustPin,positivePin,negativePin)  #parameters have to be adjusted appropiately
        self.thust = Motor(thrustPin,positivePin,negativePin)
        self.rudder = Motor(thrustPin,positivePin,negativePin)
        
        #Altimeter
        self.altimeter = ds.DistanceSensor()
        self.dHeight = 0
        
        #Camera
        self.camera = None
    
    #Used to set the desired height.
    #Effects ill only become apparent after _keepHeight pulls the new info
    def setDesiredHeight(self,height):
        self.dHeight = height
        
    #Algorithm to invoke motors to achieve a certain height
    #Pyhton convention: methods names preceded by '_' should be deemed 'private'
    def _keepHeight(self):
        while(True):
            #-- algorithm
            #End by sleeping for 250 ms not to overload main thread(optimal variable should be found later
            time.sleep(0.250)
    
    #Starts running background threads
    # _keepHeight
    def start(self):
        thread.start_new(self._keepHeight, ())
        
