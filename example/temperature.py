# coding: utf-8
## @package faboTemperature.py
#  This is a library for the FaBo Temperature I2C Brick.
#
#  http://fabo.io/207.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoTemperature_ADT7410
import time
import sys

adt7410 = FaBoTemperature_ADT7410.ADT7410()

try:
    while True:
        temp = adt7410.read()
        print "Temperature = ", temp

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
