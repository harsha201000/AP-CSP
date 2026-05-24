# CODE TO COPY
#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  # Create a new horizontal turtle with the specified shape
  ht = trtl.Turtle(shape=s)
  # Add the turtle to the horizontal list
  horiz_turtles.append(ht)
  # Lift the pen to move without drawing
  ht.penup()
  # Get a color from the horizontal colors list
  new_color = horiz_colors.pop()
  # Set the turtle's color
  ht.fillcolor(new_color)
  # Move the turtle to its starting position on the left
  ht.goto(-350, tloc)
  # Set the heading to move right (0 degrees)
  ht.setheading(0)

  # Create a new vertical turtle with the same shape
  vt = trtl.Turtle(shape=s)
  # Add the turtle to the vertical list
  vert_turtles.append(vt)
  # Lift the pen to move without drawing
  vt.penup()
  # Get a color from the vertical colors list
  new_color = vert_colors.pop()
  # Set the turtle's color
  vt.fillcolor(new_color)
  # Move the turtle to its starting position at the top
  vt.goto( -tloc, 350)
  # Set the heading to move down (270 degrees)
  vt.setheading(270)
  
  # Increment the location for the next pair of turtles
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
# ... (Previous code remains the same) ...

tloc = 50
for s in turtle_shapes:
  # ... (Initialization code remains the same) ...
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

# Loop for 50 steps of movement and collision checking
for step in range(50):
    # Move all existing horizontal turtles
    for ht in horiz_turtles:
        ht.forward(1)
    
    # Move all existing vertical turtles
    for vt in vert_turtles:
        vt.forward(1)

    # Check for collisions between all pairs of remaining turtles
    # We create copies of the lists ([...]) so we can modify the original lists during iteration
    for ht in horiz_turtles[:]:
        for vt in vert_turtles[:]:
            # Calculate the distance in x and y coordinates
            x_distance = abs(ht.xcor() - vt.xcor())
            y_distance = abs(ht.ycor() - vt.ycor())

            # If both distances are less than 20 pixels, a collision has occurred
            if x_distance < 20 and y_distance < 20:
                # Remove the collided turtles from their respective lists
                horiz_turtles.remove(ht)
                vert_turtles.remove(vt)
                # Optional: Hide the turtles when they "crash"
                ht.hideturtle()
                vt.hideturtle()
                # Since this pair collided, move to the next vertical turtle
                break 

wn = trtl.Screen()
wn.mainloop()

# Remainder of the code to be added below...
