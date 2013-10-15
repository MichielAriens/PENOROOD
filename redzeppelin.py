#!/usr/bin/env python

#The top level zeppelin code. 

import distSensor

#testcode to check the distSensor code

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
    
    
        
    