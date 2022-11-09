import time
from tkinter import N
from cs1robots import *
create_world()
hubo = Robot() 
hubo.set_trace('blue')

# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

def find_height():
    global cnt
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

#def Width():

cnt = 0

m = 9
n = 10
hubo.turn_left()
for i in range(n):
    Height()