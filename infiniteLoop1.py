#   a114_infinite_loop_1

import turtle as trtl

color1 = "navy"

wn = trtl.Screen()
painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

space = 50 # the radius of the circle
angle = 65 # experiment
seg = int(360/angle) # the length of a line

start_loop = 'y' 

while (start_loop == 'y'):
  painter.right(angle)
  painter.forward(space)
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()

wn.mainloop() 

