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

"""def reboot():
    arm_motor.run_angle(speed=100,rotation_angle=-215, then=Stop.HOLD)
    while touch_sensor.pressed()== False :
        turning_motor.run_until_stalled(120, then=Stop.COAST, duty_limit=25)

    claw_motor.run_until_stalled(215, then=Stop.COAST, duty_limit=50)
    arm_motor.run_until_stalled(120, then=Stop.COAST, duty_limit=30)
    turning_motor.reset_angle(0)
    arm_motor.reset_angle(0)
    claw_motor.reset_angle(0)
    return
"""
def reboot():
    ##arm_motor.run_angle(speed=100,rotation_angle=-215, then=Stop.HOLD)
    #changed from coast to break
    while touch_sensor.pressed()== False :
        turning_motor.run_angle(speed=300,rotation_angle=20, then=Stop.HOLD)
    
    wait(1000)

    claw_motor.run_until_stalled(215, then=Stop.HOLD, duty_limit=50)
    #changed the arm power to  5 and it goes up instead of down
    arm_motor.run_until_stalled(-150, then=Stop.COAST, duty_limit=75)
    wait(4000)
    turning_motor.reset_angle(0)
    arm_motor.reset_angle(0)
    claw_motor.reset_angle(0)
    return


#arm_motor.run_angle(speed=100,rotation_angle=-200, then=Stop.HOLD)

#the robot can turn max 600 and 300 is the medium when reboot function is used
#the max value that is good for using the arm is 400
# claw motor open and close fully if it is -80 degree
#If turning motor angle is plus the motor turn to left
#if arm angle is minus it goes up




"""def takethebox(position):
    
    arm_motor.run_angle(speed=100,rotation_angle=-215)
    claw_motor.run_angle(100, -80 , then=Stop.HOLD)
    turning_motor.run_angle(speed=100,rotation_angle=-position, then=Stop.HOLD)
    arm_motor.run_angle(speed=100,rotation_angle=215)
    claw_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=70)
    arm_motor.run_angle(speed=100,rotation_angle=-215)
    

  
    return"""

def takethebox(position):
    #newedition
    arm_motor.run_angle(speed=100,rotation_angle=-400)
    print(arm_motor.angle())
    claw_motor.run_angle(100, -80 , then=Stop.HOLD)
    turning_motor.run_angle(speed=100,rotation_angle=-position, then=Stop.HOLD)

    arm_motor.run_until_stalled(100, then=Stop.COAST, duty_limit=10)
    print(arm_motor.angle())
    claw_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=70)
    wait(2000)
    #arm_motor.run_until_stalled(100, then=Stop.HOLD, duty_limit=10)
    
    





 

def place_the_box(position):
    #arm_motor.run_angle(speed=100,rotation_angle=-215)
    turning_motor.run_angle(speed=150,rotation_angle=position, then=Stop.HOLD)
    arm_motor.run_angle(speed=100,rotation_angle=215)
    claw_motor.run_angle(80, -20 , then=Stop.HOLD)
    arm_motor.run_angle(speed=150,rotation_angle=-215)
    wait(2150)
    claw_motor.run_until_stalled(100, then=Stop.COAST, duty_limit=65)
    #turning_motor.run_angle(speed=100,rotation_angle=-80, then=Stop.HOLD)
    return

def where_to_place(PO_RED,PO_BLUE,PO_YELLOW,PO_GREEN):
    
    if box_color== Color.RED:
        place_the_box(PO_RED)
    elif box_color== Color.BLUE:
        place_the_box(PO_BLUE)
    elif box_color== Color.YELLOW:
        place_the_box(PO_YELLOW)
    elif box_color== Color.GREEN:
        place_the_box(PO_GREEN)
    
    return

"""def check_arrived_boxess()
    take the box
    while there is box== False
    
        arms goes up 
        wait
        arms goes down
    the where to place depand on the color sensor
    #where_to_place(PO_RED,PO_BLUE,PO_YELLOW,PO_GREEN)

    return"""

"""def diffrent height placing():
     #one of them must be for the camerea and other 
     arm_motor.run_angle(speed=150,rotation_angle=-215) 
     arm_motor.run_angle(speed=150,rotation_angle=-215)
     arm_motor.run_angle(speed=150,rotation_angle=-215)
     arm_motor.run_angle(speed=150,rotation_angle=-215)
     it must know where it is so it can go back and go in the loop again."""


def check_box():
    
    print(claw_motor.angle())
    claw_motor.run_angle(100, -80 , then=Stop.HOLD)
    wait(1000)
    print(claw_motor.angle())
    claw_motor.run_until_stalled(-200, then=Stop.COAST, duty_limit=50) # Close the claw. Check what is the angle at the close position is? check also if there are something what is the angle.
    print(claw_motor.angle())
    if claw_motor.angle() < -170: # Check if the claw can close totaly.
        claw_motor.run_target(100,0)
        arm_motor.run_angle(speed=100,rotation_angle=-175)
        print("NO OBJECT detected")

    elif claw_motor.angle() >-170:
        print("There is a box")
    return


#allt detta kommer sen att gå in i en loop for att roboten ska fungera under hela tiden


"""#userstory5
reboot()

#claw_motor.run_angle(100, -80 , then=Stop.HOLD)

#take the box from this poistion
takethebox(615)
arm_motor.run_angle(speed=100,rotation_angle=-220)
wait(2000)
color_sensor.color()
print(color_sensor.rgb())
box_color=color_sensor.color()
print(box_color)
wait(8000)

#Place the box function when the attrbiute is 600 it means that it is going in the opposite direction
#place_the_box(300)

# THE poistions of the colors is red for first cell and then blue, yellow and green
where_to_place(450,450,300,150)"""



#there are box at a location

reboot()
takethebox(615)
check_box()













