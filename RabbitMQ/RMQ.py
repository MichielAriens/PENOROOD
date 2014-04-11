from RabbitMQ import RMQreceiver as r
from RabbitMQ import RMQSender as s
from RPI.software import main
from RPI.hardware.distSensor import DistanceSensor as ds

class RMQ:

    def __init__(self,ip='localhost'):
        self.ip = ip
        self.sender = s.Sender
        self.receiver = r.Receiver
        self.sendRequest = SendRequest

        self.startRMQ()

    def startRMQ(self):
        self.receiver.startReceiving()

    def sendCommand(self,command):
        print 'command: ' + command
        self.sender.sendCommand(command)

    def sendLocation(self):
        zeppelinCoordinates = main.userInterface.findZeppelinLocation()
        command = self.sendRequest.location(zeppelinCoordinates)
        self.sendCommand(command)

    def sendHeight(self):
        pass


class SendRequest:

    def __init__(self):
        pass

    def location(self,x,y):
        return 'rood.info.location ' + str(x) + ',' + str(y)

    def height(self,z):
        return 'rood.info.height ' + str(z)

    def move(self,x,y):
        return 'rood.hcommand.move ' + str(x) + ',' + str(y)

    def elevate(self,z):
        return 'rood.hcommand.elevate' + str(z)

    def motor(self,motorIndex,percentage):
        if(motorIndex == 1 or motorIndex == 2 or motorIndex == 3):
            if(self.validPercentage(percentage)):
                return 'rood.lcommand.motor' + str(motorIndex) + ' ' + str(percentage)
            return 'rood.lcommand.motor' + str(motorIndex) + ' 100'

    def validPercentage(self,perc):
        if(perc >= -100 and perc <= 100):
            return True
        else: return False

class ReceiveRequest:

    def __init__(self):
        self.color = 'rood'

    def selectTeamColor(self,selectedColor='rood'):
        self.color = selectedColor

