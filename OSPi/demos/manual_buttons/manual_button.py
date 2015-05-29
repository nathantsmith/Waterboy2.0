from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import os
import Adafruit_BBIO.GPIO as GPIO
import atexit

# GPIO PIN DEFINES

pin_sr_clk = "P9_13"
pin_sr_noe = "P9_14"
pin_sr_dat = "P9_11"
pin_sr_lat = "P9_12"

# NUMBER OF STATIONS
num_stations = 16

# STATION BITS
values = [0]*num_stations

def enableShiftRegisterOutput():
    GPIO.output(pin_sr_noe, GPIO.LOW)

def disableShiftRegisterOutput():
    GPIO.output(pin_sr_noe, GPIO.HIGH)

def setShiftRegister(values):
    GPIO.output(pin_sr_clk, GPIO.LOW)
    GPIO.output(pin_sr_lat, GPIO.LOW)
    for s in range(0,num_stations):
        GPIO.output(pin_sr_clk, GPIO.LOW)
	if values[num_stations-1-s] == 1:
	        GPIO.output(pin_sr_dat, GPIO.HIGH)
	else:
		GPIO.output(pin_sr_dat, GPIO.LOW)
        GPIO.output(pin_sr_clk, GPIO.HIGH)
    GPIO.output(pin_sr_lat, GPIO.HIGH)

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        global values
        rootdir = '.' #file location
        try:
            if self.path.endswith('.js'):
                f = open(rootdir + self.path) #open requested file

                #send code 200 response
                self.send_response(200)

                #send header first
                self.send_header('Content-type','text/html')
                self.end_headers()

                #send file content to client
                self.wfile.write(f.read())
                f.close()
                return
            elif '/cv?' in self.path:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
		parsed=urlparse.parse_qs(urlparse.urlparse(self.path).query)
                sn = int(parsed['sid'][0])
                v = int(parsed['v'][0])
                if sn<0 or sn>(num_stations-1) or v<0 or v>1:
                    self.wfile.write('<script>alert(\"Wrong value!\");</script>');
                else:
                    if v==0:
                        values[sn] = 0
                    else:
                        values[sn] = 1
                    setShiftRegister(values)

		self.wfile.write('<script>window.location=\".\";</script>')
            else:
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('<script>\nvar nstations=')
                self.wfile.write(num_stations)
                self.wfile.write(', values=[')
                for s in range(0,num_stations):
                    self.wfile.write(values[s])
                    self.wfile.write(',')
                self.wfile.write('0];\n</script>\n')
                self.wfile.write('<script src=\'manual.js\'></script>')

        except IOError:
            self.send_error(404, 'file not found')
    
def run():
    #GPIO.cleanup()
    # setup GPIO pins to interface with shift register
    #GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_sr_clk, GPIO.OUT)
    GPIO.setup(pin_sr_noe, GPIO.OUT)
    disableShiftRegisterOutput()
    GPIO.setup(pin_sr_dat, GPIO.OUT)
    GPIO.setup(pin_sr_lat, GPIO.OUT)

    setShiftRegister(values)
    enableShiftRegisterOutput()

    #ip and port of servr
    #by default http server port is 8080
    server_address = ('', 26)
    #HTTPServer.ThreadingTCPServer.allow_reuse_address = True
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('OpenSprinkler Beagle is running...')
    while True:
        httpd.handle_request()

def progexit():
    global values
    values = [0]*num_stations
    setShiftRegister(values)
    GPIO.cleanup()

if __name__ == '__main__':
    atexit.register(progexit)
    run()
