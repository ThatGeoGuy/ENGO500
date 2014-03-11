# Detect motion from PIR module and PhotoInterrupterSwitch
# AC march 6 2014

# Import required Python libraries
import RPi.GPIO as GPIO

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO.setup(17,GPIO.IN)
Switch_State = 0

if GPIO.input(25):
  print('Port 17 is 1/GPIO.HIGH/True')
else:
  print('Port 17 is 0/GPIO.LOW/False')

def PhotoIntSwitch(switch):
  Switch_State = GPIO.input(17)
  while True:
    if (Switch_State == 1):
      print('SWITCH STATE')
      print(Switch_State)
    else:
      print('SWITCH STATE IS else')
      print(Switch_State)
  return Switch_State

  
#Main Program Loop
while True:
  try:
    switch = 17
    SwitchTest = PhotoIntSwitch(switch)
    print("testing")
     
  except KeyboardInterrupt:
    print "  Quit"
    # Reset GPIO settings
    GPIO.cleanup()

