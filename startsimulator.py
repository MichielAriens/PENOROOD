import RPI.FakeZeppelin as fz


startgoal = (50,50)
ipads = [(1,20,70,"bleep",False,False),(2,220,300,"bleep",False,False)]
targets = [(1,0,0),(2,100,0),(3,200,200)]

zep = fz.FakeZeppelin(startgoal, ipads, targets)