---

layout: post
title: New feature! View store history
author: Ben Trodd and Kathleen Ang

excerpt: Today we added a new feature to our store viewer -- you can now view the past 1-24 hours of traffic and stock history.

---
# New feature! View store history
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

Today we added a new feature to our store viewer -- you can now view the past 1-24 hours of traffic and stock history.

Check out this awesome screenshot of the History tab in action:

![Sweet historical stuff]({{ site.baseurl }}/images/storeViewer/history.png)

At the very top, you can see there are two new tabs added in: Real-Time and History (marked by 1 in the figure). Both modes will render the same store layout, but different observations. The default tab, Real-Time, shows the current traffic and stock information as our original version did. However, if you select the History tab instead, you can see traffic and stock information based on the past 1-24 hours.

In the top right-hand corner, there is a slider (marked by 2 in the figure). This slider is used to select the number of hours you would like to view. For example, if you want to see aggregate traffic and stock data for the last 14 hours, you can slide it to 14. In the screenshot shown, we selected 24 hours.

Once you've selected a time frame, the traffic and stock observations will be overlaid on the store map. The heat map (marked by 3 in the figure) is rendered much like the real-time version, except this time the colour of the heat map corresponds to the total number of motion sensor observations (i.e. how many people passed by that section in the past, for example, 24 hours). Yellow corresponds to fewer traffic observations, and the colour varies from orange to red as the number of traffic observations increases.

Finally, stock observations are also updated (marked by 4 in the figure). The number in each section is reflective of the number of times that section was emptied in the past time period. In our example, one of the shelves had been emptied 17 times in the past 24 hours, whereas the shelf adjacent had only been emptied 3 times in the past 24 hours. 

#### Future work

While this feature is really neat and we think it adds a lot of value to the store owner, there are still some small user experience items to be added in the future. We would like to add a colour bar/legend so that it's more clear what heat map shades correspond to in terms of real numbers. 