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
import EncoderDriver
import MotorDriver

# Instantiates two motor driver objects with appropriate pins and timer number
motor1 = MotorDriver.MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
motor2 = MotorDriver.MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)

# Instantiates two encoder driver objects with appropriate pins and timer number
encoder1 = EncoderDriver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.B6), pyb.Pin(pyb.Pin.cpu.B7), 4)
encoder2 = EncoderDriver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.C6), pyb.Pin(pyb.Pin.cpu.C7), 8)

# Instantiates controller object to calculate desired motor effort/duty cycle
control1 = ClosedLoop.ClosedLoop(100, math.pi*2)

motor1.enable()

# for data collection, set period between data calls
period = 10 #ms
data = []

try:
    while True:
        
        control1.change_kp(int(input("set Kp: ")))
        encoder1.zero()
        start = utime.ticks_ms()
        time = utime.ticks_ms()
        timeData = []
        data = []
        motor1.enable()
        
        while True:
            # Step Response Test
            encoder1.update()
            pos = encoder1.read()
            if utime.ticks_ms() > (time + period):
                motor1.set_duty_cycle(control1.update(pos))
                time += period
                timeData.append(time-start)
                data.append(pos)
                #print(time - start, pos)
                if time - start > 600:
                    motor1.disable()
                    break
        
        for x in range(0, len(timeData)):
            print(timeData[x], data[x])
    
# create try and except to handle Ctr-C 
except KeyboardInterrupt:
    motor1.disable()
    print("canceled")

