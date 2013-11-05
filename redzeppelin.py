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

#import Bottle: allows explicit linking of a URL request (GET, POST, ...) to python methods (see below)
from modules.srv.bottle import *

#Homepage.
@route('/')
def home():
    return static_file("index.html",root="modules/srv/")

#HTML must be loaded explicitly from the root folder.
@route('/<filename:re:.*\.html>')
def send_html(filename):
    return static_file(filename, root='modules/srv/')

#Images must be loaded explicitly from the images folder.
@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='modules/srv/images/', mimetype='image/png')

#CSS, must be loaded from the css folder.
@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='modules/srv/css/', mimetype='text/css')

@route('/scripts/<filename:re:.*\.js>')
def send_javascript(filename):
    return static_file(filename, root='modules/srv/scripts/', mimetype='text/javascript')

@route('/height')
def send_height():
    global zeppelin
    return str(zeppelin.llc.altimeter.getHeight())

@route('/lift')
def send_lift():
    global zeppelin
    return str(zeppelin.llc.lift.thrust)

@route('/info')
def send_info():
    global zeppelin
    global simMode
    if simMode == "sim":
        Xlift = str(zeppelin.llc.lift.thrust)
        Xheight = str(zeppelin.llc.altimeter.getHeight())
        return {'lift':Xlift,'height':Xheight}
    else:  #Rpi mode
        Xlift = str(zeppelin.llc.lift.thrust)
        Xthrust = str(zeppelin.llc.thrust.thrust)
        Xrudder = str(zeppelin.llc.rudder.thrust)
        Xheight = str(zeppelin.llc.altimeter.getHeight())
        return {'lift': Xlift,'thrust': Xthrust, 'rudder': Xrudder, 'height': Xheight}
    
@post('/setheight')
def set_height():
    global zeppelin
    try: 
        nheight = float(request.forms.get('dHeight'))
    except ValueError:
        return
    zeppelin.llc.setDesiredHeight(nheight)
    
@post('/setmotors')
def set_motors():
    global zeppelin
    try:
        nLift = float(request.forms.get('lift'))
        nThrust = float(request.forms.get('thrust'))
        nRudder = float(request.forms.get('rudder'))
    except ValueError:
        pass
    zeppelin.llc.lift.setThrust(nLift)
    zeppelin.llc.thrust.setThrust(nThrust)
    zeppelin.llc.rudder.setThrust(nRudder)
    
    
    
mode = raw_input("ControlMode?\n   auto\n   controlled(or anything else)")
#start zeppelin background tasks.
if mode == "auto":
    zeppelin.llc.start()
#Start the server
run(host='localhost', port=54322, debug=True)



