import RPI.FakeZeppelin as FakeZeppelin
import GUI.gridTest as gridTest
import GUI.GuiListener as GuiListener
import RPI.ZepListener as ZepListener
from GUI.GuiListener import *
from RPI.ZepListener import *
from GUI.gridTest import *
from tkinter import *
import tkinter as tkinter
from tkinter import filedialog








root = Tk()
root.title("team ROOD")

zepl = ZepListener()
zep = FakeZeppelin.FakeZeppelin(zepl)
zepl.zeppelin = zep
guil = GuiListener()
Gui = GUI(root, guil)
zepl.link(guil)

#pack() is used for positioning/drawing the widgets on the frame
Gui.canvas.pack(side = LEFT)
Gui.text.pack()
Gui.labelframe.pack(expand="yes")
Gui.controlFrame.pack(expand="yes")
#grid() positions/draws widget in a grid-like-layout
Gui.label1.grid(row = 0, column = 0)
Gui.label2.grid(row = 1, column = 0)
Gui.heightLabel.grid(columnspan = 2)
Gui.entry1.grid(row = 0, column = 1)
Gui.entry2.grid(row = 1, column = 1)

Gui.upbutton.grid(row = 0, column = 1)
Gui.downbutton.grid(row = 2, column = 1)
Gui.leftbutton.grid(row = 1, column = 0)
Gui.rightbutton.grid(row = 1, column = 2)

root2 = tkinter.Tk()
root2.withdraw()

file_path = tkinter.filedialog.askopenfilename()
print(file_path)
if(len(file_path)>0):
    Gui.initiateFromFile(file_path)
else:
    Gui.grid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")


Gui.grid.addZeppelin(120, 243, 1)
Gui.grid.addZeppelin(200, 200, 2)
Gui.addDisplayedMessage("Nothing to be displayed atm.")
Gui.setHeightLabel("230cm")
Gui.updateCanvas()

#loop that registers action in the frame
#keep calling Gui.task every 1000ms
root.after(33,Gui.task)
root.mainloop()
