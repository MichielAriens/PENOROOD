#!/usr/bin/env python

#The top level zeppelin code. 

import distSensor

#testcode to check the distSensor code

continuebool = True
distSensor = distSensor.DistanceSensor()


while continuebool:
    height = distSensor.getHeight()
    print height
    cont = raw_input("continue? ('n' to stop): ")
    if(cont == "n"):
        continuebool = False
    
    
        