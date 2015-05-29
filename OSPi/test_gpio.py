#import gv
import time
import Adafruit_BBIO.GPIO as GPIO # Required for accessing General Purpose Input Output pins on Beagle Bone Black
print GPIO

#gv.platform = 'bo'
#print 'using bo'
#GPIO.cleanup()
#pin_sr_dat = "P9_11"
#pin_sr_clk = "P9_13"
#pin_sr_noe = "P9_14"
#pin_sr_lat = "P9_12"
#pin_rain_sense = "P9_15"
#pin_relay = "P9_16"

GPIO.cleanup()
GPIO.setup("P9_12", GPIO.OUT)
while 1:
    print "HIGH"
    GPIO.output("P9_12", GPIO.HIGH)
    time.sleep(3)
    print "LOW"
    GPIO.output("P9_12", GPIO.LOW)
    time.sleep(3)

#GPIO.output(pin_sr_latIO.HIGH)
#print 'blahh'

