#!/usr/bin/env python

#numpy and scipy will need to be installed on the PI for some code to work.

#The top level zeppelin code. 

import distSensor
import camera

#testcode to check the distSensor code


def testDistSens():
    continuebool = True
    distSensor1 = distSensor.DistanceSensor()
    counter = 1
    
    
    while continuebool:
        height = distSensor1.getHeight()
        print str(counter) + ": " + str(height)
        counter += 1
        cont = raw_input("continue? ('n' to stop): ")
        if(cont == "n"):
            continuebool = False
            
def testCamera():
    continuebool = True
    cam = camera.Camera()
    while continuebool:
        print str(cam.detectMovement())
        cont = raw_input("continue? ('n' to stop): ")
        if cont == "n":
            continuebool = False
            
testCamera()
    
    
        
    
