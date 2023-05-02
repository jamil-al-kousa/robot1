#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
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
base_switch = TouchSensor(Port.S1)



def rgb_function():
    rgb = color_sensor.rgb()
    begin = False
    Done = False
    # (rgb[0] < 85) and
    print(rgb)

    if rgb[0] == 0 or rgb[1] == 0 or rgb[2] == 0:
        try:
                
            print("move the box, pls!")
            begin = True
            wait(8000)

            rgb_function()
        except:
            print(".--..")
        #break()

    if begin == False and (((((int(rgb[2])) / int(rgb[1]))) <= 0.6) or (int(rgb[2]) / int(rgb[0])) <= 0.6): # check if it is yellow
        if int(rgb[0]) < int(rgb[1]): 
            if (int(rgb[2] / int(rgb[1]))) <= 0.6 and ((int(rgb[0])) / int(rgb[1]) >=0.8):
                if (int(rgb[2] / int(rgb[0]))) <= 0.8:
                    print("Color is yellow")
                    Done = True

            elif (int(rgb[2] / int(rgb[0]))) <= 0.6 and ((int(rgb[0])) / int(rgb[1]) >=0.8):
                if (int(rgb[2] / int(rgb[1]))) <= 0.8:
                    print("Color is yellow")
                    Done = True
        elif int(rgb[0]) > int(rgb[1]):
            if (int(rgb[2] / int(rgb[1]))) <= 0.6 and ((int(rgb[1])) / int(rgb[0]) >=0.52):
                if (int(rgb[2] / int(rgb[0]))) <= 0.8:
                    print("Color is yellow")
                    Done = True

            elif (int(rgb[2] / int(rgb[0]))) <= 0.6 and ((int(rgb[1])) / int(rgb[0]) >=0.52):
                if (int(rgb[2] / int(rgb[1]))) <= 0.8:
                    print("Color is yellow")
                    Done = True
        else: # do it again in case it did not get any color
            try:
                rgb_function()
            except: 
                print("...")

    if Done == False and begin == False: # If it is not read so check the rest of the colors
        if (int(rgb[1] / int(rgb[0]))) < 0.5 and (int(rgb[2] / int(rgb[0]))) < 0.5:
            print("Color is red")

        elif (int(rgb[0] / int(rgb[1]))) < 0.5 and (int(rgb[2] / int(rgb[1]))) < 0.5:
            print("Color is green")

        elif (int(rgb[0] / int(rgb[2]))) < 0.5 and (int(rgb[1] / int(rgb[2]))) < 0.5:
                print("Color is blue")
        else: # if it got no color so do it again
            try:
                print("Movie the box, pls")
                wait(5000)
                rgb_function()
                print("f")
            except:
                print("...")


rgb_function()