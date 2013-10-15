#Distance Sensor
#import time
#import RPi.GPIO as GPIO 

class FakeDistanceSensor:
    data = None
    
    def __init__(self):
        global data
        try:
            data = open("data/exp3-73cm.csv","r")
        except IOError:
            print "IOError happened :("
    
    def measure(self):
        string = data.readline()
        string = string[0:7]
    
        return float(string)
        
    def getHeight(self):
        return self.measure()
    
    
"""
class DistanceSensor :
    #setup pins: BCM noation. 17 means GPIO17, 4 means GPIO4
    echo_gpio = 17
    trig_gpio = 4
    TRIG_DURATION = 0.0001
    SPEED_OF_SOUND = 340.29
    TIMEOUT = 5000
    
    def __init__(self):   
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT
        echo_gpio = 17
        trig_gpio = 4
        TRIG_DURATION = 0.0001
        SPEED_OF_SOUND = 340.29
        TIMEOUT = 2100
        #Init GPIO
        #Adressingmode
        GPIO.setmode(GPIO.BCM)
        #Bind pins
        GPIO.setup(echo_gpio,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(trig_gpio,GPIO.OUT)
        GPIO.output(trig_gpio,False)
        time.sleep(0.5)
        
    
    #Returns the height of the sensor in meters. This value should be accurate.
    #This means: two consecutive invocations of the function should return close results.
    def getHeigth(self):
        return
    
    #Perform one instantaneous measurement (not accurate)
    #Timeout places bounds on the wait. If -1 is returned regularly consider increasing the timeout
    def measure(self, timeout = TIMEOUT):
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT
        GPIO.output(trig_gpio, True)
        time.sleep(TRIG_DURATION)
        GPIO.output(trig_gpio, False)
        
        countdown = timeout
        while(GPIO.input(echo_gpio) == 0 and countdown > 0):
            countdown -= 1
        
        distance= -1
        starttime = -1
        endtime = -1
        if countdown > 0:
            starttime = time.time()
            countdown = timeout
            while(GPIO.input(echo_gpio) == 1 and countdown > 0):
                countdown -=1
            
            if(countdown > 0):
                endtime =time.time()
            
        if(starttime != -1 and endtime != -1):
            distance = (endtime - starttime) * SPEED_OF_SOUND * 100/2
            
        return distance
 """   
            
            
            
            
        
        
        
        
        
        
        
        