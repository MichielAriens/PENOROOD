from RPI.software.recognition import shapeRecognition as sr

shapes = sr.ShapeFinder()
analyzer = sr.Analyzer(shapes)
path = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\13.jpg'
shapes.setImage(path)
# shapes.calibrateColors()

# tests all figures
print analyzer.analyze(path)

# tests a given color
shapes.generalTest('green')
shapes.generalTest('yellow')
shapes.generalTest('red')
shapes.generalTest('blue')
shapes.generalTest('white')
