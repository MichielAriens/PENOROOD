import time

import RPI.software.recognition.shapeRecognition as sr

with picamera.PiCamera() as camera:
        camera.resolution = (res,res)
        camera.capture(path, "jpeg")

class Camera:
    def __init__(self):
        self.res= 250
        self.shape = sr.ShapeFinder()
        self.path = "/home/pi/zep2/output/path.jpg"
        self.shape.setImage(path)
        self.sf = sr.Analyzer(self.shape)
    
    #f = open('/home/pi/zep2/output/results.csv','w')
    #f.write('hi there\n') # python will convert \n to os.linesep
    
    def analyzePosition(self,grid):
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
        return pos
            
    
    
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
