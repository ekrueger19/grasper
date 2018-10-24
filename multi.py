import setup
import RoboPiLib as RPL
import time

x = 1
y = 2
twist = 0

print "h controls opening/closing"
print "v controls up"
print "q controls down"
print "motor controls twisting"
def op(h):
    L = 0.5 + h - 1
    L >= 0
    L < 5.6 #placeholder maximum
    T = time.time() + L
    while time.time() < T:
        RPL.servoWrite(x, 2000)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
def up(v):
    P = 0.5 + v - 1
    P >= 0
    P < 5.6 #placeholder maximum
    A = time.time() + P
    while time.time() < A:
        RPL.servoWrite(y, 2000)
        if time.time() >= A:
            RPL.servoWrite(y, 0)
def do(q):
    B = 0.5 + q - 1
    B >= 0
    B < 5.6 #placeholder maximum
    C = time.time() + B
    while time.time() < C:
        RPL.servoWrite(y, 1000)
        if time.time() >= C:
            RPL.servoWrite(y, 0)
def tw(motor):
    motor = servoRead(0)
    if motor == 3000:
        RPL.servoWrite(twist, 600)
    elif motor == 600:
        RPL.servoWrite(twist, 3000)

h = raw_input("h: ")
v = raw_input("v: ")
q = raw_input("q: ")
motor = raw_input("motor: ")
