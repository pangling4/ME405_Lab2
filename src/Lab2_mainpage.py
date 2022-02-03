## @file mainpage.py
# @author Jonathan Cedarquist, Tim Jain, Philip Pang
# @mainpage Lab 2: Control Freaks
# @section intro_sec Introduction
# In the words of Master Yoda, "Control, control, you must learn control". 
# @image html yoda.png Figure 1: The greatest Jedi who ever existed, Master Yoda [1]
# Speaking of control, this lab assignment involved applying positional control
# to a DC motor. We used a closed loop Kp controller in order to adjust the 
# position of the motor. Closed loop control is necessary to find an acceptable
# speed at which to run the motor at without causing overshoot and steady state
# error. A step response is a good indicator of these faults within a controller.
# Multiple step responses of the motor running at different Kp values are shown
# within this lab assignment. The Kp value is a gain. The actuation signal
# which controls the motor position is found by multiplying the Kp value
# by the setpoint position minus the measured position. This is shown in the block
# diagram in Figure 2. A larger Kp value amplifies the actuation signal,
# which means that the motor will reach the specified setpoint position at a faster
# rate. The setpoint is 2 times pi radians, which is a full revolution
# of the motor
# @image html block_diagram.JPG Figure 2: Positional Control Closed Loop Block Diagram [2]
# @section ss_serial Serial Interaction
# This lab involved serial interaction between the PC and the Nucleo. This was necessary
# in order to provide a user interface that would allow a user to input a Kp value on
# the PC front end that could be recognized on the Nucleo backend. The process behind 
# serial communication is as follows. 
# [1] The user runs main.py on the Nucleo, which has the utilization of the MotorDriver
# EncoderDriver, and Closed Loop Controller. The user is prompted in this script 
# to enter a Kp value. The program collects the time and data based based on the set 
# point. The time and data are printed. Print acts like a uart.write().
# \n
# [2] The StepResponse.py file is the User interface script that runs on the PC.
# This script asks for a Kp value input from the user and converts it to bytes. It then
# writes it over serial to the COM port. This Kp value is immediately read by serial.
# It also is being read on main.py through the input() command. It acts like a uart.read()
# \n
# [3] Thus, main.py is updated with the user inputted Kp from the front end and it collects
# data accordingly. This data is printed to the console 
# \n
# [4] This data is read over serial on the PC, and then used to plot the step response
# of position vs time.  
# @section ss_Kp Controlling Small DC Motors
# First, we used positional control to analyze the small DC motors that are given
# in the ME 405 kit. These plots are shown below. The Kp value of 25 in Figure 4 yields a step response
# with the position closest to setpoint (small steady state error) and unnoticeable overshoot.
# @image html kp_15.png Figure 3: Kp = 15
# @image html kp_25.png Figure 4: Kp = 25 (Best)
# @image html kp_50.png Figure 5: Kp = 50
# @image html kp_150.png Figure 6: Kp = 150
# @image html kp_200.png Figure 7: Kp = 200
# @section ss_Flywheel Controlling a Motor attached to a Flywheel
# A flywheel adds additional inertia to the motor. This increases the amount of 
# effort that the motor must spin. This flywheel is shown below in Figure 8.
# @image html flywheel.png Figure 8: Motor attached to flywheel
# The step response plots with this added inertia are shown below. 
# @image html Flywheel_Kp_10.png Figure 9: Kp = 10
# @image html Flywheel_Kp_20.png Figure 10: Kp = 20
# @image html Flywheel_Kp_50.png Figure 11: Kp = 50 (BEST)
# @image html Flywheel_Kp_200.png Figure 12: Kp = 200
# @section ss_ref References
# [1] Baver, Kristin. “8 Great Life Teachings from Yoda.” StarWars.com, 5 June 2017, https://www.starwars.com/news/8-great-life-teachings-from-yoda.
# \n 
# [2] Ridgeley, John, ME 405 Lab #2 Control Freaks, W22lab2.html, January 27, 2022
