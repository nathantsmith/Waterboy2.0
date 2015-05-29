===========================================
OpenSprinkler Beagle (OSBo) Manual_Buttons Demo
Nov 2013, http://beagle.opensprinkler.com
===========================================

Description
-----------
This demo starts a Python HTTP server, which presents a simple webpage with a list of buttons, each corresponding to a stations. Clicking on each button to manually turn on/off a station.

Before running this demo, it is assumed that you have the Adafruit_BBIO.GPIO Python module installed (http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu)

To run the demo, type in command line:
> sudo python manual_button.py

This will start the Python HTTP server. Next, open a browser, and type into the following url:

http://x.x.x.x:8080

where x.x.x.x is the ip address of your BeagleBone Black.

You should see a list of 16 buttons. Clicking on each button to toggle the corresponding station.


Modification
------------
The code consists of two files: manual_button.py runs the HTTP server and maintains station variables; the webpage is formatted using the Javascripts in manual.js. You can follow the examples to extend the functionality of this demo.


