import shapeRecognition as sr

"""
Use this class to get the shape, color and coordinates for each figure (using analyze()).

Manual:
- give path to setImage every time a picture has been taken with the picamera
- perform analyze to get the shape, color and coordinates for each figure (in a list of tuples)
- use calibrate if you wish to adjust the rgb values.
- if you merely want to show the rgb values after calibration, but don't override the default rgb values,
        use printCalibrate()
- printDefaultRGB returns the currently set RGB values.  This will be the default rgb values, unless calibrate()
        has been performed.
"""
class main:
    def __init__(self, shape = sr.ShapeFinder()):
        self.shape = shape
        self.analyzer = sr.Analyzer(shape)

    # Set the image path for self.shape. Any calibration or analyzation will depend on the image set for self.shape.
    def setImage(self, path):
        self.shape.setImage(path)

    # Changes the default rgb values using HSV.  Note that if a color is not found, that color will
    # keep its previous rgb value.
    def calibrate(self):
        self.shape.calibrateColors()

    # Prints the rgb values found by calibration WITHOUT changing the default rgb values.  If a color is not found,
    # it will print (0,0,0) for that color.
    def printCalibrate(self):
        self.shape.printCalibrate()

    # Prints the current rgb values for self.shape.  This will be the default rgb values unless they have been
    # overridden by calibrate()
    def printDefaultRGB(self):
        self.shape.printRGB()

    # Prints a list of tuples, containing shape, color and coordinates for each figure.
    def analyze(self):
        return self.analyzer.analyze()