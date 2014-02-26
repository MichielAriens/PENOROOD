# look into SimpleCV.Features.Blob -> can determine left/right/above/below positioning between two shapes

# template matching can find an input picture within a larger picture:
#   http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

# help('modules')

from SimpleCV import Color, Image

class ShapeFinder:
    def __init__(self):
        self.imagePath = 'C:\Users\Babyburger\Desktop\cshapes.jpg'

    # Load picture here
    def renewImage(self):
        return Image(self.imagePath)

    # Highlight color (the input color should be case insensitive)
    def highlightColor(self,color=None):
        image = self.renewImage()  # Load picture from image path
        fig = None

        if color.lower() == "yellow":     # lower() makes sure the characters are not capitalized
            fig = image.colorDistance(Color.YELLOW)
        elif color.lower() == "red":
            fig = image.colorDistance(Color.RED)
        elif color.lower() == "green":
            fig = image.colorDistance(Color.GREEN)
        elif color.lower() == "blue":
            fig = image.colorDistance(Color.BLUE)
        elif color.lower() == "white":
            fig = image.colorDistance(Color.WHITE)
        else: print "Bad color input, this should never have happened!"

        """     # If the selected color is colored black, then it's working as intended
        fig.show()
        raw_input()
        """

        # The contrast of the yellow color has been made stronger.
        filteredFigure = image - fig

        """     # If the selected color has a stronger contrast with the other colors than before, then it's working as intended
        filteredFigure.show()
        raw_input()
        """

        return filteredFigure

    # Value of the color can be found.
    def colorValue(self, filteredFigure):
        return filteredFigure.meanColor()

    # This method first parses the color, then parses the shape from the figure. It should return only figures
    # of the chose color and shape.
    def locateFigures(self,color=None,shape=None):
        filteredFig = self.highlightColor(color)

        # Contains figures of the chosen color
        blobs = filteredFig.findBlobs()

        # self.testFoundColor(blobs,filteredFig)    # Use this method to test if the figures from the given color are correct

        # Contains figures of the chosen shape (and color)
        shapes = self.findShapes(shape,blobs,filteredFig)

        self.testFoundShape(shapes,filteredFig)  # Use this method to test if the figures from the given shape are correct

    def testFoundColor(self,blobs=None,filteredFig = None):
        for blob in blobs:
            blob.draw()
            print blob
            if (blob.isCircle(0.2) == True): print "circle"
            if (blob.isRectangle(0.05) == True): print "rectangle"
            filteredFig.show()
            raw_input()

    def findShapes(self,shape=None,blobs=None,filteredFig=None):
        tolerance = None
        fig = None

        if shape.lower() == "circle":     # lower() makes sure the characters are not capitalized
            circleTolerance = 0.2  # 0.2 may be a bit too large, but 0.05 is definately too small.  Further testing required.
            tolerance = circleTolerance
            fig = [b for b in blobs if b.isCircle(circleTolerance)]  # find all the circles within a certain tolerance
        elif shape.lower() == "rectangle":
            rectangleTolerance = 0.05  # Keep this number very low or every figure becomes a rectangle...
            tolerance = rectangleTolerance
            fig = [b for b in blobs if b.isRectangle(rectangleTolerance)]  # find all the rectangles within a certain tolerance
        elif shape.lower() == "heart":
            print 'not yet implemented'
        elif shape.lower() == "star":
            print 'not yet implemented'
        else: print "Bad shape input, this should never have happened!"

        return fig



    def testFoundShape(self,shapes=None,filteredFig=None):
        for shape in shapes:
            shape.draw()
            print shape
            filteredFig.show()
            raw_input()


shapes = ShapeFinder()
shapes.locateFigures('Yellow','Rectangle')
# filtering method: http://stackoverflow.com/questions/14036944/how-do-i-locate-the-rabbit


# java method for detecting figures: https://opencv-code.com/tutorials/detecting-simple-shapes-in-an-image/


