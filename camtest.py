#import RPI.hardware.camera as cam

#camera = cam.Camera(500,"/home/pi/zep2/output.jpg")
#camera.update()
#camera.camera.close()

import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (250,250)
    i = 0
    while (i < 20):
        print "taking pic " + str(i)
        camera.capture("/home/pi/zep3/PENOROOD/output/" + str(i) + ".jpg", "jpeg")
        i += 1
        time.sleep(1)
