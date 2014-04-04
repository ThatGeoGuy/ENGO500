---

layout: post 
title: Webserver Design - Basics
author: Jeremy Steward

excerpt: A critical component of our website development revolved around building a webserver that could render pages and serve content dynamically. What's more, we wanted to develop our server such that everybody involved in the project could set it up easily with minimal barriers for development. Currently, the code for the webserver has been split off from the main repository and is now hosted in the ENGO500-Webserver repostitory. This post will take you through how to install the pre-requisites and get the server up and running on your local machine. 

---
# Webserver Design: Basics
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

A critical component of our website development revolved around building a webserver that could render pages and serve content dynamically. What's more, we wanted to develop our server such that everybody involved in the project could set it up easily with minimal barriers for development. Currently, the code for the webserver has been split off from the main repository and is now hosted in the [ENGO500-Webserver](https://github.com/ThatGeoGuy/ENGO500-Webserver) repostitory. This post will take you through how to install the pre-requisites and get the server up and running on your local machine. 

The first design decision we made when choosing how to develop our server was to choose a language or framework to write it in. Ultimately, we decided to develop the server application using [Node.js](http://nodejs.org). We chose node for a number of reasons, but it basically broke down to the following: 

1. Node.js is basically just JavaScript. Since a large portion of the frontend development involved jQuery, D3.js, and other JavaScript functionality, we thought it would be best to use Node.js since it meant we could develop in a single language for both the server and the client. 
2. Using the [Express.js](http://expressjs.com) framework with Node made it really easy to set up our server. Beyond that, it is even easy enough to understand for people who are beginners at JavaScript, which was an unintentinoal side-effect we were very happy to run into. Effectively, we found that this lowered the barrier to entry to our server development, which makes it easy to hack and tinker with. 
3. The Node.js community is thriving, and the number of packages available in the Node Package Manager (NPM) is already quite extensive and growing. This made it easier to implement some of the more difficult components of the server (such as user authentication), by providing extensible modules with which we could develop on top of. 

Secondly, we needed something with which to handle our user authentication / storage system. In this sense, we don't need to store data about the sensors, since that is handled by the SensorThings API service. Instead, we need to store user preferences and password data. For this, we decided on using [MongoDB](http://www.mongodb.org/), handled by the [Mongoose](http://mongoosejs.com/) module provided by NPM. 

Together, these are the major software dependencies of our project (barring [git](http://git-scm.org), which we highly recommend using, since our project is tracked using git and hosted on Github). Most of these are incredibly easy to set up and install, which I will explain in the following section.

## Installing Pre-requisites 

Installing Node.js can be managed in a few ways. The installation process itself varies based on the operating system that you use, but the documentation at [nodejs.org](http://nodejs.org) is quite good. While the project itself was mostly developed using Node v0.10.25 and v0.10.26, it should for the most part be forwards compatible with newer versions of node. If there are any troubles, please feel free to contact anyone on our team and we'll try our best to help you. If you're on a Mac OS X machine or a Linux machine, I highly recommend using the [Node Version Manager (NVM)](https://github.com/creationix/nvm), which makes managing your Node.js installation much, much easier. 

Installing MongoDB can be a bit more of a beast than installing Node.js. In particular, MongoDB presents particular troubles when installing on Windows, but has similar issues when installing from outside the package manager on Mac or Linux. For this reason, we provided a script in the [ENGO500-Webserver](https://github.com/ThatGeoGuy/ENGO500-Webserver) repository in the scripts/ folder, to make this easier. The particular issues with how Mongo distributes binaries in a zip archive aside, if you're able to use any version higher than 2.4, you should be set to use what we've built for this project. If you are on Mac OS X or any Linux variant, I highly suggest the use of a package manager to install MongoDB, unless you know what you're doing. If you don't have a package manager on Mac OS X, I highly recommend [Homebrew](http://brew.sh/). A simple `brew install mongodb` should suffice, but please check the documentation first. 

## Running the Server

Great, so now I'll assume that you have both of the major pre-requisites installed, it should be easy enough to get the project up and running. The following few commands are copied from the ENGO500-Webserver `README.md` file, but basically you'll just want to: 

    $ git clone https://github.com/ThatGeoGuy/ENGO500-Webserver.git
    $ cd ENGO500-Webserver
    $ npm install            # Installs extra node.js modules

And just like that, the server should now have all the current modules installed. Running the server has one more step involved, but it is a simple one. Since MongoDB needs to be told *where* to start saving the database, we'll have to specify it to start before we run the `server.js` app in Node. For the purposes of development up until now, we've used a folder called `mongo/` within our repository (don't worry, git will ignore your database) on port 29999 to store the database. In a separate terminal window, in the ENGO500-Webserver repository, run: 

    $ mkdir mongo/ 
    $ mongod --dbpath mongo/ --port 29999

Alternatively, if you don't mind starting with a fresh database everytime you want to run the server, you can run `./scripts/startServer.sh` (or `./scripts/startServer.bat` if you're on Windows) which will remove the `mongo/` directory before running the two above commands again. 

Afterwards, run the following command in a separate terminal window: 

    $ node server.js

And voila! The website should be available on http://localhost:8000/. 
