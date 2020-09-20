import turtle
turtle.penup()
turtle.goto(-250,250)
for i in range(6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
turtle.penup()
turtle.goto(-250,250)
turtle.right(90)
for i in range(6):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.right(90)
    turtle.backward(100)
    turtle.left(90)
turtle.exitonclick()
    
