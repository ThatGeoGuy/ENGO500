# Detect motion from PIR module and blink LED
# by AC Jan 26 2014

# Import required Python libraries
import RPi.GPIO as GPIO, time
#import testclass_olab3.py

### Use board pin numbering
##GPIO.setmode(GPIO.BOARD)
### Set pins
##GPIO.setup(7, GPIO.OUT)
##GPIO.output(7, False)
##GPIO.setup(11, GPIO.IN)
##GPIO.input(11,True)

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi (11 for now. gpio 0)
GPIO_PIR = 11
# Set pin as input, check connection to sensor
GPIO.setup(GPIO_PIR,GPIO.IN)
Current_State  = 0
Previous_State = 0
# data voltage

try:
 
  print "Waiting for PIR to settle ..."
 
  # This will run unless PIR intput is zero, ensuring that it settles
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
 
  print "  Ready"
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
 
    if Current_State==1 and Previous_State==0:
    # PIR is triggered
      print "  Motion detected!"
        # Voltage is reocrded as high
        # voltage.v  = high
        # ACTUAL VALUE
      # GPIO.output(7,True) - LED on
      # Update previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      # GPIO.output(7, False) - LED off
      print "  Ready"
      Previous_State=0

    # Output voltage and time to formatting function / database
    #  
    #
  
    # Wait for 10 milliseconds; may change with testing
    time.sleep(0.01)
 
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()

  #
  #if GPIO.input = GPIO.HIGH
  #

  
