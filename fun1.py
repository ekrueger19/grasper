import setup
import RoboPiLib as RPL
import time

x = 1
y = 2
twist = 0

print "   What do you want to do? add a comma between each action."
print "   Actions include: up, down, close, op"

def act(w):
    egg = list(str(w))
    for up in egg:
        T = time.time() + 0.5
        while T > time.time():
            print "going up"
            RPL.servoWrite(y, 2000)
            if T <= time.time():
                RPL.servoWrite(y, 0)
    for down in egg:
        A = time.time() + 0.5
        while A > time.time():
            print "going down"
            RPL.servoWrite(y, 1000)
            if A <= time.time():
                RPL.servoWrite(y, 0)
    for close in egg:
        B = time.time() + 0.5
        while B > time.time():
            print "closing"
            RPL.servoWrite(x, 1000)
            if B <= time.time():
                RPL.servoWrite(x, 0)
    for op in egg:
        C = time.time() + 0.5
        while C > time.time():
            print "opening"
            RPL.servoWrite(x, 2000)
            if C <= time.time():
                RPL.servoWrite(x, 0)

w = raw_input("> ")
act(w)
