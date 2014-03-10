#! /bin/bash

scp pi@rpural:cpuTemp/rmTemp.log ~/cpuTemp/rmTemp.log
scp pi@rpural:cpuTemp/cpuTemp.log ~/cpuTemp/cpuTemp.rpural
scp pi@rpural2:cpuTemp/cpuTemp.log ~/cpuTemp/cpuTemp.rpural2
~/uDooTemp/buildGraph.py

