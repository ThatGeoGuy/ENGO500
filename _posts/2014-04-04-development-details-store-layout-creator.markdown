---

layout: post
title: Development Details - Store Layout Creator
author: Ben Trodd
published: false

excerpt: The Store Layout Creator page made up a significant portion of the front-end software development effort. There was a need to create a system by which the user can create a digital representation of a physical space. The format chosen was one that resembles inventory plans that are used in large stores to organize products. Efforts were made to build a system that can be altered dynamically in order to create an accurate and up to date model. In this post, we talk about the development details of the Store Layout Creator.

---
# Development Details: Store Layout Creator
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

The Store Layout Creator page made up a significant portion of the front-end software development effort. There was a need to create a system by which the user can create a digital representation of a physical space. The format chosen was one that resembles inventory plans that are used in large stores to organize products. Efforts were made to build a system that can be altered dynamically in order to create an accurate and up to date model. In this post, we talk about the development details of the Store Layout Creator.

## Enabling Technologies

To enable the user to build a model dynamically, it was decided that both a visual representation and easy to modify controls were needed. The user interface that was eventually decided upon was uses the [bootstrap](http://getbootstrap.com) front end framework for positioning and styling, [jQueryUI accordion](http://jqueryui.com/accordion/) elements to organize the user's information, [X-editable](http://vitalets.github.io/x-editable/) to allow real-time editing of attributes, and [D3.js](http://d3js.org/) to vizualise the store floorplan. To simplyfy the javascript necessary to merge all of these technologies together, [jQuery](http://jquery.com/) was utilzied.

## Store Layout Creator Architecture

Shown below is a screenshot of the system with some shelves and sections added:

![Store Layout Creator]({{ site.url }}/ENGO500/images/storeLayoutCreator/FullLabelled.png)

### System Overview

As you can see in the screenshot above, the system is split into two distinct panels. When a user wants to create a model of their store, what they are really doing is manipulating a javascript object with the controls that have been provided to them. While both the left and right panels are representations of the same object, they present this data in a different way. 

The user is given control over the javascript object via the controls of the left panel, labelled 1. The elements labelled 'Shelf 1', 'Shelf 2', etc, are jQueryUI accordion elements. Note that inside of the open element, 'Shelf 2', there are a set of nested accordions. These contain the attributes and sections of 'Shelf 2'. By utlizing the '+ Section', '+ Shelf' and '(x)' (remove) buttons, users can add to the object or remove the selected accordion element. Within each of the nested accordions, editable text fields exist. These allow users to configure the attributes of each part of their model.

The visual representation of this model is shown in the right panel, labelled 2. This is displayed to guide the user's creation by allowing them to relate what they are building to physical space. The visualization is updated in real time as elements are added and removed. In the screenshot provided, the shelves are represented by the 6 light blue rectangles that contain an assortment of smaller blue rectangles. They are created as from left to right, and are in groups of two to represent two opposing sides of a shelf. Thus, the white space between the shelves represents the concept of an 'aisle'. The smaller blue rectangles contained within them represent Sections, which can be used to set up logical divisions to differeniate products on a shelf. They are created from top to bottom.

Once the user is happy with the layout of their store, the javascript object is converted to JSON and saved to database. Anytime the Store Layout Creator is opened thereafter, the object is loaded and the accordion elements, attributes, and visualization are rendered exactly as they were configured when the user saved. This allows the user to edit their store layout at any time without needing to build a new one from scratch.

### Data Structure

An example of the object that is being manipulated and displayed by the user interface is shown below:

~~~ javascript
shelves = [
	{
		"sections": [
			{
				"displayID":"Dog Food",
				"pirURL":".../Things(1)/Datastreams(1)/Observations",
				"pintURL":".../Things(1)/Datastreams(2)/Observations"
			},
			{
				"displayID":"Cat Food",
				"pirURL":".../Things(2)/Datastreams(3)/Observations",
				"pintURL":".../Things(2)/Datastreams(4)/Observations"
			},
			{
				"displayID":"Bird Seed",
				"pirURL":".../Things(3)/Datastreams(5)/Observations",
				"pintURL":".../Things(3)/Datastreams(6)/Observations"
			}
		],
		"notes":"Pet Food Shelf"
	},
	{
		"sections": [
			{
				...
			}
		]
		"notes":"Some other Shelf"
	}
]
~~~

The `shelves` array holds the `shelf` objects which, in this example, are comprised of `notes` which is assigned in the 'Shelf Attributes' accoridon, and an internal array for `sections` which holds the `section` objects. There are three sections in the first shelf, for 'Dog Food', 'Cat Food' and 'Bird Seed'. Alongside these attributes is the `pirURL` and the `pintURL`. These are the addresses of the observations of the sensors that are contained within those sections. A second shelf exists, with some filler text for its attributes.

### Technical Challenges

This section details some of the challenges encountered in building the Store Layout Creator. It serves to explain the inner workings of the system to guide anyone that wishes to use of modify our code.

#### Nested Accordions

jQueryUI accordions are based off of pre-defined html structures which are converted to an accordion once the accordion events are attached to them. In order to facilitate this in an on-the-fly manner, the first step was to create a template of an accordion and house it in the HTML document for the page. We also need a 'parent' accordion for all of the new accordion elements to be added to. These can be seen below:

~~~ html
<!-- Parent for all accordions -->
<div id='parentAccordion'></div>

<!-- Template for accordions -->
<div class='accordion'>
	<h3 class='accordion-title'></h3>
	<div class='accordion-content'></div>
</div>
~~~

Then, the accordion events must be attached to `#parentAccordion`. The options available are defined in the [documentation](http://api.jqueryui.com/accordion/).

~~~ javascript
var accordionConfig = { ...options... };
var $parentAccordion = $("#parentAccordion");
$parentAccordion.accordion(accordionConfig);
~~~

With our accordion template defined, we can clone each time a new accordion is needed.

~~~ javascript
var $newAccordion = $('.accordion').children().clone();
~~~

Each of these clones will require the accordion events to be attached to them, just like `#parentAccordion`.

~~~ javascript
$newAccordion.accordion(accordionConfig);
~~~

Then we append them to `#parentAccordion`.

~~~ javascript
$parentAccordion.append($newAccordion);
$parentAccordion.accordion("refresh");
~~~

The accordion elements are created with the following:
* The header (title bar) with `id="#ui-accordion-parentAccordion-header-" + n`
* The panel (body) with `id="#ui-accordion-parentAccordion-panel-" + n`
Where `n` is the nth element in the accordion.

Utilizing these selectors, you can change the title and body contents. Additionally, by selecting the body of an accordion, you can attach a nested accordion by following the steps described above.

#### Removing Shelves and Sections

#### Saving and loading editable attributes

#### D3.js