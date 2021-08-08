import gridworld

# A global message var that is modified by both bugs.
message = ""

#################################################
# Fizz Bug. Poops every multiple of 3.
#################################################
fizzBug = gridworld.createBug(0, 0)
fizzBug.setColor("red")

# Bugs spawn facing north, turn this one to start facing east.
fizzBug.turnRight()
fizzBug.turnRight()

tickCount = 1
def tickFizz():
    global message, tickCount
    if fizzBug.canMoveForward():
        if tickCount % 3 == 0:
            fizzBug.poop()
            message += "Fizz"
        fizzBug.moveForward()
gridworld.onTick(tickFizz)

#################################################
# Buzz Bug. Poops ever multiple of 5.
#################################################
buzzBug = gridworld.createBug(0, 1)
buzzBug.setColor("blue")

# Bugs spawn facing north, turn this one to start facing east.
buzzBug.turnRight()
buzzBug.turnRight()

def tickBuzz():
    global message, tickCount
    if buzzBug.canMoveForward():
        if tickCount % 5 == 0:
            buzzBug.poop()
            message += "Buzz"
        buzzBug.moveForward()
gridworld.onTick(tickBuzz)

# After the bugs are done moving, output their combined message.
def tickPrinter():
    global message, tickCount
    if fizzBug.canMoveForward() or buzzBug.canMoveForward():
        if not message:
            message += str(tickCount)
        tickCount += 1
        print(message)
        message = ""
gridworld.onTick(tickPrinter)