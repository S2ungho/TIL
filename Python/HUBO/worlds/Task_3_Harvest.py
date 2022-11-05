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
    cnt = 0
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()
        cnt += 1

cnt = 0
while cnt < 36:
    if hubo.front_is_clear():
        move_and_pick()
    else:
        hubo.turn_left()




#hubo.front_is_clear()
#hubo.pick_beeper()

#hubo.on_beeper()

