from ospi import *
from thermistorconversion import *
import ast
import Adafruit_BBIO.UART as UART
import serial
import time
from ISStreamer.Streamer import Streamer

rssi = Streamer(bucket_name="RSSI", access_key="YourAccessKey")
shallowtemp = Streamer(bucket_name="Shallow Temperature", access_key="YourAccessKey")
shallowvwc = Streamer(bucket_name="Shallow VWC", access_key="YourAccessKey")
deeptemp = Streamer(bucket_name="Deep Temperature", access_key="YourAccessKey")
deepvwc = Streamer(bucket_name="Deep VWC", access_key="YourAccessKey")

UART.setup("UART1")
UART.setup("UART2")

ser1 = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser2 = serial.Serial(port = "/dev/ttyO2", baudrate=57600)

if(ser1.isOpen()==False):
    ser1.open()
if(ser2.isOpen()==False):
    ser2.open()

time.sleep(60) #Sleep to let ospi get fully established
while 1:
    gv.hubnames = data('hubnames')

    gv.hubnames = ast.literal_eval(gv.hubnames)

    uartstring = ser2.readline()
    print uartstring
    uartstring = uartstring.replace("\r\n", "")
    uartlist = uartstring.split(",")

    if (len(uartlist)==6):
        uartlist[2] = int(uartlist[2])
        uartlist[3] = int(uartlist[3])
        uartlist[4] = int(uartlist[4])
        uartlist[5] = int(uartlist[5])
        for i in range(1,3):
            temperature = convert_to_temperature((uartlist[i+3]))
            vwc = convert_to_vwc((uartlist[i+1]), temperature)
            uartlist[i+1] = vwc
            uartlist[i+3] = temperature

        rssi.log(uartlist[1])
        shallowtemp.log(uartlist[2])
        shallowvwc.log(uartlist[3])
        deeptemp.log(uartlist[4])
        deepvwc.log(uartlist[5])

        rssi.close()
        shallowtemp.close()
        shallowvwc.close()
        deeptemp.close()
        deepvwc.close()

    i=0
    for x in gv.hubnames:
        if ((uartlist[0] == x[1]) and (len(uartlist)==6)):
            if (len(gv.hubnames[i]))==3:
                gv.hubnames[i].extend(uartlist[2:6])
            elif (len(gv.hubnames[i]))==7:
                for j in range(3,7):
                    ((gv.hubnames[i])[j]) = uartlist[j-1]
        i = i + 1

    hubnames = str(gv.hubnames)
    print hubnames
    save('hubnames', hubnames)
    time.sleep(5)
