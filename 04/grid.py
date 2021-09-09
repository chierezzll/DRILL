import turtle

turtle.left(90)
x = 0
y = 0
count = 6
while (count > 0):
    turtle.forward(500)
    turtle.penup()
    x += 100
    turtle.goto(x, y)
    turtle.pendown()
    count -= 1

x = 0
y = 0
count = 6
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.right(90)
while (count > 0):
    turtle.forward(500)
    turtle.penup()
    y += 100
    turtle.goto(x, y)
    turtle.pendown()
    count -= 1


turtle.exitonclick()
