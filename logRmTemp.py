#!/usr/bin/python

# Read the room temperture via a one-wire thermal sensor
# on the Raspberry Pi

import os
import glob
import time
     
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
     
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '10*')[0]
device_file = device_folder + '/w1_slave'
     
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
     
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

prev_temp = 0.0
temp_c = 99.0
while (prev_temp != temp_c):
    prev_temp = temp_c
    (temp_c, temp_f) = read_temp()

local = time.localtime()
print "\"{:4d}-{:02d}-{:02d} {:02d}:{:02d}\", {:.1f}".format(local[0], local[1], local[2], local[3], local[4], temp_f)
