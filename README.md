# PA1473 - Software Development: Agile Project (Template)



## Introduction

The primary function of this robot is to pick up items and place them in different locations and at varying heights. It possesses the capability to accommodate specific placement requests from the client. Regarding height adjustments, the robot can autonomously detect the surface area and place the box accordingly.

Furthermore, the robot is equipped with color recognition capabilities, enabling it to identify four distinct colors: blue, green, yellow, and red. 

It is important to note that the robot exclusively utilizes the MicroPython library alongside a few additional libraries to facilitate its operations.

## Getting started


To begin programming the robot, you will require Visual Studio Code and a robot equipped with a claw motor, turning motor, and arm motor. Additionally, the robot should be equipped with a color sensor and a touch sensor.

To facilitate coding, it is necessary to import specific libraries that enable the robot to interpret the code correctly. It is important to note that this robot employs MicroPython as its programming language.

To initiate coding, please copy and paste the provided code into your Visual Studio Code environment.

%%%%%
comment- !/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

This program requires LEGO EV3 MicroPython v2.0 or higher.
Click "Open user guide" on the EV3 extension tab for more information.

comment- Create your objects here.
ev3 = EV3Brick()

comment- Write your program here.
ev3.speaker.beep()

comment- Initialize a motor at port A.
claw_motor= Motor(Port.A)
arm_motor = Motor(Port.B)
turning_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S2)
touch_sensor = TouchSensor(Port.S1)
%%%%%%%

Every thing you need to code and to understand how things work is found in the link below

https://pybricks.com/ev3-micropython/     

Please note that certain libraries that are not part of MicroPython may not function properly in this project. Attempting to use such libraries could result in multiple errors. It is recommended to rely solely on MicroPython libraries, as they are sufficient to ensure the full functionality of this project.

The only step left is to connect your PC with the robot and you can push fn + F5 button to run the code.

comments#
Here are some useful inforamtion about the robot
the robot can turn max 600 from pickup postion
the max value that is good for using the arm is 400
claw motor open and close fully if it is -80 degree
If turning motor angle is plus the motor turn to left
if arm angle is minus it goes up




## Building and running



wait(arg1) # first argument
comment-first one red, Then blue, yellow, green
loop(arg2,arg3, arg4, arg5)

This code instructs the robot to perform a series of actions based on the provided inputs:

The first input sets the time at which the robot should start. A value of 10000 corresponds to 10 seconds, so if you enter 5000, the robot will wait for 5 seconds before starting.

The second input represents the position of the box with the red color. This box is placed at a 45-degree angle from the pickup position.

The third input represents the position of the box with the blue color. This box is placed at a 135-degree angle from the pickup position.

The fourth input represents the position of the box with the yellow color. This box is placed at a 90-degree angle from the pickup position.

The fifth input represents the position of the box with the green color. This box is placed at a 180-degree angle from the pickup position.

The valid range for box positions is between 0 and 600, with 0 being the pickup position.

wait(10000)
comment- first one red, Then blue, yellow, green
loop(150,450, 300, 600)

## Features

Lastly, you should write which of the user stories you did and didn't develop in this project, in the form of a checklist. Like this:

- [x] US_1: As a user I want to...
- [x] US_2: As a user I want to...
- [x] US_3: As a user I want to...
- [x] US_4: As a user I want to...
- [x] US_4B: As a user I want to...
- [x] US_5: As a user I want to...
- [x] US_6: As a user I want to...
- [x] US_8: As a user I want to...
- [x] US_9: As a user I want to...
- [x] US_10: As a user I want to...
- [ ] US_11: As a user I want to...
- [x] US_12: As a user I want to...
