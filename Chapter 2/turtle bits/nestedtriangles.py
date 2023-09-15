import turtle
import math
# Triangle 1
turtle.penup()
turtle.goto(-100,-150)
turtle.pendown()
turtle.forward(300)
turtle.left(180 - (math.acos(150/250) * (180/math.pi)))
turtle.forward(250)
turtle.setheading(270)
turtle.right(math.acos(200/250)*(180/math.pi))
turtle.forward(250)

#Triangle 2
new_ang = math.atan(75/150)*(180/math.pi)
new_measure = math.sqrt((150**2)+(75**2))
turtle.begin_fill()
turtle.setheading(0)
turtle.left(new_ang)
turtle.forward(new_measure)
turtle.penup()
turtle.goto(200,-150)
turtle.pendown()
turtle.setheading(180)
turtle.right(new_ang)
turtle.forward(new_measure)
turtle.end_fill()

turtle.exitonclick()