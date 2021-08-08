import gridworld

# Create a bug at the coordinates (3, 5).
# Coordinates are from the top left of the grid.
bug = gridworld.createBug(3, 5)

# Give the bug a recognizable color.
bug.setColor("red")

def tick():
    bug.moveForward() # Move forward one tile.
    bug.turnRight() # Turn clockwise 45 degrees.

gridworld.onTick(tick) # Register our tick function to be called repeatedly.
