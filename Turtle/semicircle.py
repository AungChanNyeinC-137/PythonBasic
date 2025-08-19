import turtle as t 
colors = ( 'blue', 'red', 'orange','yellow')
for i in range(4):
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(80,180)
    t.left(90)
    t.forward(160)
    t.end_fill()
t.hideturtle()
t.done()
