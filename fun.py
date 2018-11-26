import time
#this code should take a string and make it an action
#PROBLEMS: doesn't do the things in order of the string or more than once

x = 1
y = 2
twist = 0

print "What do you want to do? add a space between each action."
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

# The reason up1, down1, etc. didn't work was because it sees if the letters -
# up are in a word and if it is then it does the action once
# It doesn't matter how many ups, it only measures if there is one
