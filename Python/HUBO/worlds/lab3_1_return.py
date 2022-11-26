from cs1robots import *
create_world(avenues=10, streets=7)

hubo = Robot(orientation ='W', avenue = 7, street = 5)
hubo.set_trace("blue")

def see_west(robot):
  while not robot.facing_north():
    robot.turn_left()
  robot.turn_left()

def move_straight(robot):
  while robot.front_is_clear():
    robot.move()

def comeback_to_starting(robot):
  see_west(robot)
  move_straight(robot)
  robot.turn_left()
  move_straight(robot)
  robot.turn_left()

comeback_to_starting(hubo)