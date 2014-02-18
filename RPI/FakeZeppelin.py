from enum import Enum
class Axis(Enum):
    x = 1
    y = 2
    z = 3
    
################################################

import hardware.motor as motor
class FakeZeppelin:
    self.height = 0
    
    def __init__(self):
        self.motorOffset = 50
        self.fe = FakeEnvironment()
        self.motorX = motor.FakeMotor(Axis.x)
        self.motorY = motor.FakeMotor(Axis.y)
        self.motorZ = motor.FakeMotor(Axis.z)
        self.altimeter = ds.FakeDistanceSensor2(self.fe)
        thread.start_new(self.fe.update, ())
        self.pid = PID(0.2,0.1,5)
        self.camera = None
        
        
class FakeEnvironment:
    self.pos = (0,0,0) 
    self.speed = (0,0,0)
    self.force = (0,0,0)
    
    def __init__(self):
        #pull of gravity somewhere around 10 newtons
        self.mass = random.gauss(1,0.05)
        print "mass of the fake zeppelin is " + str(self.mass)
        self.gravity = (0,0,-self.mass * 9.81)
    
    
    def update(self):
        while True:
            
            force = self.force - self.gravity 
            if(self.height < 0):
                self.height = 0
                self.vSpeed = 0
            else:
                self.vSpeed += force/self.mass
                self.height += self.vSpeed
            time.sleep(1)
            
class Vector3:
    self.x = 0
    self.y = 0
    self.z = 0
    
    def __init__(self,x,y,z):
        self.x = 0
        self.y = 0
        self.z = 0
        
    