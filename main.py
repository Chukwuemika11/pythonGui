from turtle import Turtle, Screen
import random

lawrence = Turtle()
lawrence.shape("turtle")
lawrence.pencolor("magenta")
lawrence.pensize(12)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def drawShape(num_sides):
    angle = 360 / num_sides

    for _ in range(num_sides):
        lawrence.forward(100)
        lawrence.right(angle)

for shape_side_n in range(3, 11):
    lawrence.color(random.choice(colours))
    drawShape(shape_side_n)
screen = Screen()
screen.exitonclick()