======================================
OpenSprinkler Beagle (OSBo) Self-Test Demo
Nov 2013, http://beagle.opensprinkler.com
======================================

Description
-----------
This demo turns on each station for 10 seconds in turn one after another. The osbo_relay demo turns on and off the on-board relay at 1Hz.

Before running this demo, it is assumed that you have the Adafruit_BBIO.GPIO Python module installed (http://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/installation-on-ubuntu)

Note that if a station is running when the user presses Ctrl+C to terminate the program, that station will not reset. This is because the program does not capture the Ctrl+C event.

To run the demo, type in command line:
> sudo python selftest.py
> sudo python relaytest.py
