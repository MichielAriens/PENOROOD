#Controls the positioning of the zeppelin at high level.
#You tell this class what results you wish to achieve instead of how to achieve them.


#-------------------------------------
import grid as gridTest
import camera
import distSensor as ds
import motor as motor
import camera as cam
import thread
import time
import random
import shapeRecognition as sr
import ZepListener
import os

import picamera
sf = sr.ShapeFinder()
path = "/home/pi/zep2/output/data.jpg"

def analyze():
    global sf,path
    with picamera.PiCamera() as camera:
        camera.resolution = (500,500)
        camera.capture(path, "jpeg")
        
    sf.findAll(path)


class Zeppelin:
    #initmethod variables (call start to invoke backround methods)
    def __init__(self):
        print "loading zeppelin"
        self.override = False
        self.loadGrid("/home/pi/zep3/PENOROOD/OTHER/grid25-04.csv")
        #still requirs grid loading
        self.path = "/home/pi/temp/img.jpg"
        #Init PID (0.1,0,0.5) works slightly, (0.1,0.05,3) better P to 0.2 increases responsiveness, I increses overshoot but decreases settletime
        #D decreases overshoot but engthens settletime. (slows machine down)
        self.altimeter = ds.BackgroundDistanceSensor()
        #self.lift = motor.PWMMotor(24,4)
        #self.xMot = motor.PulsedMotor(17,23)
        #self.yMot = motor.PulsedMotor(9,7)

        self.motorY = motor.PulsedMotor(24,4)
        self.motorX = motor.PulsedMotor(17,23)
        self.lift = motor.PWMMotor(9,7)

        self.heightPID = PID(5,0.5,5)
        self.xPID = PID(1,0,0.1)
        self.yPID = PID(1,0,0.1)
        print("loading camera")
        self.camera = camera.Camera()
        self.listener = ZepListener.zepListener(self)
        
        self.dHeight = self.altimeter.getHeight()
        self.dHeight = 70
        self.dPos = (0,0)
        self.pos = (0,0)
        self.height = 0
        
        self.heightPID.setPoint(self.dHeight)
        self.xPID.setPoint(self.dPos[0])
        self.yPID.setPoint(self.dPos[1])

        self.goal = (0,0,0) #tuple = (volgnummer,x,y)
        self.ipads = [(1,0,0,"bleep",False,False),(2,220,300,"bleep",False,False)] # tuple = (ipadID,x,y,qr,ipad_boolean,qr_boolean) ipad_boolean/qr_boolean = false if zep hasnt been there yet
        self.targets = [(1,0,0),(2,100,0),(3,200,200)] #tuple = (volgnummer,x,y)
        self.targetcount = len(self.targets) #increase this when you add a target
        self.goalnumber = 0 #increase this when you reached goal

        self.lastQRRead = time.time() - 5

        print("zeppelin loaded!")
    
    #Used to set the desired height.
    #Effects will only become apparent after _keepHeight pulls the new info
    def setDesiredHeight(self,height):
        self.dHeight = height
        self.pid.setPoint(height)

    def getLiftMotor(self):
        return self.lift

    def getXMotor(self):
        return self.motorX

    def getYMotor(self):
        return self.motorY
        
    def loadGrid(self, path):
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
        number_of_rows = len(data)
        number_of_columns = len(data[0])
        init_string = list[0]
        self.grid = gridTest.GRID(number_of_columns, number_of_rows)
        self.grid.initiate(init_string);
        
    #Algorithm to invoke motors to achieve a certain height
    #Python convention: methods names preceded by '_' should be deemed 'private'
    def _keepHeight(self):
        time.sleep(1)
        while(True):
            #Set the thrust to the PID output.
            self.height = self.altimeter.getHeight()
            self.listener.pushHeight(self.height)
            self.lift.setThrust(self.yPID.setPoint(self.height))
            time.sleep(0.5)

    def _keepPos(self):
        time.sleep(1)
        while(True):
            if not self.override:
                self.pos = self.camera.analyzePosition(self.grid)
                self.listener.pushPosition(self.pos)
                self.doAction()


    def doAction(self):
        if not self.override:
            self.motorX.setThrust(self.xPID.update(self.pos[0]))
            self.motorY.setThrust(self.yPID.update(self.pos[1]))
        if(self.checkGoal() == True):
            self.checkTargets()
            self.xPID.setPoint(self.goal[0])
            self.yPID.setPoint(self.goal[1])


    
    #Starts running background threads
    # _keepHeight
    def start(self):
        print "Starting zeppelin main loop."
        thread.start_new(self.listener.start, ())
        thread.start_new(self._keepHeight, ())
        thread.start_new(self._keepPos, ())

    def checkTargets(self):
        hasNew = False
        if(self.goalnumber == 0):
            nextgoalnumber = 1
        else:
            nextgoalnumber = self.goal[0] + 1
        for i in range(len(self.targets)):
            tup = self.targets[i]
            if(tup[0] == nextgoalnumber):
                self.goal = tup
                hasNew = True
                self.goalnumber = nextgoalnumber
        if(hasNew == False):
            self.checkIpad()

    def checkGoal(self):
        currentpos = self.pos
        range = 10
        if(( (((currentpos[0] > (self.goal[1]-range))) and ((currentpos[0] < (self.goal[1]+range)))) and (((currentpos[1] > (self.goal[2]-range))) and ((currentpos[1] < (self.goal[2]+range)))))):
            return True
        return False

    def getNextIpad(self):
        for i in range(len(self.ipads)):
            pad = self.ipads[i]
            if(pad[4] == False):
                return (pad[1], pad[2])
        return None

    def checkIpad(self):
        addedQR = False
        addedipad = False
        for j in range(len(self.ipads)):
            pad = self.ipads[j]
            if(pad[4] == True and pad[5] == False and addedQR == False):
                qr = pad[3]
                self.completeQR(qr)
                self.ipads.remove(pad)
                self.ipads.append((pad[0],pad[1],pad[2],pad[3],pad[4],True))
                addedQR = True
        for i in range(len(self.ipads)):
            pad = self.ipads[i]
            if(pad[4] == False and addedQR == False and addedipad == False):
                print("added ipad")
                self.targets.append((self.targetcount+1, pad[1], pad[2]))
                self.targetcount += 1
                self.ipads.remove(pad)
                self.ipads.append((pad[0],pad[1],pad[2],pad[3],True,pad[5]))
                addedipad = True
        
   
    def getPos(self):
       return self.camera.analyzePosition(self.grid)

    def completeQR(self):
        print "READING QR"
        #Pic in memory.
        now = time.time()
        if self.lastQRRead <= now - 5:
            #tablet numbering starts with 1
            self.listener.pushPublicKey(self.goal[0] + 1)
            os.system("java -jar read_qr_zep.jar /home/pi/zep2/output/path.jpg > /home/pi/temp/qrresults.txt")
            file = open("/home/pi/temp/qrresults.txt","r")
            results = file.read()
            print str(results)

        else:
            self.listener.pushMessage("qr not read, too early to try again.")

       

class PID:
    """
    Discrete PID control
    """

    def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=100, Integrator_min=-100):

        self.Kp=P
        self.Ki=I
        self.Kd=D
        self.Derivator=Derivator
        self.Integrator=Integrator
        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min

        self.set_point=0.0
        self.error=0.0

    def update(self,current_value):
        """
        Calculate PID output value for given reference input and feedback
        """

        self.error = self.set_point - current_value

        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * ( self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error

        if self.Integrator > self.Integrator_max:
            self.Integrator = self.Integrator_max
        elif self.Integrator < self.Integrator_min:
            self.Integrator = self.Integrator_min

        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value

        return PID

    def setPoint(self,set_point):
        """
        Initilize the setpoint of PID
        """
        self.set_point = set_point
        self.Integrator=0
        self.Derivator=0

    def setIntegrator(self, Integrator):
        self.Integrator = Integrator

    def setDerivator(self, Derivator):
        self.Derivator = Derivator

    def setKp(self,P):
        self.Kp=P

    def setKi(self,I):
        self.Ki=I

    def setKd(self,D):
        self.Kd=D

    def getPoint(self):
        return self.set_point

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.Integrator

    def getDerivator(self):
        return self.Derivator

    
        
    
        
        
    
    
    
        
