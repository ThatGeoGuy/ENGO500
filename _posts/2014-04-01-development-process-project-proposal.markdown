---

layout: post
title: Development Process - Project Proposal
author: Jeremy Steward

excerpt: This is the first part in a series of posts describing the beginning of our development process for our ENGO 500 final year design project (codename LASS - Location Aware Shelf System). Hopefully, from reading through these blog posts, you'll gain some insight regarding the development progress of the project, and gain some insight into how the project came together as a whole. Ultimately, these posts won't be highly technical in nature, but will help clarify some of the design decisions we made throughout the course of the project, up to the projects actualization (current state). 

---
# Development Process: Project Proposal
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

This is the first part in a series of posts describing the beginning of our development process for our ENGO 500 final year design project (codename: LASS - Location Aware Shelf System). Hopefully, from reading through these blog posts, you'll gain some insight regarding the development progress of the project, and gain some insight into how the project came together as a whole. Ultimately, these posts won't be highly technical in nature, but will help clarify some of the design decisions we made throughout the course of the project, up to the projects actualization (current state). 

## Project Proposal 

When our group began the project, we were not entirely sure as to what we might choose to develop for the project. While we obviously had course requirements (as outlined for the ENGO 500 course guidelines), we were largely given free reign as to what we wished to develop, given the following constraints: 

1. The project was to be an "[Internet Of Things](http://www.rfidjournal.com/articles/view?4986) (IoT)" based project. 
2. The intent of the project was to be developed in tandem with the [Open Geospatial Consortium (OGC) SensorThings API](http://www.belkin.com/us/Products/home-automation/c/wemo-home-automation/), which was at the time in its infancy.
3. Since the purpose of our project was in a way a test drive of the OGC SensorThings API, we wanted our application to be open source, so that others could benefit from our work and learn from any mistakes or issues we may have encountered along the way. 

### Rationale behind project

When thinking about the Internet of Things, there's three major components that comprise an IoT-based system. These are 

1. The "Thing" that is to be connected through the internet,
2. The interface with which to interact with the object or thing, and
3. Some system which allows both the thing and the user-facing interface to connect and *speak* with one another. 

Looking at the market today, there are a few IoT-based applications that have already been successful. Some examples are the [Philips Hue](http://meethue.com/), or any of the [WeMo](http://www.belkin.com/us/Products/home-automation/c/wemo-home-automation/) Home Automation products. Effectively, our *thing* that we wish to connect to the internet can be almost anything that has some sensors connected to it; likewise, our interface can range from common websites, to full-fledged smartphone applications. Unfortunately, these products do have some pitfalls, in particular due to the proprietary nature of the software they run on. This makes it difficult to directly acquire data from the sensors, and use various products in tandem with one another (mostly due to user-facing software only being compatible with the proprietary information reported by the sensors). This can result in vendor lock-in for the user, but likewise means that users have to overcome the burden of investing entirely in one ecosystem when they want to buy IoT-based products.

Naturally, this was the rationale behind building the OGC SensorThings API, which advertises itself as: 

> [A]n OGC candidate standard for providing an open and unified way to interconnect IoT devices, data, and applications over the Web.

For this reason, we were tasked with developing an application that used the OGC SensorThings API, because it served as an open standard with which anyone could develop interoperable IoT applications. That said, we set out to develop for a few key objectives: 

1. Our "Thing" could be anything, but we needed to develop some software which allowed regular sensors to communicate with the SensorThings API.
2. We likewise needed some interface to make the application more than just sensors sending readings to a server. For this reason, we developed a [website](https://github.com/ThatGeoGuy/ENGO500-Webserver) that would allow users to interact with the system that we envisioned. 

That about sums up the information we had regarding the overall project scope, as well as the rationale behind why we eventually developed our LASS. While some other minor considerations had taken place as well, I won't go into details here as they will be touched on in more depth in subsequent articles. If you want to read the original project proposal, see it listed [here](https://github.com/ThatGeoGuy/ENGO500/raw/master/Reports/Proposal/GIS%26LT2_ProjectProposal_2013-09-27.pdf) on Github. 

* * *

**Next Post:** [Development Process: Literature Review]({{ site.baseurl }}/2014/04/01/development-process-literature-review/)

* * *
