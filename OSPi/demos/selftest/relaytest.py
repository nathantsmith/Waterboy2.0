import Adafruit_BBIO.GPIO as GPIO
import time

global RELAY_PIN
RELAY_PIN="P9_16"

GPIO.setup(RELAY_PIN, GPIO.OUT)

while True:
	for x in range(0,10):
		GPIO.output(RELAY_PIN, GPIO.HIGH);
		print "Relay On"
		time.sleep(1)
		GPIO.output(RELAY_PIN, GPIO.LOW);
		print "Relay Off"
		time.sleep(1)
