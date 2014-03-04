
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os
import thread
import time
import subprocess

import picamera

class Camera:
    def __init__(self,resolution,path):
        self.res = res;
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.res, self.res)
        self.path = path
        
    def update(self):
        camera.capture(path,'jpeg')

