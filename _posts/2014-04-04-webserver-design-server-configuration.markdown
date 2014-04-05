---

layout: post 
title: Webserver Design - Server Configuration
author: Jeremy Steward

excerpt: This post discusses how the code and structure of the server is laid out in the ENGO500-Webserver repository. Hopefully, this article will provide some insight into how the project was structured from a software point of view, and likewise should give you enough information to hack and modify the webserver to suit your own needs. 

---
# Webserver Design: Server Configuration
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

This post discusses how the code and structure of the server is laid out in the ENGO500-Webserver repository. Hopefully, this article will provide some insight into how the project was structured from a software point of view, and likewise should give you enough information to hack and modify the webserver to suit your own needs. 

## Directory Structure

The directory structure of the repository is meant to be straightforward, and follows a typical Model-View-Controller (MVC) style. A tree structure of the directories in the repository is shown, along with a short descripiton of what each directory represents and what kinds of files are inside of them.

    ENGO500-Webserver/
    ├── config
    ├── models
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

### Views (views/) 

As could be expected, the `views/` folder represents the *view* portion of our MVC framework. As mentioned previously, we used Nunjucks (Jinja2) style templates, from within the [Express.js](http://expressjs.org) framework. Effectively this means that our views consist of a series of templates that structure the basic content that populates the website. The majority of these are derived from `views/base.html`, which provides the base template for the entire site. From there, several blocks are defined, including a CSS block for adding additional stylesheets, a CONTENT block for adding content dynamically depending on the page, and a SCRIPTS block, which allows users to add specific JavaScript files for each different page type. This is especially important, as it is not necessary to add the layout creator functionality to every page, but just for the pages that require it.

A couple of *includes* are also defined within views, namely the header and footer of the website. Unlike `views/base.html` and those that inherit from it, the includes are files that are merely substituted into files that require them, but don't need inheritance based on the page being viewed. The header and the footer of the site are good examples for how includes work within our project, as they do not change between pages. 

### Public (public/) 

The `public/` folder as it is, exists for the purpose of storing static files that will be served directly from the server. Page stylesheets, client-side JavaScript files, and images are all types of files that would ideally be stored in the public folder. Even static html files can be hosted within the `public/` directory, however, this is typically unwise for several reasons. 

First and foremost, it's typically easier to create additional pages using templates, which will also give you a consistent style across your page (since the template will take care of common stylistic traits). Furthermore, because of the way Express.js works, templates and routes defined in the `routes/getHandlers.js` file are rendered with priority over static files. In the case that a static file has the same name as one of the routes in `routes/getHandlers.js`, the application will return the corresponding route instead of the static file. In practice, you typically will want to define most of your content through `views/`, and use `public/` for stylesheets and client-side JavaScript files. 

### Models (models/)

Like with the views directory, the `models/` directory specifies the *models* component of our MVC framework. In particular, this directory only contains one file, which defines the model that defines our database. The specifics of the model itself are saved for another post, but if you want to extend our model beyond login information and store layout data, modifying or adding a schema to this folder would be the first place to start. Note that it may also be necessary to edit other areas of the code to accommodate new models, however this will vary depending on the scale of change you wish to make. 

### Configuration (config/)

Lastly, configuration for various components within the *controllers* is put in the `config/` folder. An example is the global configuration, which lies in `config.js`. In particular, we defined two configuration types: development and production. This way, our server can run in either mode, and change the configuration dynamically without having to change anything between the two servers. 

`config/passportConfiguration.js` defines the structure for using local authentication with the [Passport](http://passportjs.org). This is complementary to `config/auth.js`, which provides some helper functions for checking user authentication. While it seems strange to put the helper functions there, they were placed for convenience as they directly relate to Passport itself, and are typically used in conjunction when passport is used or called. 

With the brief descriptions above, you should be able to find and change much of the code within the project. Moreover, the importance of splitting the project into separate components such as outlined above should be considered. In many cases, small changes to various components (such as in the templates within the `views/` folder) can result in large changes across the site. However, since this separation decouples much of the data and the logic of the application, we find that even if large changes occur, they seldom affect other pieces of the code. The most strongly coupled piece of code above is likely to be the model(s). This is an unfortunate necessity of an application that requires authentication, but it is manageable since extending the model is possible without affecting more than two or three different files at most (i.e. even if you extend the model, you won't have to extend the existing routes and handlers, etc.).
