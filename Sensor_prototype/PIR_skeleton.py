# Detect motion from PIR module
# SKELETON code modified from http://www.raspberrypi-spy.co.uk
# Added computation of voltage time from PIR and checks
# by AC Jan 06 2014


# Import required Python libraries
import RPi.GPIO as GPIO, time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7

# Set pin as input, check connection to sensor
GPIO.setup(GPIO_PIR,GPIO.IN)
Current_State  = 0
Previous_State = 0

# Check unique ID and datastream
#
#


# Define function to measure charge time
  # allows for PROPORTIONAL motion level not just high/low
  # (need breadboard w/resistor and capacitor in series)
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(0.1)

  GPIO.setup(PiPin, GPIO.IN)
  # Count loops until voltage across capacitor reads high on GPIO
  while (GPIO.input(PiPin) == GPIO.LOW):
    measurement += 1
  return measurement




try:
 
  print "Waiting for PIR to settle ..."
 
  # This will run unless PIR output is zero, ensuring that it settles
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
      # Voltage is reocrded as high or low
      # Record time taken to reach high voltage for proportional motion level
      time = RCtime(7) 
      # Update previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
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

  
