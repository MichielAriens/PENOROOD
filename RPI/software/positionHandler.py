from recognition.main import main
from locationZeppelin import NearbyFigures as nf
from camera import camera as cam

class Handler:

    def __init__(self):
        True

    # takes an image, finds all the figures and returns the coordinate of the zeppelin based on the 3 nearest figures
    def run(self, path = "/home/pi/zep2/output/path.jpg"):
        newpath = self.captureImage(path)
        figureList = self.processFigures(newpath)
        figures = self.findNearestFigures(figureList)
        return self.findCoordinate(figures)

    # captures an image and returns the path to which the image is saved
    def captureImage(self, path = "/home/pi/zep2/output/path.jpg"):
        return cam.captureImage(path)

    # finds a list of the color, shape and coordinates of all the found figures.
    def processFigures(self, path):
        main.setImage(path)
        return main.analyze()

    # finds the 3 nearest figures and returns their color and shape in a list
    def findNearestFigures(self, list):
        return nf.findFigures(list)

    # finds a tuple with the x and y coordinate of the zeppelin, based on 3 figures
    def findCoordinate(self, figures):
        return nf.locateZeppelin(figures)