# Turtle Intro #

from turtle import Screen, Turtle
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def rnd_color():
    """Returns random rgb color code for each rgb value (red, green, blue) from 0 to 255"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# tim.shape("turtle")
# tim.color("red")

# Challenge 1 - Draw a Square #
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2 - Draw a Dashed Line #
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3 - Draw Shapes #
# screen.colormode(255)
#
#
# def rnd_color():
#     """Returns random rgb color code for each rgb value (red, green, blue) from 0 to 255"""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# def draw_shape(num_sides):
#     tim.color(rnd_color())
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

# Challenge 4 - Random Walk #
# directions = [0, 90, 180, 270]
#
# tim.pensize(10)
# tim.speed("fast")
#
# for _ in range(200):
#     tim.color(rnd_color())
#     tim.forward(50)
#     tim.setheading(random.choice(directions))

# Challenge 5 - Spirograph #
# tim.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(rnd_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)


screen.exitonclick()
