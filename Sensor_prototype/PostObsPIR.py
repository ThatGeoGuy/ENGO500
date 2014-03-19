#!/usr/bin/python
# PostObsPIR.py
# an attempt at mashing up existing scripts (oh boy!)
# and cleaning them up while we're at it
# Last Edited: march 19 2014 AC

import time, datetime, requests, json, RPi.GPIO as GPIO
ID = " RPi 1 "
       
class data:

    def __init__(self,ID):
        self.ID = ID

    def __str__(self):
        return '{' + str(self.ID) + ' , ' + str(self.v) + ' , ' + str(self.t) +'}'

    def rootURI(self):
        return 'http://demo.student.geocens.ca:8080/SensorThings_V1.0_students/'

    def initRequest(self):
        n=1
        with open('/home/pi/ENGO500/Sensor_prototype/checkthinglocation.txt', 'a+') as ctl:
            with open('/home/pi/ENGO500/Sensor_prototype/checksensorlocation.txt','a+') as csl:
                c = ctl.read(n)
                if (c == 'h'):
                    print("Things exists")
                    thing_location = ctl.readline()
                    self.thing_location = 'h' + thing_location
                    print(self.thing_location)
                    r2 = requests.get(self.thing_location)
                    sr2 = str(r2)
                    print(sr2)
                    print('check r2')
                    if (sr2 == '<Response [404]>'):
                        ctl.seek(0)
                        ctl.truncate()
                        csl.seek(0)
                        csl.truncate()
                        print(sr2)
                        print("Server has reset. Links have been changed, please restart.")
                        #LED HOLD
                        GPIO.output(GPIO_LED, True)
                        exit()
                    elif (sr2 == '<Response [200]>'):
                        print(sr2)
                        print('this is 200')
                    else:
                        print("rcode sting match failed")
                    self.sensors_location = csl.readline()
                    rcode = requests.get(self.sensors_location)
                    response = rcode.json()
                    self.sensorID = response['ID']
                    print(self.sensorID)   
                    
                else:
                    print("Thing does not exist.  Create thing.")
                    url = self.rootURI() + 'Things'
                    payload = {'Description': 'This is the real TurboCat (Raspberry Pi)',
                        'Datastreams':
                            [{'Description': 'This is a datastream for measuring people traffic'},
                                {'Description': 'This is for measuring shelf facing'}]}
                    headers = {'content-type': 'application/json'}

                    r = requests.post(url, data=json.dumps(payload), headers=headers)
                    ## ERROR CHECKING?! status code
                    thing_location = r.headers['location']
                    self.thing_location = thing_location
                    ctl.write(thing_location)

                    url3 = self.rootURI() + 'Sensors'
                    payload2 = {'Metadata': 'This is a PIR sensor'}
                    rsensor = requests.post(url3, data=json.dumps(payload2), headers=headers)
                    self.sensors_location = rsensor.headers['location']

                    csl.write(self.sensors_location)
                    rsensor = requests.get(self.sensors_location)
                    response = rsensor.json()
                    self.sensorID = response['ID']            

        return thing_location

    def getDatastreamID(self, dsIndex):
        url= self.thing_location + '/Datastreams'
        r = requests.get(url)
        response = r.json()
        datastreamID = response['Datastreams'][dsIndex]['ID']
        print(datastreamID)
        return datastreamID

    def sendObs(self, obs, datastreamID):
        urlOBS = self.rootURI() + 'Observations'
        headers = {'content-type': 'application/json'}
        payloadOBS = {'Time':time.strftime('%FT%T%z'),
                      'ResultValue':str(obs),
                      'ResultType':'Measure',
                      'Datastream':{'ID':datastreamID},
                      'Sensor' : {'ID' : self.sensorID}
                      }
        try:
            r3 = requests.post(urlOBS, data=json.dumps(payloadOBS), headers=headers)
        except requests.exceptions.Timeout as e:
            print e
        except requests.exceptions.HTTPError as e:
            print e
        except requests.exceptions.ConnectionError as e:
            print e
        except requests.exceptions.RequestException as e:
            print e

        return None
        

##### Main #####

# Create instance of data class
thing1 = data(ID)
thing1.initRequest()

# Get datastream ids
PIR_datastreamID = thing1.getDatastreamID(0)
PInt_datastreamID = thing1.getDatastreamID(1)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# LED GPIO
GPIO_LED = 4
GPIO.setup(GPIO_LED,GPIO.OUT)
# For PhotoInt
GPIO.setup(17,GPIO.IN)
# For PIR
GPIO_PIR = 18
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

if GPIO.input(17):
  print('Port 17 is 1/GPIO.HIGH/True')
else:
  print('Port 17 is 0/GPIO.LOW/False')
if GPIO.input(18):
  print('Port 18 is 1/GPIO.HIGH/True')
else:
  print('Port 18 is 0/GPIO.LOW/False')

Switch_State = 1
PSS = 1
Current_State  = 1
Previous_State = 1

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==0:
    Current_State  = 1    

  print "  Ready GO"     
    
  # Loop until users quits with CTRL-C
  while True :
   
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
   
    if Current_State==0 and Previous_State==1:
      # PIR is triggered
      print "  Motion detected!"
      thing1.sendObs(1,PIR_datastreamID)
      GPIO.output(GPIO_LED, True)
      # Record previous state
      Previous_State=0
    elif Current_State==1 and Previous_State==0:
      # PIR has returned to ready state
      print "  Ready"
      thing1.sendObs(0,PIR_datastreamID)
      GPIO.output(GPIO_LED, False)
      Previous_State=1

    #------PhotoInt
    Switch_State = GPIO.input(17)
    if Switch_State == 0 and PSS == 1:
        print("SWITCH STATE IS ZERO")
        thing1.sendObs(1,PInt_datastreamID)
        PSS = 0
    elif Switch_State == 1 and PSS == 0:
        print('Switch is reset')
        thing1.sendObs(0,PInt_datastreamID)
        PSS = 1

    time.sleep(0.01)      
    #time.sleep(1)
except KeyboardInterrupt:
  print "  Quit" 
  # Reset GPIO settings
  GPIO.cleanup()
  
  
