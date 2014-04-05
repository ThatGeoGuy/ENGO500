---

published: false
layout: post 
title: Webserver Design - Server Configuration
author: Jeremy Steward

excerpt: This post discusses how the code and structure of the server is laid out in the ENGO500-Webserver repository. Hopefully, this article will provide some insight into how the project was structured from a software point of view, and likewise should give you enough information to hack and modify the webserver to suit your own needs. 

---
# Webserver Design: Basics
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

This post discusses how the code and structure of the server is laid out in the ENGO500-Webserver repository. Hopefully, this article will provide some insight into how the project was structured from a software point of view, and likewise should give you enough information to hack and modify the webserver to suit your own needs. 

## Directory Structure

The directory structure of the repository is meant to be straightforward, and follows a typical Model-View-Controller (MVC) style. A tree structure of the directories in the repository is shown, along with a short descripiton of what each directory represents and what kinds of files are inside of them.

    ENGO500-Webserver/
    ├── config
    ├── models
    ├── mongo
    ├── public
    │   ├── css
    │   ├── img
    │   │   └── icons
    │   └── js
    ├── routes
    ├── scripts
    └── views
    
### Root Folder (ENGO500-Webserver/)

The root folder (presumably named ENGO500-Webserver) contains the whole of the project. Mostly, files are split up amongst the other folders within the repository, but one file in particular is important in this directory: `server.js`

The `server.js` file is important because it defines the very base commands for configuring the server. If you were to download and start using this project with the intent of modifying it, starting with this file would be your best bet. The reason for that is that `server.js` is the most central file to the entire system. With regards to our MVC model, the `server.js` is the beginning of our *controllers*. 

### Routes and Route Handlers (routes/)

The purpose of the routes folder is primarily an extension of the `server.js` file found in the root folder. Within this directory there are two files of particular importance: `getHandlers.js` and `postHandlers.js`, which comprise functions and route definitions for the website for both HTTP GET requests (`getHandlers.js`) and HTTP POST requests (`postHandlers.js`). Again, these files constitute functionality that corresponds to the *controller* part of our MVC framework. If you're planning on adding a page to the server, or planning on studying / changing how information is passed to the server, the two files in this folder will be where you want to make your changes. 

If you look at `getHandlers.js` specifically, you'll notice that it (much like it's counterpart `postHandlers.js`) is a module that returns a function. The two arguments for the function are the Express.js application variable (aptly named `app`) and a variable which holds the functionality to user-authentication for the server. This functionality will be explained in a later post, but for now let's get back to how `getHandlers.js` works. For each HTTP GET request that gets sent to the server, a route and handler will be specified in the following way:

    app.get(route, handler); 

Where route is the name of the path on the site (e.g. /login), and handler is a callback function that takes in two arguments (a request and a response) and tells the application what to do once a request is found for that route. Since `server.js` has been configured to allow for [Nunjucks](http://jlongster.github.io/nunjucks/) templating, it's easy to return a simple template rendered from our views in our MVC framework. 


