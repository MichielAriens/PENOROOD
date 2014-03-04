
try:
    import RPi.GPIO
    simMode = False
except ImportError:
    simMode = True
    
import os
import thread
import time
import subprocess


class FakeCamera:
    pass

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
                x = out.readline().replace("\n","")
                y = out.readline().replace("\n","")
                command = out.readline().replace("\n","")
                if (x == "" or y == "" or command == ""):
                    eof = True
                else:
                    retval.append([x,y,command])
        except:
            pass
        return retval
            
        
