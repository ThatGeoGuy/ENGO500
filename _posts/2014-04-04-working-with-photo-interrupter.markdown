--- 

layout: post
title: Working with a Photo Interrupter
author: Alexandra Cummins

excerpt: In addition to tracking customer movement, we also wanted to be able to tell if the shelf was 'faced' or not.  We chose to use a Photo Interrupter to complete this task.
 
---
#  Working with a Photo Interrupter
<p class='blog-post-meta'>{{ page.date | date: "%Y-%m-%d" }} by {{ page.author }}</p>

In addition to tracking customer movement, we also wanted to be able to tell if the shelf was 'faced' or not.  We chose to use a [Photo Interrupter](https://www.sparkfun.com/products/9299) to complete this task.

This small sensor has [five pins](https://www.sparkfun.com/datasheets/Components/GP1A57HRJ00F.pdf) and sits directly in the breadboard.  It works by shooting a beam of light between its two prongs. When an object is placed between the prongs, the path of light is blocked, and the detector reads zero.  Otherwise, it reads one. We plan to use these sensors with self-facing shelves as discussed [here]({{ site.baseurl }}/2014/04/03/development-process-technical-deliverables-progress-report/).

##Wiring
Since the Photo Interrupter is pretty much symmetrical, it is important to note that the data sheet diagram shows the sensor FROM ABOVE (as confirmed by the small and barely noticeable capacitor icon on the tip of one if the prongs).  Mixing this up has the potential to result in roasted equipment.

![PhotoInt diagram]({{ site.baseurl }}/images/sensors/photoint.PNG)

Another interesting thing is that both sides of the Photo Interrupter are wired individually.  This gives us the option of splitting it in half to widen the gap between prongs if need be.

Since each side is independent (one is a simple capacitor), the sensor has two ground connections (one with a resistor) and two voltage connections.  On the detector side, there is an alarm connection, which we attached to GPIO # 17.


##Coding in Python

As described in my post about the [PIR Motion Sensor]({{ site.baseurl }}/2014/04/04/working-with-a-PIR-motion-sensor/), the GPIO pins were set up and tested.

	import RPi.GPIO as GPI
	GPIO.setmode(GPIO.BCM)
	GPIO_Pint = 17
	
	GPIO.setup(GPIO_Pint,GPIO.IN) 
	
	if GPIO.input(17):
  		print('Port 17 is 1/GPIO.HIGH/True')
	else:
  		print('Port 17 is 0/GPIO.LOW/False')

This time, the steady state of the sensor would not rest at zero, but at one. Using a while loop to continuously check the sensor status, we used the following logic to isolate instances in which the sensor transitions from steady state to triggered state.  Only under these conditions will it attempt to [post an observation to the server]({{ site.baseurl }}/2014/04/04/post-ing-from-the-RPi/).  This eliminates the constant stream of zeros that it would otherwise post once it is triggered. 

	Switch_State = 1
	Prev_Switch_State = 1
	try:
		Switch_State = GPIO.input(17)
    		if Switch_State == 0 and PSS == 1:
       			#SWITCH STATE IS ZERO
			#post obs
       			Prev_Switch_State = 0
    		elif Switch_State == 1 and PSS == 0:
       			#Switch is reset
			#post obs
        		PSS = 1
   		 time.sleep(0.01)      
	except KeyboardInterrupt:
	GPIO.cleanup()

And not only that - it allows us to post at both instances in time: when the switch was triggered, and when it returned to steady state. In other words - when the shelf became unfaced and when it was stocked up again.  Both of these transitions of state would be valuable information to a store owner.