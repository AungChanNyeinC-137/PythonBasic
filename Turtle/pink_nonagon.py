import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("green")
screen.title("Filled Pink Nonagon")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

# Set the color for drawing and filling
my_turtle.color("pink")

# Begin the fill process
my_turtle.begin_fill()

# --- Loop to draw the nonagon ---
# A nonagon has 9 sides.
# The angle to turn after each side is 360 / 9 = 40 degrees.
for _ in range(9):
    my_turtle.forward(100)  # You can change this value to make the nonagon bigger or smaller
    my_turtle.left(40)

# Complete the filling of the shape
my_turtle.end_fill()

# Hide the turtle so only the shape is visible
my_turtle.hideturtle()

# Keep the window open until you click on it
screen.exitonclick()