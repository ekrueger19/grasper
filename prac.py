import time
#this is a test of whether multi would work
print "h controls opening"
print "v controls up"
print "q controls down"
print "motor controls twisting"
def op(h):
    L = 0.5 + h - 1
    L >= 0
    L < 5.6 #placeholder maximum
    T = time.time() + L
    while time.time() < T:
        print "opening"
        if time.time() >= T:
            print "stopping"
def up(v):
    P = 0.5 + v - 1
    P < 5.6 #placeholder maximum
    P >= 0
    A = time.time() + P
    while time.time() < A:
        print "going up"
        if time.time() >= A:
            print "stopping"
def do(q):
    B = 0.5 + q - 1
    B < 5.6 #placeholder maximum
    B >= 0
    C = time.time() + B
    while time.time() < C:
        print "going down"
        if time.time() >= C:
            print "stopping"
def tw(motor):
    if motor == 3000:
        print "turn left"
    elif motor == 600:
        print "turn right"
    else:
        print "oops"

h = raw_input("h: ")
v = raw_input("v: ")
q = raw_input("q: ")
motor = raw_input("motor: ")
