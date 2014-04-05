---

layout: post
title: Front End Development - Store Viewer
author: Ben Trodd (and Kathleen Ang)
publish: false

excerpt: The Store Viewer page uses the `shelves` array created in the Store Layout Creator to display observations on a map user interface. Additionally, some statistics are shown to give an overall feel of the status of the store. Observations are pulled from a database in real-time so that the Store Viewer displays temporally relevant information. In this post, we talk about the development details of the Store Viewer.

---
# Front End Development: Store Viewer
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

The Store Viewer page uses the `shelves` array created in the Store Layout Creator to display observations on a map user interface. Additionally, some statistics are shown to give an overall feel of the status of the store. Observations are pulled from a database in real-time so that the Store Viewer displays temporally relevant information. In this post, we talk about the development details of the Store Viewer.

## Use Cases Fulfilled

2.3 - Get aisle traffic observations
: Observations from the PIR motion sensors are requested from the database. The URLs for these GET requests are taken from the `shelves` array configured in the Store Layout Creator.

2.4 - Get facing observations
: Observations from the Photo-Interrupter sensors are requested from the database. The URLs for these GET requests are taken from the `shelves` array configured in the Store Layout Creator.

2.5 - Get aisle traffic
: Using the observations obtained from use case 2.3, aisle traffic is displayed in two ways. The first is a heat map to show the location of customers within a store, and the second is a stacked bar chart showing overall traffic levels over time.

2.6 - See if products are faced
: Using the observations obtained from use case 2.4, stock levels are displayed in two ways. The first is by showing which sections are empty, and the second is showing an overall stock level for the store.

## Enabling Technologies

Similar to the [Store Layout Creator]({{ site.url }}/ENGO500/2014/04/04/development-details-store-layout-creator/), the Store Viewer relies on a few different technologies. First, the user interface uses the [bootstrap](http://getbootstrap.com) front end framework for positioning and styling. Also [D3.js](http://d3js.org/) is used to visualize the store, observations, and statistics. To simplify GET requests and the JavaScript necessary to merge all of these technologies together, [jQuery](http://jquery.com/) was utilized.

## Store Layout Creator Architecture

Shown below is a screenshot of the system with some active observations being displayed:

![Store Layout Creator]({{ site.url }}/ENGO500/images/storeViewer/activeLabelled.png)

### System Overview

As you can see in the screenshot above, there are 4 different types observation representations being displayed. The left pane shows overall statistics, and the right pane shows a real-time representation of the store.

For real time-stats, there are two ways to display observations. The first type of observation that is visualized is an empty or full section. Full sections appear blue, and empty sections appear purple, as shown by label 1. The second type of observation that is visualized is traffic within an aisle. This is represented by a 'heat map'. When someone walks past a sensor, an orange section is displayed, as shown by label 2.

For the overall statistics, there are also two ways of displaying information. The first is an overall level of traffic within the store, shown by label 3. This takes the number of readings from all motion sensors for an epoch in time and displays them in a bar graph that updates as new epochs become available. The second is an overall stock level, shown by label 4. It calculates the overall stock level by taking the number of full and empty sections for each epoch.

### Technical Challenges

This section details some of the challenges encountered in building the Store Viewer. It serves to explain the inner workings of the system to guide anyone that wishes to use or modify our code.

#### Getting Observations Asynchronously

One of the challenges we ran into was managing the many GET requests being made from the website. When dealing with multiple sections, we were making requests for each individual section and the response latency sometimes shifted the way that observations were rendered. To deal with this at first, we set all of our requests to be done synchronously; however, we soon found that this created significant lag in response to simple things like navigating to a different page.

To make the asynchronous requests work, we created a separate function containing the GET request itself, which would also take in arguments for the shelf and section indices. This took care of the latency issue. (Sometimes, the response for one section would be drawn onto a different section because of the time lag). Here is an example of that code:

    function doGet(shelfInd, sectionInd, URL, type) {
        jQuery.get(URL, function ( data, textStatus, xhr ) {
            if(xhr.status < 400){
                shelves[shelfInd].sections[sectionInd].obs = data;
                //Call function to render observations
            }
        });
    }
    
    // "Main" script
    for( var i = 0; i < shelves.length; i++ )   {
        for( var j = 0; j < shelves[i].sections.length; j++){
            // Set the url depending on what type of observation it is
            if (obsType == "motion"){ // PIR Motion sensor
                var obsURL = shelves[i].sections[j].pirURL;
            } else if (obsType == "stock"){ // Photo interrupter
                var obsURL = shelves[i].sections[j].pintURL;
            }
            if( obsURL != null ){
            // Pass the variables of the get to a function so that indices don't get borked
                doGet(i,j, obsURL, obsType);
            }
        }
    }

#### Displaying Overall Statistics

The overall statistics, being a more standard use of D3.js, were completed by referencing existing tutorials. The store traffic display is a product of examining a [dynamic stacked bar chart](http://bl.ocks.org/benjchristensen/1488375) example, while the stock levels comes from this [animated donut](http://bl.ocks.org/mbostock/5100636) example.

#### Displaying Real-time Observations

Once the observations become available, displaying the observations with d3.js is straightforward. Changing the color for an empty or full shelf is just a matter of changing the fill color of the SVG. The heat map works by creating a 0% opacity rectangle SVG element that is positioned relative to the section that contains the motion sensor. If the motion sensor detects motion, the opacity is increased and then decreases slowly back to 0% using a timer.
