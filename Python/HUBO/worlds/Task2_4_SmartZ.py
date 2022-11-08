import time
from cs1robots import *
create_world()
hubo = Robot() 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

n = 10
m = 7
x = 0
y = 0
swi = 0
hubo.turn_left()
while x < n:
    while y < m:
        hubo.move()
        y+=1
    if swi == 0:
        turn_right()
        hubo.move()
        turn_right()
        swi = 1
    else: 
        hubo.turn_left()
        hubo.move()
        hubo.turn_left()
        swi = 0
    x+=1