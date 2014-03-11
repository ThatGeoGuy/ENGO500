# Detect motion from PIR module and PhotoInterrupterSwitch
# AC march 10 2014

# Import required Python libraries
import RPi.GPIO as GPIO, time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO.setup(17,GPIO.IN)
Switch_State = 0

if GPIO.input(17):
  print('Port 17 is 1/GPIO.HIGH/True')
  print(GPIO.input(17))
else:
  print('Port 17 is 0/GPIO.LOW/False')
  print(GPIO.input(17))

def PhotoIntSwitch(switch):
  while True:
    Switch_State = GPIO.input(switch)
    if (Switch_State == 1):
      print('HIGH')
      print(Switch_State)
    else:
      print('SWITCH STATE IS else')
      print(Switch_State)
    time.sleep(2)
  return Switch_State

    
  #Main Program Loop
try:
  
  while True:
      switch = 17
      SwitchTest = PhotoIntSwitch(switch)
      print("testing")
     
except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()

