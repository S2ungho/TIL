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
#def one():
    

def up():
    global a
    for i in range(a):
        move_and_pick()
        turn_right()
        move_and_pick()
        hubo.turn_left()

def around():
    global a
    for i in range(3):
        up()
        hubo.turn_left()
    up(4)
    #a -= 2

def first():
    for i in range(5):
        move_and_pick()
    hubo.turn_left()
    move_and_pick()


cnt = 0 
cnt_s = 0
a = 5
while cnt < 36:
    first()
    around()

print(cnt_s)


        
#hubo.front_is_clear()
#hubo.pick_beeper()
#hubo.on_beeper()

