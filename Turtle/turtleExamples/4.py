import turtle as t 
t.pensize(10)
t.fillcolor('yellow')
t.hideturtle()
t.bgcolor('grey')
radius = 180
t.penup()
t.setposition(0,-radius)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(radius)
t.end_fill()
mouth_radius = radius * 0.6
mouth_angle = 70

t.penup()
t.setposition(0,-mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,mouth_angle)

t.penup()
t.setposition(0,-mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,-mouth_angle)

x= 50
y= 50
eye_size = 60
t.penup()
t.setposition(x,y)
t.pendown()
t.dot(eye_size)
t.penup()
t.setposition(-x,y)
t.pendown()
t.dot(eye_size)
t.done()