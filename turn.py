import setup
import RoboPiLib as RPL
import time

x = 0
start = 3000
left = 600

# read whether the motor is at 3000 or 600
# make the motor turn to the other, based on
motor = RPL.servoRead(0)
if motor == start:
    RPL.servoWrite(0, left)
elif motor == left:
    RPL.servoWrite(0, start)
else:
    print "WRONG"
