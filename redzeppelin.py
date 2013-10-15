#!/usr/bin/env python

#numpy and scipy will need to be installed on the PI for some code to work.

#The top level zeppelin code. 

import distSensor

#testcode to check the distSensor code


def testDistSens():
    continuebool = True
    distSensor = distSensor.FakeDistanceSensor()
    counter = 1
    
    
    while continuebool:
        height = distSensor.getHeight()
        print str(counter) + ": " + str(height)
        counter += 1
        cont = raw_input("continue? ('n' to stop): ")
        if(cont == "n"):
            continuebool = False
            
testDistSens()
    
    
        
    