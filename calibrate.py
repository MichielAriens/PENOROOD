import RPI.software.recognition.main as imp

path = "/home/pi/zep2/output/path.jpg"


with picamera.PiCamera() as camera:
        camera.resolution = (res,res)
        camera.capture(path, "jpeg")

c = imp.main

c.setImage(path)

c.calibrate()

print str(c.analyze())