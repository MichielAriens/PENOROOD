import time
import thread
try:
    import RPi.GPIO as GPIO
except:
    pass

#A logical motor provides an abstraction layer above the specific layout of the motors. 
#specifically a logical motor is a rudder or a thruster. It relies on a composite thruster to distribute the thrust among the
#real engines. This class should not be used by the user: it should be deemed private.
class LogicalMotor:
    def __init__(self,master):
        self.master = master
        self.thrust = 0
        
        
    def setThrust(self,nThrust):
        if(nThrust > 100):
            self.thrust = 100.0
        elif(nThrust < -100):
            self.thrust = -100.0
        else:
            self.thrust = nThrust
        self.master.setThrust()
        
#A class that converts logical motors like the rudder and actuates that into real motors.
#Defines two logical classes: rudder and thruster which can be used as normal motors.
#Rudder is clockwise for increasing thrust values
class CompositeMotor:
    #Takes two real motor implementations. These should be the two thrusters on the wings
    def __init__(self,leftMotor,rightMotor):
        #define the real motors
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        #define the logical motors
        self.rudder = LogicalMotor(self)
        self.thruster = LogicalMotor(self)
        #determines strength of the rotation
        self.rotationFactor = 1
    
    def setThrust(self):
        self.leftMotor.setThrust(self.thruster.thrust + self.rudder.thrust)
        self.rightMotor.setThrust(self.thruster.thrust - self.rudder.thrust)
        
#A pysical implementation of a motor. Uses PWM (varaible output pins) to drive motors
#Provides best control. Usefull for most critical motors like the lifter.
class VectoredMotor:
    def __init__(self,postivePin,negativePin):
        #Instantiate pin objects
        #--Placeholder--
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.thrustPin = GPIO.PWM(18, 50)
        self.positivePin = postivePin
        self.negativePin = negativePin
        self.thrust = 0
        GPIO.setup(self.positivePin,GPIO.OUT)
        GPIO.setup(self.negativePin,GPIO.OUT)
        GPIO.output(self.positivePin,True)
        GPIO.output(self.negativePin,False)
        
        self.thrustPin.start(0.0)
            
    def setThrust(self,nThrust):
        if(nThrust > 100):
            self.thrust = 100.0
        elif(nThrust < -100):
            self.thrust = -100.0
        else:
            self.thrust = nThrust
        self._actuate()
        
    def _actuate(self):
        GPIO.setmode(GPIO.BCM)
        if(self.thrust < 0):
            GPIO.output(self.positivePin,False)
            GPIO.output(self.negativePin,True)
        else:
            GPIO.output(self.positivePin,True)
            GPIO.output(self.negativePin,False)
        self.thrustPin.ChangeDutyCycle(abs(self.thrust))

#A pysical implementation of a motor. Uses fixed pins but still provides a way to pass real numbers to setThrust()
#Runs a thread in the background and runs the motors on max power for abs(thrust) percent of the time.
class PulsedMotor:
    def __init__(self,postivePin,negativePin):
        #Instantiate pin objects
        #--Placeholder--
        GPIO.setmode(GPIO.BCM)
        self.positivePin = postivePin
        self.negativePin = negativePin
        GPIO.setup(self.positivePin,GPIO.OUT)
        GPIO.setup(self.negativePin,GPIO.OUT)
        GPIO.output(self.positivePin,False)
        GPIO.output(self.negativePin,False)
        self.thrust = 0
        thread.start_new(self.pulse, (1000,1))
        
    def setThrust(self,nThrust):
        if(nThrust > 100):
            self.thrust = 100.0
        elif(nThrust < -100):
            self.thrust = -100.0
        else:
            self.thrust = nThrust
        
    #Endless loop to control the motors. TimeQuantum decides how fine grained the loop is (ms). The proper value should be found experimentally
    #percent defines the percent of time that the motor should give 100% of its power.
    def pulse(self,timeQuantum,ignore):
        GPIO.output(self.negativePin,False)
        GPIO.output(self.positivePin,False)
        while(True):
            percent = self.thrust
            if abs(percent) < 5: #cuttoff
                GPIO.output(self.negativePin,False)
                GPIO.output(self.positivePin,False)
            else:
                if percent > 0:
                    direction = self.positivePin
                    otherDir = self.negativePin
                else:
                    direction = self.negativePin
                    otherDir = self.positivePin
                
                GPIO.output(otherDir,False)
                GPIO.output(direction,True)
                time.sleep((timeQuantum/1000)*(percent/100))
                GPIO.output(direction,False)
                time.sleep((timeQuantum/1000)*(1-(percent/100)))

class FakeMotor:
    
    def __init__(self,env):
        self.MAXFORCE = 20
        self.env = env
        self.thrust = 0
        
    #simulate thrust change with a small delay
    def setThrust(self,thrust):
        if thrust > 100:
            self.thrust = 100
        elif thrust < -100:
            self.thrust = -100
        else:
            self.thrust = thrust
        self.env.verticalForce = self.thrust/100 * self.MAXFORCE
        
        
