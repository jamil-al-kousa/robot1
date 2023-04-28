#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
turning_motor = Motor(Port.C)
arm_motor = Motor(Port.B)
Claw_motor = Motor(Port.A)
color_sensor = ColorSensor(Port.S2)
base_switch = TouchSensor(Port.S1) # inte säker om det är s1, fråga eller checka!

arm_motor.reset_ange(0)
arm_motor.run_target(150, 35) # upp till it gets recognized of the color sensor.


rgb = color_sensor.rgb()

def rgb_function():
    if (int(rgb[1] / int(rgb[0]))) < 0.5 and (int(rgb[2] / int(rgb[0]))) < 0.5:
        print("Color is red")

