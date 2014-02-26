from enum import Enum
class Axis(Enum):
    x = 1
    y = 2
    z = 3

class Vector3:
    self.x = 0
    self.y = 0
    self.z = 0
    
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
        return x
    
    def snd(self):
        return y
    
    def thrd(self):
        return z
    
    def asArray(self):
        return [x,y,z]