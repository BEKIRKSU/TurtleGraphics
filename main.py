from turtle import Turtle, Screen



ttt = Turtle()
ttt.shape("turtle")
# Use documentation to find different shapes, particular functions etc such as .shape("")
# Or Google it
ttt.color("DarkSeaGreen")
# ttt.right(77)
# ttt.forward(77)
# ttt.right(77)

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

import random
# You can import anywhere, just has to be before you use it.

# We tap into the module to change the colour.
Turtle.colormode(255)

# colours = ["blue", "green", "orange", "yellow", "black", "red", "DeepSkyBlue", "cyan4", "coral", "AntiqueWhite3"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        ttt.speed(9)
        ttt.forward(100)
        ttt.right(angle)


for shape_side_n in range(3, 11):
    ttt.color(random.choice(colours))
    draw_shape(shape_side_n)

# Here's how to do a random walk, which is used in many disciplines such as Maths and Physics.



for _ in range(5):
    ttt.pensize(5)
    ttt.pendown()
    ttt.forward(10)
    ttt.penup()
    ttt.forward(10)

directions = [0, 90, 100, 180, 250, 270, 275, 360]
speed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
distance = range(0, 27)
# These are nice examples ^ can be used in many ways

for _ in range(220):
    ttt.color(random.choice(colours))
    ttt.speed(random.choice(speed))
    ttt.pendown()
    ttt.forward(random.choice(distance))
    ttt.setheading(random.choice(directions))
# Good use of documentations

# tuples are different to arrays/lists. Values cannot be changed like in lists.
# tuple[2] = 7 wouldn't work. When you create a tuple it cannot be changed.
# Use case = you want a list which no one can change, accidentally especially.
# If you want to change your tuple you can put it inside a list and convert it into a list.
# list(tuple) = would result in [1, 2, 3] whatever the tuple is.
# Look above the colours array to see an example.












# Use documentations to figure out how to use these packages and modules.

screen = Screen()
screen.exitonclick()
# this will exit on click, so when you click the window it will exit. So we move it to the bottom of the
# file