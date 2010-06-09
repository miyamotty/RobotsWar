#!/usr/bin/python

import serial
import os
from struct import pack
try:
    ser = serial.Serial('/dev/ttyACM0', baudrate=115200)
    ser.open()

    # pull dtr and rts low
    ser.setRTS(0)
    ser.setDTR(0)

    # toggle DTR
    ser.setDTR(1)
    ser.setDTR(0)

    programDelay = pack("b",35)
    ser.write(programDelay)

    # close
    ser.close()

except:
    print "Failed to open the serial port for reset, perhaps this is your first upload or the board was already in bootloader mode"
