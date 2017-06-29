# Beginning of a python file begins with imports
# The package we are using for this activity is called turtle
import turtle

# Let's design the world our turtle lives in
# turtle.Screen() returns a handle on the world. Using
# 'window' we can control properties of the world.
window = turtle.Screen()

# Create a turtle instance and give it a shape
tammy = turtle.Turtle()
tammy.shape('turtle')

# Move turtle
tammy.forward(10)
tammy.left(10)
tammy.forward(10)

# Your turn, make the turtle draw a rectangle

# This command is used to keep the window open
turtle.done()
