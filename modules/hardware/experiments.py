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
        dur = int(round(time.time() * 1000))
        h = ds.getHeightRaw(i)
        totDur += int(round(time.time() * 1000)) - dur
        file.write(str(h) + ";")
        j += 1
        
    file.write(";" + str(totDur) + "\n")
    i += 1
    

    
    
        
