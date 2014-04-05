---

layout: post
title: Development Process - Literature review
author: Jeremy Steward

excerpt: This will serve as the second part in a series of posts describing in part the development process for our ENGO 500 final year design project (codename LASS - Location Aware Smart Shelf). In particular, this post reflects on a review of the literature surrounding the Internet of Things (IoT) that we performed as part of the course components. Some of the conclusions we drew at this stage became key components of our overall software design. 

---
# Development Process: Literature Review
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

This will serve as the second part in a series of posts describing in part the development process for our ENGO 500 final year design project (codename: LASS - Location Aware Smart Shelf). In particular, this post reflects on a review of the literature surrounding the Internet of Things (IoT) that we performed as part of the course components. Some of the conclusions we drew at this stage became key components of our overall software design. 

## Literature Review

During the project proposal, there was little talk as to what we would do to fulfill our objectives for our final project. This was mostly due to the amount of freedom we had in picking a topic; We wanted to develop something that not only seemed useful, but was likewise accomplishable within the scope of the project. 

We had several ideas from the beginning that might have benefited from being incorporated into the internet of things. Some examples include a system to measure the capacity of parking lots around the city, a system to measure and report soil moisture throughout fields or areas, and even a system that could detect and report when snow removal would be required in residential areas (Calgary has had some nasty storms of late). Ultimately, we decided to go with developing a shelving system, that would be capable of measuring if a shelf is stocked or empty, as well as being capable of tracking the location of customers within the store. 

The primary purpose of our literature review was to evaluate previous attempts at solving these problems, as well as attempt to evaluate some of the different equipment or methods we would need to employ in order to make this project successful. 

### Retail Analytics and Shelf Stock

Overall, we found that there is an incredible amount of work and research put into this topic already. Many previous implementations have touted the use of [RFID](http://www.rfidjournal.com/articles/view?1339) tags in order to map movements and shelf stock. There are even [several](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3705755/) [examples](https://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=4663949) where such systems have been implemented and tested. While the efficacy of these solutions is not debated, RFID tags have shown some particular shortcomings, particularly: 

1. RFID tags can potentially become very noisy, especially if there are a lot of them in a small area. 
2. Direct information cannot be obtained from RFID tags. Unlike sensors, RFID tags always act like on/off switches in that they're either connected or not. 
3. RFID tags require advanced techniques to track customer motion throughout the store, and are typically not as scalable, since you cannot add more sensors or information into RFID systems as easily as in full sensor networks (such as the OGC SensorThings API). 

Ultimately, we chose to avoid RFID based solutions for the purpose of our project. Partially because of what's listed above, but likewise because we wouldn't be able to make an IoT-based project out of RFID tags. Other retail analytics solutions involve the use of closed caption television (CCTV) footage to track customers, or require customer tracking based off of their smartphone's bluetooth / MAC address. These solutions are considerably harder to implement, and much more costly. In the case of CCTV networks, many stores have their own proprietary solution (from various vendors, many being local vendors) and this makes it very hard to integrate the CCTV footage into other projects. Since the purpose of our project is to help proliferate the open standard, these networks pose a much higher barrier to entry to get users on board with what we developed. 

### Prototype / Hardware Specifications

All that said, we therefore wanted to create a sensor-based solution to provide shelf-stock and customer location information. Thus, we needed to determine what kind of sensors we wanted to use, and how we were going to link all of the sensors together. To manage information throughput to/from the sensors, we ultimately decided on using a [Raspberry Pi](http://www.raspberrypi.org/). While we debated on some other solutions, such as the [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) or the [Netduino](http://www.netduino.com/), we ultimately decided on the Raspberry Pi for the following reasons:

* Because it was simple; we could set it up with a full GNU/Linux operating system and start developing without requiring any special libraries or frameworks
* We could develop in Python rather than C or C#, which would ease the learning curve and development process for the team
* Our project supervisor had some available. 

Unfortunately, since very little research could be found with regards to solving this problem using sensors, we did not come to any conclusion at the time regarding which sensors we would use, or how we would coordinate the sensors. We did, however, generate the following functional and non-functional requirements for the project: 

#### Functional Requirements 

1. The proposed shelf system should be able to tell when a product is no longer faced / in stock. 
2. The proposed shelf system should be able to sense if a customer is standing in front of one of its sections. 
3. The shelf should (as a final product) be sized similarly to to existing store shelves, and should not obstruct or displace current shelf systems. 
4. The final device should not break down if internet access is lost, but otherwise should expect that a reliable internet connection is in place in order to perform normally. 

#### Non-functional Requirements

1. The shelf system should conform to the Open Geospatial Consortium SensorThings API standard. 
2. As a corollary to *Functional Specification #4* above, a stable internet connection should be made available so that the shelf can operate and communicate through the SensorThings API. 
3. Power must be made available to the shelf. While a final "ready-made" product was never developed, we specced the power draw to be similar to that of a Raspberry Pi (700mA / 5V). 

### Website / Software Specifications 

Naturally, as mentioned in the previous post for the project proposal, an interface of some kind is needed in order for users of the system to interact and view the information that our sensors are sending to the IoT service. While our group had the option of developing a smartphone application, we felt that the necessary overhead in learning how to create an application would be too much given the scope of all the other components of the project. Combining that with the fact that some members of our group had some previous experience building and developing websites, it was decided that the simplest way to provide an interface would be through a website that users could sign in and connect to. We came up with the following requirements that our website should fulfill: 

#### Functional Requirements

1. The ability to pull shelf stock / facing measurements in real time, so that users could figure out where to restock things.
2. The ability to track customers traveling through aisles within the store. 
3. The ability for the website to generate some basic analytics based on data from the sensors. 

#### Non-functional Requirements

1. The system should be painless to introduce, and should require no more than signing up for a service, similar to signing up for something such as Github or Twitter.
2. The system should provide some means of security so that unauthorized access to the system is prevented or stopped.
3. The system should not fail or cease to work if there is no power in the store or if the shelf system itself is prevented from working normally. 
4. The website should be interoperable with the OGC SensorThings API, as was the case for the Prototype / Hardware. 

We also mentioned requirements regarding the ease-of-use and testing requirements for the final system, but I won't list those here explicitly since they are more concerned with the final product than the development process itself. 

From this point, we continued to plan a development methodology for both branches of work (the Prototype of the shelf itself, as well as the Website development). This work leads us to the next step in our overall Development Process, which will be the discussion of the next post on this subject. As before, you can read our [full literature review](https://github.com/ThatGeoGuy/ENGO500/raw/master/Reports/Lit_Review/ENGO500_GIS%26LT2_LitReview_2013-11-18.pdf) on Github, and see a more in-depth look into how we approached it at that time. Look forward to the next post, which will discuss our development up until the halfway point of our Project Timeline! 

* * *

**Previous Post:** [Development Process: Project Proposal]({{ site.baseurl }}/2014/04/01/development-process-project-proposal/)

**Next Post:** [Development Process: Technical Deliverables]({{ site.baseurl }}/2014/04/03/development-process-technical-deliverables/)

* * *
