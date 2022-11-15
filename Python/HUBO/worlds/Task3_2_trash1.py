import time
from cs1robots import *
#create_world()
load_world("Python/HUBO/worlds/trash1.wld")
hubo = Robot() 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_and_pick():
    global cnt
    hubo.move()
    while hubo.on_beeper():
    #if hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1

def last_move():
    global cnt
    while hubo.front_is_clear():
        move_and_pick()

def wall():
    while hubo.carries_beepers():
        if not hubo.front_is_clear() and not hubo.left_is_clear() and not hubo.right_is_clear():
            hubo.turn_left()
            hubo.turn_left()
            last_move()
        else:
            turn_right()
            hubo.move()
            while hubo.carries_beepers():
                hubo.drop_beeper()
            hubo.turn_left()
            hubo.turn_left()
            hubo.move()


cnt = 0
last_move()
print(cnt)
wall()