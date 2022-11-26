from cs1robots import *

load_world("Python/HUBO/worlds/harvest2.wld")
count=0

def turn_right(robot):
  for i in range(3):
    robot.turn_left()


def goto_start(robot):
  global count
  for i in range(5):
    robot.move()
  robot.turn_left()
  robot.move()
  count+=6

def stairs(robot, n):
  global count
  for i in range(n):
    robot.pick_beeper()
    robot.move()
    count+=1
    turn_right(robot)
    robot.move()
    count+=1
    robot.turn_left()

def diamond(robot, n):
  global count
  for i in range(3):
    stairs(robot, n)
    robot.turn_left()
  stairs(robot, n-1)
  robot.pick_beeper()
  robot.turn_left()
  robot.move()
  count+=1
  turn_right(robot)
  robot.move()
  count+=1
  robot.turn_left()

def diamond_rev(robot, n):
  for i in range(3):
    stairs(robot, n)
    robot.turn_left()
  robot.pick_beeper()
  
def harvest_all(robot):
  for i in range(2):
    n = 5 - 2 * i
    diamond(robot, n)
  n = 5 - 2 * 2
  diamond_rev(robot, n)
#def happy_dance(robot):
#  for i in range(102):
#    robot.turn_left()

hubo = Robot()
hubo.set_trace("blue")
hubo.set_pause(0.1)

goto_start(hubo)
harvest_all(hubo)
#happy_dance(hubo)
print(count)
