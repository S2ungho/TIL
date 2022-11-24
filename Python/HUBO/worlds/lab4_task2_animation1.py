from cs1graphics import*
from time import*
import copy

paper = Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(300)
paper.setHeight(200)
paper.setTitle('My World')

car = Layer()
tire1 = Path(Point(-20, -10),Point(-20, 0))
tire1.setBorderWidth(3)
car.add(tire1)
tire2 = Path(Point(20, -10),Point(20, 0))
tire2.setBorderWidth(3)
car.add(tire2)
body = Rectangle(70, 30, Point(0, -25))
body.setFillColor('blue')
body.setDepth(60)# behind the tires
car.add(body)
car.moveTo(110, 180)
car.setDepth(20)# in front of the house
paper.add(car)
