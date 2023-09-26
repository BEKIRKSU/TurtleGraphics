from turtle import Turtle, Screen



timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# Use documentation to find different shapes, particular functions etc such as .shape("")
# Or Google it
timmy_the_turtle.color("DarkSeaGreen")
timmy_the_turtle.right(77)
timmy_the_turtle.forward(77)
timmy_the_turtle.right(77)

# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# instead use the for loop and range operator:

for _ in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)









# Use documentations to figure out how to use these packages and modules.

screen = Screen()
screen.exitonclick()
# this will exit on click, so when you click the window it will exit. So we move it to the bottom of the
# file