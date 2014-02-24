from tkinter import *

#initiate tinker, tk() acts as a frame
root = Tk()
root.title("team ROOD")

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
    def __init__(self, master):
        self.labelframe = LabelFrame(master, text="Input&Output")
        self.canvas = Canvas(master, bg = "White", width = 500, height = 500)
        self.label1 = Label(self.labelframe, text="input 1")
        self.label2 = Label(self.labelframe, text="input 2")
        self.heightLabel = Label(self.labelframe, text="Height = n.a.")
        self.entry1 = Entry(self.labelframe)
        self.entry2 = Entry(self.labelframe)
        self.grid = GRID(10,12)
        self.text = Text(master,width = 50, height = 15)
        self.greendot = PhotoImage(file="greendot1.gif") #needs replacement
        self.bh = PhotoImage(file="blauw_hart.gif")
        self.glh = PhotoImage(file="geel_hart.gif")
        self.grh = PhotoImage(file="groen_hart.gif")
        self.bc = PhotoImage(file="blauwe_cirkel.gif")
        self.glc = PhotoImage(file="gele_cirkel.gif")
        self.grc = PhotoImage(file="groene_cirkel.gif")
        self.br = PhotoImage(file="blauwe_rechthoek.gif")
        self.glr = PhotoImage(file="gele_rechthoek.gif")
        self.grr = PhotoImage(file="groene_rechthoek.gif")
        self.bs = PhotoImage(file="blauwe_ster.gif")
        self.gls = PhotoImage(file="gele_ster.gif")
        self.grs = PhotoImage(file="groene_ster.gif")
        self.images = (self.bh,self.glh,self.grh,self.bc,self.glc,self.grc,self.br,self.glr,self.grr,self.bs,self.gls,self.grs)
        
        
        
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
            self.canvas.create_text(paintx+5,painty+30,text="ZID =" + str(shapeID), fill = "red")
            self.canvas.create_text(paintx+5,painty+40,text="POS = (" + str(posx) +","+ str(posy)+")", fill = "red")
    
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
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(posx) +","+ str(posy)+")", fill = "red")
        else:
            self.canvas.create_image(xoffset + x,yoffset + y,image=self.reddot)
            self.canvas.create_text(xoffset + x + 5,yoffset + y+30,text="ZID =" + str(ZID), fill = "red")
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(posx) +","+ str(posy)+")", fill = "red")
        
    
        
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
                self.canvas.create_line(position_width*(3/2),position_height*(i+1),can_width-position_width*(5/2),position_height*(i+1))
        #diagonal lines
        for j in range(max_vertical_triangles-1):
            if((j%2)==0):
                for i in range(max_horizontal_triangles*2-2):
                    if((i%2)==0):
                        self.canvas.create_line(position_width+position_width*i/2, position_height+position_height*j,position_width+position_width*(1/2)+position_width*i/2,2*position_height+position_height*j)
                    else:
                        self.canvas.create_line((3/2)*position_width+position_width*i/2, position_height+position_height*j,(3/2)*position_width-position_width*(1/2)+position_width*i/2,2*position_height+position_height*j)
            else:
                for i in range(max_horizontal_triangles*2-2):
                    if((i%2)==0):
                        self.canvas.create_line(position_width+position_width*i/2,2*position_height+position_height*j,position_width+position_width*(1/2)+position_width*i/2,position_height+position_height*j)
                    else:
                        self.canvas.create_line((3/2)*position_width+position_width*i/2,2*position_height+position_height*j,(3/2)*position_width-position_width*(1/2)+position_width*i/2,position_height+position_height*j)
    
    #requests all zeppelins and refreshes them on canvas
    def updateCanvas(self):
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
    
    
    #set the message in the text-widget          
    def setDisplayedMessage(self, text):
        self.text.insert(INSERT, text)
    
    #set the height parameter
    def setHeightLabel(self, text):
        self.heightLabel.textvariable = text

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
    
    #get all zeppelins and their positions and return them in a list ((x,y),ZID)
    def getShapesAndPositions(self):
        list = []
        for i in range(self.rows):
            for j in range(self.columns):
                if(self.table[i][j] > 0):
                    list.append(((i,j),self.table[i][j]))
        return list
    
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
    
    #add zeppelin x and y in cm
    def addZeppelin(self,x,y,ZID):
        self.zeplist.append(((x,y),ZID))
    
    #!!!!!!!!!!!!!!!!!!!! x and y are in cm !!!!!!!!!!!!!!!!!!!
    def setZeppelinPosition(self, x, y, ZID):
        for i in range (len(self.zeplist)):
            zep = self.zeplist[i]
            if(zep[1] == ZID):
                zep[0] = (x,y)
    
        
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
    
    def goalReached(self,x,y,list):
        for i in range(len(list)):
            path = list[i]
            endpos = path[len(path-1)]
            if(endpos[0] == x and endpos[1] == y):
                return True
        return False
                
        
            
#Initiate GUI
Gui = GUI(root)

#pack() is used for positioning/drawing the widgets on the frame
Gui.canvas.pack(side = LEFT)
Gui.text.pack()
Gui.labelframe.pack(expand="yes")
#grid() positions/draws widget in a grid-like-layout
Gui.label1.grid(row = 0, column = 0)
Gui.label2.grid(row = 1, column = 0)
Gui.heightLabel.grid(columnspan = 2)
Gui.entry1.grid(row = 0, column = 1)
Gui.entry2.grid(row = 1, column = 1)

Gui.grid.addZeppelin(120, 243, 1)
Gui.grid.setValue(5, 2, 3)
Gui.grid.setValue(1, 5, 1)


#Set values of positions on the grid

print(Gui.grid.getZeppelins())
Gui.setDisplayedMessage("Nothing to be displayed atm.")
Gui.setHeightLabel("230cm")
Gui.updateCanvas()

#loop that registers action in the frame
root.mainloop()