


import time
import picamera

global sf = ShapeFinder()
global path = "/home/pi/zep2/output/data.jpg"

def analyze():
    global sf,path
    with picamera.PiCamera() as camera:
        camera.resolution = (500,500)
        camera.capture(path, "jpeg")
        
    sf.findAll(path)
