import setup
import RoboPiLib as RPL
import time

w = raw_input("> ")
x = 2
y = 2000
z = 1000

print "Enter a to open little, b to close little, c to open lot, d to close lot"
if w == "a":
    T = time.time() + 1
    while time.time() < T:
        RPL.servoWrite(x, y)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
if w == "b":
    T = time.time() + 1
    while time.time() < T:
        RPL.servoWrite(x, z)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
if w == "c":
    T = time.time() + 2
    while time.time() < T:
        RPL.servoWrite(x, y)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
if w == "d":
    T = time.time() + 2
    while time.time*() < T:
        RPL.servoWrite(x, z)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
else:
    print "You done messed up"
