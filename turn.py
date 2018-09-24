import setup
import RoboPiLib as RPL
import time

x = 0
start = 600
end = 3000

RPL.servoWrite(0, start)
print "press a to turn right and b to turn left"
while raw_input("> ") == "a":
    RPL.servoWrite(0, end)
    if raw_input("> ") != "a":
        RPL.servoWrite(0, start)
