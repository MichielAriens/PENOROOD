#!/usr/bin/env python

# Import time module to keep track of time
import time

# Import RPi.GPIO module to access GPIO pins
import RPi.GPIO as GPIO

# Set the pins we use
# -----------------------------------------------------------------
# Here we use the BCM notation.  This is the notation corresponding
# to the GPIO labels.  17 means GPIO17, 4 means GPIO4.
echo_gpio = 17
trig_gpio = 4

# Initiate the GPIO pins
# -----------------------------------------------------------------
# First we set the addressing mode to BCM, corresponding to how we
# have setup the echo_gpio and trig_gpio variables.
#
# Next we set the echo gpio in input mode and the trig_gpio in
# output mode.  Finally, we set the output signal on trig_gpio to
# False, meaning no signal.
# 
# For more information about the RPi.GPIO module check out:
# http://pypi.python.org/pypi/RPi.GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setup( echo_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup( trig_gpio, GPIO.OUT )
GPIO.output( trig_gpio, False )

# Setup some other variables
# -----------------------------------------------------------------
loop = True          # Infinite loop
trig_duration = 0.0001        # Trigger duration
inttimeout = 2100        # Timeout on echo signal
v_snd = 340.29            # Speed of sound in m/s

# Wait for 2 seconds for the ultrasonics to settle
# -----------------------------------------------------------------
# Probably not needed...
time.sleep( 2 )

while loop:
    # Trigger trig_gpio for trig_duration
    GPIO.output( trig_gpio, True )
    time.sleep( trig_duration )
    GPIO.output( trig_gpio, False )
    
    # Wait for the echo signal (or timeout)
    countdown_high = inttimeout
    while ( GPIO.input( echo_gpio ) == 0 and countdown_high > 0 ):
        countdown_high -= 1

    # If we've gotten a signal
    if countdown_high > 0:
        echo_start = time.time()
        
        countdown_low = inttimeout
        while( GPIO.input( echo_gpio ) == 1 and countdown_low > 0 ):
            countdown_low -= 1
        echo_end = time.time()

        echo_duration = echo_end - echo_start
        
    # Display the distance, unless there was a timeout on 
    # the echo signal
    if countdown_high > 0 and countdown_low > 0:
        # echo_duration is in seconds, so multiply by speed
        # of sound.  Divide by 2 because of rounttrip and 
        # multiply by 100 to get cm instead of m.
        distance = echo_duration * v_snd * 100 / 2
        print "Distance = " + str( distance ) + "cm"
    else:
        print "Timeout"

# Wait before retriggering
time.sleep( 1 )