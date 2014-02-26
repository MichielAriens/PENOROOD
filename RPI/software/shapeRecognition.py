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
        print type(color)

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

    def locateFigures(self,color=None):
        print type(color)
        print type(self)
        filteredFig = self.highlightColor(color)

        # Contains figures of the chosen color
        blobs = filteredFig.findBlobs()

        self.testFoundFigures(blobs,filteredFig)    # Use this method to test if the figures from the given color are correct

    locateFigures('Yellow')

    def testFoundFigures(self,blobs=None,filteredFig = None):
        for blob in blobs:
            blob.draw()
            print blob
            if (blob.isCircle(0.2) == True): print "circle"
            if (blob.isRectangle(0.05) == True): print "rectangle"
            filteredFig.show()
            raw_input()


    """
    # Renders light colors vs dark colors. I think.  I actually don't know what this does.  ;o
    binarized = image.binarize(220).invert()
    blobs = binarized.findBlobs()
    """

    """
    # Shows the distinguished blobs, give a random input for each iteration
    for blob in blobs:
        blob.draw()
        print blob
        if (blob.isCircle(0.2) == True): print "circle"
        if (blob.isRectangle(0.05) == True): print "rectangle"
        binarized.show()
        raw_input()
    """

    """
    # Find circles
    circleTolerance = 0.2  # 0.2 may be a bit too large, but 0.05 is definately too small.  Further testing required.
    circles = [b for b in blobs if b.isCircle(circleTolerance)]  # find all the circles within a certain tolerance
    for circle in circles:
        circle.draw()
        print circle
        binarized.show()
        raw_input()
    """

    """
    # Find rectangles
    rectangleTolerance = 0.05  # Keep this number very low or every figure becomes a rectangle...
    rectangles = [b for b in blobs if b.isRectangle(rectangleTolerance)]  # find all the rectangles within a certain tolerance
    for rectangle in rectangles:
        rectangle.draw()
        print rectangle
        binarized.show()
        raw_input()
    """


    """
    # General method for drawing found figures.
    def findFigure(self,figures):
        self.figure = figures
        for figure in figures:
            figure.draw()
            print figure
            binarized.show()
            raw_input()
    """



# filtering method: http://stackoverflow.com/questions/14036944/how-do-i-locate-the-rabbit


# java method for detecting figures: https://opencv-code.com/tutorials/detecting-simple-shapes-in-an-image/


