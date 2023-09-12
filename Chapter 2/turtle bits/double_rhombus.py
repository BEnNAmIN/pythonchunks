import turtle
import math

# Shape #1

# setting a background color so the shape infill is visible
turtle.bgcolor('grey')

turtle.penup()
turtle.goto(-150,-25)
turtle.left(45)
turtle.begin_fill()
turtle.fillcolor('white')
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.exitonclick