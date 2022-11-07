from cs1robots import*

load_world("Python/HUBO/worlds/harvest2.wld")
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
while cnt < 36:


    if hubo.front_is_clear() and hubo.left_is_clear():
        hubo.turn_left()
    elif hubo.front_is_clear() and hubo.right_is_clear():
        turn_right()
    else:
        hubo.turn_left()
        hubo.turn_left()


        
#hubo.front_is_clear()
#hubo.pick_beeper()
#hubo.on_beeper()

