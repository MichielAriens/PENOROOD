# template matching can find an input picture within a larger picture:
#   http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

# alternative method if blobs aren't working for 'live' pictures: contour method with opencv

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

        """     # Test: If the selected color is colored black, then it's working as intended
        fig.show()
        raw_input()
        """

        # The contrast of the given color has been made stronger; this should ideally show only the figures with the color we want.
        # Play around with the amount of times you subtract fig (black is (0,0,0) though our chosen color is not completely black in fig, so
        # be careful not to subtract too much or everything becomes black). Keep doing this until everything but the figures we need are black.
        # Numbers below zero automatically become zero. Subtracting fig twice seems to be the sweet spot. :)
        filteredFigure = image - fig - fig

        """     # Test: If the selected color has a stronger contrast with the other colors than before, then it's working as intended
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
        blobs = filteredFig.findBlobs()  # findBlobs() function easily finds lightly colored blobs on a dark background

        self.testFoundColor(blobs,filteredFig)    # Use this method to test if the figures from the given color are correct

        # Contains figures of the chosen shape (and color)
        shapes = self.findShapes(shape,blobs)

        # self.testFoundShape(shapes,filteredFig)  # Use this method to test if the figures from the given shape are correct

        return shapes

    # Tests whether the figures correspond to the given color or not by displaying the current results.
    def testFoundColor(self,blobs=None,filteredFig = None):
        for blob in blobs:
            blob.draw()
            print blob
            if (blob.isCircle(0.2) == True): print "circle"
            if (blob.isRectangle(0.05) == True): print "rectangle"
            filteredFig.show()
            raw_input()

    # Returns all the figures with the specified shapes. This should only apply to the figures of the chosen color.
    def findShapes(self,shape=None,blobs=None):
        tolerance = None
        fig = None

        if shape.lower() == "circle":     # lower() makes sure the characters are not capitalized
            circleTolerance = 0.2  # 0.2 may be a bit too large, but 0.05 is definately too small.  Further testing required.
            tolerance = circleTolerance
            fig = [b for b in blobs if b.isCircle(tolerance)]  # find all the circles within a certain tolerance
        elif shape.lower() == "rectangle":
            rectangleTolerance = 0.05  # Keep this number very low or every figure becomes a rectangle...
            tolerance = rectangleTolerance
            fig = [b for b in blobs if b.isRectangle(tolerance)]  # find all the rectangles within a certain tolerance
        elif shape.lower() == "heart":
            print 'not yet implemented'
        elif shape.lower() == "star":
            print 'not yet implemented'
        else: print "Bad shape input, this should never have happened!"

        return fig

    # Tests whether the figures correspond to the given shape or not by displaying the current results.
    def testFoundShape(self,shapes=None,filteredFig=None):
        for shape in shapes:
            shape.draw()
            print shape
            filteredFig.show()
            raw_input()


shapes = ShapeFinder()
shapes.locateFigures('yellow','circle')