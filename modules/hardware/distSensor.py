#Distance Sensor
#
#This file contains two similar classes, one which actively controls the distance sensor and one which
#emulates a distance sensor using empirical data for testing purposes.
#Although not explicitly defined, both classes have the exact same methods. Implementing code should
#see no difference between the opperation of these classes.

import time
try:
    import numpy
except ImportError:
    pass
import random
import thread


try:
    import RPi.GPIO as GPIO
except ImportError:
    print "GPIO pins not imported."
    

class FakeDistanceSensor2:
    def __init__(self,env):
        self.env = env
        
    #Simulate a slightly less acurate reading that's not instantaneaous
    def getHeight(self):
        time.sleep(0.0010)
        return random.gauss(self.env.height, self.env.height/200)

#This class emulates a distance sensor based on real data.
class FakeDistanceSensor:
    data = None
    
    def __init__(self):
        global data
        try:
            data = open("./data/exp4-190cm.csv","r")
        except IOError:
            print "IOError happened :("
    
    def measure(self):
        string = data.readline()
        #cut off line delimiters and semicolons.
        string = string[:-3]
    
        return float(string)
        
    def getHeight(self, nopoints = 10):
        points = []
        triesleft = 2*nopoints
        while len(points) < nopoints and triesleft > 0:
            point = self.measure()
            if point == -1:
                triesleft -= 1
            else:         
                points.append(self.measure())
            
        if triesleft <= 0:
            return -1
        else:
            return numpy.median(points)

    def calibrate(self):
        return

    def getHeightRaw(self):
        return
            
    
    

class DistanceSensor :
    #setup pins: BCM noation. 17 means GPIO17, 4 means GPIO4
    echo_gpio = 27
    trig_gpio = 22
    TRIG_DURATION = 0.0001
    SPEED_OF_SOUND = 340.29
    TIMEOUT = 5000

    scalefactor = 0
    offset = 0
    
    #Constructor
    def __init__(self):   
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT, offset, scalefactor
        echo_gpio = 27
        trig_gpio = 22
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
        
        #initial calibration
        offset = 0
        scalefactor = 1
        
    
    #Returns the height of the sensor in meters applying calibration data. This value should be accurate.
    #This means: two consecutive invocations of the function should return close results.
    #This is implemented by calculating the median of (nopoints = 10) measurements. 
    #Returns -1 when measure function fails too often.
    def getHeight(self, nopoints = 20):
        global offset, scalefactor
        return self.getHeightRaw(10)
    
    #Returns the height of the sensor in meters NOT applying calibration data. This value should be accurate.
    #This means: two consecutive invocations of the function should return close results.
    #This is implemented by calculating the median of (nopoints = 10) measurements. 
    #Returns -1 when measure function fails too often.
    def getHeightRaw(self, nopoints):
        points = []
        triesleft = 2*nopoints
        while len(points) < nopoints and triesleft > 0:
            point = self.measure()
            if point == -1:
                triesleft -= 1
            else:         
                points.append(self.measure())
                #points.append(point)
            
        if triesleft <= 0:
            return -1
        else:
            return numpy.median(points)        
    
    #Calibration of the sensor. Calibration is linear. Allows two inputs: Point zero calibration translates the output. For other inputs
    #scaling is applied (not yet working)
    def calibrate(self, height=0):
        global offset, scalefactor
        if(height == 0):
            offset = -self.getHeightRaw(50)
        else:
            scalefactor = self.getHeightRaw(50)/height
    
    #Perform one instantaneous measurement (not accurate)
    #Timeout places bounds on the wait. If -1 is returned regularly consider increasing the timeout
    def measure(self, timeout = TIMEOUT):
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT
        #settletime
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
            # Distance pulse travelled in that time is time
            # multiplied by the speed of sound (cm/s)
            # That was the distance there and back so halve the value
            distance = (endtime - starttime) * SPEED_OF_SOUND * 100/2
            # sleep zinloos?
            time.sleep(endtime - starttime)
            
        return distance
   
            
class BackgroundDistanceSensor :
    #setup pins: BCM noation. 17 means GPIO17, 4 means GPIO4
    echo_gpio = 27
    trig_gpio = 22
    TRIG_DURATION = 0.0001
    SPEED_OF_SOUND = 340.29
    TIMEOUT = 5000

    scalefactor = 0
    offset = 0
    
    #Constructor
    def __init__(self,buffersize = 10, resolution = 0.1):   
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT, offset, scalefactor
        echo_gpio = 27
        trig_gpio = 22
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
        
        #initial calibration
        offset = 0
        scalefactor = 1
        
        thread.start_new(self.monitorHeight,(buffersize,resolution))
        
    def monitorHeight(self,buffersize, resolution):
        size = buffersize
        self.points = [0] * size        
        while True:
            height = self.measure()
            if (height != -1):
                self.points.pop(0)
                self.points.append(height)
            time.sleep(resolution)
            
            
    def getHeight(self):
        return numpy.median(self.points)
    
    #Perform one instantaneous measurement (not accurate)
    #Timeout places bounds on the wait. If -1 is returned regularly consider increasing the timeout
    def measure(self, timeout = TIMEOUT):
        global echo_gpio, trig_gpio, TRIG_DURATION, SPEED_OF_SOUND, TIMEOUT
        #settletime
        time.sleep(0.05)
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
            time.sleep(endtime - starttime)
            
        return distance
            
            
        
        
        
        
        
        
        
        
