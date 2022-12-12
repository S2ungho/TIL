from cs1robots import *
load_world("Python/HUBO/worlds/yardwork.wld")

hubo = Robot()
hubo.set_trace("blue")

def turn_right(robot):
  for _ in range(3):
    robot.turn_left()
  
def move_straight(robot):
  while robot.front_is_clear():
    robot.move()

def move_pick(robot):
  while robot.front_is_clear():
    if robot.on_beeper():
      robot.pick_beeper()
    else:
      robot.move()
  while robot.on_beeper():
      robot.pick_beeper()


def zig(robot):
  turn_right(robot)
  robot.move()
  turn_right(robot)
  move_pick(robot)

def zag(robot):
  robot.turn_left()
  robot.move()
  robot.turn_left()
  move_pick(robot)


def collect(robot):
  c=0
  move_pick(robot)
  robot.turn_left()
  robot.move()
  robot.turn_left()
  move_pick(robot)
  while (robot.left_is_clear() and robot.right_is_clear()):
    if c==0:
      zig(robot)
      c+=1
    else:
      zag(robot)
      c-=1
  return c

def comeback_to_starting(robot,c):
  if c==0:
    robot.turn_left()
    move_straight(robot)
    robot.turn_left()
  else:
    turn_right(robot)
    move_straight(robot)
    turn_right(robot)
    move_straight(robot)
    turn_right(robot)
    turn_right(robot)
  while robot.carries_beepers():
    robot.drop_beeper()

def trash2(robot):
  c=collect(robot)
  comeback_to_starting(robot,c)

trash2(hubo)
