#Controls the positioning of the zeppelin at high level.
#You tell this class what results you wish to achieve instead of how to achieve them.


#--------------------------------------

import hardware.distSensor as ds
class LowLevelController:
    def __init__(self):
        #Primary declarations.
        #Motors:
        self.lift = None
        self.thust = None
        self.rudder = None
        
        #Altimeter
        self.altimeter = ds.FakeDistanceSensor()
        
        #Camera
        self.camera = None

