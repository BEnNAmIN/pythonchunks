import turtle
import math

turtle.penup()
turtle.goto(-100,-100)
def dotlinemaker():
    turtle.pendown()
    turtle.dot(10)
    turtle.forward(25)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.forward(37.5)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.forward(37.5)
    turtle.penup()
    turtle.forward(25)
    turtle.pendown()
    turtle.forward(25)
    turtle.dot(10)

dotlinemaker()

turtle.left(90)
turtle.forward(200)
turtle.left(90)

dotlinemaker()

turtle.left(90)
turtle.forward(200)
turtle.left(135)
turtle.forward(math.sqrt((200**2)*2))

turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.setheading(-45)
turtle.forward(math.sqrt((200**2)*2))

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.dot(10)

turtle.exitonclick()