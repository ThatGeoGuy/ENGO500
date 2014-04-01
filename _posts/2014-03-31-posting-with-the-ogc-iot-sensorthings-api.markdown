--- 

layout: post
title: Posting with the OGC IoT SensorThings API
author: Kathleen Ang

excerpt: Today I'll briefly explain how to HTTP POST (corresponding to the "CREATE" in Create, Read, Update, Delete) data to the OGC IoT data service.

---
# Posting with the OGC IoT SensorThings API 
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

Today I'll briefly explain how to HTTP POST (corresponding to the "CREATE" in Create, Read, Update, Delete) data to the OGC IoT data service. You can find further documentation here at their [website](http://ogc-iot.github.io/ogc-iot-api/index.html). There is a handy [quickstart](http://ogc-iot.github.io/ogc-iot-api/quickstart.html) and their Interactive SDK, which shows examples in terms of how to format your request.

Let's try making a simple POST request and create a new [Thing](http://ogc-iot.github.io/ogc-iot-api/datamodel.html). For the purposes of experimenting and debugging, I would recommend using [Hurl](http://www.hurl.it/). 

We'll start by changing GET in the dropdown menu to POST. Following that, we can put the following URL in the textbox:
    http://demo.student.geocens.ca/SensorThings_V1.0/Things

Next, we need to add a new header (by clicking on the +Add Header(s) button). The "name" field should be Content-Type and the "value" field should be application/json.

Finally, we can add the content we would like to post. We will keep it simple for now, and make our Thing with just a description. Something like this will do:
    {"Description":"This is a chair"}

Your final screen will look something like this:
![](images/hurl_screenshot.png)

Once you send it (just click Launch Request), the response you will get is 201 Created:
![](images/hurl_result.png)

And there you have it! Happy POST-ing :)
