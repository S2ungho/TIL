import time
from cs1robots import *
load_world("Python/HUBO/worlds/rain2.wld") #맵 크기 수정 rain2, 크기 22 -> 15
hubo = Robot(beepers = 7, avenue = 3, street = 6, orientation = 'E')
hubo.set_trace('blue')

def turn_right():
  for _ in range(3):
    hubo.turn_left()

def move_front():
    while hubo.front_is_clear():
      hubo.move()
      time.sleep(0.1)
      window()
    hubo.turn_left()
    window()

def window():
  if hubo.right_is_clear():
    turn_right()
    hubo.move()
    if hubo.left_is_clear() and hubo.right_is_clear(): 
      hubo.turn_left()
      hubo.turn_left()
      hubo.move()
      hubo.drop_beeper()
      turn_right()


turn_right()
while (1): #hubo.carries_beepers():
  move_front()