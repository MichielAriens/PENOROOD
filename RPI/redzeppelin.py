
#!/usr/bin/env python
import RPI.hardware.distSensor as Ids
import os
import thread
import time

#Zeppelin class.
class Zeppelin:
    def __init__(self, simMode = "RPi", dist = None):
        dsr = Ids.DistanceReader(location = dist)
        self.llc = llcp.LowLevelController(simMode, dists = dsr)

#Check to see whether we're running on the RaspberryPi. store result in simMode
simMode = "RPi"
try:
    import RPi.GPIO as GPIO
except ImportError:
    simMode = "sim"
    print "running in simulation mode."
    
    
os.system("rm data/ds/data")
filelocation = "data/ds/data"
pid = os.fork()
if pid == 0:
    #This is the child process
    os.nice(-1)
    print "Distsence on: " + str(os.getpid()) + " | priority: " + str(os.nice(0))
    dist = Ids.PriorityDistanceSensor(location = filelocation)
    #safety lock
    while(True):
        print "Line 33 passed by child = fatal!!!!!"
        time.sleep(1000)

#else this is the parent
else:
    print "main on: " + str(os.getpid()) + " | priority: " + str(os.nice(0))
    zeppelin = Zeppelin(simMode, dist = filelocation)
    #########################
    ####Initiate zeppelin####
    #########################



