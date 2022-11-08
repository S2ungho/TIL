from shutil import move
from cs1robots import*

load_world("Python/HUBO/worlds/harvest2.wld")
hubo = Robot() 
hubo.set_trace('blue')
# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_and_pick():
    global cnt, cnt_s
    hubo.move()
    cnt_s += 1
    if hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1
#def find_beeper():
def one():
    move_and_pick()
    turn_right()
    move_and_pick()
    hubo.turn_left()

def two():
    for i in range(a):
        one()
    

cnt = 0 
cnt_s = 0
a = 5

while cnt < 36:
    for i in range(5):
        move_and_pick()
    hubo.turn_left()
    move_and_pick()
    while cnt < 36:
        for i in range(3):
            two()
            hubo.turn_left()
        a -= 1
print(cnt_s)


        
#hubo.front_is_clear()
#hubo.pick_beeper()
#hubo.on_beeper()

