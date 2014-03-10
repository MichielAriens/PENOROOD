# Using a method to determine hsv per pixel is getting cpu intensive and complicated fast.
# Use http://www.rapidtables.com/convert/color/hsv-to-rgb.htm to experiment with the color ranges.

import shapeRecognition as sr

shapes = sr.ShapeFinder()
shapes.setImage('C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\4.jpg')
shapes.locateFigures('blue','circle')
