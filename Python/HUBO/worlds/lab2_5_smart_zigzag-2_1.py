from cs1robots import *
m=int(input("Number of streets-->"))
n=int(input("Number of streets-->"))
create_world(streets=m, avenues=n)

hubo = Robot()

hubo.set_trace("blue")

def turn_right():
  for _ in range(3):
    hubo.turn_left()
  
def move_straight():
  while hubo.front_is_clear():
    hubo.move()

def zig():
  hubo.move()
  turn_right()
  move_straight()
  hubo.turn_left()

def zag():
  hubo.move()
  hubo.turn_left()
  move_straight()
  turn_right()

c=0
hubo.turn_left()
move_straight()
turn_right()

while hubo.front_is_clear():
  if c==0:
    zig()
    c+=1
  elif c==1:
    zag()
    c-=1
  else:
    print('error')