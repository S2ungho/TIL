from cs1robots import *
load_world("./worlds/trash2.wld")

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

def comeback_to_start(robot):
  robot.turn_left()
  robot.turn_left()
  move_straight(robot)

def throw_and_comeback(robot):
  turn_right(robot)
  robot.move()
  while robot.carries_beepers():
    robot.drop_beeper()
  robot.turn_left()
  robot.turn_left()
  robot.move()
  robot.turn_left()

def collect_and_throw_and_comeback(robot):
  move_pick(robot)
  comeback_to_start(robot)
  throw_and_comeback(robot)


collect_and_throw_and_comeback(hubo)
