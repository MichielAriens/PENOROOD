
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os
import thread
import time
import subprocess

class Camera:    
    def __init__(self,height = 200, width = 200, output = "still.jpg", root = "data/cam/", readroot = "images/"):
        self.height = width
        self.width = width      
        self.output = output  
        self.root = root
        self.readroot = readroot
    
    
    #launches repeating 
    def click(self):
        #command = "raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -q 5 -o " + self.root + self.output + " -t 9999999 -th 0:0:0 -tl 100 -n &"
        command = "raspistill -w " + str(self.width) + " -h " + str(self.height)+ " -o " + self.root + self.output + " -t 0.001 -n"
        print "trying: " + command
        os.system(command)
        timestamp = time.time()
        tsfile = open(self.root + "TIMESTAMP",'w')
        tsfile.write(str(timestamp))
        tsfile.close()
        
    #provide the interval in ms
    def detectMovement(self, interval = 1000):
        pass #os.system("java /home/pi/PENOROOD/resources/test_multi_QR_400x400.jar")
        
    #Returns a list of lists [[x,y,info]] where x & y represent the position of the found QR code in the screen (taking the midpoint of the screen as the origin.
    #Info contains a formatted string to be parsed higher up.
    def getQR(self):
        retval = []
        try:
            writeout = "data/cam/QR"
            os.system("java -jar resources/QR_decoder.jar > " + writeout)
            #p = subprocess.Popen("java -jar resources/QR_decoder.jar")
            #out, err = p.communicate()
            #Try to open the file 
            out = None
            while(out == None):
                try:
                    out = open(writeout,'r')
                except IOError:
                    pass
            eof = False
            while not eof:
                x = float(out.readline().replace("\n","")) - self.width/2
                y = float(out.readline().replace("\n","")) - self.height/2
                command = out.readline().replace("\n","")
                if (x == "" or y == "" or command == ""):
                    eof = True
                else:
                    retval.append([x,y,command])
        except:
            pass
        return retval
            
        
