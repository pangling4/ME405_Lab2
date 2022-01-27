''' @file       ClosedLoop.py
    @brief      Implements closed loop proportional controller for position
    @details    Class of closed loop controller that can be used to control PITTMAN motors given in ME 405 lab
                with NUCLEO L476RG microcontroller
                
    @author     Jonathan Cederquist
    @author     Tim Jain
    @author     Philip Pang
    @date       Last Modified 1/27/22
'''

import pyb
import utime

class ClosedLoop:
    '''!
    @brief This class implements a closed loop controller
    '''
    
    def __init__ (self, kp, setpoint):
        '''! 
        @brief          Creates an encoder driver object
        @details        Creates an encoder driver by initializing timers and channels with 
                        given pins and timer number
        @param in1pin   A pyb.Pin object corresponding to the encoder channel A 
        @param in2pin   A pyb.Pin object corresponding to the encoder channel B
        @param timer    The timer number corresponding to the encoder pins
        '''
        self.kp = kp
        self.setpoint = setpoint
        
    def update(self, measured):
        error = self.setpoint - measured
        return self.kp*error
        
    def change_setpoint(self, setpoint):
        self.setpoint = setpoint
        
    def change_kp(self, kp):
        self.kp = kp