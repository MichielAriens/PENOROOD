import heapq
from RPI.grid import GRID as grid

class NearbyFigures:

    def __init__(self):
        True

    # Finds and returns the color and shape of the 3 closest figures to the zeppelin.
    def findFigures(self, figList):
        list = self.convergeLength(figList)
        smallestElements = heapq.nsmallest(3,list)
        newlist = [(c,s) for (c,s,l) in list if l in smallestElements]
        return newlist

    def convergeLength(self,figList):
        list = []
        if figList is not None:
            for (color,shape,x,y) in figList:
                z = (x**2 + y**2)**(0.5)
                list.append((color,shape,z))
        return list

    def locateZeppelin(self,list):
        [(c,s),(c2,s2),(c3,s3)] = list
        SID1 = grid.getShapeID(c[0] + "" + s[0])
        SID2 = grid.getShapeID(c2[0] + "" + s2[0])
        SID3 = grid.getShapeID(c3[0] + "" + s3[0])
        grid.calculatePositionFromShapes(SID1,SID2,SID3)