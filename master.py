#!/usr/bin/env python

import os, sys

print "I'm going to fork now - the child will write something to a pipe, and the parent will read it back"

r, w = os.pipe() # these are file descriptors, not file objects

pid = os.fork()
if pid:
    # we are the parent
    os.close(w) # use os.close() to close a file descriptor
    r = os.fdopen(r) # turn r into a file object
    print "parent: reading"
    txt = r.read()
    os.waitpid(pid, 0) # make sure the child process gets cleaned up
else:
    # we are the child
    os.close(r)
    w = os.fdopen(w, 'w')
    #Write to this writer
    
    w.close()
    print "child: closing"
    sys.exit(0)

#No children beyong this point
#r is the reader




print "parent: got it; text =", txt



"""
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
    
    
    
    
"""