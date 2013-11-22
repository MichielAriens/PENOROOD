import time
from decimal import *

count = 10000


prev = Decimal(time.time())
while(count > 0):
    now = Decimal(time.time())
    #print str(now - prev)
    b = 0.01 >=  (now - prev)
    if not b:
        print "An interrupt happened"
    prev = now
    count -= 1
    
    
    
    
