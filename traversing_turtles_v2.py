# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#  Initializes starting position and heading
startx = 0
starty = 0
start_heading = 0 # Initial Direction

# Create turtles with shape and color, and set pen up
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    new_color = turtle_colors.pop() # Pop color from list
    
    t.fillcolor(new_color)
    t.pencolor(new_color)
    t.penup() # Modification 1: Pen up before moving
    
    t.goto(startx, starty)
    t.setheading(start_heading) # Set initial heading
    
    t.pendown() # Modification 1: Pen down after moving
    
    my_turtles.append(t)
    
    # Move turtle and update position and heading
    t.right(45)
    t.forward(50)
    
    # Modification 2: update startx/starty to current turtles position
    startx = t.xcor()
    starty = t.ycor()
    
    # Modification 3: update heading for next turtle
    start_heading = t.heading()

wn = trtl.Screen()
wn.mainloop()