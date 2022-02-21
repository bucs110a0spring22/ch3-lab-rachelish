import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
michelangelo.speed(1)
leonardo.speed(1)
## 5. your code goes here

leonardo.forward(random.randrange(1, 100))
michelangelo.forward(random.randrange(1, 100))
leonardo.goto(-100,-20)
michelangelo.goto(-100,20)

for i in range(10):
  leonardo.forward(random.randrange(1, 10))
  michelangelo.forward(random.randrange(1, 10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
sides_length = 20
num_of_sides = [4, 6, 9, 12]
leonardo.goto(-20, -30)

for i in range(len(num_of_sides)):
  leonardo.clear()
  for j in range(num_of_sides[i]):
    angle = 360/num_of_sides[i]
    leonardo.pendown()
    leonardo.forward(50)
    leonardo.left(angle)
  






window.exitonclick()
