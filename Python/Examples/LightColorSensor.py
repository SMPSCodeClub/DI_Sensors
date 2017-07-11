#!/usr/bin/env python
#
# https://www.dexterindustries.com
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information see https://github.com/DexterInd/DI_Sensors/blob/master/LICENSE.md
#
# Python example program for the Dexter Industries Light Color Sensor

from __future__ import print_function
from __future__ import division

import time
from di_sensors import light_color_sensor

print("Example program for reading a Dexter Industries Light Color Sensor on an I2C port.")

lcs = light_color_sensor.LightColorSensor(led_state = True)

while True:
    # Read the R, G, B, C color values
    r, g, b, c = lcs.get_raw_colors()
    
    # Print the values
    print('Red: %5.3f Green: %5.3f Blue: %5.3f Clear: %5.3f' % (r, g, b, c))
    
    time.sleep(0.02)
