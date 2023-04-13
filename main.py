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

# Write your program here.
ev3.speaker.beep()

# Initialize a motor at port A.
claw_motor= Motor(Port.A)

arm_motor = Motor(Port.B)
turning_motor = Motor(Port.C)
color_sensor = ColorSensor(Port.S2)
touch_sensor = TouchSensor(Port.S1)

def reboot():
    arm_motor.run_angle(speed=100,rotation_angle=-200, then=Stop.HOLD)
    while touch_sensor.pressed()== False :
        turning_motor.run_until_stalled(120, then=Stop.COAST, duty_limit=25)

    claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
    arm_motor.run_until_stalled(120, then=Stop.COAST, duty_limit=30)
    turning_motor.reset_angle(0)
    arm_motor.reset_angle(0)
    claw_motor.reset_angle(0)
    return



#the robot can turn max 600 and 300 is the medium when reboot function is used
#the max value that is good for using the arm is 400
# claw motor open and close fully if it is -80 degree
#If turning motor angle is plus the motor turn to left
#if arm angle is minus it goes up




def takethebox(position):
    wait(3000)
    arm_motor.run_angle(speed=100,rotation_angle=-175)
    claw_motor.run_angle(100, -80 , then=Stop.HOLD)
    turning_motor.run_angle(speed=100,rotation_angle=-position, then=Stop.HOLD)
    arm_motor.run_angle(speed=100,rotation_angle=175)
    claw_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=70)
    arm_motor.run_angle(speed=100,rotation_angle=-175)
    
  
    return

 

def place_the_box(position):
    turning_motor.run_angle(speed=150,rotation_angle=position, then=Stop.HOLD)
    arm_motor.run_angle(speed=100,rotation_angle=175)
    claw_motor.run_angle(80, -20 , then=Stop.HOLD)
    arm_motor.run_angle(speed=150,rotation_angle=-175)
    wait(2000)
    claw_motor.run_until_stalled(100, then=Stop.COAST, duty_limit=70)
    turning_motor.run_angle(speed=100,rotation_angle=-80, then=Stop.HOLD)
    return

def where_to_place():
    if box_color== Color.RED:
        place_the_box(600)
    elif box_color== Color.BLUE:
        place_the_box(300)
    return

reboot()
#take the box from this poistion
takethebox(600)
color_sensor.color()
print(color_sensor.rgb())
box_color=color_sensor.color()
print(box_color)

#Place the box function when the attrbiute is 600 it means that it is going in the oppiosite direction
place_the_box(600)

#where_to_place()











