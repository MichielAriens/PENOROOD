import time
import RPI.grid as grid

myGrid = grid.GRID(8,7)
myGrid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")
while True:
    #with picamera.PiCamera() as camera:
    #    camera.resolution = (res,res)
    #    camera.capture(path, "jpeg")
        
    starttime = time.time()
    #found = sf.analyze(path)
    
    found = [("blue","star",1,1),("green","heart",1,1),("red","heart",3,4)]
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