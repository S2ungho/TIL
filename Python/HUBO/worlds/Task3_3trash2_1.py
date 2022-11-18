import time
from cs1robots import *
#create_world(streets=10, avenues=10)
load_world("Python/HUBO/worlds/yardwork.wld")
hubo = Robot() 
hubo.set_trace('blue')

def turn_right():
  for _ in range(3):
    hubo.turn_left()
  
def move_straight():
  while hubo.front_is_clear():
    move_and_pick()

def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def zig():
  move_and_pick()
  turn_right()
  move_straight()
  hubo.turn_left()

def zag():
  move_and_pick()
  hubo.turn_left()
  move_straight()
  turn_right()

def see():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()

def start_position():
    for i in range(2):
        move_straight()
        hubo.turn_left()

c=0
#hubo.turn_left()
move_straight()
#turn_right()
hubo.turn_left()
while hubo.front_is_clear():
  if c==0:
    zag()
    c+=1
  elif c==1:
    zig()
    c-=1
  else:
    print('error')
see()
start_position()