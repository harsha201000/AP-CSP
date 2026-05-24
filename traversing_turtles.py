# a117_traversing_turtles.py
# Extended turtle drawing with colors, shapes, spiral motion, and pen customization

import turtle as trtl
import random

# Create an empty list of turtles
my_turtles = []

# Use interesting shapes and colors (doubled for more turtles)
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic",
                 "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold",
                 "pink", "cyan", "lime", "brown", "magenta", "gray"]

# Initialize starting position and heading
startx = 0
starty = 0
start_heading = 0  # Initial direction
distance = 50      # Initial forward distance

# Create turtles with shape, color, and pen settings
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    new_color = turtle_colors.pop()
    t.fillcolor(new_color)
    t.pencolor(new_color)
    t.pensize(random.randint(1, 5))  # Random pen size for variety
    t.penup()
    t.goto(startx, starty)
    t.setheading(start_heading)
    t.pendown()
    my_turtles.append(t)

    # Move turtle in a spiral pattern
    t.right(random.randint(30, 90))  # Random heading change
    t.forward(distance)

    # Update position and heading for next turtle
    startx = t.xcor()
    starty = t.ycor()
    start_heading = t.heading()
    distance += 20  # Increase distance for spiral effect

# Keep window open
wn = trtl.Screen()
wn.mainloop()