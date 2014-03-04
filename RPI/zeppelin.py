#Controls the positioning of the zeppelin at high level.
#You tell this class what results you wish to achieve instead of how to achieve them.


#--------------------------------------

import hardware.distSensor as ds
import hardware.motor as motor
import hardware.camera as cam
import thread
import time
import random

class Zeppelin:
    #initmethod variables (call start to invoke backround methods)
    def __init__(self, dists=None):
        
        self.path = "cam.jpg"
        #Init PID (0.1,0,0.5) works slightly, (0.1,0.05,3) better P to 0.2 increases responsiveness, I increses overshoot but decreases settletime
        #D decreases overshoot but engthens settletime. (slows machine down)
        self.altimeter = dists
        self.lift = motor.VectoredMotor(24,4)
        self.xMot = motor.PulsedMotor(17,23)
        self.yMot = motor.PulsedMotor(9,7)
        self.heightPID = PID(5,0.5,5)
        self.xPID = PID(1,0,0.1)
        self.yPID = PID(1,0,0.1)
        self.camera = cam.Camera(500, self.path)
        
        self.dHeight = self.altimeter.getHeight()
        self.dPos = camera.getPos()
        
        self.heightPID.setPoint(dHeight)
        
        self.xPID.setPoint(dPos.fst())
        self.yPID.setPoint(dPos.snd())
    
    #Used to set the desired height.
    #Effects will only become apparent after _keepHeight pulls the new info
    def setDesiredHeight(self,height):
        self.dHeight = height
        self.pid.setPoint(height)
        
        
        
    #Algorithm to invoke motors to achieve a certain height
    #Python convention: methods names preceded by '_' should be deemed 'private'
    def _keepHeight(self):
        while(True):
            #Set the thrust to the PID output.
            pos = self.camera.getPos()
            self.lift.setThrust(self.heightPID.update(self.altimeter.getHeight()) + self.motorOffset)
            self.xMot.setThrust(self.xPID.update(self.pos.fst()))
            self.xMot.setThrust(self.xPID.update(self.pos.snd()))
            time.sleep(1)       
    
    #Starts running background threads
    # _keepHeight
    def start(self):
        thread.start_new(self._keepHeight, ())
   


class PID:
    """
    Discrete PID control
    """

    def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=100, Integrator_min=-100):

        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.Derivator=Derivator
        self.Integrator=Integrator
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min

        self.set_point=0.0
        self.error=0.0

    def update(self,current_value):
        """
        Calculate PID output value for given reference input and feedback
        """

        self.error = self.set_point - current_value

        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * ( self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value

        return PID

    def setPoint(self,set_point):
        """
        Initilize the setpoint of PID
        """
        self.set_point = set_point
        self.Integrator=0
        self.Derivator=0

    def setIntegrator(self, Integrator):
        self.Integrator = Integrator

    def setDerivator(self, Derivator):
        self.Derivator = Derivator

    def setKp(self,P):
        self.Kp=P

    def setKi(self,I):
        self.Ki=I

    def setKd(self,D):
        self.Kd=D

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator

    
        
    
        
        
    
    
    
        
