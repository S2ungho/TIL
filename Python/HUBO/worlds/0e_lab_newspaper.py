from cs1robots import*
import time
load_world("Python/HUBO/worlds/newspaper.wld")

hubo = Robot(beepers = 1)

def turn_right():
  for _ in range(3):
    hubo.turn_left()
  
def turn_around():
  for _ in range(2):
    hubo.turn_left()
  
def climb_up_four_stairs():
  for _ in range(4):
    climb_up_one_stair()
    time.sleep(0.5)   

def climb_down_four_stairs():
  for _ in range(4):
    climb_down_one_stair()
    time.sleep(0.5)   
  
def climb_up_one_stair():
  hubo.turn_left()
  time.sleep(0.5)
  hubo.move()
  time.sleep(0.5)
  turn_right()
  time.sleep(0.5)
  hubo.move()
  time.sleep(0.5)
  hubo.move()

def climb_down_one_stair():
  hubo.move()
  hubo.move()
  hubo.turn_left()
  hubo.move()
  turn_right()

time.sleep(2)
climb_up_four_stairs()
hubo.move()
hubo.drop_beeper()
turn_around()
hubo.move()
climb_down_four_stairs()