from cs1robots import*

load_world("Python/HUBO/worlds/hurdles1.wld")
hubo = Robot() 
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def one_hurdle():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    
hubo.move()
for i in range(6):
    one_hurdle()
    