import random
from turtle import Turtle, Screen


t = Turtle()
screen = Screen()

colors = ["gold", "darkolivegreen", "red", "indigo", "coral", "yellow", "blue", "orange"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 11):
    t.color(random.choice(colors))
    draw_shape(shape_side_n)


screen.exitonclick()

