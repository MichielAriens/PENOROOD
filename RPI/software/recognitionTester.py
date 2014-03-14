import shapeRecognition as sr

shapes = sr.ShapeFinder()
analyzer = sr.Analyzer()
path = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\8.jpg'
shapes.setImage(path)
shapes.calibrateColors()

# tests all figures
#print analyzer.analyze(path)

# tests a given color
shapes.generalTest('green')
