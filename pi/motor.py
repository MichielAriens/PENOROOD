import time
import thread
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)                      # choose BCM or BOARD 
except:
    pass

        
#A physical implementation of a motor. Uses PWM (variable output pins) to drive motors
#Provides best control. Useful for most critical motors like the lifter.
class PWMMotor:
    def __init__(self,positivePin,negativePin):
        #Instantiate pin objects
        
        GPIO.setup(18, GPIO.OUT)                    # set a port/pin (18) as an output 
        self.thrustPin = GPIO.PWM(18, 50)           # create an object thrustPin for PWM on port 18 at 50 Hertz (maximum 1k Hz I think)
        self.positivePin = positivePin
        self.negativePin = negativePin
        self.thrust = 0
        
        GPIO.setup(self.positivePin,GPIO.OUT)
        GPIO.setup(self.negativePin,GPIO.OUT)
        GPIO.output(self.positivePin,True)          # set port/pin value to 1/GPIO.HIGH/True  
        GPIO.output(self.negativePin,False)         # set port/pin value to 0/GPIO.LOW/False  
        
        self.thrustPin.start(0.0)                    # start the PWM on 0 percent duty cycle
                                                     # explanation duty cycles: http://raspi.tv/2013/rpi-gpio-0-5-2a-now-has-software-pwm-how-to-use-it
                                                     # may vary from 0 to 100 (obviously)
            
    def setThrust(self,nThrust):
        if(nThrust > 100):
            self.thrust = 100.0
        elif(nThrust < -100):
            self.thrust = -100.0
        else:
            self.thrust = nThrust
        self._actuate()

    def getThrust(self):
        return self.thrust
        
    def _actuate(self):
        #decide direction
        if(self.thrust < 0):
            GPIO.output(self.positivePin,False)
            GPIO.output(self.negativePin,True)
        else:
            GPIO.output(self.positivePin,True)
            GPIO.output(self.negativePin,False)
            
        #decide power of thrust
        self.thrustPin.ChangeDutyCycle(abs(self.thrust))

#A pysical implementation of a motor. Uses fixed pins but still provides a way to pass real numbers to setThrust()
#Runs a thread in the background and runs the motors on max power for abs(thrust) percent of the time.
#Cool note: PWM works on the exact same principle!
class PulsedMotor:
    def __init__(self,postivePin,negativePin):
        #Instantiate pin objects

        self.positivePin = postivePin
        self.negativePin = negativePin
        
        GPIO.setup(self.positivePin,GPIO.OUT)
        GPIO.setup(self.negativePin,GPIO.OUT)
        GPIO.output(self.positivePin,False)
        GPIO.output(self.negativePin,False)
        self.thrust = 0
        
        thread.start_new(self.pulse, (100,1))
        
    def setThrust(self,nThrust):
        if(nThrust > 100):
            self.thrust = 100.0
        elif(nThrust < -100):
            self.thrust = -100.0
        else:
            self.thrust = nThrust

    def getThrust(self):
        return self.thrust
        
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
                time.sleep((timeQuantum/1000)*(abs(percent)/100))
                GPIO.output(direction,False)
                time.sleep((timeQuantum/1000)*(1-(abs(percent)/100)))

class FakeMotor:
    
    def __init__(self,env,axis):
        self.MAXFORCE = 20
        self.env = env
        self.axis = axis
        self.thrust = 0
        
    def setThrust(self,thrust):
        if thrust > 100:
            self.thrust = 100
        elif thrust < -100:
            self.thrust = -100
        else:
            self.thrust = thrust
        self.env.force.setAxis(self.axis,self.thrust/100 * self.MAXFORCE)
        
        
        
        