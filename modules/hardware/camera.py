
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os
import thread
import time

class Camera:    
    def __init__(self,height = 200, width = 200, output = "still.jpg", root = "data/cam/", readroot = "images/"):
        self.height = width
        self.width = width      
        self.output = output  
        self.root = root
        self.readroot = readroot
    
    
    #launches repeating 
    def click(self):
        #command = "raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -q 5 -o " + self.root + self.output + " -t 9999999 -th 0:0:0 -tl 100 -n &"
        command = "raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -o " + self.root + self.output + " -t 0.001 -n"
        print "trying: " + command
        os.system(command)
        timestamp = time.time()
        tsfile = open(self.root + "TIMESTAMP",'w')
        tsfile.write(str(timestamp))
        tsfile.close()
        
    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        pass #os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
        
    def getQR(self):
        os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
