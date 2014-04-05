--- 

published: false
layout: post
title: Improving Prototype Usability
author: Alexandra Cummins

excerpt: Ultimately, as much as we enjoyed messing with sensors all day, the LASS prototype wasn't supposed to be used only by the developpers. This post considers the steps we took to make our prototype as hands free as possible, so that the user - potentially a store manager - can just plug it in and go.
---
# Improving Prototype Usability
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

Ultimately, as much as we enjoyed [messing with sensors all day](harshinis post), the LASS prototype wasn't supposed to be used only by the developpers. This post considers the steps we took to make our prototype as hands free as possible, so that the user - potentially a [store manager](one of bens posts) - can just plug it in and go.

##Plug In and Go

During the development process, we found the most efficient way to get things done was to write code directly on the RaspberryPi itself.  This allowed us to test the sensor functions via GPIO library as we went along, but also required us to view the display via HDMI cable.  

Now that the sensors have been tested and are [fully operational](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTmiml_wmLBeANGy9MOW8lsaHuxwfXtIpNuorQbyMOTvaHW8P4s), there is no longer a need to view the screen on the conditions that we can:
 
1. Run the code automatically 
2. We are given some sort of confirmation that the system is running error free.

##Run On StartUp

##LEDs for Posting Observations

![LED]({{ site.baseurl }}/images/sensors/ledx.JPG)

![LED diagram]({{ site.baseurl }}/images/sensors/ledp.PNG)

