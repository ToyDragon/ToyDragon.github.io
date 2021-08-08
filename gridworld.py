from browser import window
from browser import timer

grid_width = 9
grid_height = 9
next_id = 0
class Actor:
  id = 0
  x = 0
  y = 0
  direction = 0
  img = ""
  color = ""
  def __init__(self, img):
    global next_id
    self.id = next_id
    next_id += 1
    self.img = img
    self.moveTo(0, 0)
    self.rotateTo(0)
  def updateHost(self):
    window.postMessage("gridworld__internal__command:update_actor:{\"id\": " + str(self.id) + ", \"img\": \"" + self.img + "\", \"color\": \"" + self.color + "\", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + ", \"direction\": " + str(self.direction) + "}")
  def rotateTo(self, direction):
    if direction < 0: direction += 8
    direction %= 8
    self.direction = direction
    self.updateHost()
  def moveTo(self, x, y):
    global grid_width, grid_height
    if x < 0 or y < 0 or x >= grid_width or y >= grid_height:
      print("Invalid move position (x = ", x, ", y = ", y, ")")
      return
    self.x = x
    self.y = y
    self.updateHost()
  def setColor(self, color):
    self.color = color
    self.updateHost()
  def getLinearOffest(self, forward):
    dir = [
      [0, -1],
      [1, -1],
      [1, 0],
      [1, 1],
      [0, 1],
      [-1, 1],
      [-1, 0],
      [-1, -1],
    ][self.direction]
    mult = 1
    if not forward: mult = -1
    return (self.x + dir[0] * mult, self.y + dir[1] * mult)
  def moveLinear(self, forward):
    new_pos = self.getLinearOffest(forward)
    self.moveTo(new_pos[0], new_pos[1])
  def moveForward(self):
    self.moveLinear(True)
  def moveBackward(self):
    self.moveLinear(False)
  def rotate(self, right):
    amount = 1
    if not right: amount = -1
    self.rotateTo(self.direction + amount)
  def turnLeft(self):
    self.rotate(False)
  def turnRight(self):
    self.rotate(True)
  def canMoveForward(self):
    global grid_width, grid_height
    new_pos = self.getLinearOffest(True)
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= grid_width or new_pos[1] >= grid_height:
      return False
    return True
  def poop(self):
    flowerInstance = Actor("flower")
    flowerInstance.moveTo(self.x, self.y)
    flowerInstance.setColor(self.color)

def createBug(x, y):
  bugInstance = Actor("bug")
  bugInstance.moveTo(x, y)
  return bugInstance

tickFns = []
def gridworld__internal__onMessage(e):
  global tickFns, grid_width, grid_height
  if e.data.startswith("gridworld__internal__tick"):
    for fn in tickFns:
      fn()
  if e.data.startswith("gridworld__internal__setsize"):
    grid_width = int(e.data.split(":")[1])
    grid_height = int(e.data.split(":")[2])

initialized = False
def init():
  global initialized
  if not initialized:
    initialized = True
    # Let the container know we are initialized.
    window.postMessage("gridworld__internal__ready")
    window.addEventListener("message", gridworld__internal__onMessage)

def onTick(fn):
  global tickFns
  tickFns.append(fn)