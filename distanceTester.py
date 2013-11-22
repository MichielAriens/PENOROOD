#Distance Sensor
#
#This file contains two similar classes, one which actively controls the distance sensor and one which
#emulates a distance sensor using empirical data for testing purposes.
#Although not explicitly defined, both classes have the exact same methods. Implementing code should
#see no difference between the operation of these classes.

#test

import time
try:
    import numpy
except ImportError:
    pass
import random
import thread
from threading import Semaphore


try:
    import RPi.GPIO as GPIO
except ImportError:
    print "GPIO pins not imported."


class DistanceSensor :
    #setup pins: BCM noation. 17 means GPIO17, 4 means GPIO4
    TRIG_DURATION = 0.00001
    SPEED_OF_SOUND = 340.29
    TIMEOUT = 8000
    TIMEOUT_SEMAPHORE = 1
    UNLOCK_CPU_TIME = 0
    TIME_BETWEEN_MEASUREMENTS = 0.01

    scalefactor = 1
    offset = 0
    
    #Constructor
    def __init__(self):   
        global echo_gpio, trig_gpio
        #Init GPIO
        echo_gpio = 27
    	trig_gpio = 22
        #Adressingmode
        GPIO.setmode(GPIO.BCM)
        #Bind pins
        GPIO.setup(echo_gpio,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(trig_gpio,GPIO.OUT)
        GPIO.output(trig_gpio,False)
        time.sleep(0.5)
        
        #initial calibration
        self.previousPoint = -1
        
    
    #Returns the height of the sensor in meters applying calibration data. This value should be accurate.
    #This means: two consecutive invocations of the function should return close results.
    #This is implemented by calculating the median of (nopoints = 10) measurements. 
    #Returns -1 when measure function fails too often.
    def getHeight(self, amountPoints = 20):
        return self.simpleTestHeight()

    # Use 'self.measureWithSemaphores()' instead of self.measure() to use semaphores

    # Test #1: literally prints the measurements without any modifications
    #          one measurement per function call
    def simpleTestHeight(self):
        file = open('/home/pi/distanceTesting.csv', 'r+')
        while(True):
            distance = self.measure()
            # give other threads a chance to use the cpu
            file.write(distance)
            file.write('\n')

    # Test #2: calculates the distance x times and returns the median
    def secondTestHeight(self):
        # amount of times to measure the distance
        counter = 5
        distancePoints = []
        while(counter > 0):
            distance = self.measure()
            if distance != -1:
                distancePoints.append(distance)
            counter -= 1
        # if somehow all the measurements have failed, then 0 will be returned
        if(len(distancePoints) > 0):
            medianDistances = numpy.median(distancePoints)
        else:
            medianDistances = 0
        # give other threads more chances to use the cpu
        # lower the sleep if you need more measurements per second
        time.sleep(self.UNLOCK_CPU_TIME)
        return medianDistances

    # Measure distance, using a semaphore to give the measurement full priority.
    def measureWithSemaphore(self):
        global echo_gpio, trig_gpio
        GPIO.output(trig_gpio, True)
        time.sleep(self.TRIG_DURATION)
        GPIO.output(trig_gpio, False)

        distance = -1
        semaphore = Semaphore()

        # Purpose of loop: ability to break at any time
        while(True):
            # Note: if this doesn't work, try assuming there's always a signal and cpu is always ready
            #       so remove the need to check for end and start times

            # START SEMAPHORE HERE
            semaphore.acquire()

            start = time.time()
            end = time.time()
            timeDifference = end - start
            while(GPIO.input(echo_gpio) == 0 and timeDifference < self.TIMEOUT_SEMAPHORE):
                end = time.time()
                timeDifference = end - start

            if(timeDifference >= self.TIMEOUT_SEMAPHORE):
                # END SEMAPHORE HERE
                semaphore.release()
                break

            start = time.time()
            end = time.time()
            timeDifference = end - start
            while(GPIO.input(echo_gpio) == 1 and timeDifference < self.TIMEOUT_SEMAPHORE):
                end = time.time()
                timeDifference = end - start

            # END SEMAPHORE HERE
            semaphore.release()

            if(timeDifference >= self.TIMEOUT_SEMAPHORE):
                break

            # Distance pulse travelled in that time is equal to time
            # multiplied by the speed of sound * 100 (cm/s)
            # That was the distance forth and back, so halve the value
            distance = timeDifference * self.SPEED_OF_SOUND * 100/2
            break
        # wait before retriggering
        time.sleep(self.TIME_BETWEEN_MEASUREMENTS)
        return distance
    
    #Returns the height of the sensor in meters NOT applying calibration data. This value should be accurate.
    #This means: two consecutive invocations of the function should return close results.
    #This is implemented by calculating the median of (nopoints = 10) measurements. 
    #Returns -1 when measure function fails too often.
    def getHeightRaw(self, amountPoints):
        counter = 5
        while(counter > 0):
            points = []
            medianPoints = []
            triesleft = 2*amountPoints
            while len(points) < amountPoints and triesleft > 0:
                point = self.measure()
                if point == -1:
                    triesleft -= 1
                else:         
                    points.append(point)
                
            if triesleft <= 0:
                return -1
            else:
                medianPoint = numpy.median(points)
                if abs(medianPoint - self.previousPoint) <= 20:
                    self.previousPoint = medianPoint
                    return self.previousPoint
                else:
                    medianPoints.append(medianPoint)
                    counter -= 1
        #alternative: 
        self.previousPoint = min(medianPoints)
        return self.previousPoint
        #self.previousPoint = medianPoint
        #return medianPoint
        
        
            
    
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
    def measure(self):
        global echo_gpio, trig_gpio
        GPIO.output(trig_gpio, True)
        time.sleep(self.TRIG_DURATION)
        GPIO.output(trig_gpio, False)
        
        countdown = self.TIMEOUT
        while(GPIO.input(echo_gpio) == 0 and countdown > 0):
            countdown -= 1
        
        distance= -1
        starttime = -1
        endtime = -1
        if countdown > 0:
            starttime = time.time()
            countdown = self.TIMEOUT
            while(GPIO.input(echo_gpio) == 1 and countdown > 0):
                countdown -=1
            
            if(countdown > 0):
                endtime =time.time()
            
        if(starttime != -1 and endtime != -1):
            # Distance pulse travelled in that time is time
            # multiplied by the speed of sound (cm/s)
            # That was the distance there and back so halve the value
            distance = (endtime - starttime) * self.SPEED_OF_SOUND * 100/2
            # Voer een sleep in, in functie van de hoogte, te bepalen door experimenten
            #time.sleep(endtime - starttime)
        # wait before retriggering
        time.sleep(self.TIME_BETWEEN_MEASUREMENTS)
        return distance

    getHeight()