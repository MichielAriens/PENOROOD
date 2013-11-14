
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os

class Camera:
    cam = None
    
    def __init__(self,height = 200, width = 200, output = "still.jpg", root = "modules/srv/images/", readroot = "images/"):
        self.height = width
        self.width = width      
        self.output = output  
        self.root = root
        self.readroot = readroot
        return
    
    def click(self):
        os.system("raspistill -n -h" + str(self.height) + " -w " + str(self.width)+ " -o " + self.root + self.output)
        return self.readroot + self.output

    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        pass #os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
        
    def getQR(self):
        os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")