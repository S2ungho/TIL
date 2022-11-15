import time
from cs1robots import *
create_world()
hubo = Robot(orientation='E', avenue=5, street=9) 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

def see():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()

def last_move():
    while hubo.front_is_clear():
        hubo.move()

def start_position():
    for i in range(2):
        last_move()
        hubo.turn_left()

see()
start_position()
