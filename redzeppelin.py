#!/usr/bin/env python

import modules.lowLevelController as llcp

#Check to see whether we're running on the RaspberryPi. store result in simMode
simMode = "RPi"
try:
    import RPi.GPIO as GPIO
except ImportError:
    simMode = "sim"
    print "running in simulation mode."

#Zeppelin class.
class Zeppelin:
    def __init__(self, simMode = "RPi"):
        self.llc = llcp.LowLevelController(simMode)

#########################
####Initiate zeppelin####
#########################
zeppelin = Zeppelin(simMode)

######################
####Server-methods####
######################

#imort Bottle: allows explicit linking of a URL request (GET, POST, ...) to python methods (see below)
from modules.srv.bottle import *

#Homepage.
@route('/')
def home():
    return static_file("index.html",root="modules/srv/")

#Images must be loaded explicitely from the images folder.
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='modules/srv/images/', mimetype='image/png')

#CSS, must be loaded from the css folder.
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='modules/srv/css/', mimetype='text/css')

@route('/scripts/<filename:re:.*\.js')
def send_javascript(filename):
    return static_file(filename, root='modules/srv/scripts/', mimetype='text/javascript')

@route('/height')
def send_height():
    global zeppelin
    return str(zeppelin.llc.altimeter.getHeight())
    
    

#start zeppelin background tasks.
zeppelin.llc.start()
#Start the server
run(host='localhost', port=54322, debug=True)











#Old testing code below

"""
def testDistSens():
    continuebool = True
    distSensor1 = distSensor.DistanceSensor()

    print "commands: \n q: quit \n m:measure \n c: calibrate"
    
    
    while continuebool:
        command = raw_input("> ")
        if(command == "q"):
            continuebool = False
        elif(command == "c"):
            command = raw_input("Set height: ")
            distSensor1.calibrate(float(command))
        else:
            height = distSensor1.getHeight()
            print str(height)
     
def testCamera():
    continuebool = True
    cam = camera.Camera()
    while continuebool:
        print str(cam.detectMovement())
        cont = raw_input("continue? ('n' to stop): ")
        if cont == "n":
            continuebool = False
            
testDistSens()"""


    
    
        

    
"""
@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
"""


