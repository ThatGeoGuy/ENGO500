--- 

layout: post
title: Working with a PIR Motion Sensor
author: Alexandra Cummins

excerpt: One of the main focuses on the hardware side of LASS involved setting up a PIR sensor to track customer movement.  In this post we will look at what we did to include this equipment in our prototype development, in terms of wiring, python code, and design choices.
 
---
#  Working with a PIR Motion Sensor
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>


One of the main focuses on the hardware side of LASS involved setting up a [PIR sensor](https://www.sparkfun.com/products/8630) to track customer movement.  In this post we will look at what we did to include this equipment in our prototype development, in terms of wiring, python code, and design choices.



**Wiring**


Since none of us had much experience with electronics when we started this project, the first thing we learned was to [stick to your datasheet](https://www.sparkfun.com/datasheets/Sensors/Proximity/SE-10.pdf).  This can be found easily enough online through a simple search.  The datasheet provides specific information for your sensor and how to use it without burning the place down.  

For the PIR, you will notice that it has three connections: DC 12V, Alarm, and Ground. Using a Raspberry Pi, a breakout cable and a breadboard, we were able to simply connect each of these to their respective pins as shown below.  For the alarm connection, we used GPIO Pin #18.  

![PIR sensor set up]({{ site.baseurl }}/images/sensors/DSC00952.JPG)



**Coding in Python**


Now that the sensor was set up, something had to read and record the data once it reached the RaspberryPi on the other side of the breakout cable.  For this we implemented a short python script, beginning with the inclusion of the GPIO library, the pin set-up, and a quick connection check.  It is also necessary to specify the numbering mode of the GPIO pin, since more than one exists.  We used BCM, or Broadcom.

	import RPi.GPIO as GPI
	GPIO.setmode(GPIO.BCM)
	GPIO_PIR = 18
	
	GPIO.setup(GPIO_PIR,GPIO.IN) 
	
	if GPIO.input(18):
  		print('Port 18 is 1/GPIO.HIGH/True')
	else:
  		print('Port 18 is 0/GPIO.LOW/False')

As you can probably tell from the above code, if the input of GPIO #18 is 1, then the sensor has been activated.  Otherwise, it is zero.

To continuously check the status of the sensor, we used to following logic contained within a while loop:

	try:
  		print "Waiting for PIR to settle ..."
  		while GPIO.input(GPIO_PIR)==0:
    		Current_State  = 1
		# Loop until users quits with CTRL-C
  		while True :
    			# Read PIR state
    			Current_State = GPIO.input(GPIO_PIR)
   		
    			if Current_State==0 and Previous_State==1:
      				# PIR is triggered
     				Previous_State=0
    			elif Current_State==1 and Previous_State==0:
      				# PIR has returned to ready state
      				Previous_State=1
			time.sleep(0.01)      
	except KeyboardInterrupt:
  	GPIO.cleanup()

Since we are sending observations to the server in real time, this code allows us to send only when the PIR transition between steady and triggered states.  Since the sleep time is so small, it helps us avoid constant triggers during high movement periods or periods of complete rest, while still posting in real time.


**Other Challenges**


The PIR sensor turned out to be extremely sensitive, to the point where it would be constantly triggered by nothing at all.  We managed to calm it down by placing a resistor between the voltage and alarm connections.  You can see it in the above picture.