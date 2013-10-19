#!/usr/bin/env python

#set up zeppelin (temp)
import modules.lowLevelCotroller as llcp
llc = llcp.LowLevelController()


<<<<<<< HEAD
#Bottle allows explicit linking of a URL request (GET, POST, ...) to python methods. 
from modules.srv.bottle import *
=======
#import modules.hardware.distSensor as distSensor
#import camera
>>>>>>> Python-branch

#placeholder method
def check_login(user,passw):
    return True

<<<<<<< HEAD
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
    global llc
    return str(llc.altimeter.getHeight())
    
import modules.srv.server

run(host='localhost', port=8080, debug=True)


#Old testing code below
=======
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


    
    
        
>>>>>>> Python-branch
    
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


