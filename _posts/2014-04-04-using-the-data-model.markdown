--- 

layout: post
title: Using the data model
author: Kathleen Ang

excerpt: The OGC SensorThings API has a general data model, designed to be adaptable to any IoT application. This post will discuss the components of the data model which we deemed relevant for our project, and how these components were used in our application.
 
---
# Using the data model
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

The OGC SensorThings API has a general data model, designed to be adaptable to any IoT application. This post will discuss the components of the data model which we deemed relevant for our project, and how these components were used in our application. For more details regarding other applications, please see the full documentation on the [OGC IoT data model page](http://ogc-iot.github.io/ogc-iot-api/datamodel.html).

As you can see in the figure below, we have highlighted the entities in the data model which were the most crucial for our application. 

![Entities of interest]({{ site.baseurl }}/images/dataModel/DataModelofInterest.png)

The core of this data model is the "Thing", which usually corresponds to some real-world object. In the case of LASS, the Thing should be a shelf; however, in the proof-of-concept phase, we decided to identify the Raspberry Pi as our Thing.

From this Thing, there can be 0 to many associated Datastreams. A Datastream is an entity which groups observations together. Since we were interested in tracking two main types of observations, we likewise had two Datastreams.

Finally, each of these associated Datastreams have 0 to many Observations, which are direct readings from the sensors. Both of our sensors operate as "on/off"-type switches, so our Observation values were either 0 or 1.

All this information is set up and sent from the Raspberry Pi to the OGC IoT data service, which in turn was read from our website. The diagram below shows a high-level overview of our project, with the appropriate entities from the SensorThings API Data Model applied.

![Our data model]({{ site.baseurl }}/images/dataModel/AdoptedDataModel.png)
