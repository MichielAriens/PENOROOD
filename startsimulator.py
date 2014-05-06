import RPI.FakeZeppelin as fz


startgoal = (50,50)
ipads = [(1,160,156,"bleep",False,False),(2,440,156,"bleep",False,False),(3,240,329,"bleep",False,False)]
targets = [(1,0,0)]

zep = fz.FakeZeppelin(startgoal, ipads, targets)