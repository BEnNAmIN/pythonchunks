import turtle

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.setheading(180)
turtle.speed(0)

for i in range(0,500,5):
    for u in range (4):
            turtle.forward(10+i)
            turtle.right(90)
turtle.exitonclick()