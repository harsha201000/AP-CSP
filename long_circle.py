#   a113_long_circle.py
#   Draw a circle calling only the forward and
#   right methods
import turtle as trtl

painter = trtl.Turtle()

# Your code here
for i in range(18):
  painter.forward(20)
  painter.right(20)


wn = trtl.Screen()
wn.mainloop()