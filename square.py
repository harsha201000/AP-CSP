#   a113_square.py
#   Write code to draw a square.
import turtle as trtl

painter = trtl.Turtle()

# Your code here
for line in range(4):
  painter.forward(100)
  painter.right(90)


wn = trtl.Screen()
wn.mainloop()