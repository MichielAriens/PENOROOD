import COMMON.enum as enum
class Axis(enum.Enum):
  x = 1
  y = 2
  z = 3
    
################################################

import RPI.hardware.motor as motor

   #//TODO PID's for all axis. 
class Vector3:
    
    def __init__(self,x,y,z):
        self.x = 0
        self.y = 0
        self.z = 0
        
    def add(self,other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def inverse(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    #Get a specific axis.
    def getAxis(self,axis):
        if axis == Axis.x:
            return self.x
        elif axis == Axis.y:
            return self.y
        elif axis == Axis.z:
            return self.z
        else:
            return None
        
    #Set a specific axis.
    def setAxis(self,axis, val):
        if axis == Axis.x:
            self.x = val
        elif axis == Axis.y:
            self.y = val
        elif axis == Axis.z:
            self.z = val
        else:
            pass
        
            
    
    def fst(self):
        return self.x
    
    def snd(self):
        return self.y
    
    def thrd(self):
        return self.z
    
    def asArray(self):
        return [self.x,self.y,self.z]
           
class FakeEnvironment:
    
    def __init__(self):
        self.pos = Vector3(0,0,0)
        self.speed = Vector3(0,0,0)
        self.force = Vector3(0,0,0)
        #pull of gravity somewhere around 1 m/s².
        import random
        self.mass = random.gauss(1,0.05)
        print("mass of the fake zeppelin is " + str(self.mass))
        self.gravity = Vector3(0,0,self.mass * 9.81)
        self.lift = Vector3(0,0,self.mass * 8)
    
    
    def update(self):
        while True:
            
            actuatedForce = self.force.add(self.gravity.inverse()).add(self.lift)
            self.speed = self.speed.add(force)
            
            if(self.pos.thrd() < 0):
                self.pos = 0
                self.vSpeed = 0
            else:
                self.vSpeed += force/self.mass
                self.height += self.vSpeed
            time.sleep(1)

import _thread as thread
 
class FakeZeppelin:
    
    def __init__(self, listener):
        self.height = 0
        self.zepListener = listener 
        self.motorOffset = 50
        self.fe = FakeEnvironment()
        self.motorX = motor.FakeMotor(self.fe,Axis.x)
        self.motorY = motor.FakeMotor(self.fe,Axis.y)
        self.motorZ = motor.FakeMotor(self.fe,Axis.z)
        #self.altimeter = ds.FakeDistanceSensor2(self.fe)
        thread.start_new(self.fe.update, ())
        #self.pid = PID(0.2,0.1,5)
        self.camera = None
        
        self.fe.force = Vector3(0.5,0.5,0)
        
    def getPosition(self):
        return self.fe.pos
    
    def getSpeed(self):
        return self.fe.speed
    
        
 