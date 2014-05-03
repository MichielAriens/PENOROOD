import pygame
import time
import thread

#Find all joysticks
pygame.joystick.init()
pygame.display.init()


class JoyStick:
    def __init__(self):
        pygame.joystick.init()
        pygame.display.init()
        self.js = pygame.joystick.Joystick(0)
        self.js.init()
        thread.start_new(self.pumpInBackground,())

    def pumpInBackground(self,dt = 0.1):
        while(True):
            pygame.event.pump()
            time.sleep(dt)

    #   X axis from joystick (forwards backward axis).
    #   @return x = [-1.0,1.0] positive for forwards
    #
    def getX(self):
        return -1 * self.js.get_axis(1)

    #   Y axis from joystick (left right axis).
    #   @return y = [-1.0,1.0] positive for right
    #
    def getY(self):
        return self.js.get_axis(0)

    #   Z axis from joystick (throttle slider).
    #   @return z = [-1.0,1.0] positive for forwards. 0 in center
    #
    def getZ(self):
        return -1 * self.js.get_axis(0)


"""
while(True):
    pygame.event.pump()
    print "axis 0: " + str(js.get_axis(0))      #-left      +right          ailerons
    print "axis 1: " + str(js.get_axis(1))      #-forwards  +backwards      elevator
    print "axis 2: " + str(js.get_axis(2))      #-forwards  +backwards      throttle
    print "axis 3: " + str(js.get_axis(3))      #-left      +right          rudder
    time.sleep(0.1)
    """
