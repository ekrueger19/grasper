import setup
import RoboPiLib as RPL
import time

w = raw_input("> ")
x = 1
y = 2000
z = 1000

print "Enter a to open and b to close: "
if w == "a":
    T = time.time() + 2
    while time.time() < T:
        RPL.servoWrite(x, y)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
elif w == "b":
    T = time.time() + 2
    while time.time() < T:
        RPL.servoWrite(x, z)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
else:
    print "You done messed up"

#this should open and close the grasper based on input commands
#we should do it based on time, which means we need a max time so it won't break
