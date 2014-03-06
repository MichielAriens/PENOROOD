#import picamera
import time
import RPI.software.shapeRecognition as sr

#sf = sr.Analyzer()
#path = "/home/pi/zep2/output/data.jpg"

#f = open('/home/pi/zep2/output/results.csv','w')
#f.write('hi there\n') # python will convert \n to os.linesep

def analyze():
    global sf,path
    #with picamera.PiCamera() as camera:
    #    camera.resolution = (500,500)
    #    camera.capture(path, "jpeg")
        
    found = sf.analyze()#path)
    print str(found)
    return found
    
    
#import RPI.grid
#grid =  RPI.grid.Grid()
    
#while(true):
#    listOfShapes = analyze()
#    for (shape,colour,x,y) in listOfShapes:
        
