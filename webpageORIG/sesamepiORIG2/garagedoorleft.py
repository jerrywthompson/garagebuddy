#!/usr/bin/python

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.LOW)
          time.sleep(0.5) 
          GPIO.output(i, GPIO.HIGH)
          GPIO.cleanup()
     

try: 
    trigger()
         
      
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()