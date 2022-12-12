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
  hubo.turn_left()
  hubo.move()
  hubo.turn_left()
  move_straight()
  
def zag():
  turn_right()
  hubo.move()
  turn_right()
  move_straight()

c=0
hubo.turn_left()
move_straight()
turn_right()
hubo.move()
turn_right()
move_straight()
while (hubo.left_is_clear() and hubo.right_is_clear()):
  if c==0:
    zig()
    c+=1
  else:
    zag()
    c-=1
    