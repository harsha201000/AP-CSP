#   a114_infinite_loop_2.py
#   This code will also run forever!
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.penup()
painter.color("salmon")

line = 4 # Starting value for line

while (line % 2 != 2): # What does this do?
  painter.goto(0,0)
  painter.right(20)
  painter.forward(80)
  painter.pendown()
  painter.circle(10)
  painter.penup()
  line = line + 1 # What does this do?
  if (line % 18 == 0):
    painter.color("navy")
  if (line % 36 == 0):
    painter.color("salmon")

wn = trtl.Screen()
wn.mainloop()