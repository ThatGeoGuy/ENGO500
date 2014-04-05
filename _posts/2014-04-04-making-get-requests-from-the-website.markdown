---

layout: post
title: Making GET requests from the website
author: Kathleen Ang

excerpt: In a previous post, we explained how to POST observations. Now we'll take a look at how to GET those observations, and how to do some fancy things with it.

---
# Making GET requests from the website
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

In a previous post, we explained [how to POST observations](http://thatgeoguy.github.io/ENGO500/2014/04/04/post-ing-from-the-RPi/). Now we'll take a look at how to GET those observations, and how to do some fancy things with it.

Making GET requests, in general, is easier than making POST requests. We are essentially just reading from the server what information is there, so all we really need is the correct URI to read from. In our case, we are interested in retrieving observations, which can be easily read from a URL provided you have the following information:
* Thing ID (e.g. 7)
* Datastream ID (e.g. 12)

You'd construct the URL -- based on our example values -- as follows:

	http://demo.student.geocens.ca:8080/SensorThings_V1.0/Things(7)/Datastreams(12)/Observations

(Don't forget to change your root URI as appropriate!)

Unfortunately, after we've been running our Raspberry Pi for a few hours, we are going to end up with potentially thousands of observations. If we make a GET request to that URL, we're going to end up with a huge object, and that's just no good.

However, the data service has functionality for filtering -- you can read up on it more in the [API reference](http://ogc-iot.github.io/ogc-iot-api/api.html), under section 2.2.4. 

For our purposes, we used two of the possible filter capabilities. The first one was to filter ResultValue, so that we could get only Observations with a ResultValue property of 1. (This made it easier to render the store traffic statistics, as discussed in [another post](http://thatgeoguy.github.io/ENGO500/2014/04/04/front-end-development-store-viewer/).) To do this, you make a GET request to the following URL:

	http://demo.student.geocens.ca:8080/SensorThings_V1.0/Things(7)/Datastreams(12)/Observations?$filter= ResultValue eq '1'

The second filtering capability we used was filtering by time. For example, if you want observations after 12:00 noon on April 4, 2014, you would use the following URL:

	http://demo.student.geocens.ca:8080/SensorThings_V1.0/Observations?$filter=Time ge STR_TO_DATE('2014-04-04t12:00:00-0600','%Y-%m-%dt%H:%i:%s')

The "ge" stands for greater than or equal to and "eq" from the previous URL stands for equal to (as you may have guessed). You can also combined multiple filters, simply by adding "and" to your URL:

	http://demo.student.geocens.ca:8080/SensorThings_V1.0_students/Observations?$filter=Time ge STR_TO_DATE('2014-04-04t12:00:00-0600','%Y-%m-%dt%H:%i:%s') and Time le STR_TO_DATE('2014-04-05t12:00:00-0600','%Y-%m-%dt%H:%i:%s')

This request would get all observations between 12:00 noon on April 4 and 12:00 noon on April 5.
