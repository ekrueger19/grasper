import setup
import RoboPiLib as RPL
import time
x = 1
y = 2000
z = 1000

print "Enter a to open and move up"
if raw_input("> ") == "a":
    T = time.time() + 2
    while time.time() < T:
        RPL.servoWrite(x, y)
        RPL.servoWite(2, y)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
            RPL.servoWrite(2, 0)
else:
    print "You done messed up"
