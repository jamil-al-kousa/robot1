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





arm_motor.run_time(-30, 1000) # go ner för en secund med hastigheten -30 vikel
Claw_motor
arm_motor.run(15) # go upp med hastigheten 15 vikel upp per secund



time1 = -30
turning_motor.run(time1)
while true:
    if base_switch.pressed():
        wait(1000)
        turning_motor.reset_angel(0) # Jag är inte säker om det här steget behövs, testa det!
        time1 = -time1
        turning_motor.run(time1)

    elif turning_motor.angle() == 0:
