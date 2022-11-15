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
    Robot.move()
    while hubo.on_beeper():
    #if hubo.on_beeper():
        Robot.pick_beeper()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def find_height():
    while hubo.front_is_clear():
        hubo.move()
        cnt += 1


def Height():
    global m, swi, n
    for i in range(m):
        hubo.move()
        if not hubo.front_is_clear():
            if n % 2 == 0:
                turn_right()
                hubo.move()
                turn_right()
                n -= 1
            else:
                hubo.turn_left()
                hubo.move()
                hubo.turn_left()
                n -= 1

cnt = 0

m = 9
n = 10
hubo.turn_left()
for i in range(n):
    Height()