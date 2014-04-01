import shapeRecognition as sr

class main:
    def __init__(self, shape = sr.ShapeFinder()):
        self.shape = shape
        self.analyzer = sr.Analyzer(shape)

    def setImage(self, path):
        self.shape.setImage(path)

    def calibrate(self):
        self.shape.calibrateColors()

    def analyze(self):
        return self.analyzer.analyze()