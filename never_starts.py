#   a114_never_starts.py
#   The way that this code is written, it will never enter the loop.
#   Examine the commented lines to learn why.

import turtle as trtl

color1 = "navy"

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 50 # the radius of the circle
angle = 65 # experiment
seg = int(360/angle) # the length of a line

start_loop = 'n' 

while (start_loop == 'y'):
  painter.right(angle)
  painter.forward(space)
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()

wn = trtl.Screen()
wn.mainloop() 
# wn.bye() # new method to close the turtle window

