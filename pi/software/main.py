from positionHandler import Handler


class userInterface:

    def __init__(self):
        self.handler = Handler()

    def findZeppelinLocation(self, path = "C:/Users/Babyburger/PycharmProjects/PENOROODpy/output/7.jpg"):
        pos = self.handler.run(path)
        print "found " + str(pos)
        return pos

"""
ui = userInterface()
ui.findZeppelinLocation()
"""