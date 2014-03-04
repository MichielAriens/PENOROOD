import RPI.FakeZeppelin as FakeZeppelin
import GUI.gridTest as gridTest
import GUI.GuiListener as GuiListener
import RPI.ZepListener as ZepListener
from GUI.GuiListener import *
from RPI.ZepListener import *
from GUI.gridTest import *
from tkinter import *

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

Gui.grid.addZeppelin(120, 243, 1)
Gui.grid.addZeppelin(200, 200, 2)
Gui.grid.setValue(5, 2, 3)
Gui.grid.setValue(1, 5, 1)
Gui.grid.setValue(7, 0, 1)
Gui.grid.setValue(9, 11,1)
Gui.grid.setValue(17, 0, 0)
Gui.grid.setValue(12,1,0)
Gui.grid.setValue(19, 11,0)
Gui.grid.setValue(13, 5,7)
Gui.grid.setValue(14, 5,8)
Gui.grid.setValue(15, 6,8)
Gui.grid.setValue(2, 7,8)
Gui.grid.setValue(3, 6,9)
Gui.grid.setValue(4, 7,9)
Gui.grid.setValue(1,10,11)



#Set values of positions on the grid
print(Gui.grid.getZeppelins())
Gui.addDisplayedMessage("Nothing to be displayed atm.")
Gui.setHeightLabel("230cm")
Gui.updateCanvas()

#loop that registers action in the frame
#keep calling Gui.task every 1000ms
root.after(33,Gui.task)
root.mainloop()
