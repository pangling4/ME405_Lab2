"""!
@file main.py
 Implements proportional control for motors connected to nucleo board provided
 in ME 405 lab. Asks for kp input.

@author Jonathan Cederquist
@author Tim Jain
@author Philip Pang

@date   2-Feb-2022
"""

import pyb
import utime
import math
import ClosedLoop
import RoboEncoderDriver
import RoboMotorDriver

# Instantiates two motor driver objects with appropriate pins and timer number
pinA6 = pyb.Pin(pyb.Pin.board.PA6, pyb.Pin.OUT_PP)
pinA7 = pyb.Pin(pyb.Pin.board.PA7, pyb.Pin.OUT_PP)
    
motor2 = RoboMotorDriver.RoboMotorDriver(pinA6, pinA7, 3, 2)

# Instantiates two encoder driver objects with appropriate pins and timer number
encoder2 = RoboEncoderDriver.RoboEncoderDriver(pyb.Pin(pyb.Pin.board.PC6), pyb.Pin(pyb.Pin.board.PC7), 8)


# Instantiates controller object to calculate desired motor effort/duty cycle
control = ClosedLoop.ClosedLoop(0.5, 0, 180)

# for data collection, set period between data calls
period = 5 #ms
data = []

try:
    while True:
        
        control.change_kp(float(input("set Kp: ")))
        control.change_ki(float(input("set Ki: ")))
        encoder2.zero()
        control.reset_time()
        start = utime.ticks_ms()
        time = utime.ticks_ms()
        timeData = []
        data = []
        
        while True:
            # Step Response Test
            encoder2.update()
            pos = encoder2.read()
            if utime.ticks_ms() > (time + period):
                motor2.set_duty_cycle(control.update(pos))
                time += period
                timeData.append(time-start)
                data.append(pos)
                #print(time - start, pos)
                if time - start > 700:
                    motor2.set_duty_cycle(0)
                    break
        
        for x in range(0, len(timeData)):
            print(timeData[x], data[x])
    
# create try and except to handle Ctr-C 
except KeyboardInterrupt:
    motor2.set_duty_cycle(0)
    print("canceled")

