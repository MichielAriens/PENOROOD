import shapeRecognition as sr

shapes = sr.ShapeFinder()
shapes.setImage('C:\\Users\\Babyburger\\PycharmProjects\\PENOROODpy\\output\\4.jpg')
shapes.locateFigures('blue','circle')
