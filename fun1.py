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
    for up1 in egg:
        D = time.time() + 0.5
        while D > time.time():
            print "going up"
            RPL.servoWrite(y, 2000)
            if D <= time.time():
                RPL.servoWrite(y, 0)
    for down1 in egg:
        E = time.time() + 0.5
        while E > time.time():
            print "going down"
            RPL.servoWrite(y, 1000)
            if D <= time.time():
                RPL.servoWrite(y, 0)
    for close1 in egg:
        F = time.time() + 0.5
        while F > time.time():
            print "closing"
            RPL.servoWrite(x, 1000)
            if F <= time.time():
                RPL.servoWrite(x, 0)
    for op1 in egg:
        G = time.time() + 0.5
        while G > time.time():
            print "opening"
            RPL.servoWrite(x, 2000)
            if G <= time.time():
                RPL.servoWrite(x, 0)
    for up2 in egg:
        H = time.time() + 0.5
        while H > time.time():
            print "going up"
            RPL.servoWrite(y, 2000)
            if H <= time.time():
                RPL.servoWrite(y, 0)
    for down2 in egg:
        I = time.time() + 0.5
        while I > time.time():
            print "going down"
            RPL.servoWrite(y, 1000)
            if I <= time.time():
                RPL.servoWrite(y, 0)
    for close2 in egg:
        J = time.time() + 0.5
        while J > time.time():
            print "closing"
            RPL.servoWrite(x, 1000)
            if J <= time.time():
                RPL.servoWrite(x, 0)
    for op2 in egg:
        K = time.time() + 0.5
        while K > time.time():
            print "opening"
            RPL.servoWrite(x, 2000)
            if K <= time.time():
                RPL.servoWrite(x, 0)

w = raw_input("> ")
act(w)
