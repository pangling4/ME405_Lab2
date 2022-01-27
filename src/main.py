import pyb
import utime
import math
#import serial
import ClosedLoop
import EncoderDriver
import MotorDriver

# Instantiates two motor driver objects with appropriate pins and timer number
motor1 = MotorDriver.MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
motor2 = MotorDriver.MotorDriver(pyb.Pin.board.PC1, pyb.Pin.board.PA0, pyb.Pin.board.PA1, 5)

encoder1 = EncoderDriver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.B6), pyb.Pin(pyb.Pin.cpu.B7), 4)
encoder2 = EncoderDriver.EncoderDriver(pyb.Pin(pyb.Pin.cpu.C6), pyb.Pin(pyb.Pin.cpu.C7), 8)

control1 = ClosedLoop.ClosedLoop(100, math.pi*2)

motor1.enable()

period = 10 #ms
data = []


try:
    while True:
        
        control1.change_kp(int(input("set Kp: ")))
        encoder1.zero()
        start = utime.ticks_ms()
        time = utime.ticks_ms()
        data = []
        motor1.enable()
        
        while True:
            # Step Response Test
            encoder1.update()
            pos = encoder1.read()
            if utime.ticks_ms() > (time + period):
                motor1.set_duty_cycle(control1.update(pos))
                time += period
                data.append((time - start, pos))
                if time - start > 400:
                    motor1.disable()
                    break
        for x in data:
            print(x[0], ",", x[1])
    
except KeyboardInterrupt:
    motor1.disable()
    print("canceled")

