
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os
import thread

class Camera:
    cam = None
    
    def __init__(self,height = 200, width = 200, output = "still.jpg", root = "modules/srv/images/", readroot = "images/"):
        self.height = width
        self.width = width      
        self.output = output  
        self.root = root
        self.readroot = readroot
        thread.start_new(self.start, ())
        return
    
    #deprecated
    def click(self):
        thread.start_new(self.takeImage, ())
        return self.readroot + self.output
    
    #launches repeating 
    def start(self):
        print "trying: " + "raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -q 5 -o " + self.root + self.output + " -t1 100 -t 9999999 -th 0:0:0 -n &"
        os.system("raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -q 5 -o " + self.root + self.output + " -t1 100 -t 9999999 -th 0:0:0 -n &")

    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        pass #os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
        
    def getQR(self):
        os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
