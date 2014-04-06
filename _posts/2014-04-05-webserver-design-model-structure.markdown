---

layout: post 
title: Webserver Design - Model Implementation
author: Jeremy Steward

excerpt: If you've been reading until now, you may have noticed that I had surreptitiously avoided defining our model implementation explicitly. In this post, I'll go through each part of our overall schema, and attempt to show how this satisfies the proposed use case. 

---
# Webserver Design: Model Implementation
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

If you've been reading until now, you may have noticed that I had surreptitiously avoided defining our model implementation explicitly. In this post, I'll go through each part of our overall schema, and attempt to show how this satisfies the proposed use case (Use Case 2.8, see [this post]({{ site.baseurl }}/2014/04/03/development-process-technical-deliverables-progress-report/) for details). 

## Use Cases Fulfilled

2.8 - Log In / Authenticate
: A user can register for the website by visiting the signup page from within their browser. After registering a username and password, they can log in to the site and authenticate their session with the server. Afterwards, they are able to save and load user data that specifies the data format for [viewing the store layout]({{ site.baseurl }}/2014/04/04/front-end-development-store-viewer/). 

## Use Cases Abandoned

2.9 - Become System Configurator
: Due to time constraints, extending the user authentication model to allow for different tiers of users, as well as incorporating organization level grouping of users was not implemented. Ultimately, each user has their own individual profile and data, which may not be the expected behaviour of the final application; however, while this may be the case, as a prototype of a final system, the functionality of the model that we specify below doesn't hinder the implementation or usage of any other use-case or feature. 

From a technical standpoint, we have currently implemented this in such a way that any *Authenticated User* is automatically promoted to *System Configurator* status. However, while we realize that this is not the intuitive interpretation of the [use cases](https://github.com/ThatGeoGuy/ENGO500/wiki/Use-Cases), we chose not to pursue this avenue further in order to better implement more primary functionality of the site. 

## Model Schema 

As mentioned in one of the previous posts on [Webserver Design]({{ site.baseurl }}/2014/04/04/webserver-design-basics/), one of the great things about using Node.js is the wealth of modules made available through the [Node Package Manager](http://npmjs.org). Thanks to this, it's often very easy to find a module that will meet your requirements, and help you ship your final project much more rapidly than if you were to write each individual component yourself. 

For the purposes of implementing the use cases which pertain to user authentication, we chose to use [Passport.js](http://passportjs.org) in combination with [MongoDB](http://mongodb.org) (via the [Mongoose](http://mongoosejs.org) database wrapper). The great part about all of the above is that while each individual module is great on their own, they can easily be swapped out with other databases / database managers if you have different requirements.

The actual implementation of our schema can be seen below. As can be seen, the code itself is rather short, thanks to the expressive power that Mongoose provides as a database wrapper.

    UserSchema = mongoose.Schema({
        username:  String,
        userData:  String,
        salt:      String,
        hash:      String
    });

We can break the above schema down as follows: 

* `username` is the name that the user registered with
* `salt` is the random data we use to form a cryptographic hash of the user's password. [Wikipedia](https://en.wikipedia.org/wiki/Salt_%28cryptography%29), while not terribly academic in nature, has a wonderful definition of the subject matter.
* `hash` is the hash of the user's password hashed with the corresponding cryptographic salt. For the purposes of generating this and the corresponding `salt` parameter used above, we opted to not implement our own cryptography, so we use the wonderful [pwd](https://www.npmjs.org/package/pwd) module available through NPM. 
* `userData` is a string that defines a JSON object, of which constitutes the data that is saved from the [Layout Creator Tool]({{ site.baseurl }}/2014/04/02/using-lass-store-layout-creator/)

From this, we then defined two functions in particular, `signup` and `isValidUserPassword`, which were used to register new users, and validate user passwords respectively. While the code is openly available on [Github](https://github.com/ThatGeoGuy/ENGO500-Webserver), the following implementation for `isValidUserPassword` below is provided as a reference:

    UserSchema.statics.isValidUserPassword = function(username, password, done) { 
        this.findOne({ username: username }, function(err, user) { 
            if(err) { 
                return done(err);
            }
            if(!user) { 
                return done(null, false, { message: 'Incorrect username.' });
            }
            hash(password, user.salt, function(err, hash) { 
                if(err) {
                    return done(err);
                }
                if(hash === user.hash) { 
                    return done(null, user); 
                } 
                done(null, false, { message: 'Incorrect password' });
            });
        });
    }

This function is then later put to use when we configure Passport.js, in the `config/passportConfiguration.js` file. Specifically, it's used in the exports in the following way: 

    module.exports = function(passport, config) { 
        passport.serializeUser(function(user, done) { 
            done(null, user.id);
        });
    
        passport.deserializeUser(function(id, done) { 
            User.findOne({ _id: id }, function(err, user) { 
                done(err, user);
            });
        });
    
        passport.use(new LocalStrategy({ 
            usernameField: 'username',
            passwordField: 'password'
        }, 
        function(username, password, done) { 
            User.isValidUserPassword(username, password, done);
        }));
    }

The above configuration relies on `isValidUserPassword` from our User model to validate if a user's password was entered correctly. Thus, the only significant coupling of our model with Passport occurs at this point, which means that outside of the model itself, you should only have to change this file dependency in order to use a different model with Passport. 

Lastly, I should talk about how all of this is put to use within the server. The short snippets above show how Passport will serialize you as a user, and validate whether or not you entered your password correctly. However, the server itself uses the wrapper functions provided in `config/auth.js` to assist with checking user authentication in the route handlers. See the function definitions below: 

    module.exports = { 
        isAuthenticated : function(req, res, next) { 
            if(req.isAuthenticated()) { 
                next();
            } else { 
                res.redirect('/login');
            }
        }, 

        userExists : function(req, res, next) { 
            User.count({ 
                username: req.body.username
            },
            function(err, count) { 
                if(count === 0) { 
                    next();
                } else { 
                    res.redirect('/signup');
                }
            });
        }
    }

This is taken from `config/auth.js`. In particular, by using these configuration wrappers, we can test for two things: If a user exists, and if the current session is authenticated with a specific user profile. For defining pages in `routes/getHandlers.js` that require authentication, or adding additional routes to `routes/postHandlers.js` for sending data in an authenticated session, you'll want ot use the `isAuthenticated` function as follows in the application: 

    app.get('/home', function(req, res) { 
        Auth.isAuthenticated(req, res, function() { 
            var templateParameters = { 
                // Metadata options
                "title"       : "Home",
                "authors"     : authors,
                "description" : false,
                "user"        : req.user.username,
                // Navbar options
                "navStatic" : true,
                "home"     : true,
            };
            res.render('home.html', templateParameters);
        });
    });

Note that in this specific example, we first check for if a user is in an authenticated session, and then we render/output the template with the above parameters. Of interest is the `req.user.username` seen above, which returns the username of the current user who is logged in. You can choose any field from the schema defined at the beginning of this post, but I would warn against sending the salt or hashed password, as that could potentially destroy your user security entirely. 

One interesting parameter that can be returned is the `req.user.id` parameter, which was not explicitly outlined in the schema above. This is a parameter that is automatically generated by Mongoose when the schema is compiled into a Model object, which happens at the end of `models/userSchema.js`. One notable use case for this is making GET and POST requests to specific fields for users. Take for example the `userData` field that each user has, which needs to be obtained and updated every time the store layout configuration changes: 

    app.get('/get-user-data', function(req, res) { 
        Auth.isAuthenticated(req, res, function() { 
            User.findById(req.user.id, function(err, doc) { 
                console.log(doc.userData);
                if(err) { 
                    res.send(500);
                } else {
                    res.set({
                        "Content-Type": "application/json",
                        "Content-Length": doc.userData.length
                    });
                    res.send(doc.userData);
                }
            });
        });
    });

The above will return the JSON string stored in the `userData` field, using some built in functionality of our User model (returned by including `models/userSchema.js`) our authentication helpers (defined in `config/auth.js` above). If you want to learn more about these in detail, I highly suggest reading the extensive documentation and API reference available both for Passport ([guide](http://passportjs.org/guide/)) and Mongoose ([docs](http://mongoosejs.com/docs/guide.html)). 
