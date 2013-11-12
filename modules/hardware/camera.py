from imgproc import *
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os

class Camera:
    cam = None
    
    def __init__(self,height = 200, width = 200, output):
        self.height = width
        self.width = width
        self.output= output
        
        return
    
    def click(self):
        os.system("raspistill -n -h" + self.height + " -w " + str(self.width)+ " -o " + self.output)

    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        pass #os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
        
    def getQR(self):
        os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")