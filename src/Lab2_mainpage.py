## @file mainpage.py
# @author Jonathan Cedarquist, Tim Jain, Philip Pang
# @mainpage Lab 2: Control Freaks
# @section intro_sec Introduction
# In the words of Master Yoda, "Control, control, you must learn control". 
# @image html yoda.JPG 
# Speaking of control, this lab assignment involved applying positional control
# to a DC motor. We used a closed loop Kp controller in order to adjust the 
# speed of the motor. Closed loop control is necessary to find an acceptable
# speed at which to run the motor at without causing overshoot and steady state
# error. A step response is a good indicator of these faults within a controller.
# Multiple step responses of the motor running at different Kp values will be shown
# within this lab assignment
# @image html block_diagram.JPG [2]
# @section ss_Kp Controlling Small DC Motors
# 

# @image html motor_control.JPG Figure 1: H-Bridge [1]

# @image html pins_motors.JPG Figure 2:Pin Diagram [1]

# @section ss_Flywheel Controlling a Motor attached to a Flywheel
# A flywheel adds additional inertia to the motor. This increases the amount of 
# effort that the motor must spin. 

# @image html enc_diag.JPG Figure 3: Encoder Timing Diagram [1]

# @image html charlie_encoder.JPG Figure 4:Charlie Refvem Encoder Delta Diagram [2]
# @section ss_main Main Script 

# @section ss_ref References
# [2] Ridgeley, John, ME 405 Lab #2 Control Freaks, W22Lab2.html, January 27, 2022
# \n
# [1] 
