import distSensor
import time

ds = distSensor.DistanceSensor()

file = open('../../data/esp.csv','w')

max = 20
repeats = 50

i = 0
while i < max:
    file.write(str(i) + ";")
    j=0
    totDur = 0
    while j < repeats:
        dur = time.gmtime()
        h = ds.getHeightRaw(i)
        totDur += time.gmtime() - dur
        file.write(str(h + ";"))
        j += 1
        
    file.write(";" + str(totDur) + "\n")
    i += 1
    

    
    
        
