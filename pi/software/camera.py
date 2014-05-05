import picamera

class camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.configureResolution()

    def configureResolution(self, res = 250):
        self.camera.resolution(res,res)

    def captureImage(self, path = "/home/pi/zep2/output/path.jpg"):
        self.camera.capture(path, "jpeg")
        return path

