import time
from cs1robots import *
create_world()
hubo = Robot() 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_last():
    for i in range(9):
        hubo.move() 

def one_step():
    hubo.turn_left() 
    move_last()
    turn_right() 
    hubo.move() 
    turn_right() 
    move_last()
    hubo.turn_left()
    hubo.move()

for i in range(5):
    one_step()