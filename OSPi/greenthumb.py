from HTTPRequests import *
from ospi import *
import ast
import time

###print gv.hub
"""Conditions
if vwc 1 or 2 < ? auto water for set duration
if vwc 1 or 2 > ? shutoff valves for set duration
if temp1 or temp2 < 32 shutoff everything
"""
#Uncomment this
#time.sleep(60) #Sleep 60 seconds so ospi has time to fully initialize
while 1:
    if ((gv.sd['mm'])==1):
        ###add watering duration option to the webpage
        ###use gv.hubnames

        ltct = int(gv.sd['ltct'])
        lwlt = int(gv.sd['lwlt'])
        hwlt = int(gv.sd['hwlt'])
        wd = int(gv.sd['wd'])

        wd = wd * 60 #converts minutes into seconds for the api
	#hub example
	#testhub = {}

        hubnames = ast.literal_eval(gv.hubnames)

        print hubnames

        runoncelist = [0] * (len((hubnames[0])[2]))

        for sh in hubnames:
    	    if (len(sh) != 7):
                print "No Data"
	    else:
                try:
                    sh[3] = int(sh[3])
                except ValueError:
                    sh[3] = 99999.9
                try:
                    sh[4] = int(sh[4])
                except ValueError:
                    sh[4] = 99999.9
                try:
		    sh[5] = int(sh[5])
                except ValueError:
                    sh[5] = 99999.9
                try:
	            sh[6] = int(sh[6])
                except ValueError:
                    sh[6] = 99999.9

    	    if ((sh[5]) < ltct) or ((sh[6]) < ltct):
                print "Temperature is too low. Shutting down all watering."
                #runonce([0,0,0,0,0,0,0,0,0])
                disableallprograms()
	    else:
                print "Temperature is ok. Continuing to water."
                if ((sh[3]) < lwlt) or ((sh[4]) < lwlt):
                    print "Enabling First Program"
                    valvecontrol = (sh[2])
	    	    valvecontrol = map(int,valvecontrol)
		    ##run once methodology
	    	    #i = 0
    		    #for x in valvecontrol:
                    #    if (runoncelist[i] == 0):
                    #        x = x * wd
    	    	    #        runoncelist[i] = x
	    	    #    i = i + 1
                    disableallprograms()
                    enableprogram(0)
	        elif ((sh[3]) > hwlt) or ((sh[4]) > hwlt):
                    print "Disabling All Programs"
	    	    #valvecontrol = (sh[2])
    		    #valvecontrol = map(int,valvecontrol)
                    #i=0
		    #for x in valvecontrol:
                    #    x = 0
	    	    #    valvecontrol[i] = x
    		    #    i = i + 1
                    #valvecontrol.append(0)
                    #runonce(valvecontrol)
                    disableallprograms()
                    enableprogram(1)
	        else:
	    	    print "Enabling Second Program"
                    disableallprograms()
                    enableprogram(1)
	    #need next two lines for runonce methodology
            #runoncelist.append(0)
	    #runonce(runoncelist)
    else:
        print "Runnning in program mode"

    time.sleep(10)
