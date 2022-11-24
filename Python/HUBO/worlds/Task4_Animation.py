from cs1graphics import*
from time import*
import copy

def draw_animal():
    print("a")

paper = Canvas()
paper.setBackgroundColor('Green')
paper.setWidth(700)
paper.setHeight(500)
paper.setTitle('My World')

pig = Layer()
leg1 = Path(Point(-20, 10),Point(-20, 0))
leg1.setBorderWidth(3)
pig.add(leg1)
leg2 = Path(Point(20, 10),Point(20, 0))
leg2.setBorderWidth(3)
pig.add(leg2)
leg3 = Path(Point(-20, 10),Point(-15, 0))
leg3.setBorderWidth(3)
pig.add(leg3)
leg4 = Path(Point(-20, 10),Point(25, 0))
leg4.setBorderWidth(3)
pig.add(leg4)
body = Rectangle(100, 50, Point(0, -25))
body.setFillColor('pink')
body.setDepth(60)# behind the tires
pig.add(body)
pig.moveTo(110, 180)
pig.setDepth(20)# in front of the house
paper.add(pig)