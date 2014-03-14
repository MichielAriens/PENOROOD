import picamera
import time
import RPI.software.shapeRecognition as sr
import RPI.grid as grid



sf = sr.Analyzer()
path = "/home/pi/zep2/output/path.jpg"
res = 250

#f = open('/home/pi/zep2/output/results.csv','w')
#f.write('hi there\n') # python will convert \n to os.linesep


def analyze():
    global sf,path,res
    print "ready"
    while True:
        raw_input("")
        with picamera.PiCamera() as camera:
            camera.resolution = (res,res)
            camera.capture(path, "jpeg")
            
        starttime = time.time()
        found = sf.analyze(path)
        print str(time.time() - starttime)
        print str(found)
    return found

"""
def takePics():
    global res
    path = "/home/pi/zep2/output/"
    i = 0
    while i < 20:
        print str(i)
        with picamera.PiCamera() as camera:
            camera.resolution = (res,res)
            camera.capture(path + str(i) + ".jpg", "jpeg")
            
        raw_input("go?")
        print "gone!"
        i += 1
    return found
"""
"""

def analyzePosition():
    global sf,path,res,grid
    #myGrid = grid.Grid(8,7)
    #myGrid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")
    with picamera.PiCamera() as camera:
        camera.resolution = (res,res)
        camera.capture(path, "jpeg")
    while True:
        print str(i)
        with picamera.PiCamera() as camera:
            camera.resolution = (res,res)
            camera.capture(path, "jpeg")
            
        starttime = time.time()
        found = sf.analyze(path)
        print str(time.time() - starttime)
        print str(found)
        
        
        if len(found) < 3:
            print "Not enough shapes found for analysis"
        elif len(found) == 3:
            vals = [myGrid.getShapeID(x[0] + y[0]) for (x,y,z,k) in found]
            pos = myGrid.calculatePositionFromShapes(vals[0],vals[1],vals[2])
            print "found " + str(pos)
        else:
            vals = [(a,b,x^2 + y^2) for (a,b,x,y) in found]
            vals = sorted(vals, key=lambda tup: tup[2])
            vals = vals[0:2]
            vals = [myGrid.getShapeID(x[0] + y[0]) for (x,y,z) in vals]
            pos = myGrid.calculatePositionFromShapes(vals[0],vals[1],vals[2])
            print "found " + str(pos)
            """
            
#takePics()
analyze()
 

 
    
#import RPI.grid
#grid =  RPI.grid.Grid()
    
#while(True):
#    listOfShapes = analyze()
#    for (shape,colour,x,y) in listOfShapes:
        
