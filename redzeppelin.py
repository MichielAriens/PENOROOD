#!/usr/bin/env python

#set up zeppelin (temp)
import modules.lowLevelCotroller as llcp
llc = llcp.LowLevelController()


#Bottle allows explicit linking of a URL request (GET, POST, ...) to python methods. 
from modules.srv.bottle import *

#placeholder method
def check_login(user,passw):
    return True

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

run(host='localhost', port=8080, debug=True)