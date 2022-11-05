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
    hubo.move()
    if hubo.on_beeper():
        hubo.pick_beeper()

for i in range(10):
    move_and_pick()

#hubo.front_is_clear()
#hubo.pick_beeper()
#hubo.on_beeper()

