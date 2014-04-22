from recognition.main import main
from locationZeppelin import NearbyFigures
from camera import camera as cam

class Handler:

    def __init__(self):
        self.main = main()
        self.nf = NearbyFigures()

    # takes an image, finds all the figures and returns the coordinate of the zeppelin based on the 3 nearest figures
    def run(self, path = "/home/pi/zep2/output/path.jpg"):
        newpath = self.captureImage(path)
        print "camera has taken a picture"
        #newpath = path  # TEMPORARY PATH
        figureList = self.processFigures(newpath)
        print "found list " + str(figureList)
        figures = self.findNearestFigures(figureList)
        print "3 nearest figures " + str(figures)
        return self.findCoordinate(figures)


    # captures an image and returns the path to which the image is saved
    def captureImage(self, path = "/home/pi/zep2/output/path.jpg"):
        print "camera is taking a picture"
        return cam.captureImage(path)

    # finds a list of the color, shape and coordinates of all the found figures.
    def processFigures(self, path):
        self.main.setImage(path)
        self.main.calibrate()
        return self.main.analyze()

    # finds the 3 nearest figures and returns their color and shape in a list
    def findNearestFigures(self, list):
        return self.nf.findFigures(list)

    # finds a tuple with the x and y coordinate of the zeppelin, based on 3 figures
    def findCoordinate(self, figures):
        return self.nf.locateZeppelin(figures)