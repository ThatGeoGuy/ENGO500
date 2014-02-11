# press ctrl+c to kill datastream
# x represents high or low voltage
# AC Feb 03 2014

import random, time
ID = " this sensor "

class data:

    def __init__(self,ID, v, time):
        self.ID = ID
        self.v = v
        self.time = time
    def __str__(self):
        return '{' + str(self.ID) + ' , ' + str(self.v) + ' , '+ str(self.time) + '}'


##### Main #####

tlist = []
while True:
  try:
    x = random.randrange(0,2)
    print (x)
    if x == 1 :
      timerec = time.localtime()
      instance = data(ID, x, timerec)
      print ("\n", instance)
      tlist.append(instance.v)  #will change to time later
      print (tlist)
      # if ready to update
        # function to format and update
        # tlist = []
      if len(tlist) == 15:
        tlist = []
    
  except KeyboardInterrupt:
    print ("\n Quit")
    break

