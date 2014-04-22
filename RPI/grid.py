class GRID:
    
    #defines a matrix with y rows and x columns. Each M(x,y) contains a value, this value represents the Shape-ID (SID)
    def __init__(self,x,y):
        print(str(range(x)))
        self.table = [ [ 0 for i in range(y) ] for j in range(x) ]
        print(self.table)
        self.rows = y
        self.columns = x
        self.height_cm = 400
        self.width_cm = 400
        self.zeplist = []



    def initiate(self,string):
        part_strings = string.rsplit("=");
        value = 0
        x = 0
        y = 0
        for i in range(len(part_strings)):
            string = part_strings[i]
            if(string == "bh"):
                value = 1
            elif(string == "yh"):
                value = 2
            elif(string =="gh"):
                value = 3
            elif(string =="rh"):
                value = 4
            elif(string =="wh"):
                value = 5
            elif(string =="bo" or string =="bc"):
                value = 6
            elif(string =="yo" or string =="yc"):
                value = 7
            elif(string =="go" or string =="gc"):
                value = 8
            elif(string =="ro" or string =="rc"):
                value = 9
            elif(string =="wo" or string =="wc"):
                value = 10
            elif(string =="br"):
                value = 11
            elif(string =="yr"):
                value = 12
            elif(string =="gr"):
                value = 13
            elif(string =="rr"):
                value = 14
            elif(string =="wr"):
                value = 15
            elif(string =="bs"):
                value = 16
            elif(string =="ys"):
                value = 17
            elif(string =="gs"):
                value = 18
            elif(string =="rs"):
                value = 19
            elif(string =="ws"):
                value = 20
            elif(string =="xx" or string =="0"):
                value = 0
            else:
                value = 0
            self.setValue(value, x, y)
            x = x + 1
            if(x >= self.columns):
                x = 0
                y = y + 1 
    

    # returns a value corresponding to the given string (string is based on shape and color)
    def getShapeID(self, string):
        if(string == "bh"):
            value = 1
        elif(string == "yh"):
            value = 2
        elif(string =="gh"):
            value = 3
        elif(string =="rh"):
            value = 4
        elif(string =="wh"):
            value = 5
        elif(string =="bc"):
            value = 6
        elif(string =="yc"):
            value = 7
        elif(string =="gc"):
            value = 8
        elif(string =="rc"):
            value = 9
        elif(string =="wc"):
            value = 10
        elif(string =="br"):
            value = 11
        elif(string =="yr"):
            value = 12
        elif(string =="gr"):
            value = 13
        elif(string =="rr"):
            value = 14
        elif(string =="wr"):
            value = 15
        elif(string =="bs"):
            value = 16
        elif(string =="ys"):
            value = 17
        elif(string =="gs"):
            value = 18
        elif(string =="rs"):
            value = 19
        elif(string =="ws"):
            value = 20
        elif(string =="0"):
            value = 0
        return value

    #set the value of specified position on the grid.
    def setValue(self, value, x, y ): #value = zeppelin_ID
        self.table[x][y] = value
    
    #print the value of a position (value = shape-ID)
    def printPosition(self, x, y):
        if(x < self.rows and y < self.columns):
            print(self.table[x][y])
        else:
            print("not a valid position")
    
    #get empty positions
    def getEmptyPositions(self):
        listy = []
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.table[j][i] <= 0):
                    listy.append(((j,i),self.table[j][i]))
        return listy
    
    #get all shapes and their positions and return them in a list ((x,y),ZID)
    def getShapesAndPositions(self):
        listy = []
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.table[j][i] > 0):
                    listy.append(((j,i),self.table[j][i]))
        return listy
    
    #return a list of all zeppelins
    def getZeppelins(self):
        return self.zeplist
    
    #returns the position and SID of a shape: ((x,y),ZID). If the shape can't be found it returns ((-1,-1),-1)
    def getShape(self, SID):
        shapes = []
        for i in range(self.rows):
            for j in range(self.columns):
                if(SID == self.table[i][j]):
                    shapes.append(((i,j),SID))
        if(len(shapes)>0):
            return shapes
        else:
            return []
        
    def getZeppelin(self, ZID):
        zeps = self.getZeppelins()
        for i in range(len(zeps)):
            zep = zeps[i]
            if(ZID == zep[1]):
                return zep
        else:
            return ((-1,-1),-1)
    
    #add zeppelin x and y in cm
    def addZeppelin(self,x,y,ZID):
        self.zeplist.append(((x,y),ZID))

    # returns the calculated position (tuple of x and y coordinates) from given list of shapes
    # the shapes contain (value for shape and color, xcoordinate, ycoordinate)
    def calculatePositionFromShapesFlexible(self, shapes):
        positions = []
        checked_shapes = []
        for i in range(len(shapes)):    # looping through all the shapes
            shape = shapes[i]   # current shape in the for loop
            if not self.checkList(checked_shapes, shape):
                shape_pos = self.getShape(shape)
                if(shape_pos != []):
                    print("Shape: "+str(shape))
                    print("Shape_Positions: " + str(shape_pos))
                    for j in range(len(shape_pos)):
                        new_pos = (shape_pos[j][0][0]*40, shape_pos[j][0][1]*36)
                        positions.append(new_pos)
                    checked_shapes.append(shape)
        #alle positions van de shapes toegevoegd in positions
        print("positions:" + str(positions))
        x = 0
        y = 0
        count = 0
        for k in range(len(positions)):
            x += positions[k][0]
            y += positions[k][1]
            count += 1
        print("x-coord: " + str(x))
        print("y-coord: " + str(y))
        print("count: " + str(count))
        if count == 0:
            print("-1,-1")
        else:
            x = x/count
            y = y/count
            print(x,y)
            
            
    def checkList(self,list,element):
        for i in range(len(list)):
            if(list[i] == element):
                return True
        else:
            return False
            
        print str(aPos)
                
    
    #nog afwerken    
    def calculatePositionFromShapes(self, SID1, SID2, SID3):
        for i in range(self.rows-1):
            #for j in range(self.columns):
            for j in range(self.columns-1):
                if((self.table[i][j]==SID1 and self.table[i+1][j]==SID2) or (self.table[i][j]==SID2 and self.table[i+1][j]==SID1)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID3):
                        return((i+1)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 1 and self.table[i+1][j-1]==SID3):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID3):
                        return((i+1/2)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 0 and self.table[i][j-1]==SID3):
                        return((i+1/2)*40,(j-1/2)*35)
                if((self.table[i][j]==SID1 and self.table[i+1][j]==SID3) or (self.table[i][j]==SID3 and self.table[i+1][j]==SID1)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID2):
                        return((i+1)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 1 and self.table[i+1][j-1]==SID2):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID2):
                        return((i+1/2)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 0 and self.table[i][j-1]==SID2):
                        return((i+1/2)*40,(j-1/2)*35)
                if((self.table[i][j]==SID2 and self.table[i+1][j]==SID3) or (self.table[i][j]==SID3 and self.table[i+1][j]==SID2)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID1):
                        return((i+1)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 1 and self.table[i+1][j-1]==SID1):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID1):
                        return((i+1/2)*40,(j+1/2)*35) #klopt wrs nog ni
                    if(j%2 == 0 and self.table[i][j-1]==SID1):
                        return((i+1/2)*40,(j-1/2)*35)
        return (-1,-1)

    #!!!!!!!!!!!!!!!!!!!! x and y are in cm !!!!!!!!!!!!!!!!!!!
    def setZeppelinPosition(self, x, y, ZID):
        for i in range (len(self.zeplist)):
            zep = self.zeplist[i]
            if(zep[1] == ZID):
                self.zeplist.remove(zep)
                zep1 = ((x,y),ZID)
                self.zeplist.append(zep1)
    
        
    #moves a zeppelin from his old position to a new position(x,y), returns true if this new position doesn't contain another zeppelin
    #DEPRECATED
    def moveZeppelin(self, ZID, x, y):
        if(x < self.rows and y < self.columns):
            zeppelin = self.getZeppelin(ZID)
            coords = zeppelin[0]
            old_x = coords[0]
            old_y = coords[1]
            self.table[old_x][old_y] = 0
            if(self.table[x][y] != 0):
                self.table[x][y] = ZID
                return True
            else:
                return False
        else:
            return False
    
    #check if a position is empty or not
    def checkPosition(self, x, y):
        if(x < self.rows and y < self.columns):
            if(self.table[x][y] != 0):
                return False
            else:
                return True
    
    #!!!!!!!!!!
    #NOT TESTED
    #(probably not working, yet)
    #!!!!!!!!!!
    def getPathToPositionForZep(self, x, y, ZID):     
        if(x < self.rows and y < self.columns):
            if(self.checkPosition(x,y)):
                zep = self.getZeppelin(ZID)
                zep_position = zep[0]
                zep_x = zep_position[0]
                zep_y = zep_position[1]
                current_x = zep_x
                current_y = zep_y
                queue = []
                pos = []
                pos.append((current_x,current_y))
                queue.append(pos)
                while(self.goalReached() == False):
                    for i in range(len(queue)):
                        pathinqueue = queue[i]
                        newpaths = self.createPathsToChild(pathinqueue)
                        queue.remove(pathinqueue)
                        for j in range(len(newpaths)):
                            queue.append(newpaths[j])
                        j = 0
                    i = 0
    
    def createPathsToChild(self,pos):
        oldpath = pos
        lastposition = oldpath[len(pos)-1]
        children = self.getChildren(lastposition[0],lastposition[1])
        newpaths = []
        for i in range(len(children)):
            newpath = pos.append(children[i])
            newpaths.append(newpath)
        return newpaths
            
    
    def getChildren(self, x, y):
        children = []
        if(y+1 < self.columns and self.checkPosition(x, y+1) == True):
            children.append((x-1,y-1))
        if(x+1 < self.rows and self.checkPosition(x+1, y+1) == True):
            children.append((x+1,y+1))
        if(y-1 > 0 and self.checkPosition(x, y-1) == True):
            children.append((x,y-1))
        if(x-1 > 0 and self.checkPosition(x-1,y) == True):
            children.append((x-1,y))
    
    def goalReached(self,x,y,listy):
        for i in range(len(listy)):
            path = listy[i]
            endpos = path[len(path-1)]
            if(endpos[0] == x and endpos[1] == y):
                return True
        return False

# this method returns the grid from the given path
def initiateFromFile(path):
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
    retval = GRID(number_of_columns, number_of_rows)
    print init_string + " rows: " + str(number_of_rows) + " cols: " + str(number_of_columns)
    retval.initiate(init_string);
    return retval
                
