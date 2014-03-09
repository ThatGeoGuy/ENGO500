# Detect motion from PIR module and PhotoInterrupterSwitch
# AC march 6 2014

# Import required Python libraries
import RPi.GPIO as GPIO, time, datetime

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
# Define GPIO to use on Pi
GPIO_PIR = 18
GPIO_Switch = 2

# Set pin as input, check connection to sensor
GPIO.setup(GPIO_PIR,GPIO.IN)
Current_State  = 0
Previous_State = 0
Switch_State = 0

def PhotoIntSwitch(PiPin1):
  
  Switch_State = GPIO.input(GPIO_Switch)
  while True:
    if Switch_State == 0
        continue
    else
      break
return Switch_State
  

#---------This whole function will need to reworked with 'data' class----------#
def detectmov(PiPin):  
  
  print "Waiting for PIR to settle ..." 
  # This will run unless PIR intput is zero, ensuring that it settles
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
  print "  Ready"
  
  # Loop until users quits with CTRL-C
  while True :
    
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
    if Current_State==1: #and Previous_State==0:
      
    # PIR is triggered
      print "  Motion detected!"
      print datetime.datetime.now()
      
      # Records most recent time
      timerec = datetime.datetime.now()
        # GPIO.output(7,True) - LED on
      
      # Update previous state
      Previous_State=1
      
    elif Current_State==0 and Previous_State==1:
      
      # PIR has returned to ready state
        # GPIO.output(7, False) - LED off
      print "  Ready"
      Previous_State=0
      
    # Wait for 10 milliseconds; may change with testing
    time.sleep(0.01)
  return timerec



    
#Main Program Loop
t = []
try:
  #t.append(detectmov(PiPin))
  SwitchTest = PhotoIntSwitch(PiPin2)
  print (SwitchTest)
   
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()

