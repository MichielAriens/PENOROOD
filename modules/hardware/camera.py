from imgproc import *
import time
import phase_corr

class Camera:
    cam = None
    
    __init__(self,size = 100):
        cam = Camera(size,size)

    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        image1 = cam.grabImage()
        time.sleep(interval/1000)
        image2 = cam.grabImage()
        corr = phase_corr.phase_correlation(image1, image2)
        return corr
        
        
        
        
    my_camera = Camera(100, 100)
    my_image = my_camera.grabImage()