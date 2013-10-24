#Controls the positioning of the zeppelin at high level.
#You tell this class what results you wish to achieve instead of how to achieve them.


#--------------------------------------

import hardware.distSensor as ds
import hardware.motor as motor
import thread
import time
import random

class LowLevelController:
    #initmethod variables (call start to invoke backround methods)
    def __init__(self,simMode = "RPi"):
        if simMode == "RPi":
            self.altimeter = ds.DistanceSensor()
            self.lift = None
            self.thrust = None
            self.rudder = None
        elif simMode == "sim":
            self.fe = FakeEnvironment()
            self.lift = motor.FakeMotor(self.fe)
            self.altimeter = ds.FakeDistanceSensor2(self.fe)
            thread.start_new(self.fe.update, ())
            
        else:
            print "LowLevelController was not passed a valid simulation format.\n The application will now quit."
            raise RuntimeError()
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
            delta = self.dHeight - self.altimeter.getHeight()
            
            #first very simple algorithm
            if delta > 0:
                self.lift.setThrust(100)
            else:
                self.lift.setThrust(-100)
            
            
            time.sleep(0.250)
    
    #Starts running background threads
    # _keepHeight
    def start(self):
        thread.start_new(self._keepHeight, ())
        
class FakeEnvironment:
    
    def __init__(self):
        #pull of gravity somewhere around 10 newtons
        self.mass = random.gauss(1,0.05)
        print "mass of the fake zeppelin is " + str(self.mass)
        self.gravity = self.mass * 9.81
        
        self.verticalForce = 0
        
        self.height = 0
        self.vSpeed = 0
        
    def update(self):
        while True:    
            force = self.verticalForce - self.gravity 
            if(self.height < 0):
                self.height = 0
                self.vSpeed = 0
            else:
                self.vSpeed += force/self.mass
                self.height += self.vSpeed
            time.sleep(1)
        
    
        
    
        
        
    
    
    
        
