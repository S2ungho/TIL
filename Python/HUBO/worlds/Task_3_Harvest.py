from cs1robots import*

load_world("Python/HUBO/worlds/harvest1.wld")
hubo = Robot() 
hubo.set_trace('blue')
# Write your own code below !
def turn_right():
    for i in range(3):
        hubo.turn_left()

#def find_beeper():


def move_and_pick():
    global cnt
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1

cnt = 0
swi = 0
while cnt < 36:
    if hubo.front_is_clear():
        move_and_pick()
    else:
        if swi == 0:
            hubo.turn_left()
            move_and_pick()
            hubo.turn_left()
            swi = 1
        else:
            turn_right()
            move_and_pick()
            turn_right()
            swi = 0

#hubo.front_is_clear()
#hubo.pick_beeper()

#hubo.on_beeper()

