from RPI.software.recognition import shapeRecognition as sr

shapes = sr.ShapeFinder()
analyzer = sr.Analyzer(shapes)
path = 'C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\12.jpg'
shapes.setImage(path)

"""
print shapes.blue
print shapes.green
print shapes.red
print shapes.white
print shapes.yellow

shapes.calibrateColors()

print shapes.blue
print shapes.green
print shapes.red
print shapes.white
print shapes.yellow
"""

# tests a given color
shapes.generalTest('green')
shapes.generalTest('yellow')
shapes.generalTest('red')
shapes.generalTest('blue')
shapes.generalTest('white')

# tests all figures
print analyzer.analyze(path)
