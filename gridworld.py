from browser import window

size = 9
next_id = 0
class Actor:
  id = 0
  x = 0
  y = 0
  direction = 0
  img = ""
  def __init__(self, img):
    global next_id
    self.id = next_id
    next_id += 1
    self.img = img
    self.moveTo(0, 0)
    self.rotateTo(0)
  def updateHost(self):
    window.postMessage("gridworld__internal__command:update_actor:{\"id\": " + str(self.id) + ", \"img\": \"" + self.img + "\", \"x\": " + str(self.x) + ", \"y\": " + str(self.y) + ", \"direction\": " + str(self.direction) + "}")
  def rotateTo(self, direction):
    if direction < 0: direction += 8
    direction %= 8
    self.direction = direction
    self.updateHost()
  def moveTo(self, x, y):
    if x < 0 or y < 0 or x >= size or y >= size:
      print("Invalid move position (x = ", x, ", y = ", y, ")")
      return
    self.x = x
    self.y = y
    self.updateHost()
  def moveLinear(self, forward):
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
    self.moveTo(self.x + dir[0] * mult, self.y + dir[1] * mult)
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

bugInstance = Actor("bug")
bugInstance.moveTo(1, 5)
def getBug():
  return bugInstance

tickFn = None
def gridworld__internal__onMessage(e):
  global tickFn
  if e.data.startswith("gridworld__internal__tick"):
    if tickFn is not None:
      tickFn()
window.addEventListener("message", gridworld__internal__onMessage)

def onTick(fn):
  global tickFn
  tickFn = fn