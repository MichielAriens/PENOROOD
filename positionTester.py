import time

import RPI.software.recognition.shapeRecognition as sr


res = 250

shape = sr.ShapeFinder()
path = "/home/pi/zep2/output/path.jpg"
shape.setImage(path)
raw_input("ready to calibrate")
with picamera.PiCamera() as camera:
    camera.resolution = (res,res)
    camera.capture(path, "jpeg")
print "pic taken"
shape.calibrateColors()
sf = sr.Analyzer(shape)



#f = open('/home/pi/zep2/output/results.csv','w')
#f.write('hi there\n') # python will convert \n to os.linesep

def analyzePosition():
    global sf,path,res,grid
    myGrid = grid.initiateFromFile('/home/pi/zep2/OTHER/grid.csv')
    #myGrid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")
    with picamera.PiCamera() as camera:
        camera.resolution = (res,res)
        camera.capture(path, "jpeg")
    while True:
        with picamera.PiCamera() as camera:
            camera.resolution = (res,res)
            camera.capture(path, "jpeg")
            
        starttime = time.time()
        found = sf.analyze(path)    # found is a list of (color, shape, xcoordinate, ycoordinate)
        print str(time.time() - starttime)
        print str(found)

        # vals is a list of ('shape/color value', xcoordinate, ycoordinate)
        vals = [(myGrid.getShapeID(color[0] + "" +  shape[0]),x,y) for (color,shape,x,y) in found]
        pos = myGrid.calculatePositionFromShapesFlexible(vals)
        print "found " + str(pos)
        
       
           
analyzePosition()


"""
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
