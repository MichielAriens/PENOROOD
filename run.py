import RPI.FakeZeppelin as FakeZeppelin
import GUI.gridTest as gridTest
import GUI.GuiListener as GuiListener
import CONNECTION.multithreaded_server as multithreaded_server
import RPI.ZepListener as ZepListener
from GUI.GuiListener import *
from RPI.ZepListener import *
from GUI.gridTest import *
from tkinter import *
from CONNECTION.multithreaded_server import *
import tkinter as tkinter

def addSimulator(communicator,x,y,z,id):
    zepl = ZepListener()
    zep = FakeZeppelin.FakeZeppelin(zepl)
    zep.setPosition(x,y,z)
    zepl.zeppelin = zep
    communicator.addZeppelinListener(zepl,id)
    
root = Tk()
root.title("team ROOD")

Gui = GUI(root)

addSimulator(Gui.communicator, 0,0,0,10)
addSimulator(Gui.communicator, 100,50,50,11)

Gui.canvas.pack(side = LEFT)
Gui.text.pack()
Gui.labelframe.pack(expand="yes")
Gui.controlFrame.pack(expand="yes")

Gui.label1.grid(row = 0, column = 0)
Gui.label2.grid(row = 1, column = 0)
Gui.heightLabel.grid(columnspan = 2)
Gui.entry1.grid(row = 0, column = 1)
Gui.entry2.grid(row = 1, column = 1)
Gui.gobutton.grid(row = 2, column = 0)

Gui.upbutton.grid(row = 0, column = 1)
Gui.downbutton.grid(row = 2, column = 1)
Gui.leftbutton.grid(row = 1, column = 0)
Gui.rightbutton.grid(row = 1, column = 2)


#<<<<<<< HEAD
#file_path = 'C:\\Users\\Michiel\\Documents\\GitHub\\PENOROOD\\OTHER\\example_grid2.csv'
#=======
file_path = 'C:\\Users\\simon\\Desktop\\peno-1314-zeppelin-frame-master\\new_peno.csv'
#>>>>>>> check
if(len(file_path)>0):
    Gui.initiateFromFile(file_path)
else:
    Gui.grid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")

Gui.addDisplayedMessage("Nothing to be displayed atm.")
Gui.setHeightLabel("230cm")
Gui.updateCanvas()

#loop that registers action in the frame
#keep calling Gui.task every 1000ms
root.after(33,Gui.task)
root.grab_set()
root.mainloop()
