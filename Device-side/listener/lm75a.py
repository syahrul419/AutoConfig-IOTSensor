#!/usr/bin/python

# Raspberry Pi LM75A I2C temperature sample code.
# Author: Leon Anavi <leon@anavi.org>

import sys
import smbus
import time

address = 0x48
suhu_state = False

def suhu():
    global address, suhu_state
    while True:
        try:
            # cek alamat lain lebih spesifik
            if 1 < len(sys.argv):
                address = int(sys.argv[1], 16)

            # Read I2C data and calculate temperature
            bus = smbus.SMBus(1)
            raw = bus.read_word_data(address, 0) & 0xFFFF
            raw = ((raw << 8) & 0xFF00) + (raw >> 8)
            temperature = (raw / 32.0) / 8.0
            # Print temperature
            print ('Temperature: {0:0.2f} *C'.format(temperature))

            time.sleep(1)
            suhu_state = True
            #print (suhu_state)
            return suhu_state
            break
        except Exception as e:
            #print (e)
            suhu_state = False
            #print (suhu_state)
            time.sleep(1)
            return suhu_state
            continue

#while True:
#	suhu()
