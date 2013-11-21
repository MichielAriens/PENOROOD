import modules.hardware.distSensor as distSensor
import time


ds = distSensor.DistanceSensor()
wait = 0
waitIncrease = 5
amount = 100
maxi = 1000
myfile = open('data/exp/timing.csv','w')

while(wait < maxi):
    print str(wait) + "ms\n"
    myfile.write(str(wait)+";")
    i = 0
    while( i < amount):
        myfile.write(str(ds.measure()) + ";")
        time.sleep(wait/1000)
        i+=1        
    myfile.write("\n")
    wait += waitIncrease



"""
file = open('../../data/esp.csv','w')

max = 20
repeats = 50

i = 1
while i < max:
    #file.write(str(i) + ";")
    j=0
    totDur = 0
    while j < repeats:
        dur = int(round(time.time() * 1000))
        h = ds.getHeightRaw(i)
        totDur += int(round(time.time() * 1000)) - dur
        #file.write(str(h) + ";")
        print str(h)
        j += 1
        
    #file.write(";" + str(totDur) + "\n")
    i += 1"""
    
""" 
ds = distSensor.DistanceSensor()
#file = open('data/exp.csv','w')

max = 40
maxheight = 300
height = 50

while(height < maxheight):
    #file.write(str(height)+";")
    i = 0
    while i < max:
        h = ds.getHeightRaw(1)
        file.write(str(h) + ";")
        i+=1
    #file.write("/n")
    #height += 50
    #raw_input("move to" + str(height))
   """ 

    
    
        
