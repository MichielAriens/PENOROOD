from Tkinter import *
import GUI.listener as listener
from GUI.listener import *

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
    def __init__(self, master):
        self.root = master
        self.labelframe = LabelFrame(master, text="Input&Output")
        self.canvas = Canvas(master, bg = "White", width = 1000, height = 1000)
        self.label1 = Label(self.labelframe, text="X")
        self.label2 = Label(self.labelframe, text="Y")
        self.heightLabel = Label(self.labelframe, text="Height = n.a.")
        self.entry1 = Entry(self.labelframe)
        self.entry2 = Entry(self.labelframe)
        self.grid = GRID(8,7)
        self.text = Text(master,width = 50, height = 15)
        self.goal = (0,0)
        self.communicator = listener.Listener()
       
        self.ipads = []
        self.addIpad(25, 100, 100)
        
        self.controlFrame = LabelFrame(master, text="Controls")
        self.upbutton= Button(self.controlFrame, text="UP", command=self.moveUpWithButton)
        self.downbutton= Button(self.controlFrame, text="DOWN", command=self.moveDownWithButton)
        self.leftbutton= Button(self.controlFrame, text="LEFT", command=self.moveLeftWithButton)
        self.rightbutton= Button(self.controlFrame, text="RIGHT", command=self.moveRightWithButton)
        self.gobutton= Button(self.labelframe, text="GO", command=self.setGoal)
        
        self.greendot = PhotoImage(file="GUI/goodzep.gif")
        self.reddot = PhotoImage(file="GUI/badzep.gif")
        self.bh = PhotoImage(file="GUI/blauw_hart.gif") #1
        self.yh = PhotoImage(file="GUI/geel_hart.gif")#2
        self.gh = PhotoImage(file="GUI/groen_hart.gif")#3
        self.rh = PhotoImage(file="GUI/rood_hart.gif")#4
        self.wh = PhotoImage(file= "GUI/wit_hart.gif")#5
        self.bc = PhotoImage(file="GUI/blauwe_cirkel.gif")#6
        self.yc = PhotoImage(file="GUI/gele_cirkel.gif")#7
        self.gc = PhotoImage(file="GUI/groene_cirkel.gif")#8
        self.rc = PhotoImage(file="GUI/rode_cirkel.gif")#9
        self.wc = PhotoImage(file="GUI/witte_cirkel.gif")#10
        self.br = PhotoImage(file="GUI/blauwe_rechthoek.gif")#11
        self.yr = PhotoImage(file="GUI/gele_rechthoek.gif")#12
        self.gr = PhotoImage(file="GUI/groene_rechthoek.gif")#13
        self.rr = PhotoImage(file="GUI/rode_rechthoek.gif")#14
        self.wr = PhotoImage(file="GUI/witte_rechthoek.gif")#15
        self.bs = PhotoImage(file="GUI/blauwe_ster.gif")#16
        self.ys = PhotoImage(file="GUI/gele_ster.gif")#17
        self.gs = PhotoImage(file="GUI/groene_ster.gif")#18
        self.rs = PhotoImage(file="GUI/rode_ster.gif")#19
        self.ws = PhotoImage(file="GUI/witte_ster.gif")#20
        self.fb = PhotoImage(file="GUI/forbidden_area.gif")#1
        self.ipadgif = PhotoImage(file="GUI/ipad.gif")#1
        self.images = (self.fb,self.bh,self.yh,self.gh,self.rh, self.wh,self.bc,self.yc,self.gc,self.rc,self.wc,self.br,self.yr,self.gr,self.rr,self.wr,self.bs,self.ys,self.gs,self.rs,self.ws)
        
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
        if(shapeID < len(self.images) and shapeID > 0):
            self.canvas.create_image(paintx,painty,image=self.images[shapeID])
        else:
            self.canvas.create_image(paintx,painty,image=self.fb)
        
    
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
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(round(posx)) +","+ str(round(posy))+")cm", fill = "red")
        elif(ZID == 100):
            self.canvas.create_image(xoffset + x,yoffset + y,image=self.ipadgif)
        else:
            self.canvas.create_image(xoffset + x,yoffset + y,image=self.reddot)
            self.canvas.create_text(xoffset + x + 5,yoffset + y+30,text="ZID =" + str(ZID), fill = "red")
            self.canvas.create_text(xoffset + x + 5,yoffset + y+40,text="POS = (" + str(round(posx)) +","+ str(round(posy))+")cm", fill = "red")
        
    
        
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
        self.drawGrid()
        list_empty = self.grid.getEmptyPositions()
        for k in range(len(list_empty)):
            emp = list_empty[k]
            position_emp = emp[0]
            EID = emp[1]
            self.paintShape(position_emp[0], position_emp[1], EID)
        list_shapes = self.grid.getShapesAndPositions()
        for j in range(len(list_shapes)):
            shape = list_shapes[j]
            position_shape = shape[0]
            SID = shape[1]
            self.paintShape(position_shape[0], position_shape[1], SID)
        list = self.grid.getZeppelins()
        for i in range(len(list)):
            zep = list[i]
            position_zep = zep[0]
            ZID = zep[1]
            self.paintZeppelin(position_zep[0], position_zep[1], ZID)
        list_pads = self.ipads
        for l in range(len(list_pads)):
            ipad = list_pads[l]
            ipad_pos = ipad[0]
            self.paintZeppelin(ipad_pos[0], ipad_pos[1], ipad[1])
        self.updateMessage()
    
    #updates the displayed message
    def updateMessage(self):
        zeps = self.grid.getZeppelins()
        message = "Info:"
        for i in range(len(zeps)):
            zep = zeps[i]
            pos = zep[0]
            if(zep[1] == 1):
                message = message + "\n" + "Our zeppelin at (" + str(round(pos[0])) + "," + str(round(pos[1])) + "," + str(self.grid.getHeight(zep[1])) +")"
            else:
                message = message + "\n" + "Other zeppelin, ID="+ str(zep[1])+ " at ("+ str(round(pos[0])) + "," + str(round(pos[1])) + "," + str(self.grid.getHeight(zep[1])) + ")"
        if(self.goal != (-1,-1)):
            message = message + "\n" + "Current goal = " +  "("+ str(self.goal[0]) + "," + str(self.goal[1]) + ")"
        for l in range(len(self.ipads)):
            ipad = self.ipads[l]
            pos = ipad[0]
            message = message + "\n" + "iPad at (" + str(round(pos[0])) + "," + str(round(pos[1])) + ")"
            
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
        self.checkZeppelins()                                                       
        self.updateTaskForSimulators()
        self.updateZeppelins()
        self.updateCanvas()
        self.readFromFile()
        self.root.after(33,self.task)
    
    def checkZeppelins(self):
        sims = self.communicator.simulators
        print("CheckZeps: sims  " + str(sims))
        for i in range(len(sims)):
            sim_id = sims[i][1]
            if(self.grid.getZeppelin(sim_id) == ((-1,-1),-1)):                              
                self.grid.addZeppelin(0, 0, sim_id)
                self.grid.updateHeight(sim_id, 0)
        zeps = self.communicator.zeppelins
        for i in range(len(zeps)):
            zep_id = zeps[i]
            if(self.grid.getZeppelin(zep_id) == ((-1,-1),-1)):                               
                self.grid.addZeppelin(0, 0, zep_id)
                self.grid.updateHeight(zep_id, 0)
            
    
    def updateTaskForSimulators(self):
        sims = self.communicator.simulators
        for i in range(len(sims)):
            sim_tuple = sims[i]
            zep_listener = sim_tuple[0]
            zep_id = sim_tuple[1]
            if(self.goal != (-1,-1)):
                zep_listener.sendGoalDirection(self.updateGoalDirection(zep_id))
            zep = zep_listener.getPosition()                                                
            zep_pos = zep.asArray()
            if(zep_pos[0]!=-1 and zep_pos[1]!=-1):
                print("position: "+str(zep_pos[0]) + "," + str(zep_pos[1]))                             
                self.grid.setZeppelinPosition(zep_pos[0], zep_pos[1], zep_id)   

    def updateZeppelins(self):
        for i in range(len(self.communicator.zeppelins)):
            position = self.communicator.getZeppelinPosition(self.communicator.zeppelins[i])
            if(position is not None):
                self.grid.setZeppelinPosition(position[0], position[1], self.communicator.zeppelins[i])
                self.grid.updateHeight(self.communicator.zeppelins[i], self.communicator.getZeppelinHeight(self.communicator.zeppelins[i]))
                
        
    def getGoalFromInput(self):
        inputx = self.entry1.get()
        inputy = self.entry2.get()
        try:
            x = int(inputx)
            y = int(inputy)
        except:
            x = -1
            y = -1
        return (x,y)
    
    def sendFakeZepToGoal(self):
        goal = self.getGoalFromInput()
        if(goal[0]==-1):
            a = 1 #random
        else:
            self.setGoal(goal)

    def setGoal(self,goalposition):
        self.goal = goalposition;
        
    def updateGoalDirection(self, zepID):
        currentpos = self.grid.getZeppelin(zepID)[0]
        if(currentpos[0] == self.goal):
            self.goal = (-1,-1)
            return(0,0)
        else:
            direction_x = self.goal[0] - currentpos[0];
            direction_y = self.goal[1] - currentpos[1];
            return(direction_x, direction_y)
        
        
    def getPositionFromListener(self):
        return self.listener.getPosition()
        
    def moveUpWithButton(self):
        self.listener.sendMovementToFakeZep(1)
        
    def moveDownWithButton(self):
        self.listener.sendMovementToFakeZep(3)
    
    def moveLeftWithButton(self):
        self.listener.sendMovementToFakeZep(4)
        
    def moveRightWithButton(self):
        self.listener.sendMovementToFakeZep(2)
        
    def sendMessageToListener(self, message):
        self.listener.refactor(message);
        
    def initiateFromFile(self, path):
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
        
    def setGoal(self):
        goalz = self.getGoalFromInput()
        self.goal = goalz
        
    def readFromFile(self):
        file_object = open("C:\\Users\\simon\\test.txt", "r")
        lines = file_object.readlines()
        print(lines)
        file_object.close()
        
    def addIpad(self, x, y, ID):
        self.ipads.append(((x,y),ID))
        
#class that represents the triangular grid
class GRID:
    
    #defines a matrix with y rows and x columns. Each M(x,y) contains a value, this value represents the Shape-ID (SID)
    def __init__(self,x,y):
        print(str(range(x)))
        self.table = [ [ 0 for i in range(y) ] for j in range(x) ]
        print(self.table)
        self.rows = y
        self.columns = x
        
        self.zeplist = []
        self.zepheights = []
    
    def getHeight(self, id):
        for i in range(len(self.zepheights)):
            zep = self.zepheights[i]
            if(zep[0] == id):
                return zep[1]
            else:
                return None
            
    def updateHeight(self, id, height):
        for i in range(len(self.zepheights)):
            zep = self.zepheights[i]
            if(zep[0] == id):
                tuple = (id, height)
                self.zepheights.remove(zep)
                self.zepheights.append(tuple)
    
    def initiate(self,string):
        print(string)
        part = string.rsplit("[")
        parts = part[1].rsplit("]")
        part_strings = parts[0].rsplit("=");
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
    
    def calculatePositionFromShapesFlexible(self, shapes):
        positions = []
        checked_shapes = []
        for i in range(len(shapes)):
            shape = shapes[i]
            if not self.checkList(checked_shapes, shape):
                shape_pos = self.getShape(shape)
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
        x = x/count
        y = y/count
        print(x,y)
            
            
    def checkList(self,list,element):
        for i in range(len(list)):
            if(list[i] == element):
                return True
        else:
            return False
            
        
    #nog afwerken    
    def calculatePositionFromShapes(self, SID1, SID2, SID3):
        for i in range(self.rows-1):
            for j in range(self.columns):
                if((self.table[i][j]==SID1 and self.table[i+1][j]==SID2) or (self.table[i][j]==SID2 and self.table[i+1][j]==SID1)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID3):
                        return((i+1)*40,(j+1/2)*35) 
                    if(j%2 == 1 and self.table[i+1][j-1]==SID3):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID3):
                        return((i+1/2)*40,(j+1/2)*35) 
                    if(j%2 == 0 and self.table[i][j-1]==SID3):
                        return((i+1/2)*40,(j-1/2)*35)
                if((self.table[i][j]==SID1 and self.table[i+1][j]==SID3) or (self.table[i][j]==SID3 and self.table[i+1][j]==SID1)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID2):
                        return((i+1)*40,(j+1/2)*35) 
                    if(j%2 == 1 and self.table[i+1][j-1]==SID2):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID2):
                        return((i+1/2)*40,(j+1/2)*35) 
                    if(j%2 == 0 and self.table[i][j-1]==SID2):
                        return((i+1/2)*40,(j-1/2)*35)
                if((self.table[i][j]==SID2 and self.table[i+1][j]==SID3) or (self.table[i][j]==SID3 and self.table[i+1][j]==SID2)):
                    if(j%2 == 1 and self.table[i+1][j+1]==SID1):
                        return((i+1)*40,(j+1/2)*35) 
                    if(j%2 == 1 and self.table[i+1][j-1]==SID1):
                        return((i+1)*40,(j-1/2)*35)
                    if(j%2 == 0 and self.table[i][j+1]==SID1):
                        return((i+1/2)*40,(j+1/2)*35) 
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