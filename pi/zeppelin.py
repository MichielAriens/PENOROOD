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
        print("loading zeppelin")
        self.grid = self.loadGrid("/home/pi/zep3/PENOROOD/OTHER/new_peno.csv")
        #still requirs grid loading
        self.path = "/home/pi/temp/img.jpg"
        #Init PID (0.1,0,0.5) works slightly, (0.1,0.05,3) better P to 0.2 increases responsiveness, I increses overshoot but decreases settletime
        #D decreases overshoot but engthens settletime. (slows machine down)
        self.altimeter = ds.BackgroundDistanceSensor()
        self.lift = motor.PWMMotor(24,4)
        self.xMot = motor.PulsedMotor(17,23)
        self.yMot = motor.PulsedMotor(9,7)
        self.heightPID = PID(5,0.5,5)
        self.xPID = PID(1,0,0.1)
        self.yPID = PID(1,0,0.1)
        print("loading camera")
        self.camera = camera.Camera()
        
        self.dHeight = self.altimeter.getHeight()
        self.dPos = (0,0)
        
        self.heightPID.setPoint(self.dHeight)
        
        self.xPID.setPoint(self.dPos[0])
        self.yPID.setPoint(self.dPos[1])
        
        print("zeppelin loaded!")
    
    #Used to set the desired height.
    #Effects will only become apparent after _keepHeight pulls the new info
    def setDesiredHeight(self,height):
        self.dHeight = height
        self.pid.setPoint(height)

    def getLiftMotor(self):
        return self.lift

    def getXMotor(self):
        return self.xMot

    def getYMotor(self):
        return self.yMot
        
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
        number_of_rows = len(data);
        number_of_columns = len(data[0])
        init_string = list[0]
        self.grid = gridTest.GRID(number_of_columns, number_of_rows)
        self.grid.initiate(init_string);
        
    #Algorithm to invoke motors to achieve a certain height
    #Python convention: methods names preceded by '_' should be deemed 'private'
    def _keepHeight(self):
        while(True):
            #Set the thrust to the PID output.
            pos = self.camera.analyzePosition(self.grid)
            self.lift.setThrust(self.heightPID.update(self.altimeter.getHeight()) + self.motorOffset)
            self.xMot.setThrust(self.xPID.update(self.pos[0]))
            self.xMot.setThrust(self.xPID.update(self.pos[1]))
            time.sleep(1)       
    
    #Starts running background threads
    # _keepHeight
    def start(self):
        thread.start_new(self._keepHeight, ())
   
    def getPos(self):
       return self.camera.analyzePosition(self.grid)
       

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

    
        
    
        
        
    
    
    
        
