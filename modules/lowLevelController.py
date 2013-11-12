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
        self.motorOffset = 50
        self.dHeight = 0
        #Init PID (0.1,0,0.5) works slightly, (0.1,0.05,3) better P to 0.2 increases responsiveness, I increses overshoot but decreases settletime
        #D decreases overshoot but engthens settletime. (slows machine down)
        
        if simMode == "RPi":
            self.altimeter = ds.DistanceSensor(10)
            self.lift = motor.VectoredMotor(24,4)
            compMotor = motor.CompositeMotor(motor.PulsedMotor(17,23), motor.PulsedMotor(9,7))
            self.thrust = compMotor.thruster
            self.rudder = compMotor.rudder
            self.pid = PID(0.2,0.1,5)
            
        elif simMode == "sim":
            self.fe = FakeEnvironment()
            self.lift = motor.FakeMotor(self.fe)
            self.altimeter = ds.FakeDistanceSensor2(self.fe)
            thread.start_new(self.fe.update, ())
            self.pid = PID(0.2,0.1,5)
            
        else:
            print "LowLevelController was not passed a valid simulation format.\n The application will now quit."
            raise RuntimeError()
        self.pid.setPoint(self.dHeight)
        
        #Camera
        self.camera = None
    
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
            self.lift.setThrust(self.pid.update(self.altimeter.getHeight()) + self.motorOffset)
            time.sleep(1)       
    
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
        
        
#The recipe gives simple implementation of a Discrete Proportional-Integral-Derivative (PID) controller. 
#PID controller gives output value for error between desired reference input and measurement feedback to minimize error value.
#More information: http://en.wikipedia.org/wiki/PID_controller
#
#cnr437@gmail.com
#
#######    Example    #########
#
#p=PID(3.0,0.4,1.2)
#p.setPoint(5.0)
#while True:
#     pid = p.update(measurement_value)
#
#


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

    
        
    
        
        
    
    
    
        
