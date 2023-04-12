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


#turning_motor.run_until_stalled(speed, then=Stop.COAST, duty_limit=None) Det här kan funka kanske också

def settings():
    if base_switch.pressed():
        turning_motor.reset_angel(0)
        turning_motor.hold() # Hold it so it does not move a bit.
        arm_motor.run_until_stalled(-25, then=Stop.COAST, duty_limit=None)
        arm_motor.reset_angel(0)
        claw_motor.run_until_stalled(150, then=Stop.COAST, duty_limit=50) # make the claw_motor work until stalled to the closed position.
        claw_motor.reset_angel(0) # Make the angel zero there.
        claw_motor.run_target(200, -120) # Open the claw by 120 degree
        ev3.speaker.beep() # A signal that the settings are done.

    
def grab_thing(posit, posit2):
    turning_motor.run_target(60, position)
    arm_motor.run_target(30, 40) # man ska lägga en vikel som passar så att det passar settings i början.
    claw_motor.run_until_stalled(150, then=Stop.COAST, duty_limit=50)
    arm_motor.run_target(50,0) 
    if color_sensor.color() == "Black":


    #ev3.speaker.beep() # A signal that the first step half steps of grab_thing are done.




    
#def start():
for x in range(5):
    turning_motor.run(20)
settings()


#start()
