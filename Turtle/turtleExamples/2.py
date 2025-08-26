import turtle
turtle.hideturtle()
turtle.pen(pencolor='green', pensize=3)
turtle.begin_fill()
for i in range(5):
    turtle.forward(150)
    turtle.right(144)
    turtle.fillcolor('pink')
    turtle.end_fill()