import picamera
import time

sf = ShapeFinder()
path = "/home/pi/zep2/output/data.jpg"

f = open('/home/pi/zep2/output/results.csv','w')
f.write('hi there\n') # python will convert \n to os.linesep
f.close()

def analyze():
    global sf,path
    with picamera.PiCamera() as camera:
        camera.resolution = (500,500)
        camera.capture(path, "jpeg")
        
    sf.findAll(path)
    
    
    
import RPI.grid
grid =  RPI.grid.Grid()
    
while(true):
    listOfShapes = analyze()
    for (shape,colour,x,y) in listOfShapes:
        
