import thread
from RPI import FakeZeppelin as FakeZeppelin
from RPI.ZepListener import *
from GUI.gridTest import *
from Tkinter import *
from GUI.listener import *

served = True
simon = True
sim = True
listener = Listener()

if(served):

    creds = pika.PlainCredentials('rood','rood')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost', credentials = creds))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs',
                             type='topic')

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    #binding_keys = sys.argv[1:]
    #if not binding_keys:
    #    print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
    #    sys.exit(1)

    #for binding_key in binding_keys:
    channel.queue_bind(exchange='server',
                       queue=queue_name,
                       routing_key="#")

    print ' [*] Waiting for logs. To exit press CTRL+C'

    def callback(ch, method, properties, body):
        global listener
        listener.callback(ch,method,properties,body)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)






"""def addSimulator(communicator,x,y,z,id):
    zepl = ZepListener()
    zep = FakeZeppelin.FakeZeppelin(zepl)
    zep.setPosition(x,y,z)
    zepl.zeppelin = zep
    communicator.addZeppelinListener(zepl,id)
   """
root = Tk()
root.title("team ROOD")

Gui = GUI(root, listener)

#addSimulator(Gui.communicator, 0,0,0,10)
#addSimulator(Gui.communicator, 100,50,50,11)
#addSimulator(Gui.communicator, 100,50,50,12)
#addSimulator(Gui.communicator, 100,250,50,13)
#addSimulator(Gui.communicator, 141,233,50,14)
#addSimulator(Gui.communicator, 177,5,50,15)
#addSimulator(Gui.communicator, 440,300,50,16)
#addSimulator(Gui.communicator, 87,50,50,17)
#addSimulator(Gui.communicator, 100,250,50,18)
#addSimulator(Gui.communicator, 357,50,50,19)
#addSimulator(Gui.communicator, 100,50,50,20)



Gui.canvas.pack(side = LEFT)
Gui.text.pack()
Gui.debugtext.pack()
Gui.labelframe.pack(expand="yes")
Gui.controlFrame.pack(expand="yes")

Gui.label1.grid(row = 0, column = 0)
Gui.label2.grid(row = 1, column = 0)
Gui.label3.grid(row = 2, column = 0)
Gui.entry1.grid(row = 0, column = 1)
Gui.entry2.grid(row = 1, column = 1)
Gui.entry3.grid(row = 2, column = 1)
Gui.gobutton.grid(row = 3, column = 0)
Gui.sendbutton.grid(row = 3, column = 1)
Gui.overrideButton.grid(row = 3, column = 2)

Gui.upbutton.grid(row = 0, column = 1)
Gui.downbutton.grid(row = 2, column = 1)
Gui.leftbutton.grid(row = 1, column = 0)
Gui.rightbutton.grid(row = 1, column = 2)


file_path = "C:\\Users\\Michiel\\Documents\\GitHub\\PENOROOD\\OTHER\\grid25-04.csv"
if(simon):
    file_path = "C:\Users\simon\Documents\GitHub\PENOROOD\OTHER\grid25-04.csv"
if(len(file_path)>0):
    Gui.initiateFromFile(file_path)
else:
    Gui.grid.initiate("0=0=gh=rs=bc=gr=0=0=0=wr=ys=bc=ws=gr=0=0=0=rr=yr=gh=wc=bh=wr=0=bs=rs=gc=bs=bh=bc=gs=0=0=br=yh=rh=gs=gc=yh=0=0=bh=rh=ws=wr=ys=0=0=0=0=gh=rs=bc=gr")

if(served):
    thread.start_new_thread(channel.start_consuming,())

Gui.addDisplayedMessage("Nothing to be displayed atm.")
Gui.updateCanvas()

#loop that registers action in the frame
#keep calling Gui.task every 33ms
root.after(33,Gui.task)
root.grab_set()
root.mainloop()
while True:
    pass
