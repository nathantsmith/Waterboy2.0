import Adafruit_BBIO.GPIO as GPIO
import time

global NUM_STATIONS
NUM_STATIONS = 16

global SR_CLK_PIN
global SR_NOE_PIN
global SR_DAT_PIN
global SR_LAT_PIN
SR_CLK_PIN = "P9_13"
SR_NOE_PIN = "P9_14"
SR_DAT_PIN = "P9_11"
SR_LAT_PIN = "P9_12"

values = [0] * NUM_STATIONS

def setShiftRegister(values):
	GPIO.output(SR_CLK_PIN,GPIO.LOW)
	GPIO.output(SR_LAT_PIN,GPIO.LOW)
	for x in range(0,NUM_STATIONS):
		GPIO.output(SR_CLK_PIN,GPIO.LOW)
		if values[NUM_STATIONS-1-x] == 1:
			GPIO.output(SR_DAT_PIN,GPIO.HIGH)
		else:
			GPIO.output(SR_DAT_PIN,GPIO.LOW)
		GPIO.output(SR_CLK_PIN,GPIO.HIGH)
	GPIO.output(SR_LAT_PIN,GPIO.HIGH)
def disableShiftRegisterOutput():
	GPIO.output(SR_NOE_PIN,GPIO.HIGH)
def enableShiftRegisterOutput():
	GPIO.output(SR_NOE_PIN,GPIO.LOW)
def resetStations():
	for x in range(0,NUM_STATIONS):
		values[x] = 0
	setShiftRegister(values)

GPIO.setup(SR_CLK_PIN, GPIO.OUT)
GPIO.setup(SR_NOE_PIN, GPIO.OUT)
disableShiftRegisterOutput()
GPIO.setup(SR_DAT_PIN, GPIO.OUT)
GPIO.setup(SR_LAT_PIN, GPIO.OUT)

GPIO.output(SR_LAT_PIN, GPIO.HIGH)
resetStations()
enableShiftRegisterOutput()

while True:
	for x in range(0,NUM_STATIONS):
		values[x] = 1
		setShiftRegister(values)
		print "Station", (x+1)
		time.sleep(10)
		values[x] = 0
		setShiftRegister(values)
		time.sleep(.5)
