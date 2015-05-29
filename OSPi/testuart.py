import Adafruit_BBIO.UART as UART
import serial
import time

UART.setup("UART1")

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=57600)

if(ser1.isOpen()==False):
    ser1.open()

print "Connected to: " + ser1.portstr

ser1.flushInput()
ser1.flushOutput()
result = ser1.readline()
print result
ser1.close()
