


import time
import picamera

sf = ShapeFinder()
path = "/home/pi/zep2/output/data.jpg"

def analyze(grid):
    global sf,path
    with picamera.PiCamera() as camera:
        camera.resolution = (500,500)
        camera.capture(path, "jpeg")
        
    found = sf.findAll(path)
    try:
        return grid.calculatePositionFromShapes(found[0], found[1], found[2])
    except (IndexError):
        return none
