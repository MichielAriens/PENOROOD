import distSensor

ds = distSensor.DistanceSensor()

file = open('../../data/esp.csv','w')

max = 100
repeats = 100

i = 0
while i < max:
    file.write(str(i) + ";")
    j=0
    while j < repeats:
        file.write(str(ds.getHeightRaw(i)) + ";")
        j += 1
        
    file.write("\n")
    i += 1
    

    
    
        
