import setup
import RoboPiLib as RPL
import time

x = 1
y = 2
twist = 0

print "   What do you want to do? add a comma between each action."
print "   Actions include: up, down, close, op"
print "   If you want it to do something after, add a number (starting at 1) at"
print "the end of the word (for instance, up, op, close1, down2)"
def act(w):
    egg = list(str(w))
    for up in egg:
        T = time.time() + 1
        while T > time.time():
            RPL.servoWrite(y, 2000)
            if T =< time.time():
                RPL.servoWrite(y, 0)
    for down in egg:
        A = time.time() + 1
        while A > time.time():
            RPL.servoWrite(y, 1000)
            if A =< time.time():
                RPL.servoWrite(y, 0)
    for close in egg:
        print "closing"
    for op in egg:
        print "opening"
    for up1 in egg:
        print "going up"
    for down1 in egg:
        print "going down"
    for close1 in egg:
        print "closing"
    for op1 in egg:
        print "opening"
    for up2 in egg:
        print "uping"
    for down2 in egg:
        print "downing"
    for close2 in egg:
        print "closing"
    for op2 in egg:
        print "opening"

w = raw_input("> ")
act(w)
