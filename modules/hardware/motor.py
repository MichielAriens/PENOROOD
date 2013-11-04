import time
import thread
try:
    import RPi.GPIO as GPIO
except:
    pass

class VectoredMotor:
    def __init__(self,thrustPin,postivePin,negativePin):
        #Instantiate pin objects
        #--Placeholder--
        self.thrustPin = GPIO.PWM(12, 50)
        self.thrustPin.changeDutyCycle(0.0)
        self.positivePin = postivePin
        self.negativePin = negativePin
        self.thrust = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.postivePin,GPIO.OUT)
        GPIO.setup(self.negativePin,GPIO.OUT)
        GPIO.output(self.postivePin,True)
        GPIO.output(self.negativePin,False)
            
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
            GPIO.output(self.postivePin,False)
            GPIO.output(self.negativePin,True)
        else:
            GPIO.output(self.postivePin,True)
            GPIO.output(self.negativePin,False)
        self.thrustPin.changeDutyCycle(self.thrust)


class PulsedMotor:
    def __init__(self,thrustPin,postivePin,negativePin):
        #Instantiate pin objects
        #--Placeholder--
        self.thrustPin = thrustPin 
        self.positivePin = postivePin
        self.negativePin = negativePin
        self.thrust = 0
        self.thrustControlThread = None
        
    def setThrust(self,nThrust):
        self.thrust = nThrust
        self._actuate()
        
    def _actuate(self):
        if(self.thrust < 0):
            pass#TODO Setup directional pins accordingly.
        else:
            pass#TODO Setup directional pins accordingly.
        if self.thrustControlThread != None:
            self.thrustControlThread.exit()
        self.thrustControlThread = thread.start_new(self.pulse, (1000,abs(self.thrust)))
        
    #Endless loop to control the motors. TimeQuantum decides how fine grained the loop is. The proper value should be found experimentally
    #percent defines the percent of time that the motor should give 100% of its power.
    def pulse(self,timeQuantum,percent):
        while(True):
            #TODO Set motor to run at 100% power
            time.sleep((timeQuantum/1000)*(percent/100))
            #TODO Turn off the motor
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
        
        
