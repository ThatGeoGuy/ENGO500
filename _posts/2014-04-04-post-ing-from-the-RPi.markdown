---

layout: post
title: POST-ing from the RPi
author: Kathleen Ang

excerpt: We went through a simple walkthrough of [how to POST data to the SensorThings API data service]({{ site.baseurl }}/2014/03/31/posting-with-the-ogc-iot-sensorthings-api/. Now we'll look at the details for how we formatted and sent our data.

---
# POST-ing from the RPi
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

We went through a simple walkthrough of [how to POST data to the SensorThings API data service]({{ site.baseurl }}/2014/03/31/posting-with-the-ogc-iot-sensorthings-api/. Now we'll look at the details for how we formatted and sent our data.

A summary of the procedure is as follows:
1. Create Thing with associated Datastreams
2. Obtain URI (Unique Resource Identifier) of Thing
3. Obtain assigned Datastream IDs
4. Post Observations, linked to the appropriate Datastream

**Step 1: Create Thing **

Before sending observations to the data service, it's necessary to create the appropriate Thing and Datastream. After this has been created, it doesn't need to be created again.

To create the Thing, you need to make a POST request to the Things collection at the root URI:

		url = http://demo.student.geocens.ca:8080/SensorThings_V1.0/Things

The body of the post will appear as follows:

		postBody = {'Description': 'This is a Raspberry Pi on a shelf',
     						'Datastreams':
     						[{'Description': 'This is a datastream for measuring people traffic'},
      					 {'Description': 'This is a datastream for measuring shelf stock'}]}

If you're using Python 2.7 (as we were), you can use the [Requests](http://docs.python-requests.org/en/latest/) library, which makes HTTP requests quite intuitive. It will look something like this:

		headers = {'content-type': 'application/json'}
		r = requests.post(url, data = json.dumps(postBody), headers = headers)

(You'll need to import both requests and json libraries)

After sending this request, we should have successfully created a new Thing with two Datastreams. Now let's find where it's located, so that we can eventually send Observations.

**Step 2: Obtain URI of Thing**

You'll notice that we created a variable "r" along with our post request. Once the command is executed, "r" contains our response. We can find where our Thing is using the following code:

		thing_location = r.headers('location')

Maybe you're wondering -- "Why do we have to do this at all? Can't we assign it a location?"

Well, the easy answer is this: the way that the data service is currently set up, you don't assign your Thing an ID. You create a Thing, and its ID will automatically be assigned (for example, if there are already 7 Things on the server, your Thing will have ID = 8). 

Your thing_location should have a format something like this:

		http://demo.student.geocens.ca:8080/SensorThings_V1.0/Things(8)

**Step 3: Obtain assigned Datastream IDs**

Just as Things are automatically assigned IDs, Datastreams are also assigned IDs. Because each Thing has its own associated Datastreams, we can take a look at all of them just by visiting this URL:

		http://demo.student.geocens.ca:8080/SensorThings_V1.0/Things(8)/Datastreams

Programmatically speaking, we can get our Datastream IDs if we know how many Datastreams we have (which we should -- we made them when we made our Thing). In our implementation, we achieved this with the getDatastreamID function:

		def getDatastreamID(self, dsIndex):
        url= self.thing_location + '/Datastreams'
        r = requests.get(url)
        response = r.json()
        datastreamID = response['Datastreams'][dsIndex]['ID']
        return datastreamID

dsIndex would be, in our case, either 0 or 1 -- 0 corresponds to the motion sensor and 1 corresponds to the photo interrupter (stock sensor).

**Step 4: Post Observations**

This final step is the only one that should be executed more than once. Now that everything has been set up, we can post observations as we read them in real time. They will be posted to the Observations collection, for example:

		http://demo.student.geocens.ca:808/SensorThings_V1.0/Observations

In order to attach the Observations to the proper Datastream, this should be included in the body of response. An example Observation post in the program is shown below:

		payloadOBS = {'Time':time.strftime('%FT%T%z'),
                      'ResultValue':'1',
                      'ResultType':'Measure',
                      'Datastream':{'ID':datastreamID},
                      'Sensor' : {'ID' : self.sensorID}
                      }

For our observations, the Time property is created such that it matches the ISO 8601 date format. The ResultValue is either 0 or 1, the ResultType is always 'Measure', and the 'Datastream' ID is obtained from step 3. 

*What's this 'Sensor' property about?*
Based on the current data model, an Observation should link to an associated Sensor entity. You can create a Sensor ID in a similar way as you created a Thing, except you would POST the request to the /Sensors collection. You can try it yourself, and if you're not sure, check out our source code in our [GitHub repo](https://github.com/ThatGeoGuy/ENGO500/).