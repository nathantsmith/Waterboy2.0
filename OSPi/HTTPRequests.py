import urllib2
import json
import gv

def setstation(station, status, duration):
	setmode("manual")
	station = str(station)
	status = str(status)
	duration = str(duration)
	cite = urllib2.urlopen('http://localhost:8080/sn' + station + '=' + status + '&t=' + duration)
	cite.close()

def setmode(mode):
	if mode == "auto":
		modeset = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=&mm=0&rd=&wl=&rbt=0')
		modeset.close()
	elif mode == "manual":
		modeset = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=&mm=1&rd=&wl=&rbt=0')
		modeset.close()

def startup():
	startup = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=1')
	startup.close()

def shutdown():
	shutdown = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&en=0')
	shutdown.close()

def runonce(runOnceArray):
        runOnceArray = str(runOnceArray).replace(" ","")
	runonce = urllib2.urlopen('http://localhost:8080/cr?pw=opendoor&t=' + runOnceArray)
	runonce.close()

def getstationstatus():
	getstatus =  urllib2.urlopen('http://localhost:8080/js?pw=opendoor')
	print getstatus.read()
	getstatus.close()

def getstationnames():
	getnames = urllib2.urlopen('http://localhost:8080/jn?pw=opendoor')
        print getnames.read()
	getnames.close()

def getcontrollervariables():
	getcontroller = urllib2.urlopen('http://localhost:8080/jc?pw=opendoor')
	print getcontroller.read()
	getcontroller.close()

def resetstations():
	resetstations = urllib2.urlopen('http://localhost:8080/cv?pw=opendoor&rsn=1')
	resetstations.close()

def enableprogram(pid):
    pid = int(pid)
    pf = open('./data/programs.json', 'r')
    gv.pd = json.load(pf)
    pf.close()
    (gv.pd[pid])[0] = 1
    gv.pd[pid] = str(gv.pd[pid])
    gv.pd[pid] = (gv.pd[pid]).replace(" ","")
    pidstr = str(pid)
    enpgrm = urllib2.urlopen('http://localhost:8080/cp?pw=opendoor&pid=' + pidstr + '&v=' + gv.pd[pid])
    enpgrm.close()

def disableprogram(pid):
    pid = int(pid)
    pf = open('./data/programs.json', 'r')
    gv.pd = json.load(pf)
    pf.close()
    (gv.pd[pid])[0] = 0
    gv.pd[pid] = str(gv.pd[pid])
    gv.pd[pid] = (gv.pd[pid]).replace(" ","")
    pidstr = str(pid)
    dispgrm = urllib2.urlopen('http://localhost:8080/cp?pw=opendoor&pid=' + pidstr + '&v=' + gv.pd[pid])
    dispgrm.close()

def disableallprograms():
    #pid = int(pid)
    pf = open('./data/programs.json', 'r')
    gv.pd = json.load(pf)
    pf.close()
    numofpgrms = len(gv.pd)
    for i in range(0, numofpgrms):
        disableprogram(i)

#moveupprogram(1)
#test = urllib2.urlopen('http://localhost:8080/cr?pw=opendoor&t=[60,0,60,0,60,0,600,0]')
#test.close()

#i = 1
#while i<=8:
#    setstation(i,1,60)
#    i = i + 1
#time.sleep(20)
#setmode("auto")
