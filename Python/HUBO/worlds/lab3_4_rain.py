import time
from cs1robots import *
load_world("./worlds/rain2.wld")
hubo = Robot(beepers = 10,avenue=3,street=6,orientation="E")

def turn_right(robot):
  for i in range(3):
    robot.turn_left()

def mark_starting_point_and_move(robot):
  robot.drop_beeper()
  turn_right(robot)
  robot.move()
 
def check_wall(robot):
  turn_right(robot)
  robot.move()
  check=robot.right_is_clear()
  robot.turn_left()
  robot.turn_left()
  robot.move()
  turn_right(robot)
  return check

def follow_right_wall(robot):
  if robot.right_is_clear():
    check=check_wall(robot)
    if check:
      robot.drop_beeper()
      robot.move()
    else:
      turn_right(robot)
      robot.move()
  elif hubo.front_is_clear():
    hubo.move()
  else:
    hubo.turn_left()

mark_starting_point_and_move(hubo)
while not hubo.on_beeper():
  follow_right_wall(hubo)
  time.sleep(0.3)
hubo.pick_beeper()
hubo.turn_left()
 