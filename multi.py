import setup
import RoboPiLib as RPL
import time

x = 1
y = 2

print "h controls opening"
print "egg controls closing"
print "v controls up"
print "q controls down"
def op(h):
    L = float(h) - 0.5
    L >= 0
    L < 3 #placeholder maximum
    T = time.time() + L
    while time.time() < T:
        RPL.servoWrite(x, 2000)
        if time.time() >= T:
            RPL.servoWrite(x, 0)
def clo(egg):
    gug = float(egg) - 0.5
    gug < 5.6 #placeholder maximum
    gug >= 0
    greg = time.time() + gug
    while time.time() < greg:
        RPL.servoWrite(x, 1000)
        if time.time() >= greg:
            RPL.servoWrite(x, 0)
def up(v):
    P = float(v) - 0.5
    P >= 0
    P < 5.6 #placeholder maximum
    A = time.time() + P
    while time.time() < A:
        RPL.servoWrite(y, 2000)
        if time.time() >= A:
            RPL.servoWrite(y, 0)
def do(q):
    B = float(q) - 0.5
    B >= 0
    B < 5.6 #placeholder maximum
    C = time.time() + B
    while time.time() < C:
        RPL.servoWrite(y, 1000)
        if time.time() >= C:
            RPL.servoWrite(y, 0)

h = raw_input("h: ")
egg = raw_input("egg: ")
v = raw_input("v: ")
q = raw_input("q: ")
op(h)
clo(egg)
up(v)
do(q)
