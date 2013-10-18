#!/usr/bin/env python

#numpy and scipy will need to be installed on the PI for some code to work.

#The top level zeppelin code. 

import distSensor
import camera

#testcode to check the distSensor code


def testDistSens():
    continuebool = True
    distSensor1 = distSensor.DistanceSensor()

    print "commands: \n q: quit \n m:measure \n c: calibrate"
    
    
    while continuebool:
        command = raw_input("> ")
        if(command == "q"):
            continuebool = False
        else if(command = "c"):
            command = raw_input("Set height: ")
            distSensor1.calibrate(float(command))
        else:
            height = distSensor1.getHeight()
            print str(counter) + ": " + str(height)
            
def testCamera():
    continuebool = True
    cam = camera.Camera()
    while continuebool:
        print str(cam.detectMovement())
        cont = raw_input("continue? ('n' to stop): ")
        if cont == "n":
            continuebool = False
            
testDistSens()
    
    
        
    
