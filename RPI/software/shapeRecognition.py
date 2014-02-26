# look into SimpleCV.Features.Blob -> can determine left/right/above/below positioning between two shapes

# template matching can find an input picture within a larger picture:
#   http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html

# help('modules')

from SimpleCV import Color, Image

# 0) need a way to distinguish colors
# 1) V Done
# 2) determine shape with SimpleCV.Features.Blob.Blob isCircle isRectangle isSquare method
#       (define own class for star and heart shape)

# Load picture here picture
image = Image('C:\Users\Babyburger\Desktop\cshapes.jpg')

#extract yellow color
yellowFig = image.colorDistance(Color.YELLOW)
yellowFig.show()
raw_input()

# The contrast of the yellow color has been made stronger.
filteredFig = image - yellowFig
filteredFig.show()
raw_input()

# Exact value of the color can be found.
print filteredFig.meanColor()

print type(filteredFig)

# filteredFigg = yellowFig.binarize(220).invert()
# print type(filteredFigg)
#blobs = filteredFigg.findBlobs()
blobs = filteredFig.findBlobs()
print type(blobs)


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


