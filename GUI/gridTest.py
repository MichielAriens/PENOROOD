from tkinter import *

#initiate tinker, tk() acts as a frame
#root = Tk()
#root.title("team ROOD")

class GUI:
    
    #initiate all components of GUI
    #LabelFrame(container, title) = used for containing other GUI components inside a frame/window or other labelframe
    #label(container, text) = used for displaying strings
    #Canvas(container, width, height, background color, ..) = used for painting images, lines, text etc..
    #Entry(container) = editable text entry
    #Grid(rows, columns) = an object of the grid class, which represents a field made of triangles
    #Text(container, width in characters, height in lines) = widget used for displayed multiple lines of text
    #Greendot & Reddot, images for zeppelins
    #other images are shapes
    def __init__(self, master,listener):
        self.root = master
        self.listener = listener
        self.labelframe = LabelFrame(master, text="Input&Output")
        self.canvas = Canvas(master, bg = "White", width = 500, height = 500)
        self.label1 = Label(self.labelframe, text="input 1")
        self.label2 = Label(self.labelframe, text="input 2")
        self.heightLabel = Label(self.labelframe, text="Height = n.a.")
        self.entry1 = Entry(self.labelframe)
        self.entry2 = Entry(self.labelframe)
        self.grid = GRID(12,13)
        self.text = Text(master,width = 50, height = 15)
        
        self.controlFrame = LabelFrame(master, text="Controls")
        self.upbutton= Button(self.controlFrame, text="UP", command=self.moveUpWithButton)
        self.downbutton= Button(self.controlFrame, text="DOWN", command=self.moveDownWithButton)
        self.leftbutton= Button(self.controlFrame, text="LEFT", command=self.moveLeftWithButton)
        self.rightbutton= Button(self.controlFrame, text="RIGHT", command=self.moveRightWithButton)
        
        self.greendot = PhotoImage(file="GUI/goodzep.gif")
        self.reddot = PhotoImage(file="GUI/badzep.gif")
        self.bh = PhotoImage(file="GUI/blauw_hart.gif")
        self.yh = PhotoImage(file="GUI/geel_hart.gif")
        self.gh = PhotoImage(file="GUI/groen_hart.gif")
        self.rh = PhotoImage(file="GUI/rood_hart.gif")
        self.wh = PhotoImage(file= "GUI/wit_hart.gif")
        self.bc = PhotoImage(file="GUI/blauwe_cirkel.gif")
        self.yc = PhotoImage(file="GUI/gele_cirkel.gif")
        self.gc = PhotoImage(file="GUI/groene_cirkel.gif")
        self.rc = PhotoImage(file="GUI/rode_cirkel.gif")
        self.wc = PhotoImage(file="GUI/witte_cirkel.gif")
        self.bs = PhotoImage(file="GUI/blauwe_rechthoek.gif")
        self.ys = PhotoImage(file="GUI/gele_rechthoek.gif")
        self.gs = PhotoImage(file="GUI/groene_rechthoek.gif")
        self.rs = PhotoImage(file="GUI/rode_rechthoek.gif")
        self.ws = PhotoImage(file="GUI/witte_rechthoek.gif")
        self.bs = PhotoImage(file="GUI/blauwe_ster.gif")
        self.ys = PhotoImage(file="GUI/gele_ster.gif")
        self.gs = PhotoImage(file="GUI/groene_ster.gif")
        self.rs = PhotoImage(file="GUI/rode_ster.gif")
        self.ws = PhotoImage(file="GUI/witte_ster.gif")
        self.images = (self.bh,self.yh,self.gh,self.rh, self.wh,self.bc,self.yc,self.gc,self.rc,self.wc,self.bs,self.ys,self.gs,self.rs,self.ws,self.bs,self.ys,self.gs,self.rs,self.ws)
        
        
        
    #Paints a shape on the grid    
    def paintShape(self, posx, posy, shapeID):
        can_width = self.canvas.winfo_reqwidth()
        can_height = self.canvas.winfo_reqheight()
        position_width = can_width/(self.grid.columns+2)
        position_height = can_height/(self.grid.rows+2)
        if((posy%2)==1):
            paintx = (posx+3/2)*position_width
            painty = (posy+1)*position_height
        else:
            paintx = (posx+1)*position_width
            painty = (posy+1)*position_height
        if(shapeID < len(self.images)):
            self.canvas.create_image(paintx,painty,image=self.images[shapeID])
            #self.canvas.create_text(paintx+5,painty+30,text="SID =" + str(shapeID), fill = "red")
            #self.canvas.create_text(paintx+5,painty+40,text="POS = (" + str(posx) +","+ str(posy)+")", fill = "red")
    
    #Paints a zeppelin on the grid
    #posx en posy is in cm
    def paintZeppelin(self,posx, posy, ZID):
        can_width = self.canvas.winfo_reqwidth()
        can_height = self.canvas.winfo_reqheight()
        position_width = can_width/(self.grid.columns+2)
        position_height = can_height/(self.grid.rows+2)
        xoffset = position_width
        yoffset = position_height
        x =  (posx / 40) * position_width # 
        y =  (posy / 35) * position_height #

        if(ZID == 1):   #our zeppelin
            self.canvas.create_image(xoffset + x,yoffset + y,image=self.greendot)
            self.canvas.create_text(xoffset + x + 5,yoffset + y+30,text="ZID =" + str(ZID), fill = "red")
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(posx) +","+ str(posy)+")cm", fill = "red")
        else:
            self.canvas.create_image(xoffset + x,yoffset + y,image=self.reddot)
            self.canvas.create_text(xoffset + x + 5,yoffset + y+30,text="ZID =" + str(ZID), fill = "red")
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(posx) +","+ str(posy)+")cm", fill = "red")
        
    
        
    #Draw grid on canvas
    def drawGrid(self):
        can_width = self.canvas.winfo_reqwidth()
        can_height = self.canvas.winfo_reqheight()
        position_width = can_width/(self.grid.columns+2)
        position_height = can_height/(self.grid.rows+2)
        max_horizontal_triangles = self.grid.columns
        max_vertical_triangles = self.grid.rows
        #horizontal lines
        for i in range(max_vertical_triangles):
            if((i%2)==0):
                self.canvas.create_line(position_width,position_height*(i+1),can_width-position_width*2,position_height*(i+1))
            else:
                self.canvas.create_line(position_width*(3/2),position_height*(i+1),can_width-position_width*(3/2),position_height*(i+1))
        #diagonal lines
        for j in range(max_vertical_triangles-1):
            if((j%2)==0):
                for i in range(max_horizontal_triangles*2-1):
                    if((i%2)==0):
                        self.canvas.create_line(position_width+position_width*i/2, position_height+position_height*j,position_width+position_width*(1/2)+position_width*i/2,2*position_height+position_height*j)
                    else:
                        self.canvas.create_line((3/2)*position_width+position_width*i/2, position_height+position_height*j,(3/2)*position_width-position_width*(1/2)+position_width*i/2,2*position_height+position_height*j)
            else:
                for i in range(max_horizontal_triangles*2-1):
                    if((i%2)==0):
                        self.canvas.create_line(position_width+position_width*i/2,2*position_height+position_height*j,position_width+position_width*(1/2)+position_width*i/2,position_height+position_height*j)
                    else:
                        self.canvas.create_line((3/2)*position_width+position_width*i/2,2*position_height+position_height*j,(3/2)*position_width-position_width*(1/2)+position_width*i/2,position_height+position_height*j)
    
    #requests all zeppelins and refreshes them on canvas
    def updateCanvas(self):
        self.canvas.delete(ALL)
        list = self.grid.getZeppelins()
        for i in range(len(list)):
            zep = list[i]
            position_zep = zep[0]
            ZID = zep[1]
            self.paintZeppelin(position_zep[0], position_zep[1], ZID)
        list_shapes = self.grid.getShapesAndPositions()
        print(list_shapes)
        for j in range(len(list_shapes)):
            shape = list_shapes[j]
            position_shape = shape[0]
            SID = shape[1]
            self.paintShape(position_shape[0], position_shape[1], SID)
        self.drawGrid()
        self.updateMessage()
        print(self.grid.getZeppelins())
    
    #updates the displayed message
    def updateMessage(self):
        zeps = self.grid.getZeppelins()
        message = ""
        for i in range(len(zeps)):
            zep = zeps[i]
            pos = zep[0]
            if(zep[1] == 1):
                message = message + "\n" + "Our zeppelin at (" + str(pos[0]) + "," + str(pos[1]) + ")"
            else:
                message = message + "\n" + "Other zeppelin, ID="+ str(zep[1])+ " at ("+ str(pos[0]) + "," + str(pos[1]) + ")"
        self.clearMessage()
        self.addDisplayedMessage(message)
    
    #set the message in the text-widget          
    def addDisplayedMessage(self, text):
        self.text.insert(INSERT, text)
        
    #clear message
    def clearMessage(self):
        self.text.delete(1.0, END)
    
    #set the height parameter
    def setHeightLabel(self, text):
        self.heightLabel.textvariable = text
        
    #keep updating besides running the tkinter mainloop
    #update canvas after 1000ms
    def task(self):
        if(self.listener is not None):
            zep = self.getPositionFromListener()
            zep_pos = zep.asArray()
            self.grid.setZeppelinPosition(zep_pos[0], zep_pos[1], 1)
        self.updateCanvas()
        self.root.after(33,self.task)
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        print(self.grid.calculatePositionFromShapes(12, 17, 7))
        print(self.grid.calculatePositionFromShapes(12, 7, 17))
        print(self.grid.calculatePositionFromShapes(7, 12, 17))
        print(self.grid.calculatePositionFromShapes(7, 17, 12))
        print(self.grid.calculatePositionFromShapes(17, 12, 7))
        print(self.grid.calculatePositionFromShapes(17, 7, 12))
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        print(self.grid.calculatePositionFromShapes(13, 14, 15))
        print(self.grid.calculatePositionFromShapes(13, 15, 14))
        print(self.grid.calculatePositionFromShapes(14, 13, 15))
        print(self.grid.calculatePositionFromShapes(14, 15, 13))
        print(self.grid.calculatePositionFromShapes(15, 14, 13))
        print(self.grid.calculatePositionFromShapes(15, 13, 14))
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        print(self.grid.calculatePositionFromShapes(2, 3, 4))
        print(self.grid.calculatePositionFromShapes(2, 4, 3))
        print(self.grid.calculatePositionFromShapes(3, 2, 4))
        print(self.grid.calculatePositionFromShapes(3, 4, 2))
        print(self.grid.calculatePositionFromShapes(4, 3, 2))
        print(self.grid.calculatePositionFromShapes(4, 2, 3))
        print("xxxxxxxxxxxxxxxxxxxxxxxxx")
        
    def getPositionFromListener(self):
        return self.listener.getPosition()
        
    def moveUpWithButton(self):
        our_zep = self.grid.getZeppelin(1)
        x = our_zep[0][0]
        y = our_zep[0][1]
        self.grid.setZeppelinPosition( x, y+20,1)
        
    def moveDownWithButton(self):
        our_zep = self.grid.getZeppelin(1)
        x = our_zep[0][0]
        y = our_zep[0][1]
        self.grid.setZeppelinPosition( x, y-20,1)
    
    def moveLeftWithButton(self):
        our_zep = self.grid.getZeppelin(1)
        x = our_zep[0][0]
        y = our_zep[0][1]
        self.grid.setZeppelinPosition( x-20, y,1)
        
    def moveRightWithButton(self):
        our_zep = self.grid.getZeppelin(1)
        x = our_zep[0][0]
        y = our_zep[0][1]
        self.grid.setZeppelinPosition( x+20, y,1)
        
    def sendMessageToListener(self, message):
        self.listener.refactor(message);
        
    def createGridFromFile(self, gridstring):
        strings = gridstring.rsplit(",")

#class that represents the triangular grid
class GRID:
    
    #defines a matrix with y rows and x columns. Each M(x,y) contains a value, this value represents the Shape-ID (SID)
    def __init__(self,x,y):
        self.table = [ [ 0 for i in range(x) ] for j in range(y) ]
        self.rows = y
        self.columns = x
        self.height_cm = 400
        self.width_cm = 400
        self.zeplist = []
    
    #set the value of specified position on the grid.
    def setValue(self, value, x, y ): #value = zeppelin_ID
        self.table[x][y] = value
    
    #print the value of a position (value = shape-ID)
    def printPosition(self, x, y):
        if(x < self.rows and y < self.columns):
            print(self.table[x][y])
        else:
            print("not a valid position")
    
    #get all shapes and their positions and return them in a list ((x,y),ZID)
    def getShapesAndPositions(self):
        listy = []
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.table[i][j] > 0):
                    listy.append(((i,j),self.table[i][j]))
        return listy
    
    #return a list of all zeppelins
    def getZeppelins(self):
        return self.zeplist
    
    #returns the position and SID of a shape: ((x,y),ZID). If the shape can't be found it returns ((-1,-1),-1)
    def getShape(self, SID):
        for i in range(self.rows):
            for j in range(self.columns):
                if(SID == self.table[i][j]):
                    return ((i,j),SID)
        else:
            return ((-1,-1),-1)
        
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
    
    #nog afwerken    
    def calculatePositionFromShapes(self, SID1, SID2, SID3):
        for i in range(self.rows-1):
            for j in range(self.columns):
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
        return ((-1,-1),-1)
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
                
        
            
#Initiate GUI
#Gui = GUI(root)

#pack() is used for positioning/drawing the widgets on the frame
#Gui.canvas.pack(side = LEFT)
#Gui.text.pack()
#Gui.labelframe.pack(expand="yes")
#Gui.controlFrame.pack(expand="yes")
#grid() positions/draws widget in a grid-like-layout
#Gui.label1.grid(row = 0, column = 0)
#Gui.label2.grid(row = 1, column = 0)
#Gui.heightLabel.grid(columnspan = 2)
#Gui.entry1.grid(row = 0, column = 1)
#Gui.entry2.grid(row = 1, column = 1)

#Gui.upbutton.grid(row = 0, column = 1)
#Gui.downbutton.grid(row = 2, column = 1)
#Gui.leftbutton.grid(row = 1, column = 0)
#Gui.rightbutton.grid(row = 1, column = 2)

#Gui.grid.addZeppelin(120, 243, 1)
#Gui.grid.addZeppelin(200, 200, 2)
#Gui.grid.setValue(5, 2, 3)
#Gui.grid.setValue(1, 5, 1)
#Gui.grid.setValue(7, 0, 1)
#Gui.grid.setValue(9, 11,1)
#Gui.grid.setValue(17, 0, 0)
#Gui.grid.setValue(19, 11,0)


#Set values of positions on the grid
#print(Gui.grid.getZeppelins())
#Gui.addDisplayedMessage("Nothing to be displayed atm.")
#Gui.setHeightLabel("230cm")
#Gui.updateCanvas()

#loop that registers action in the frame
#keep calling Gui.task every 1000ms
#root.after(1000,Gui.task)
#root.mainloop()