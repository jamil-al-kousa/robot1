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
    
    
    while touch_sensor.pressed()== False :
        turning_motor.run_angle(speed=300,rotation_angle=20, then=Stop.HOLD)
    

    wait(1000)

    claw_motor.run_until_stalled(215, then=Stop.HOLD, duty_limit=50)
    arm_motor.run_until_stalled(150, then=Stop.COAST, duty_limit=10)
    wait(2000)
    turning_motor.reset_angle(0)
    arm_motor.reset_angle(0)
    claw_motor.reset_angle(0)
    print(arm_motor.angle())
    return


#arm_motor.run_angle(speed=100,rotation_angle=-200, then=Stop.HOLD)

#the robot can turn max 600 and 300 is the medium when reboot function is used
#the max value that is good for using the arm is 400
# claw motor open and close fully if it is -80 degree
#If turning motor angle is plus the motor turn to left
#if arm angle is minus it goes up


def takethebox(position):
    
    #nextedtion 
    # next round in the loop it would be down with open claw and att a position of the item
    arm_motor.run_angle(speed=200,rotation_angle=-400)
    print(arm_motor.angle())
    claw_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=70)
    claw_motor.run_angle(100, -80 , then=Stop.HOLD)
    ######## the claw is open here
    turning_motor.run_angle(speed=200,rotation_angle=-position, then=Stop.HOLD)
    arm_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=10)
    print(arm_motor.angle())
    check_box()
    ### behövs inte
    #claw_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=70)
    ##
    wait(1000)
    
    return
    
     

def place_the_box(position):
    #arm_motor.run_angle(speed=100,rotation_angle=-215)
    turning_motor.run_angle(speed=200,rotation_angle=position, then=Stop.HOLD)
    #claw_motor.run_angle(80, -20 , then=Stop.HOLD)
    arm_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=10)
    
    #arm_motor.run_angle(speed=150,rotation_angle=-400)
    
    
    wait(1150)
    claw_motor.run_until_stalled(100, then=Stop.COAST, duty_limit=65)
    #turning_motor.run_angle(speed=100,rotation_angle=-80, then=Stop.HOLD)
    return

def where_to_place(PO_RED,PO_BLUE,PO_YELLOW,PO_GREEN):
    box_color=color_sensor.color()
    
    if box_color== Color.RED:
        place_the_box(PO_RED)
    elif box_color== Color.BLUE:
        place_the_box(PO_BLUE)
    elif box_color== Color.YELLOW:
        place_the_box(PO_YELLOW)
    elif box_color== Color.GREEN:
        place_the_box(PO_GREEN)
    # Oftast läsas gult som brun
    elif box_color== Color.BROWN:
        place_the_box(PO_YELLOW)
    # oftast läsas blå som svart
    elif box_color== Color.BLACK:
        place_the_box(PO_YELLOW)
    

    
    return

def check_box():
    claw_motor.reset_angle(0)
    clawAngle= claw_motor.angle()
    print(clawAngle)
    wait(1000)
   
    claw_motor.run_until_stalled(-200, then=Stop.HOLD, duty_limit=70) # Close the claw. Check what is the angle at the close position is? check also if there are something what is the angle.
    
    print(claw_motor.angle())
    if  -74 < claw_motor.angle() < 0 : # Check if the claw can close totaly.
        ##claw_motor.run_target(100,0)
        #arm_motor.run_angle(speed=100,rotation_angle=-175)
        print(" OBJECT detected")

    else  :
        print("There is no box")
        claw_motor.run_angle(100, 80 , then=Stop.HOLD)
        arm_motor.run_angle(speed=200,rotation_angle=-400)
        wait(10000)
        arm_motor.run_angle(speed=200,rotation_angle=400)
        check_box()



    
    return



#allt detta kommer sen att gå in i en loop for att roboten ska fungera under hela tiden

"""
#userstory5
reboot()

#claw_motor.run_angle(100, -80 , then=Stop.HOLD)

#take the box from this poistion
takethebox(615)
arm_motor.run_angle(speed=100,rotation_angle=-240)
wait(2000)
color_sensor.color()
print(color_sensor.rgb())
box_color=color_sensor.color()
print(box_color)
wait(8000)

#Place the box function when the attrbiute is 600 it means that it is going in the opposite direction
#place_the_box(300)

# THE poistions of the colors is red for first cell and then blue, yellow and green
where_to_place(450,450,300,150)
"""


#there are box at a location
"""
reboot()
takethebox(615)
check_box()

"""

def loop():
    reboot()
    #arm_motor.run_angle(speed=100,rotation_angle=-400)
    pickup=615
    count= 0
    while True:
       
        takethebox(pickup)

        
        
        arm_motor.run_angle(speed=100,rotation_angle=-240)
        wait(1000)
        color_sensor.color()
        print(color_sensor.rgb())
        box_color=color_sensor.color()
        print(box_color)
        wait(1000)
        PO_RED= 450
        PO_BLUE= 450
        PO_YELLOW= 300
        PO_GREEN= 150
        turning_motor.reset_angle(0)
        
        
        where_to_place(PO_RED,PO_BLUE,PO_YELLOW,PO_GREEN)
       
        grader =  turning_motor.angle()
        print(grader)
        pickup= (grader)
        
        
    return

    

loop()
#check_box()







