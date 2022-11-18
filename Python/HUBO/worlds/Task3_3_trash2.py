import time
from cs1robots import *
#create_world()
load_world("Python/HUBO/worlds/yardwork.wld")
hubo = Robot() 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        Robot.turn_left()

def move_and_pick():
    hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def last_move():
    while hubo.front_is_clear():
        move_and_pick()


def find_height():
    while hubo.front_is_clear():
        move_and_pick()
        cnt += 1


def Height():
    global m, swi, n
    last_move()
    turn_right()
    hubo.move()
    turn_right()
    last_move()
    for i in range(m-1):
        if not hubo.front_is_clear():
            if n % 2 == 1:
                hubo.turn_left()
                move_and_pick()
                hubo.turn_left()
                n -= 1
            else:
                turn_right()
                move_and_pick()
                turn_right()
                n -= 1
            move_and_pick()

def see():
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()

def start_position():
    for i in range(2):
        last_move()
        hubo.turn_left()

def first_move():
    global swi
    last_move()
    if not hubo.right_is_clear():
        hubo.turn_left()
        move_and_pick()
        hubo.turn_left()
        swi = 0
        last_move()
        turn_right()
    else:
        turn_right()
        move_and_pick()
        turn_right()
        swi = 1
        last_move()
        hubo.turn_left()

def zigzag():
    global swi
    if swi == 0:
        move_and_pick()
        turn_right()
        swi = 1
    else:
        move_and_pick()
        hubo.turn_left()
        swi = 0
    last_move()


first_move()
for i in range(8):
    zigzag()
#if hubo.front_is_clear():
#    move_and_pick()
