#!/bin/bash

echo ttyO1_armhf.com > /sys/devices/bone_capemgr.9/slots
echo ttyO2_armhf.com > /sys/devices/bone_capemgr.9/slots
echo ttyO5_armhf.com > /sys/devices/bone_capemgr.9/slots

sleep 15

while [ 1 ]
  do
    for (( i = 9000; i <= 9010; i++ )); do
      echo "Trying Port: $i"

      ssh -p 21000 -o ConnectTimeout=5 -o ExitOnForwardFailure=yes -nNTR $i:localhost:22 waterboy@www.drewthejames.com
    done

    echo "No Open Ports Found"

    sleep 30
  done
fi
