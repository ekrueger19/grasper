import setup
import RoboPiLib as RPL
import time

x = 1
y = 2
twist = 0

print "What do you want to do? add a comma between each action."
print "Actions include: up, down, close, op, left-twist, right-twist"
def act(w):
    egg = list(str(w))
    for up in egg:
        print "going up"
    for down in egg:
        print "going down"
    for close in egg:
        print "closing"
    for op in egg:
        print "opening"

w = raw_input("> ")
act(w)
