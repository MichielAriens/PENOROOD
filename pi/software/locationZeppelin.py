import heapq
from RPI.grid import GRID

class NearbyFigures:

    def __init__(self):
        True
        #self.initiateFromFile() # load the actual grid here.

    # Finds and returns the color and shape of the 3 closest figures to the zeppelin.
    def findFigures(self, figList):
        list = self.convergeLength(figList)
        #print "convergence: " + str(list)

        lengthList = [l for (c,s,l) in list]
        smallestElements = heapq.nsmallest(3,lengthList)
        #print "3 smallest: " + str(smallestElements)
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
        SID1 = self.grid.getShapeID(c[0] + "" + s[0])
        SID2 = self.grid.getShapeID(c2[0] + "" + s2[0])
        SID3 = self.grid.getShapeID(c3[0] + "" + s3[0])
        self.grid.calculatePositionFromShapes(SID1,SID2,SID3)


    def initiateFromFile(self, path= "C:\Users\Babyburger\PycharmProjects\PENOROODpy\OTHER\grid25-04.csv"):
        import csv
        with open(path) as f:
            data=[tuple(line) for line in csv.reader(f)]
        list = []
        emptyrow = []
        for i in range(len(data)):
            list.append(emptyrow)
            row = data[i]
            for j in range(len(row)):
                oldstr = row[j]
                newstr = oldstr.replace("'", " ")
                list[i].append(newstr)
        list[0] = str(list[0]).replace("'", "")
        list[0] = str(list[0]).replace(" ", "")
        list[0] = str(list[0]).replace(",", "=")
        list[0] = str(list[0]).lower()
        number_of_rows = len(data);
        number_of_columns = len(data[0])
        init_string = list[0]
        self.grid = GRID(number_of_columns, number_of_rows)
        self.grid.initiate(init_string);