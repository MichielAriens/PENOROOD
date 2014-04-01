from positionHandler import Handler as handler

class userInterface:

    def __init__(self):
        True


    def findZeppelinLocation(self, path = "/home/pi/zep2/output/path.jpg"):
        pos = handler.run(path)
        print "found " + str(pos)