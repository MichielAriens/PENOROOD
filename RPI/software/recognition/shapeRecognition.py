# personal reminder: http://www.societyofrobots.com/programming_computer_vision_tutorial_pt3.shtml#shape_detection

# template matching can find an input picture within a larger picture:
#   http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

# alternative method if blobs aren't working for 'live' pictures: contour method with opencv

from SimpleCV import Image

# Color values can easily be found by right clicking the picture and use color picker!  (in pycharm anyway)
from RPI.software.recognition import FindColorCode as fc


class ShapeFinder:
    def __init__(self):
        self.imagePath = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\7.jpg'
        self.calibrate = fc.ColorRange()
        self.whitey = (239,239,239)
        self.yellow = (236,187,120)
        self.red = (167,38,76)
        self.blue = (55,70,125)
        self.green = (62,80,75)

    # Load picture here
    def renewImage(self):
        return Image(self.imagePath)
        
    def setImage(self,path):
        self.imagePath = path

    # redefines the color codes, using HSV to scan for the 5 colors. Uses the image set for this object as a reference.
    def calibrateColors(self, brightness = "light"):
        w, y, r, g, b = self.calibrate.getColorRanges(self.imagePath, brightness)
        if(self.colorFound(w)):
            self.whitey = w
        if(self.colorFound(y)):
            self.yellow = y
        if(self.colorFound(r)):
            self.red = r
        if(self.colorFound(b)):
            self.blue = b
        if(self.colorFound(g)):
            self.green = g



    def colorFound(self,(a,b,c)):
        if(a == 0 and b == 0 and c == 0):
            return False
        else:
            return True

    # Highlight color (the input color should be case insensitive)
    def highlightColor(self,color=None):
        image = self.renewImage()  # Load picture from image path
        fig = None
        filteredFigure = None

        if color.lower() == "yellow":     # lower() makes sure the characters are not capitalized
            fig = image.colorDistance(self.yellow)
            filteredFigure = image - fig - fig - fig
        elif color.lower() == "red":
            fig = image.colorDistance(self.red)
            filteredFigure = image - fig - fig - fig
        elif color.lower() == "green":
            print self.green
            fig = image.colorDistance(self.green)
            filteredFigure = image - fig - fig - fig
        elif color.lower() == "blue":
            fig = image.colorDistance(self.blue)
            filteredFigure = image - fig - fig - fig
        elif color.lower() == "white":
            fig = image.colorDistance(self.whitey)
            filteredFigure = image - fig - fig
        else: print "Bad color input, this should never have happened!"

        # The contrast of the given color has been made stronger; this should ideally show only the figures with the color we want.
        # Play around with the amount of times you subtract fig (black is (0,0,0) though our chosen color is not completely black in fig, so
        # be careful not to subtract too much or everything becomes black). Keep doing this until everything but the figures we need are black.
        # Numbers below zero automatically become zero.
        # Deprecated: different colors need different amount of filtering.
        # filteredFigure = image - fig - fig

        """     # Test: If the selected color has a stronger contrast with the other colors than before, then it's working as intended
        filteredFigure.show()
        raw_input()
        """

        return filteredFigure

    # Value of the color can be found.
    def colorValue(self, filteredFigure):
        return filteredFigure.meanColor()

    def generalTest(self,color):
        filteredFig = self.highlightColor(color)
        blobs = filteredFig.findBlobs()

        filteredFig.show()
        raw_input()

        if blobs is not None:
            for blob in blobs:
                print blob.rectangleDistance()
                print blob.circleDistance()
                blob.draw()
                filteredFig.show()
                raw_input()

    # This method first parses the color, then parses the shape from the figure. It should find only figures
    # of the chose color and shape. It then returns a list of the coordinates of these figures.
    def locateFigures(self,color=None,shape=None):
        filteredFig = self.highlightColor(color)

        # Contains figures of the chosen color
        blobs = filteredFig.findBlobs()  # findBlobs() function easily finds lightly colored blobs on a dark background

        #self.testFoundColor(blobs,filteredFig)    # Use this method to test if the figures from the given color are correct

        width, height = filteredFig.size()
        newblobs = self.removeEdges(blobs,width,height)

        # Contains figures of the chosen shape (and color)
        shapes = self.findShapes(shape,newblobs)

        #self.testFoundShape(shapes,filteredFig)  # Use this method to test if the figures from the given shape are correct

        coordinates = self.findCoordinates(shapes,width,height)

        return coordinates


    # Tests whether the figures correspond to the given color or not by displaying the current results.
    def testFoundColor(self,blobs=None,filteredFig = None):
        if blobs is not None:
            for blob in blobs:
                blob.draw()
                print blob

                rectangleDistance = blob.rectangleDistance()
                if (rectangleDistance < 0.07): print "rectangle"
                else:
                    circleDistance = blob.circleDistance()
                    if (circleDistance < 0.18 and rectangleDistance < 0.185): print "circle"
                    elif (circleDistance < 0.23 and rectangleDistance > 0.21): print "star"
                    else: print "heart"

                filteredFig.show()
                raw_input()

    # filter edges that are within 5% margin of the edges (to ensure we scan complete figures)
    def removeEdges(self,blobs=None,width=None,height=None,percentageRemoval = 5):
        leftedge = percentageRemoval*width/100
        rightedge = width - leftedge
        upperedge = percentageRemoval*height/100
        bottomedge = height - upperedge
        newblobs = []
        if blobs is not None:
            for b in blobs:
                bw, bh = b.centroid()   # bw = blobwidth ; bh = blob height
                if(bw > leftedge and bw < rightedge and bh > upperedge and bh < bottomedge):
                    newblobs.append(b)
        return newblobs

    # Returns all the figures with the specified shapes. This should only apply to the figures of the chosen color.
    def findShapes(self,shape=None,blobs=None):
        lst = []

        if shape.lower() == "rectangle":
            rectangleTolerance = 0.07
            lst = [b for b in blobs if b.isRectangle(rectangleTolerance)]  # find all the rectangles within a certain tolerance
        elif shape.lower() == "circle":     # lower() makes sure the characters are not capitalized
            circleTolerance = 0.18
            lst = [b for b in blobs if (b.isCircle(circleTolerance) and b.rectangleDistance() < 0.185)]  # find all the circles within a certain tolerance
        elif shape.lower() == "star":
            starTolerance = 0.23
            lst = [b for b in blobs if (b.isCircle(starTolerance) and b.rectangleDistance() > 0.205)]
        elif shape.lower() == "heart":
            lst = [b for b in blobs if (b.circleDistance > 0.21 and b.rectangleDistance() < 0.205)]
        else: print "Bad shape input, this should never have happened!"

        return lst

    # Tests whether the figures correspond to the given shape or not by displaying the current results.
    def testFoundShape(self,shapes=None,filteredFig=None):
        if shapes is not None:
            for shape in shapes:
                shape.draw()
                print shape
                filteredFig.show()
                raw_input()

    # Finds the coordinates of the shapes and returns them in a list (of tuples)
    def findCoordinates(self,shapes=None,width=0,height=0):
        # use append, not extend
        coordinates = []

        if shapes is not None:
            for shape in shapes:
                coord = self.findCoordinate(shape,width,height)
                coordinates.append(coord)

        return coordinates
    
    def findCoordinate(self,shape=None,width=0,height=0):
        blobwidth, blobheight = shape.centroid()
        xcoor = blobwidth - (width / 2)
        ycoor = blobheight - (height / 2)
        return (xcoor,ycoor)



# This class offers the color, shape and coordinates of all figures found on a picture
class Analyzer:
    
    def __init__(self, shape = ShapeFinder()):
        self.shape = shape
    
    def analyze(self,path = None):
        if(path != None):
            self.shape.setImage(path)

        allfigures = []
        
        filteredFig = self.shape.highlightColor("white")
        allfigures.extend(self.colorshape(filteredFig,"white"))
        
        filteredFig = self.shape.highlightColor("blue")
        allfigures.extend(self.colorshape(filteredFig,"blue"))
        
        filteredFig = self.shape.highlightColor("red")
        allfigures.extend(self.colorshape(filteredFig,"red"))
        
        filteredFig = self.shape.highlightColor("green")
        allfigures.extend(self.colorshape(filteredFig,"green"))
        
        filteredFig = self.shape.highlightColor("yellow")
        allfigures.extend(self.colorshape(filteredFig,"yellow"))
        
        return allfigures
        
        
    def colorshape(self,filteredFig=None,color=None):
        oldBlobs = filteredFig.findBlobs()

        # removes a certain percentage of the edges
        width, height = filteredFig.size()
        blobs = self.shape.removeEdges(oldBlobs,width,height)   # put the percentage to remove behind height; 5% off all edges by default

        colorshapes = []
        
        width, height = filteredFig.size()
        
        if blobs is not None:   
            for blob in blobs:
                rectangleDistance = blob.rectangleDistance()
                if (rectangleDistance < 0.07):
                    x,y = self.shape.findCoordinate(blob,width,height)
                    colorshapes.append((color,"rectangle",x,y))
                else:
                    circleDistance = blob.circleDistance()
                    if (circleDistance < 0.18 and rectangleDistance < 0.185):
                        x,y = self.shape.findCoordinate(blob,width,height)
                        colorshapes.append((color,"circle",x,y))
                    elif (circleDistance < 0.23 and rectangleDistance > 0.205):
                        x,y = self.shape.findCoordinate(blob,width,height)
                        colorshapes.append((color,"star",x,y))
                    else:
                        x,y = self.shape.findCoordinate(blob,width,height)
                        colorshapes.append((color,"heart",x,y))
                    
        return colorshapes