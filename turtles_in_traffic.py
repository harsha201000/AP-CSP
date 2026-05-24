#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Recovering from collisions.
import turtle as trtl
import time # Import time module for delays

# --- FIX: Define wn (screen object) early so it's accessible everywhere ---
wn = trtl.Screen()

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  # Create a new horizontal turtle
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  ht.original_shape = s
  ht.original_color = new_color
  ht.speed_step = 1 # Add a custom attribute for speed tracking

  # Create a new vertical turtle
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  vt.original_shape = s
  vt.original_color = new_color
  vt.speed_step = 1 # Add a custom attribute for speed tracking
  
  tloc += 50
# --- End Initialization Code ---

# Define a specific shape and color for collisions
COLLISION_SHAPE = turtle_shapes.pop() # Removes "classic" from the list for collision use
COLLISION_COLOR = "gray"
MAX_SPEED = 5
RECOVERY_DISTANCE = 50 # How far they back up

# Loop for movement, speed changes, and collision management
for step in range(250): # Increased range because turtles move faster/stop
    
    # Speed Management
    for ht in horiz_turtles:
        ht.forward(ht.speed_step)
        if step % 20 == 0 and ht.speed_step < MAX_SPEED:
            ht.speed_step += 1
        if ht.xcor() > 380 or ht.xcor() < -380:
             ht.speed_step = 1

    for vt in vert_turtles:
        vt.forward(vt.speed_step)
        if step % 20 == 0 and vt.speed_step < MAX_SPEED:
            vt.speed_step += 1
        if vt.ycor() > 380 or vt.ycor() < -380:
             vt.speed_step = 1


    # Collision Management
    for ht in horiz_turtles:
        for vt in vert_turtles:
            x_distance = abs(ht.xcor() - vt.xcor())
            y_distance = abs(ht.ycor() - vt.ycor())

            if x_distance < 20 and y_distance < 20:
                # Collision detected!
                
                ht.shape(COLLISION_SHAPE)
                ht.fillcolor(COLLISION_COLOR)
                vt.shape(COLLISION_SHAPE)
                vt.fillcolor(COLLISION_COLOR)
                
                ht.backward(RECOVERY_DISTANCE)
                vt.backward(RECOVERY_DISTANCE)
                
                ht.shape(ht.original_shape)
                ht.fillcolor(ht.original_color)
                vt.shape(vt.original_shape)
                vt.fillcolor(vt.original_color)
                
                ht.speed_step = 1
                vt.speed_step = 1
                
                # wn.update() # Use wn here
                # time.sleep(0.01) # Use wn and time here
                break 

# Final step: Indicate the program is intentionally stopped/deactivated
DEACTIVATED_COLOR = "pink"

# Deactivate horizontal turtles
for ht in horiz_turtles:
    ht.fillcolor(DEACTIVATED_COLOR)

# Deactivate vertical turtles
for vt in vert_turtles:
    vt.fillcolor(DEACTIVATED_COLOR)

# Keep the screen open until closed by the user
wn.mainloop()
