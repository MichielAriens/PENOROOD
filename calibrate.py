import RPI.software.recognition.main as imp
import picamera

path = "/home/pi/zep2/output/path.jpg"
res = 250

with picamera.PiCamera() as camera:
        camera.resolution = (res,res)
        camera.capture(path, "jpeg")

c = imp.main()

c.setImage(path)

print "blue  : " + str(c.shape.blue)
print "green : " + str(c.shape.green)
print "red   : " + str(c.shape.red)
print "white : " + str(c.shape.white)
print "yellow: " + str(c.shape.yellow)
print "---"

c.calibrate()

print "blue  : " + str(c.shape.blue)
print "green : " + str(c.shape.green)
print "red   : " + str(c.shape.red)
print "white : " + str(c.shape.white)
print "yellow: " + str(c.shape.yellow)