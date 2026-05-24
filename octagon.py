#   a113_octagon.py
#   Write code that draws an octagon starting
#   at -50, 100 to leave enough room for the drawing
import turtle as trtl

painter = trtl.Turtle()

# new starting location so the entire
# octagon is visible
painter.penup()
painter.goto(-50, 150)
painter.pendown()

# Your code here
for i in range(8):
  painter.forward(100)
  painter.right(45)

wn = trtl.Screen()
wn.mainloop()