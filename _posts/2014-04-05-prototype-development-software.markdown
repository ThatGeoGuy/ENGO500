--- 

layout: post
title: Prototype Development - Software
author: Alexandra Cummins

excerpt: The sensor prototype for LASS has a few software requirements of its own.  This post details the use cases we set out for it and how they were fulfilled.
---
# Prototype Development - Software
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

The sensor prototype for LASS has a few software requirements of its own.  This post details the [use cases we set out for it](https://github.com/ThatGeoGuy/ENGO500/wiki/Use-Cases) and how they were fulfilled.

If you are unfamiliar with the term "use case", it is simply a way of defining the [input and output relationships between elements in a system]({{ site.baseurl }}/2014/04/03/development-process-technical-deliverables-progress-report/).  An overview of the sensor prototype's relationships is shown by the diagram below:

![Prototype Use Cases]({{ site.baseurl }}/images/sensors/Sensor_Prototype_use_case_diagram.png)

Ultimately, the RaspberryPi (microcontroller) should be able to send the data collected from the sensor to the OGC-IoT database, after which it will be access and displayed nicely on the [web page]({{ site.baseurl }}/2014/04/03/development-process-technical-deliverables-progress-report/).


## Use Cases Fulfilled


**1.1 - Update the database with formatted data**

Once the hardware is set up and working (see use case 1.4 and 1.2), the database should be accessed and updated with the new, formatted data.  This was to be implemented in real time.

This use case was completed by sending observations with the 'sendObs()' class entity that we defined as shown in use case 1.2.  It takes in two arguments: the observation, which in our prototype can only be a one or a zero, and the datastream identity (which corresponds to the sensor from which we would like to post). The 'sendObs()' entity also formats the observation as specified by the data model and by use case 1.2.


**1.2 Format data according to the OGC IoT Standard**

Data collected by the sensors and passed to the microcontroller (use case 1.4) was to be formatted to enable use case 1.1.

Below is the 'sendObs()' class entity as discussed in use case 1.1.  In addition to posting the observation integer to a datastream, it also formats the observation as required by the [data model]({{ site.baseurl }}/2014/04/04/using-the-data-model/) and this use case.

    def sendObs(self, obs, datastreamID):
        urlOBS = self.rootURI() + 'Observations'
        headers = {'content-type': 'application/json'}
        payloadOBS = {'Time':time.strftime('%FT%T%z'),
                      'ResultValue':str(obs),
                      'ResultType':'Measure',
                      'Datastream':{'ID':datastreamID},
                      'Sensor' : {'ID' : self.sensorID}
                      }


**1.3 Identify Sensors**

The sensors and microcontrollers were recognized ad given a unique ID so that their datastreams may be distinguished even after it is formatted and updated to the database.

The microcontrollers were given their own names during setup, but were also assigned a specific object number as set out by the OGC SensorThingsAPI [general data model]({{ site.baseurl }}/2014/04/04/using-the-data-model/).  Each microcontroller became a separate 'thing' entity in the data model. The general data model also permitted the creation of several 'datastreams' for each 'thing', so that multiple sensor data from the same microcontroller is distinguishable. The following demonstrates the creation of a 'thing' with two datastreams.

    url = self.rootURI() + 'Things'
    payload = {'Description': 'This is the real TurboCat (Raspberry Pi)',
        'Datastreams':
          [{'Description': 'This is a datastream for measuring people traffic'},
          {'Description': 'This is for measuring shelf facing'}]}
    headers = {'content-type': 'application/json'}

To avoid creating a new set of 'things' and 'datastreams' every time we ran the prototype, we implemented a little work-around that would store the previous 'thing' location (just a URL) on the RaspberryPi in a text file.  When running the prototype, it would first check these files for the URLs of possible existing 'things'.  

    with open(URLtextfile.txt, 'a+') as x:
        URL = x.read(starting point)
        if (URL == text):
            # thing exists
            # check URL from file for 404 response
            # use URL if response = 200
        else:
            # thing does not exist. 
            # create thing to identify microcontroller
    #continue with script

As shown by the pseudo code above, if it finds that a URL exists and does not return a 404 error, it will continue to identify the microcontroller as that 'thing'.  Otherwise, if the URL is not found, it will wipe the text files and create a new 'thing' to identify the microcontroller.  This feature was particularly useful during the testing phase in which the webserver we were provided with was being intermittently reset.


**1.4 Send data to the micro-controller**

Observations from a sensor will be acknowledged by the microcontroller and stored for use cases 1.2 and 1.1.

This use case was fulfilled through the functionalities of the GPIO library and sensor functions.  Details can be viewed in my previous posts about [working]({{ site.baseurl }}/2014/04/04/working-with-a-PIR-motion-sensor/) with [sensors]({{ site.baseurl }}/2014/04/04/working-with-photo-interrupter/).





