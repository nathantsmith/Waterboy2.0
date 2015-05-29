import time
timeoffset = -5
utctime = time.localtime()
current = utctime[3] + timeoffset
print utctime
print current
