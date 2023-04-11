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

#rotation to the right side if angle is plus

#turning_motor.run_angle(speed=100,rotation_angle=80, then=Stop.HOLD)



#if angle minus it goes up
#arm_motor.run_angle(speed=100,rotation_angle=-100, then=Stop.HOLD)

#claw_motor.run_angle(speed=100,rotation_angle=100, then=Stop.HOLD)
#arm_motor.run_angle(speed=100,rotation_angle=-100, then=Stop.HOLD)
#turning_motor.run_angle(speed=100,rotation_angle=-80, then=Stop.HOLD)
#arm_motor.run_angle(speed=100,rotation_angle=100, then=Stop.HOLD)

#if claw is negativ is  opene
#claw_motor.run_angle(speed=100,rotation_angle=-100, then=Stop.HOLD)
#print(color_sensor.color(red))
#claw_motor.run_angle(speed=150,rotation_angle=150, then=Stop.HOLD)
#turning_motor.reset_angle(180)
#recognice the color of the sensor
print(color_sensor.color())
print(touch_sensor.pressed())
