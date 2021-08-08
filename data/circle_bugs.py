import gridworld

#################################################
# Stupid Red Bug
#################################################
bugA = gridworld.createBug(7, 3)
bugA.setColor("red")

# Bugs spawn facing north, turn this one to start facing south.
bugA.turnRight()
bugA.turnRight()
bugA.turnRight()
bugA.turnRight()

bugATickCount = 0
def tickBugA():
    global bugATickCount
    state = (bugATickCount % 24)
    if state == 0: bugA.moveForward()
    if state == 1: bugA.moveForward()
    if state == 2: bugA.turnRight()
    if state == 3: bugA.moveForward()
    if state == 4: bugA.moveForward()
    if state == 5: bugA.turnRight()
    if state == 6: bugA.moveForward()
    if state == 7: bugA.moveForward()
    if state == 8: bugA.turnRight()
    if state == 9: bugA.moveForward()
    if state == 10: bugA.moveForward()
    if state == 11: bugA.turnRight()
    if state == 12: bugA.moveForward()
    if state == 13: bugA.moveForward()
    if state == 14: bugA.turnRight()
    if state == 15: bugA.moveForward()
    if state == 16: bugA.moveForward()
    if state == 17: bugA.turnRight()
    if state == 18: bugA.moveForward()
    if state == 19: bugA.moveForward()
    if state == 20: bugA.turnRight()
    if state == 21: bugA.moveForward()
    if state == 22: bugA.moveForward()
    if state == 23: bugA.turnRight()
    bugATickCount += 1
gridworld.onTick(tickBugA)

#################################################
# Intelligent Blue Bug
#################################################
bugBTickCount = 0
bugB = gridworld.createBug(1, 5)
bugB.setColor("blue")
def tickBugB():
    global bugBTickCount
    # Every third tick, turn the bug clockwise.
    if bugBTickCount % 3 == 2:
        bugB.turnRight()
    # For the other two ticks, move the bug forward.
    else:
        bugB.moveForward()
    bugBTickCount += 1  
gridworld.onTick(tickBugB)
