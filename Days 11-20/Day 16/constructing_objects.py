# constructing object
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("CornflowerBlue")
timmy.forward(100)

my_screen = Screen()
my_screen.setup(width=600, height=400)
# calling a function
my_screen.exitonclick()
