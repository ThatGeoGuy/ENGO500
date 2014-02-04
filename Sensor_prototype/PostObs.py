# press ctrl+c to kill datastream
# x represents high or low voltage
# AC Feb 03 2014

import random, time, datetime, requests, json
ID = " this sensor "

class data:

    def __init__(self,ID):
        self.ID = ID


    def __str__(self):
        return '{' + str(self.ID) + ' , ' + str(self.v) + ' , ' + str(self.t) +'}'

    def rootURI(self):
        return 'http://demo.student.geocens.ca:8080/SensorThings_V1.0/'
    
    def localtime(self):
       return time.localtime()
    
    def string(self):
        struct_time=time.strptime("%Y""-""%m""-""d","T")#added
        return struct_time

    def timeisoformat(self):
        rn = datetime.datetime.now()    
        return rn.isoformat()

    def initRequest(self):
        url = self.rootURI() + 'Things'
        payload = {'Description': 'This is the REAL TurboCat/OnionCat on Feb4',
            'Datastreams':
                   {'Description': 'This is a datastream for measuring people traffic'}}
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        ## ERROR CHECKING?! status code
        thing_location = r.headers['location']
        self.thing_location = thing_location
        return thing_location

    def sendObs(self, obs):
        url2 = self.thing_location + '/Datastreams'
        r2 = requests.get(url2)
        response2 = r2.json()
        datastreamID = response2['ID']
        # Post an observation?
        # Note: currently this does create an observation but request comes back with
        # status code 500 (internal server error)....
        urlOBS = self.rootURI() + 'Observations'
        headers = {'content-type': 'application/json'}
        timestring = self.timeisoformat();
        payloadOBS = {'Time':'2014-02-04T23:16:00-0700',
                      'ResultValue':str(obs),
                      'ResultType':'Measure',
                      'Datastream':{'ID':datastreamID}
                      }
        r3 = requests.post(urlOBS, data=json.dumps(payloadOBS), headers=headers)
        return r3.headers

        

##### Main #####

tlist = []
timerec = time.localtime()
instance = data(ID)
instance.initRequest()

while True:
  try:
    x = random.randrange(0,5)
    print (x)
    instance.sendObs(x)

    time.sleep(3)
  except KeyboardInterrupt:
    print ("\n Quit")
    break
