from turtle import Turtle, Screen



ttt = Turtle()
ttt.shape("turtle")
# Use documentation to find different shapes, particular functions etc such as .shape("")
# Or Google it
ttt.color("DarkSeaGreen")
ttt.right(77)
ttt.forward(77)
ttt.right(77)

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
    ttt.right(90)
    ttt.forward(100)
    # to change the name of anything we named we can right-click, refactor, rename and change it.
#     timmy_the_turtle turned into ttt.

import heroes
# you can just write import from a package that isn't downloaded, and pyCharm will ask if you
# want to download it, very clear and straightforward.
print(heroes.gen())











# Use documentations to figure out how to use these packages and modules.

screen = Screen()
screen.exitonclick()
# this will exit on click, so when you click the window it will exit. So we move it to the bottom of the
# file