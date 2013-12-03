import modules.hardware.distSensor as distSensor
ds = distSensor.DistanceSensor()
for x in range(0, 10):
    print str(ds.measure())
