import setup
import RoboPiLib as RPL
import time

x = #PIN number of motor
y = #motor forwards
z = #motor backwards

print "Enter a to open and b to close: "
if raw_input("> ") == "a":
    T = time.time() + 1
    while time.time() < T:
        RPL.servoWrite(x, y)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
elif raw_input("> ") == "b":
    T = time.time() + 1
    while time.time() < T:
        RPL.servoWrite(x, z)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
else:
    print "You done messed up"

#this should open and close the grasper based on input commands
#we should do it based on time, which means we need a max time so it won't break