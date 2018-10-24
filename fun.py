import time
#this code should take a string and make it an action
#PROBLEMS: doesn't do the things in order of the string or more than once

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
