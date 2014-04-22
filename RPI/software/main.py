from positionHandler import Handler


class userInterface:

    def __init__(self):
        self.handler = Handler()

    def findZeppelinLocation(self, path = "C:\Users\Babyburger\PycharmProjects\PENOROODpy\output\path.jpg"):
        pos = self.handler.run(path)
        print "found " + str(pos)


ui = userInterface()
ui.findZeppelinLocation()